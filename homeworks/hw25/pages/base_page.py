# pylint: disable=import-error
from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def get_url(self):
        return self.page.url

    def navigate(self, url):
        self.page.goto(url)
