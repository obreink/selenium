import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.edge.service import Service as EdgeService
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService('./tests/chromedriver.exe'))
    return driver

