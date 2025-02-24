import os
from selenium import webdriver


def before_all(context):
    # anything that happens before the test run starts happens here
    # accessing env vars needed for tests
    context.username = os.getenv("hudl_username")
    context.password = os.getenv("hudl_password")
    context.base_url = os.getenv("hudl_base_url")


def before_scenario(context, scenario):
    # setup before each test
    # start gecko driver
    context.driver = webdriver.Firefox()

    # navigate to base url
    context.driver.get(f"{context.base_url}/login")


def after_scenario(context, scenario):
    # actions that take place after a scenario
    # take a screenshot if the test failed
    if scenario.status == "failed":
        # behavex will set context.evedince_path.
        # if context.evidence exists, we know to format the screenshot's specifically for behavex
        if hasattr(context, "evidence_path"):
            screenshot_path = f"{context.evidence_path}/{scenario.name}.png"
        else:
            # If evidence_path doesn't exist, we are not using behavex
            # check for screenshot folder and create if missing
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")
            # create a path for the screenshot and save it
            screenshot_path = f"screenshots/{scenario.name}.png"
        context.driver.save_screenshot(screenshot_path)
    # shut down driver    
    context.driver.quit()
