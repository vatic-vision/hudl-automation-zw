# hudl-automation-zw
A small automation example for Hudl

## Package Management

This project uses [poetry](https://python-poetry.org/) to manage and install packages

### Installing Poetry

#### MacOS
Install with Homebrew

```bash
brew install poetry
```

#### Windows
Install using Powershell

```bash
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

#### Install Packages With Poetry
run from project root

```bash
poetry install
```

Alternatively, you can install the needed packages without Poetry using pip:

behave 1.2.6

behavex 4.1.0

selenium 4.29.0

## Packages

### Behave

A Python-based behavior-driven development (BDD) framework that lets you write human-readable tests using feature files and step definitions.

### Behavex
An extension to Behave that enhances its reporting capabilities—such as embedding screenshots and additional debugging information—in test reports. Behavex also easily allows parallel test execution.

### Selenium
A browser automation tool that allows you to simulate user interactions with web applications for testing purposes.


## Test Setup

### Environment Variables
These environment variables are required to run tests. You will need to provide your own credentials
```
hudl_base_url = "https://www.hudl.com"

hudl_username = a valid username

hudl_password = a valid password
```
Alternatively, if you don't want to set environment varialbes, you can update the values in the before_all function in hudl-automation-zw/features/environment.py with the base url, and your login credentials.

### Webdriver
These tests are set up to work with [Gecko 0.35.0](https://github.com/mozilla/geckodriver/releases/tag/v0.35.0) driver for Firefox

Please download Gecko and place it into a folder within your system PATH

If you're not familiar with adding folders to PATH check out these helpful articles:

[Windows](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/)

[MacOS](https://medium.com/@B-Treftz/macos-adding-a-directory-to-your-path-fe7f19edd2f7)

## Running Tests

### Sequential execution with Behave
From the root of the project, run
```bash
behave
```

### Individual Test Execution with Behave
If you would like to run just one, or a specified selection of tests, you can add a @tag directly above the scenario name in a feature file. When writing tests, I use @now to mark tests that I want to run. You can then run only tagged tests by running:
```bash
behave -k -t "@now"
```
Change @now to whatever you've set for your tag if you've changed it

#### Behave Failures and Evidence
If a failure occurs, a screenshot folder will be created and a screenshot with the failing scenario name will be added. If you wold like to easily force a failure, you can change one of the step parameters in hudl-automation-zw/features/login_page.feature User can log in.

Example: update the step **"Then I am directed to the "/home" page"** changing "/home" in **Scenario: User can log in** to some other path, then run tests. The first test will fail and you will see a screenshot and error output in your terminal

### Parallel Execution
Using behavex, we can easily run multiple scenarios in our feature files in parallel by running:
```bash
behavex --parallel-processes 10 --parallel-scheme scenario
```
This command will run up to 10 scenarios at a time until it finishes all scenarios in a feature file. --parallel-processes can be changed depending on desired performance.

#### Behavex Failures and Evidence
During a Behavex run, an ouput folder is created. Behavex is responsible for organizing evidence, and generating an after run report. You can view this report by opening hudl-automation-zw//output/report.html in a web browser. Here you will be able to see metrics about the test run. If a test fails, you can expand the failed row to see what errors occurred. You can also see a screenshot of the page that the error occurred on by clicking on "additional evidence"
