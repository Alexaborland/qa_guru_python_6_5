import pytest
from selene import browser

@pytest.fixture()
def open_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open('https://demoqa.com/automation-practice-form')



