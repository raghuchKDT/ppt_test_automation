import pytest
import time
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import InvalidSessionIdException
from PageObjects.LoginPage import Login
from PageObjects.Usermanagerpage import usermanager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import random


class Test_002_usermanager:
    User = "Jogfalls"
    Pass = "pull"

    def test_usermanager(self, user_manager):
        self.driver = user_manager
        self.driver.implicitly_wait(2)
        self.um = usermanager(self.driver)
        time.sleep(1)
        self.um.clickusermanager()
        self.driver.implicitly_wait(2)

        # Validation of User Manager in Side Menu Bar
        exp_ele = ['User Manager']
        data_bas_ele = self.driver.find_elements(By.XPATH, "//*[@id='four']/span")

        for idx, bas_ele in enumerate(data_bas_ele):
            print(idx, bas_ele.text)
            assert (exp_ele[idx] == bas_ele.text)

    def test_Validationlevelmenubar(self, user_manager):
        self.driver = user_manager
        self.driver.implicitly_wait(2)
        self.um = usermanager(self.driver)
        time.sleep(1)
        self.um.clickusermanager()
        self.driver.implicitly_wait(2)

        level_element = ['User Manager\nRole']
        data_level_ele = self.driver.find_elements(By.XPATH, "//*[@id='pills-tab']")

        for idx, level_ele in enumerate(data_level_ele):
            print(idx, level_ele.text)
            assert (level_element[idx] == level_ele.text)

    def test_level3menubar(self, user_manager):
        self.driver = user_manager
        self.um = usermanager(self.driver)
        time.sleep(1)
        self.um.clickusermanager()
        self.driver.implicitly_wait(2)
        self.um = usermanager(self.driver)
        self.um.clickusermanager()
        self.driver.implicitly_wait(2)

        assert 'Local User' in self.driver.page_source

        assert 'Access Level' in self.driver.page_source

        assert 'Access Section' in self.driver.page_source

    def test_umnewuser(self, user_manager):
        self.driver = user_manager
        self.um = usermanager(self.driver)
        time.sleep(1)
        self.um.clickusermanager()
        self.driver.implicitly_wait(2)
        self.um.clickNew()
        self.driver.implicitly_wait(2)

        rand_user_name = ''.join((random.choice('aeiourtnslcpghd') for i in range(5)))

        self.um.User(rand_user_name)
        self.driver.implicitly_wait(4)
        self.um.Pass(self.Pass)
        self.driver.implicitly_wait(4)
        self.um.clicksave()
        time.sleep(2)

        assert 'Updated Successfully.' in self.driver.page_source

    def test_generalprop(self, user_manager):
        self.driver = user_manager
        self.driver.implicitly_wait(2)
        self.um = usermanager(self.driver)
        self.um.clickusermanager()
        self.driver.implicitly_wait(4)
        self.um.clickcheckkmark()
        time.sleep(2)

        assert 'User Name' in self.driver.page_source

        assert 'Password' in self.driver.page_source

        assert 'Shift' in self.driver.page_source

        assert 'Access Level' in self.driver.page_source

        time.sleep(2)

    def test_edituser(self, user_manager):
        self.driver = user_manager
        self.um = usermanager(self.driver)
        self.um.clickusermanager()
        self.driver.implicitly_wait(4)
        self.um.clickcheckkmark()
        self.driver.implicitly_wait(4)
        self.um.clickedit()

        self.driver.find_element(By.XPATH, "//*[@id='userName']").clear()
        self.driver.find_element(By.XPATH, "//*[@id='userName']").send_keys("ppt")

        user_manager.find_element(By.XPATH, "//*[@id='password']").clear()
        user_manager.find_element(By.XPATH, "//*[@id='password']").send_keys("New Password")

        self.um.clicksave()

    def test_userdelete(self, user_manager):
        self.driver = user_manager
        self.um = usermanager(self.driver)
        self.um.clickusermanager()
        self.driver.implicitly_wait(5)
        self.um.clickcheckkmark()
        self.driver.implicitly_wait(2)
        self.um.clickdelete()
        self.driver.implicitly_wait(2)
        self.um.clickdeletepopup()

        element3 = ['Deleted Successfully.']
        data_base_element3 = self.driver.find_elements(By.XPATH, "//*[contains(text(),'Deleted Successfully.')]")

        for idx, base_element3 in enumerate(data_base_element3):
            print(idx, base_element3.text)
            assert (element3[idx] == base_element3.text)

    def test_accesssection(self, user_manager):
        self.driver = user_manager
        self.um = usermanager(self.driver)
        self.um.clickuusermanager()

        # Validation of User Management in Access Section
        expected_el = ['User Management']
        data_base_el = self.driver.find_elements(By.XPATH, "//*[@id='3']/label")
        print(len(data_base_el))
        for idx, base_el in enumerate(data_base_el):
            print(idx, base_el.text)
            assert (expected_el[idx] == base_el.text)

        # Validation of Info in Access Section
        expected_el1 = ['Info']
        data_base_el1 = self.driver.find_elements(By.XPATH, "//*[@id='1']/label")
        for idx, base_el1 in enumerate(data_base_el1):
            print(idx, base_el1.text)
            assert (expected_el1[idx] == base_el1.text)

        # Validation of Project in Access Section

        expected_el2 = ['Project']
        data_base_el2 = self.driver.find_elements(By.XPATH, "//*[@id='2']/label")
        for idx, base_el2 in enumerate(data_base_el2):
            print(idx, base_el2.text)
            assert (expected_el2[idx] == base_el2.text)

        # Validation of System in Access Section

        expected_el3 = ['System']
        data_base_el3 = self.driver.find_elements(By.XPATH, "//*[@id='6']/label")
        for idx, base_el3 in enumerate(data_base_el3):
            print(idx, base_el3.text)
            assert (expected_el3[idx] == base_el3.text)

        # Validation of Project (Web HMI) in Access Section

        expected_el4 = ['Project']
        data_base_el4 = self.driver.find_elements(By.XPATH, "//*[@id='5']/label")
        for idx, base_el4 in enumerate(data_base_el4):
            print(idx, base_el4.text)
            assert (expected_el4[idx] == base_el4.text)

        # Validation of Run Test (Web HMI) in Access Section

        expected_el5 = ['Run test']
        data_base_el5 = self.driver.find_elements(By.XPATH, "//*[@id='4']/label")
        for idx, base_el5 in enumerate(data_base_el5):
            print(idx, base_el5.text)
            assert (expected_el5[idx] == base_el5.text)

        # Validation of Report (Web HMI) in Access Section

        expected_el6 = ['Report']
        data_base_el6 = self.driver.find_elements(By.XPATH, "//*[@id='7']/label")
        for idx, base_el6 in enumerate(data_base_el6):
            print(idx, base_el6.text)
            assert (expected_el6[idx] == base_el6.text)

