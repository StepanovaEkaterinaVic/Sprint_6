import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from curl import *


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--window-size=1200,600")
    driver = webdriver.Firefox()
    driver.get(main_site)
    yield driver
    driver.quit()
