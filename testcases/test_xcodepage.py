from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time
from PageObjects.LoginPage import Login
from PageObjects.XcodePage import XCode
import random

class Test_XCode:

    NewXCodeName = "Test Dj-1 Xcode"
    NewXCodeDesc = "This is the testing xcode description"
    NewXCodeCustomerID = "2"
    EditXCodeName = "TestXCodeDJ1"
    EditXCodeCustomerID = "3"
    EditXCodeDesc = "This is the third xcode descriptions"
    EditXCodeCTPPin1Name = "p8"
    EditXCodeCTPPin2Name = "p9"
    CopyXCodeName = "Dj xCode 3"
    CopyXCodeCustomerID = "4"
    CopyXCodeDesc = "This is the copy of Test-Dj-XCode 2"

    def test_XCode_Table_Header(self, user_login):
        self.driver = user_login
        self.xcodeprop = XCode(self.driver)
        self.xcodeprop.clickProjectTab()
        self.xcodeprop.clickVariantTab()
        self.xcodeprop.clickXCodeTab()
        xCodeelement = ''
        xCode_data_base_ele = self.driver.find_elements(By.XPATH, "//*[@id='xcodedatas']/div/div[1]")

        for idx, xCode_data_base_ele in enumerate(xCode_data_base_ele):
            print(idx, xCode_data_base_ele.text)
            assert xCode_data_base_ele.text in xCodeelement

    def test_CreateNew_xCode(self, user_login):

        self.driver = user_login
        self.xcodeprop = XCode(self.driver)
        self.xcodeprop.clickProjectTab()
        self.xcodeprop.clickVariantTab()
        self.xcodeprop.clickXCodeTab()
        self.xcodeprop.ClickNewXCodeButton()

        rand_xcode_newname = ''.join((random.choice('aeiourtsndlcp') for i in range(5)))

        self.xcodeprop.setNewXCodeName(rand_xcode_newname)
        self.xcodeprop.setNewXCodeCustomerID(self.NewXCodeCustomerID)
        self.xcodeprop.setNewXCodeDesc(self.NewXCodeDesc)
        self.xcodeprop.SelectXCodeModulefromDropDownList()
        self.xcodeprop.ClickNewChooseFile()
        element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/input[3]")
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.xcodeprop.NewXCodeClickSaveButton()
        time.sleep(2)
        assert "XCode Added successfully." in self.driver.page_source

    def test_xCode_Prop(self, user_login):

        self.driver = user_login
        self.xcodeprop = XCode(self.driver)
        self.xcodeprop.clickProjectTab()
        self.xcodeprop.clickVariantTab()
        self.xcodeprop.clickXCodeTab()
        self.xcodeprop.SelectXCode()
        time.sleep(2)
        xCodeprop = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[4]/div/div/div[2]/div")
        print(len(xCodeprop))
        expected = ['XCode Name', 'Customer ID', 'Description']
        contents = []
        for var in xCodeprop:
            contents.append(var.text)
        for expvar in expected:
            assert (expvar in contents[0]) == True

    def test_Edit_xCode(self, user_login):

        self.driver = user_login
        self.xcodeprop = XCode(self.driver)
        self.xcodeprop.clickProjectTab()
        self.xcodeprop.clickVariantTab()
        self.xcodeprop.clickXCodeTab()
        self.xcodeprop.SelectXCode()
        self.xcodeprop.ClickXCodeEditButton()

        rand_edit_xcode = ''.join((random.choice('aeiourtsndlcp') for i in range(5)))
        self.xcodeprop.setEditXCodeName(rand_edit_xcode)
        self.xcodeprop.setEditXCodeCustomerID(self.EditXCodeCustomerID)
        self.xcodeprop.setEditXCodeDesc(self.EditXCodeDesc)
        self.xcodeprop.ClickEditChooseFile()
        element2 = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[2]/div[3]/div/div/div[2]/input[3]")
        self.driver.execute_script("arguments[0].scrollIntoView();", element2)
        self.xcodeprop.EditXCodeClickSaveButton()
        time.sleep(2)
        assert "XCode Updated successfully." in self.driver.page_source

    # def test_Edit_xCodePinsAndIcon(self, user_login):
    #
    #     self.driver = user_login
    #     self.xcodeprop = XCode(self.driver)
    #     self.xcodeprop.clickProjectTab()
    #     self.xcodeprop.clickVariantTab()
    #     self.xcodeprop.clickXCodeTab()
    #     self.xcodeprop.SelectXCode()
    #     self.xcodeprop.setEditXCodeCTPPin1Name(self.EditXCodeCTPPin1Name)
    #     self.xcodeprop.setEditXCodeCTPPin2Name(self.EditXCodeCTPPin2Name)
    #     self.xcodeprop.SelectXCodeSwitchStatusFromList()
    #     self.xcodeprop.XCodeSwitchSelectCheckbox()
    #     self.xcodeprop.XCodeClickUpdateButton()
    #     time.sleep(2)
    #     assert "Data Updated successfully." in self.driver.page_source

    def test_Copy_XCode(self, user_login):

        self.driver = user_login
        self.xcodeprop = XCode(self.driver)
        self.xcodeprop.clickProjectTab()
        self.xcodeprop.clickVariantTab()
        self.xcodeprop.clickXCodeTab()
        self.xcodeprop.SelectXCode()
        self.xcodeprop.ClickXCodeCopyButton()
        self.xcodeprop.SelectXCodeFromList()

        rand_copy_xcode = ''.join((random.choice('aeiourtsndlcp') for i in range(5)))
        self.xcodeprop.setCopyXCodeName(rand_copy_xcode)
        self.xcodeprop.setCopyXCodeCustomerID(self.CopyXCodeCustomerID)
        self.xcodeprop.setCopyXCodeDesc(self.CopyXCodeDesc)
        self.xcodeprop.CopyXCodeClickSaveButton()
        time.sleep(2)
        assert "Added Successfully." in self.driver.page_source

    def test_XCode_Delete(self, user_login):
        self.driver = user_login
        self.xcodeprop = XCode(self.driver)
        self.xcodeprop.clickProjectTab()
        self.xcodeprop.clickVariantTab()
        self.xcodeprop.clickXCodeTab()
        self.xcodeprop.SelectXCodeDelete()
        self.xcodeprop.XCodeClickDeleteButton()
        self.xcodeprop.XCodeConfirmDelete()
        time.sleep(2)
        assert "Deleted Successfully." in self.driver.page_source
