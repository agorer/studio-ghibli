# Studio Ghibli Django app

## How to create a development environment

To create a development environment with the right requirements [virtualenv](https://virtualenv.pypa.io/en/latest/) could be used.

```
$> virtualenv env <- Create the environment
$> . env/bin/activate <- Activate the environment
$> pip install -r requirements.txt
```

## How to launch the application

```
$> ./manage.py runserver
```

This command will launch the server on port 8000 and the app could be seen in the browser using the link http://127.0.0.1:8000/

## How to launch tests

There are three types of tests (unit, integration and acceptance).

```
$> ./manage.py test --exclude-tag=acceptance-tests --exclude-tag=integration-tests <- Launch unit tests
$> ./manage.py test --tag=integration-tests <- Launch integration tests
$> ./manage.py test --tag=acceptance-tests <- Launch acceptance tests
```

## Linting code

Checks, among other things, that the code conforms to the PEP8 conventions.

```
$> flake8
```

## Things that could be improved

- The acceptance test code could be made more readable by using the Page Object pattern.

- By mocking the whole API when launching the acceptance tests we could made them faster and less fragile.

- We could decouple our business code from the framework by using a Clean Arquitecture. Here we have make use of it when accessing the API and the cache, but the Django views could be improved by dividing the Django code from the code that is strictly business logic.

- The views are tested through acceptance tests only. If they were more complicated we could use unit tests or better breakup the application between frontend and a backend that exposes an API.

- Validations could be added to the entities (Movie and Character) so the are always in a correct state.

- URL's that point to the API should be in a configuration object instead of directly in the api_client module.

- Instead of using dependency injection implicitly through the python module system an explicit system could be used that will made dependencies easier to discover and configure (currently done using monkey-patching).
