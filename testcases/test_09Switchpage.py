import pytest
import time
from selenium import webdriver
from PageObjects.LoginPage import Login
from PageObjects.Switchpage import Switch
from PageObjects.Settingspage import Settings
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import InvalidSessionIdException
import random


class Test005_Switch:
    switchGroup = "LT2"
    SwitchGroup = "Leaktest"

    def test_switch_screen(self, user_login):
        self.driver = user_login
        self.sw = Switch(self.driver)
        time.sleep(1)
        self.sw.Project()
        self.sw.clickswitch()

        # Validation of Switch in Side Menu Bar
        expected_element4 = ['Switch']
        data_base_element4 = self.driver.find_elements(By.XPATH, "//*[@id='pills-switch-tab']")

        for idx, base_element4 in enumerate(data_base_element4):
            print(idx, base_element4.text)
            assert (expected_element4[idx] == base_element4.text)

    def test_create_newswitch(self, user_login):
        self.driver = user_login
        self.sw = Switch(self.driver)
        self.sw.Project()
        self.sw.clickswitch()
        self.sw.clickNew()

        rand_switch_name = ''.join((random.choice('aeiourtnslcp') for i in range(5)))

        self.sw.setswitchGroup(rand_switch_name)
        self.sw.save()
        # time.sleep(2)
        # assert 'Updated Successfully.' in self.driver.page_source

    def test_switch_delete(self, user_login):
        self.driver = user_login
        self.sw = Switch(self.driver)
        time.sleep(1)
        self.sw.Project()
        self.sw.clickswitch()
        self.sw.clickcheckmark()
        self.sw.clickdelete()
        self.sw.clickdeleteswitch()
        time.sleep(1)
        assert 'Deleted Successfully.' in self.driver.page_source

    def test_switch_edit(self, user_login):
        self.driver = user_login
        self.sw = Switch(self.driver)
        self.sw.Project()
        self.sw.clickswitch()
        self.sw.clickcheckmark()
        self.sw.clickeditswitch()

        rand_switch_edit = ''.join((random.choice('aeiourtnstlcp')for i in range(5)))

        self.driver.find_element(By.XPATH, "//*[@id='switchGroup']").clear()
        self.driver.find_element(By.XPATH, "//*[@id='switchGroup']").send_keys(rand_switch_edit)

        self.sw.save()
        # time.sleep(1)
        # assert 'Updated Successfully.' in self.driver.page_source

    def test_multiple_delete(self, user_login):
        self.driver = user_login
        self.sw = Switch(self.driver)
        self.sw.Project()
        self.sw.clickswitch()
        self.sw.clickmultipledelete()
        time.sleep(1)
        