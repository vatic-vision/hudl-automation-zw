from pages.page import Page


class LoginPage(Page):
    USERNAME_INPUT = "[id='username']"
    PASSWORD_INPUT = "[id='password']"
    TEXT_PASSWORD_ERROR = "[id='error-element-password']"
    TEXT_USERNAME_ERROR = "[id='error-element-username']"
    BTN_CONTINUE = "[name='action']"
    BTN_EDIT = "[data-link-name='edit-username']"

    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    def enter_username(self, username):
        Page.enter_text(self, self.USERNAME_INPUT, username)

    def enter_password(self, password):
        Page.enter_text(self, self.PASSWORD_INPUT, password)

    def click_continue(self):
        Page.click_element(self, self.BTN_CONTINUE)

    def get_password_error_text(self):
        return Page.get_text(self, self.TEXT_PASSWORD_ERROR)

    def get_username_error_text(self):
        return Page.get_text(self, self.TEXT_USERNAME_ERROR)

    def click_edit(self):
        Page.click_element(self, self.BTN_EDIT)

    def click_create_account(self):
        Page.click_link_by_text(self, "Create Account")

    def click_forgot_password(self):
        Page.click_link_by_text(self, "Forgot Password")
