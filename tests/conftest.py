from selene import browser
from selene.core.configuration import Config
import pytest


@pytest.fixture
def browser_firefox_open():
    browser.config.driver_name = 'firefox'


@pytest.fixture
def browser_size():
    Config.window_width = 1920
    Config.window_height = 1080