from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def is_url_contains(self, text):
        if self.page.url.find(text) == -1:
            return False
        return True

    def navigate(self, url):
        self.page.goto(url)
