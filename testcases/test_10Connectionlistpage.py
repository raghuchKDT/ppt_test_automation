import pytest
import time
from selenium import webdriver
from PageObjects.LoginPage import Login
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import InvalidSessionIdException
from PageObjects.Connectionlist import Connectionlist
import random


class Test009_NetList:
    ListName = 'netlist5'
    ListDesc = 'this is the new connection netlist'

    def test_Levelmenubar(self, user_login):
        self.driver = user_login
        self.cl = Connectionlist(self.driver)
        self.cl.Project()
        self.driver.implicitly_wait(4)
        self.cl.clickvariant()
        self.cl.clicknetlist()
        time.sleep(2)

        element22 = 'Connection List'
        data_base_ele22 = self.driver.find_elements(By.XPATH, "//*[@id='pills-connectionlist-tab']")

        for idx, base_ele22 in enumerate(data_base_ele22):
            print(idx, base_ele22.text)
            assert base_ele22.text in element22
        # assert 'Net List' in self.driver.page_source


    def test_connectionlist(self, user_login):
        self.driver = user_login
        self.cl = Connectionlist(self.driver)
        self.cl.Project()
        self.driver.implicitly_wait(4)
        self.cl.clickvariant()
        self.cl.clicknetlist()
        self.cl.clickconnectionlist()
        time.sleep(2)
        assert 'Connection List' in self.driver.page_source

    def test_create_newlist(self, user_login):
        self.driver = user_login
        self.cl = Connectionlist(self.driver)
        self.cl.Project()
        self.driver.implicitly_wait(4)
        self.cl.clickvariant()
        self.cl.clicknetlist()
        self.cl.clicknewlist()
        time.sleep(1)

        rand_new_list = ''.join((random.choice('aeiournstlcp')for i in range(5)))

        self.driver.find_element(By.XPATH, "//*[@id='txtNewConnectionListName']").clear()
        self.driver.find_element(By.XPATH, "//*[@id='txtNewConnectionListName']").send_keys(rand_new_list)

        self.driver.find_element(By.XPATH, "//*[@id='txtNewConnectionListDescription']").clear()
        self.driver.find_element(By.XPATH, "//*[@id='txtNewConnectionListDescription']").send_keys("this is the new connection netlist")

        time.sleep(1)
        self.cl.clicksavelist()
        time.sleep(2)
        assert 'Connection List Details Added successfully.' in self.driver.page_source

    def test_copy_list(self, user_login):
        self.driver = user_login
        self.cl = Connectionlist(self.driver)
        self.cl.Project()
        self.driver.implicitly_wait(4)
        self.cl.clickvariant()
        self.cl.clicknetlist()
        self.cl.clickcheckmarklist()
        self.cl.clickcopylist()

        rand_edit_list = ''.join((random.choice('aeiournstlcp') for i in range(5)))

        self.driver.find_element(By.XPATH, "//*[@id='txtCopyNewConnectionName']").clear()
        self.driver.find_element(By.XPATH, "//*[@id='txtCopyNewConnectionName']").send_keys(rand_edit_list)

        self.driver.find_element(By.XPATH, "//*[@id='txtCopyNewConnectionListDescription']").clear()
        self.driver.find_element(By.XPATH, "//*[@id='txtCopyNewConnectionListDescription']").send_keys("this is netlist")

        self.cl.clicksaveaslist()
        time.sleep(2)

        assert 'Connection List Details Added successfully.' in self.driver.page_source

    def test_deletelist(self, user_login):
        self.driver = user_login
        self.cl = Connectionlist(self.driver)
        self.cl.Project()
        self.driver.implicitly_wait(4)
        self.cl.clickvariant()
        self.cl.clicknetlist()
        self.cl.clickcheckmarklist()
        self.cl.deletelist()
        self.cl.popupdeletelist()

        time.sleep(2)
        assert 'Deleted Successfully.' in self.driver.page_source
