from selenium import webdriver
import pytest
from PageObjects.LoginPage import Login
# from PageObjects.UserManager import usermanager
import time

global driver
username = "admin"
password = "admin"
baseURL = "http://localhost:5003/"
chrome_path = "C:\\Downloads\\chromedriver.exe"
test = 5

@pytest.fixture(scope="session")
def setup():
    driver = webdriver.Chrome(chrome_path)
    time.sleep(2)
    driver.get(baseURL)
    driver.maximize_window()
    yield driver
    time.sleep(2)
    driver.close()



@pytest.fixture (scope="session")
def user_login():
    global driver
    print("-----------setup------------")
    driver = webdriver.Chrome(chrome_path)
    driver.get(baseURL)
    driver.maximize_window()
    lp = Login(driver)
    lp.setUserName(username)
    lp.setPassword(password)
    lp.clickLogin()
    time.sleep(2)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def user_manager():
    global driver
    print("-----------setup------------")
    driver = webdriver.Chrome(chrome_path)
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
