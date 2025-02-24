from behave import step
from pages.login import LoginPage


@step("I enter my username")
def enter_username(context):
    login = LoginPage(context.driver)
    login.enter_username(context.username)


@step("I click continue")
def click_continue(context):
    login = LoginPage(context.driver)
    login.click_continue()


@step("I enter my password")
def enter_password(context):
    login = LoginPage(context.driver)
    login.enter_password(context.password)


@step('I enter the password "{password}"')
def enter_specified_password(context, password):
    login = LoginPage(context.driver)
    login.enter_password(password)


@step('I enter the username "{username}"')
def enter_specified_username(context, username):
    login = LoginPage(context.driver)
    login.enter_username(username)


@step('a "{type}" error appears incluing text "{expected_text}"')
def check_error_message(context, type, expected_text):
    login = LoginPage(context.driver)
    match type:
        case "username":
            error_text = login.get_username_error_text()
        case "password":
            error_text = login.get_password_error_text()
        case _:
            assert False, "type must be 'username' or 'password'"
    assert (
        expected_text in error_text
    ), f"Error did not display correct text. Expected {expected_text}, but got {error_text}"


@step("I click Edit on the email input")
def click_edit(context):
    login = LoginPage(context.driver)
    login.click_edit()


@step("I click create account")
def click_create_account(context):
    login = LoginPage(context.driver)
    login.click_create_account()


@step("I click forgot password")
def click_forgot_password(context):
    login = LoginPage(context.driver)
    login.click_forgot_password()
