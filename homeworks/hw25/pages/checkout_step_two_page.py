from playwright.sync_api import Page
from homeworks.hw25.pages.base_page import BasePage


class CheckoutStepTwoPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.finish_button = page.locator('[id="finish"]')

    def click_finish_button(self):
        self.finish_button.click()
