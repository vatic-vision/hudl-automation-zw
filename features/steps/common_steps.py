from behave import *
from pages.page import Page


@step('I am directed to the "{route}" page')
def check_url(context, route):
    page = Page(context.driver)
    nav = page.does_url_contain_path(route)
    assert (
        nav
    ), f"exptected url to contain {route} but it did not. Current URL: {context.driver.current_url}"


@step("an alert does not appear")
def check_for_alert(context):
    page = Page(context.driver)
    alert = page.check_for_alert()
    assert (
        alert is False
    ), "Expected no alert messages to be seen, but one is pressent on the page. Please check screenshot"
