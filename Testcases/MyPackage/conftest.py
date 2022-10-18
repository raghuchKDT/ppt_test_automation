from selenium import webdriver
import pytest
from PageObjectModules.LoginPage import Login
import time

global driver
username = "admin"
password = "admin"
baseURL = "http://localhost:5003/"

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome("C:\\Users\\KnoDTec - Dheeraj\\Downloads\\chromedriver.exe")
    time.sleep(2)
    driver.get(baseURL)
    driver.maximize_window()
    yield driver
    time.sleep(2)
    driver.close()

@pytest.fixture (scope="module")
def user_login():
    global driver
    print("-----------setup------------")
    driver = webdriver.Chrome("C:\\Users\\KnoDTec - Dheeraj\\Downloads\\chromedriver.exe")
    driver.get(baseURL)
    driver.maximize_window()
    lp = Login(driver)
    lp.setUserName(username)
    lp.setPassword(password)
    lp.clickLogin()
    time.sleep(2)
    yield driver
    time.sleep(2)
    driver.close()

@pytest.fixture(scope="module")
def user_manager():
    global driver
    print("-----------setup------------")
    driver = webdriver.Chrome("C:\\Users\\KnoDTec - Dheeraj\\Downloads\\chromedriver.exe")
    driver.get(baseURL)
    driver.maximize_window()
    lp = Login(driver)
    lp.setUserName(username)
    lp.setPassword(password)
    lp.clickLogin()
    time.sleep(2)
    yield driver
    driver.close()

def pytest_configure(config):
    config._metadata['Project Name'] = 'Push Pull Touch WebPage'
    config._metadata['Module Name'] = 'Web Page'
    config._metadata['Tester'] = 'Rakshitha'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("PlUGINS", None)
