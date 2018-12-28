from django.test.runner import DiscoverRunner
from django.test import SimpleTestCase
from django.utils.decorators import classproperty
from django.test.testcases import LiveServerThread, _StaticFilesHandler
from django.test.utils import modify_settings


class DatabaselessTestRunner(DiscoverRunner):
    """A test suite runner that does not set up and tear down a database."""

    def setup_databases(self):
        """Overrides DiscoverRunner"""
        pass

    def teardown_databases(self, *args):
        """Overrides DiscoverRunner"""
        pass


class DatabaselessLiveServerTestCase(SimpleTestCase):
    """
    Customizacion of the Django LiveServerTestCase class to use it
    without a database
    """
    host = 'localhost'
    port = 0
    server_thread_class = LiveServerThread
    static_handler = _StaticFilesHandler

    @classproperty
    def live_server_url(cls):
        return 'http://%s:%s' % (cls.host, cls.server_thread.port)

    @classproperty
    def allowed_host(cls):
        return cls.host

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        connections_override = {}

        cls._live_server_modified_settings = modify_settings(
            ALLOWED_HOSTS={'append': cls.allowed_host},
        )
        cls._live_server_modified_settings.enable()
        cls.server_thread = cls._create_server_thread(connections_override)
        cls.server_thread.daemon = True
        cls.server_thread.start()

        # Wait for the live server to be ready
        cls.server_thread.is_ready.wait()
        if cls.server_thread.error:
            # Clean up behind ourselves, since tearDownClass won't get called
            # in case of errors.
            cls._tearDownClassInternal()
            raise cls.server_thread.error

    @classmethod
    def _create_server_thread(cls, connections_override):
        return cls.server_thread_class(
            cls.host,
            cls.static_handler,
            connections_override=connections_override,
            port=cls.port,
        )

    @classmethod
    def _tearDownClassInternal(cls):
        # There may not be a 'server_thread' attribute if setUpClass() for some
        # reasons has raised an exception.
        if hasattr(cls, 'server_thread'):
            # Terminate the live server's thread
            cls.server_thread.terminate()

    @classmethod
    def tearDownClass(cls):
        cls._tearDownClassInternal()
        cls._live_server_modified_settings.disable()
        super().tearDownClass()
