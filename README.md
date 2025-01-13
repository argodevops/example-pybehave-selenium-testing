# example-selenium-testing
Example repository demonstrating running selenium tests using [Pybehave Selenium Test Framework](https://github.com/argodevops/pybehave-selenium-test-framework).

## Installation

Install the Pybehave Selenium library and dependencies.

```
pip install pybehave-selenium-test-framework
```

## Environment Variables and Configuration Files

Create a configuration folder to add a **settings** and **configuration** file. A `.env` file can be used to source the settings and configuration environment variables.

```
export SETTINGS_FILE_PATH="${PWD}/app/configuration/test-settings.json"
export CONFIG="${PWD}/app/configuration/app-config.json"
```

### Settings Files

The `SETTINGS_FILE_PATH` env variable defines the application settings file to use. This file contains the application wide settings. The default properties are:
```
{
  "environment": "dev",
  "is_kv_config": false,
  "browser": "chrome",
  "is_headless_browser": true,
  "driver_executable_path": "/usr/local/bin/chromedriver",
  "driver_timeout": "5",
  "wait_time": "5",
  "autoretry_attempts": "1"
}
```

### Configuration File

The `CONFIG` env variable defines the application configuration file to use. This file contains properties specific to testing an application.
```
{
    "rest_api_token_url": "https://www.boredapi.com/api/activity",
    "rest_api_token_key": "uuskjfdnnds77dsjjkds;lcmmmcm-da8ghasb;s="
}
```

## Code Structure

The `app` directory contains the main codebase, structured as follows:

- **`configuration/`**: Stores application and test configuration files like `app-config.json` and `test-settings.json`.
- **`features/`**: Houses feature files, step definitions, and the `environment.py` file for `behave`.
  - **`example/`**: Contains `.feature` files written in Gherkin syntax to define test scenarios.
  - **`steps/`**: Step definitions that implement the logic for each scenario in the `.feature` files.
- **`support/`**: Helper modules for test execution.
  - **`actions/`**: Encapsulates feature-specific logic like `loginaction`.
  - **`locators/`**: Defines locators for UI elements such as `loginlocator`.
  - **`pageactions/`**: Implements page interaction logic like `loginpage`.

`behave` requires a `features/environment.py` file to define hooks that control the setup and teardown processes for your test execution.

Step definitions in `features/steps` back the Gherkin features and provide an entry point into the test business logic.

## Running the Tests

To run the example test.

```
behave app/features/example/login.feature
```

## Webdriver

You will need to maintain the correct version of the required webdriver for selenium to use. It is defined in the app-settings.json file and by default uses the chrome driver at `/usr/local/bin/chromedriver`.