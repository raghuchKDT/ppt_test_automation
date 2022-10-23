from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time
from PageObjectModules.LoginPage import Login
from PageObjectModules.WirePage import Wire
from PageObjectModules.WirePage import WireColorScheme
import random

class Test_Wire:

    NewWireID = "124421"
    PushMinValue = "2"
    PushMaxValue = "5"
    PullMinValue = "1"
    PullMaxValue = "8"
    EditWireID = "159357"
    EditPushMinValue = "5"
    EditPushMaxValue = "10"
    EditPullMinValue = "2"
    EditPullMaxValue = "12"
    CopyWireID = "951753"

    def test_Wire_Color_Scheme_Table_Header(self, user_login):

        self.driver = user_login
        self.wireprop = Wire(self.driver)
        self.wireprop.clickProjectTab()
        self.wireprop.clickVariantTab()
        self.wireprop.clickWireTab()
        time.sleep(2)
        WireElement = 'Wire Color Scheme'
        wire_data_base_ele = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[3]/div[2]/div/div/h6")

        for idx, wire_data_base_ele in enumerate(wire_data_base_ele):
            print(idx, wire_data_base_ele.text)
            assert wire_data_base_ele.text in WireElement

    @pytest.mark.sanity()
    def test_CreateNew_Wire(self, user_login):

        self.driver = user_login
        self.wireprop = Wire(self.driver)
        self.wireprop.clickProjectTab()
        self.wireprop.clickVariantTab()
        self.wireprop.clickWireTab()
        self.wireprop.ClickNewWireButton()
        rand_wire_id = ''.join((random.choice('12345678910') for i in range(1)))
        self.wireprop.setNewWireID(rand_wire_id)
        rand_wiregroup_id = ''.join((random.choice('12345678910') for i in range(1)))
        self.wireprop.SelectGroupIDFromList(rand_wiregroup_id)
        self.wireprop.SelectColor1()
        time.sleep(2)
        self.wireprop.SelectColor2()
        time.sleep(2)
        self.wireprop.SelectColor3()
        time.sleep(2)
        rand_push_minval = ''.join((random.choice('1234567') for i in range(1)))
        self.wireprop.setPushMinValue(rand_push_minval)
        rand_push_maxval = ''.join((random.choice('123456798') for i in range(1)))
        self.wireprop.setPushMaxValue(rand_push_maxval)
        rand_pull_minval = ''.join((random.choice('123456789') for i in range(1)))
        self.wireprop.setPullMinValue(rand_pull_minval)
        rand_pull_maxval = ''.join((random.choice('123456789') for i in range(1)))
        self.wireprop.setPullMaxValue(rand_pull_maxval)
        self.wireprop.SelectPickToLightFromList()
        self.wireprop.SelectWLEDPinName()
        self.wireprop.NewWireClickSaveButton()
        time.sleep(2)
        assert "Wire Added successfully." in self.driver.page_source

    def test_Edit_Wire(self, user_login):

        self.driver = user_login
        self.wireprop = Wire(self.driver)
        self.wireprop.clickProjectTab()
        self.wireprop.clickVariantTab()
        self.wireprop.clickWireTab()
        self.wireprop.SelectWire()
        self.wireprop.ClickEditWireButton()
        rand_wire_edit = ''.join((random.choice('wire12345673') for i in range(4)))
        self.wireprop.setEditWireID(rand_wire_edit)
        self.wireprop.EditGroupIDFromList()
        self.wireprop.EditColor1()
        self.wireprop.EditColor2()
        self.wireprop.EditColor3()
        rand_pushedit_minval = ''.join((random.choice('1234567') for i in range(1)))
        self.wireprop.setPushMinValue(rand_pushedit_minval)
        rand_pushedit_maxval = ''.join((random.choice('123') for i in range(2)))
        self.wireprop.setPushMaxValue(rand_pushedit_maxval)
        rand_pulledit_minval = ''.join((random.choice('1234') for i in range(2)))
        self.wireprop.setPullMinValue(rand_pulledit_minval)
        rand_pulledit_maxval = ''.join((random.choice('123') for i in range(2)))
        self.wireprop.setPullMaxValue(rand_pulledit_maxval)
        self.wireprop.EditPickToLightFromList()
        self.wireprop.EditWLEDPinName()
        self.wireprop.EditWireClickUpdateButton()
        time.sleep(2)
        assert "Wire Updated successfully." in self.driver.page_source

    def test_Copy_Wire(self, user_login):

        self.driver = user_login
        self.wireprop = Wire(self.driver)
        self.wireprop.clickProjectTab()
        self.wireprop.clickVariantTab()
        self.wireprop.clickWireTab()
        self.wireprop.SelectWire()
        self.wireprop.ClickWireCopyButton()
        rand_wire_copy = ''.join((random.choice('wire12345673') for i in range(4)))
        self.wireprop.setCopyWireID(rand_wire_copy)
        self.wireprop.CopyWireClickSaveAsButton()
        time.sleep(2)
        assert "New wire created successfully" in self.driver.page_source

    def test_Wire_Delete(self, user_login):

        self.driver = user_login
        self.wireprop = Wire(self.driver)
        self.wireprop.clickProjectTab()
        self.wireprop.clickVariantTab()
        self.wireprop.clickWireTab()
        self.wireprop.SelectWire()
        self.wireprop.WireClickDeleteButton()
        self.wireprop.WireConfirmDelete()
        time.sleep(2)
        assert "wire deleted successfully" in self.driver.page_source

class Test_WireColorScheme:

    NewWireColorSchemeName = "Brown"
    NewWireColorSchemeAbbreviation = "BR"
    EditWireColorSchemeName = "Orange"
    EditWireColorSchemeAbbreviation = "OR"

    @pytest.mark.sanity()
    def test_CreateNew_WireColorScheme(self, user_login):

        self.driver = user_login
        self.wireprop = WireColorScheme(self.driver)
        self.wireprop.clickProjectTab()
        self.wireprop.clickVariantTab()
        self.wireprop.clickWireTab()
        self.wireprop.ClickNewWireSchemeColorButton()
        self.wireprop.setNewWireColorSchemeName(self.NewWireColorSchemeName)
        self.wireprop.setNewWireColorSchemeAbbreviation(self.NewWireColorSchemeAbbreviation)
        self.wireprop.ClickWireColorArea()
        self.wireprop.ClickWireColorSchemeSaveButton()
        time.sleep(2)
        assert "Color Scheme Added successfully." in self.driver.page_source

    def test_Edit_WireColorScheme(self, user_login):

        self.driver = user_login
        self.wireprop = WireColorScheme(self.driver)
        self.wireprop.clickProjectTab()
        self.wireprop.clickVariantTab()
        self.wireprop.clickWireTab()
        self.wireprop.SelectWireColorScheme()
        self.wireprop.ClickEditWireSchemeColorButton()
        self.wireprop.setEditWireColorSchemeName(self.EditWireColorSchemeName)
        self.wireprop.setEditWireColorSchemeAbbreviation(self.EditWireColorSchemeAbbreviation)
        self.wireprop.ClickWireColorArea()
        self.wireprop.ClickWireColorSchemeUpdateButton()
        time.sleep(2)
        assert "Color Scheme Updated successfully." in self.driver.page_source

    def test_WireColorScheme_Delete(self, user_login):
        self.driver = user_login
        self.wireprop = WireColorScheme(self.driver)
        self.wireprop.clickProjectTab()
        self.wireprop.clickVariantTab()
        self.wireprop.clickWireTab()
        self.wireprop.SelectWireColorScheme()
        self.wireprop.WireColorSchemeClickDeleteButton()
        self.wireprop.WireColorSchemeConfirmDelete()
        time.sleep(2)
        assert "Deleted Successfully." in self.driver.page_source
