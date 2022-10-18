from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time
from PageObjectModules.LoginPage import Login
from PageObjectModules.PickToLightPage import PickToLight
import random

class Test_PickToLight:

    NewPickToLightName = "PickToLight 3"
    EditPickToLightName = "PickToLight 4"
    CopyPickToLightName = "PickToLight 5"
    NewPickToLightDescrption = "This is the PickToLight 3"
    EditPickToLightDescrption = "This is the PickToLight 4"
    CopyPickToLightDescrption = "This is the PickToLight 5"
    NewPickToLightLEDNo = "3"
    EditPickToLightLEDNo = "4"

    def test_PickToLight_table_Header(self, user_login):

        self.driver = user_login
        self.projprop = PickToLight(self.driver)
        self.projprop.clickProjectTab()
        self.projprop.clickPickToLightTab()
        table = self.driver.find_element(By.ID, "loadPickToLightData")
        header = table.find_elements(By.TAG_NAME, "th")
        for headerEl in header:
            print(headerEl.text)
        time.sleep(2)
        assert "Pick To Light Name" in self.driver.page_source

    @pytest.mark.sanity()
    def test_CreateNew_PickToLight(self, user_login):
        self.driver = user_login
        self.projprop = PickToLight(self.driver)
        self.projprop.clickProjectTab()
        self.driver.implicitly_wait(4)
        self.projprop.clickPickToLightTab()
        self.projprop.ClickNewPickToLightButton()

        rand_ptl_name = ''.join((random.choice('aeiourtsndlcp') for i in range(5)))
        self.projprop.setNewPickToLighteName(rand_ptl_name)
        self.projprop.setNewPickToLightDesc(self.NewPickToLightDescrption)
        self.projprop.setNewPickToLightLED_No(self.NewPickToLightLEDNo)
        self.projprop.NewPickToLightClickSaveButton()
        time.sleep(2)
        assert "Pick To Light Added successfully" in self.driver.page_source

    def test_PickToLight_Prop(self, user_login):

        self.driver = user_login
        self.projprop = PickToLight(self.driver)
        self.projprop.clickProjectTab()
        self.projprop.clickPickToLightTab()
        self.projprop.SelectPickToLightFromTable()
        time.sleep(2)
        Ptlprop = self.driver.find_elements(By.XPATH, "//*[@id='collapsePickSysDescBelow']")
        print(len(Ptlprop))
        expected = ['Description', 'Pick to Light LED No']
        contents = []
        for ptl in Ptlprop:
            contents.append(ptl.text)
        for ptls in expected:
            assert (ptls in contents[0]) == True

    def test_Edit_PickToLight(self, user_login):
        self.driver = user_login
        self.projprop = PickToLight(self.driver)
        self.projprop.clickProjectTab()
        self.projprop.clickPickToLightTab()
        self.projprop.SelectPickToLightEdit()
        self.projprop.ClickEditButton()
        rand_ptl_name = ''.join((random.choice('aeiourtsndlcp') for i in range(5)))
        self.projprop.setEditPickToLightName(rand_ptl_name)
        self.projprop.setEditPickToLightDesc(self.EditPickToLightDescrption)
        self.projprop.setEditPickToLightLED_No(self.EditPickToLightLEDNo)
        self.projprop.EditPickToLightClickSaveButton()
        time.sleep(2)
        assert "Pick To Light Updated successfully" in self.driver.page_source

    def test_Copy_PickToLight(self, user_login):
        self.driver = user_login
        self.projprop = PickToLight(self.driver)
        self.projprop.clickProjectTab()
        self.driver.implicitly_wait(4)
        self.projprop.clickPickToLightTab()
        self.projprop.SelectPickToLightCopy()
        self.projprop.PickToLightClickCopyButton()
        rand_ptl_name = ''.join((random.choice('aeiourtsndlcp') for i in range(5)))
        self.projprop.setCopyPickToLightName(rand_ptl_name)
        self.projprop.setCopyPickToLightDesc(self.CopyPickToLightDescrption)
        self.projprop.CopyPickToLightClickSaveButton()
        time.sleep(2)
        assert "Added Successfully." in self.driver.page_source

    def test_PickToLight_Delete(self, user_login):

        self.driver = user_login
        self.projprop = PickToLight(self.driver)
        self.projprop.clickProjectTab()
        self.driver.implicitly_wait(4)
        self.projprop.clickPickToLightTab()
        self.projprop.SelectPickToLightDelete()
        self.projprop.PickToLightClickDeleteButton()
        self.projprop.PickToLightConfirmDelete()
        time.sleep(2)
        assert "Pick To Light Deleted successfully" in self.driver.page_source
