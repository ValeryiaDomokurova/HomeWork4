# pylint: disable=import-error
from playwright.sync_api import Page
from homeworks.hw25.pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.username = page.locator('[name="user-name"]')
        self.password = page.locator('[name="password"]')
        self.button = page.locator('[class="submit-button btn_action"]')

    def click_login_button(self):
        self.button.click()

    def fill_username(self, username):
        self.username.fill(username)

    def fill_password(self, password):
        self.password.fill(password)

    def login(self, username, password):
        self.fill_username(username)
        self.fill_password(password)
        self.click_login_button()
