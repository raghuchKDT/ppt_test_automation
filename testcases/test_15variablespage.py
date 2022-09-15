import pytest
import time
from selenium import webdriver
from PageObjects.LoginPage import Login
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import InvalidSessionIdException
from PageObjects.Variablespage import Variables


class Test010_Variables:

    def test_variablescreen(self, user_login):
        self.driver = user_login
        self.vb = Variables(self.driver)
        self.vb.Project()
        self.driver.implicitly_wait(4)
        self.vb.clickvariant()
        self.vb.clickvariables()
        time.sleep(2)
        assert 'Variables' in self.driver.page_source

    def test_variablestable(self, user_login):
        self.driver = user_login
        self.vb = Variables(self.driver)
        self.driver.implicitly_wait(4)
        self.vb.Project()
        self.driver.implicitly_wait(4)
        self.vb.clickvariant()
        self.vb.clickvariables()

        time.sleep(2)
        table = self.driver.find_element(By.ID, "tblVariantGlobalVar")
        body = table.find_element(By.TAG_NAME, "tbody")
        cells = body.find_elements(By.TAG_NAME, "td")
        for cell in cells:
            print(cell.text)
