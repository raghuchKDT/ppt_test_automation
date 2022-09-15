import pytest
import time
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from PageObjects.LoginPage import Login
from PageObjects.Usermanagerpage import usermanager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from array import *
from selenium.common.exceptions import InvalidSessionIdException
import random


class Test_003_Role:

    roleName = "ppt"
    rolename = "Pull"

    def test_Rolescreen(self,user_manager):
        self.driver = user_manager
        self.um = usermanager(self.driver)
        self.um.clickuusermanager()
        self.um.clickRole()


        # Validation of Role
        expected_ele = ['Role']
        data_base_element = self.driver.find_elements(By.XPATH, "//*[@id='pills-device-tab']")

        for idx, base_element in enumerate(data_base_element):
            print(idx, base_element.text)
            assert (expected_ele[idx] == base_element.text)

    def test_create_newrole(self, user_manager):
        self.driver = user_manager
        self.um = usermanager(self.driver)
        self.um.clickuusermanager()
        self.um.clickRole()
        self.um.clickrolenew()

        rand_role_name = ''.join((random.choice('aieourtnslcp')for i in range (5)))

        self.um.setroleName(rand_role_name)
        self.um.clicksaverole()
        time.sleep(2)

        assert 'Updated Successfully.' in self.driver.page_source

    def test_editrole(self, user_manager):
        self.driver = user_manager
        self.um = usermanager(self.driver)
        self.um.clickuusermanager()
        self.um.clickRole()
        self.um.clickcheck()
        self.um.clickeditrole()

        user_manager.find_element(By.XPATH, "//*[@id='roleName']").clear()
        user_manager.find_element(By.XPATH, "//*[@id='roleName']").send_keys("tsk")

        self.um.clicksaverole()

        # assert "tsk" in self.driver.page_source

    def test_Roledelete(self,user_manager):
        self.driver = user_manager
        self.um = usermanager(self.driver)
        self.um.clickuusermanager()
        self.um.clickRole()
        self.um.clickcheck()
        self.um.clickroledelete()
        self.um.deletepopup()

        #  Validation of new user in role
        element2 = ['Deleted Successfully.']
        data_base_element2 = self.driver.find_elements(By.XPATH, "//*[contains(text(),'Deleted Successfully.')]")

        for idx, base_element2 in enumerate(data_base_element2):
            print(idx, base_element2.text)
            assert (element2[idx] == base_element2.text)
