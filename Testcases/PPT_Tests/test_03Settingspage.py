import pytest
import time
from selenium import webdriver
from PageObjectModules.LoginPage import Login
from PageObjectModules.SettingsPage import Settings
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import InvalidSessionIdException
import random

class Test_004_Settings:

    ProjName = "projectsk"
    ProjDesc = "protest"
    SaveAs = "look"
    switchGroup = "Leaktest1"
    projectname = "tsk"
    projdesc = "something blue "

    def test_projectscreen(self, user_login):
        self.driver = user_login
        self.driver.implicitly_wait(2)
        self.pj = Settings(self.driver)
        self.pj.Project()


        # Validation of Project in Side Menu Bar
        expected_element = ['Project']
        data_base_element = self.driver.find_elements(By.XPATH, "//*[@id='three']")

        for idx, base_element in enumerate(data_base_element):
            print(idx, base_element.text)
            assert (expected_element[idx] == base_element.text)

    @pytest.mark.sanity()
    def test_new_project(self, user_login):
        self.driver = user_login
        self.pj = Settings(self.driver)
        self.pj.Project()
        self.pj.clicknew()

        rand_project_name = ''.join((random.choice('aeiourtnslcrp')for i in range (5)))

        self.pj.setpn(rand_project_name)
        self.pj.setpd(self.ProjDesc)
        self.pj.ClickDevMang()
        self.pj.selectSysGrp()
        self.pj.clickSave()

        time.sleep(2)
        assert 'Updated Successfully.' in self.driver.page_source

    def test_general_prop(self, user_login):
        self.driver = user_login
        self.pj = Settings(self.driver)
        time.sleep(2)
        self.pj.Project()

        # Validation of General Properties in Settings Page
        expected_el = ['Project Name']
        time.sleep(2)
        data_base_el = self.driver.find_elements(By.XPATH, "//*[@id='collapseOne']/div/div[1]/div/div/div[1]")

        for idx, base_el in enumerate(data_base_el):
            print(idx, base_el.text)
            assert (expected_el[idx] == base_el.text)

        expected_el = ['Description']
        time.sleep(2)
        data_base_el = self.driver.find_elements(By.XPATH, "//*[@id='collapseOne']/div/div[1]/div/div/div[3]/div/h5")

        for idx, base_el in enumerate(data_base_el):
            print(idx, base_el.text)
            assert (expected_el[idx] == base_el.text)

    def test_project_edit(self, user_login):
        self.driver = user_login
        self.pj = Settings(self.driver)
        self.pj.Project()
        # self.pj.clickcheck()
        time.sleep(1)
        self.pj.clickedit()

        self.driver.find_element(By.XPATH, "//*[@id='ProjName']").clear()
        self.driver.find_element(By.XPATH, "//*[@id='ProjName']").send_keys("ppt")

        self.driver.find_element(By.XPATH, "//*[@id='Projdesc']").clear()
        self.driver.find_element(By.XPATH, "//*[@id='Projdesc']").send_keys("new project")

        self.pj.clickSave()
        time.sleep(2)
        assert 'Updated Successfully.' in self.driver.page_source

    def test_delete_project(self, user_login):
        self.driver = user_login
        self.pj = Settings(self.driver)
        self.pj.Project()
        # self.pj.clickcheck()
        self.pj.deleteproj()
        self.pj.popupdeleteproj()
        time.sleep(2)
        assert 'Deleted Successfully.' in self.driver.page_source

    def test_multiple_delete(self, user_login):
        self.driver = user_login
        self.pj = Settings(self.driver)
        self.pj.Project()
        self.pj.clickmultipledelete()
        time.sleep(2)
