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
    driver = webdriver.Chrome(service=ChromeService("./tests/chromedriver.exe"))
    return driver

def test_title_name(driver):
    driver.get("http://127.0.0.1:5000/labelPage")

    title= driver.title
    assert title == "Contacts"

def test_label_page_city(driver):
    driver.get("http://127.0.0.1:5000/labelPage")
    time.sleep(5)

    city_label = driver.find_element(By.ID, "city")
    city = city_label.text
    assert city == "Dundalk"
    driver.close()


def test_label_page_country(driver):    
    driver.get("http://127.0.0.1:5000/labelPage")
    time.sleep(5)

    country_label = driver.find_element(By.ID, "country")
    country = country_label.text
    assert country == "Ireland"
    driver.close()


def test_label_page_count(driver):
    driver.get("http://127.0.0.1:5000/labelPage")
    time.sleep(5)

    county_label = driver.find_element(By.ID, "county")
    county = county_label.text
    assert county == "Louth"
    driver.close()


def test_enter_data(driver):
    driver.get("http://127.0.0.1:5000/testForm")

    name_input = driver.find_element(By.ID, "first Name")