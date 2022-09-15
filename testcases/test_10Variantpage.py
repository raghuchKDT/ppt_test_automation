from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time
from PageObjects.LoginPage import Login
from PageObjects.VariantPage import Variant
import random

class Test_Variant:

    NewVariantName = "Test-Dj 2"
    NewVariantDesc = "This ia the description of Variant"
    EditVariantName = "Variant Test Dj-2"
    EditVariantDesc = "This is the modified variant"
    CopyVariantName = "Test -Dj- 4"

    def test_Variant_Header(self, user_login):
        self.driver = user_login
        self.variantprop = Variant(self.driver)
        self.variantprop.clickProjectTab()
        time.sleep(2)
        self.variantprop.clickVariantTab()
        time.sleep(2)

        Varelement = ['Variant Name']
        Var_data_base_ele = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/div/table/thead/tr/th[2]")

        for idx, Var_data_base_ele in enumerate(Var_data_base_ele):
            print(idx, Var_data_base_ele.text)
            assert Var_data_base_ele.text in Varelement

    def test_Variant_Prop(self, user_login):

        self.driver = user_login
        self.variantprop = Variant(self.driver)
        self.variantprop.clickProjectTab()
        self.variantprop.clickVariantTab()
        time.sleep(2)

        Varprop = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[1]/div/div[3]/div[1]")
        print(len(Varprop))
        expected = ['Variant Name', 'Description', 'Date Created']
        contents = []
        for var in Varprop:
            contents.append(var.text)
        for expvar in expected:
            assert (expvar in contents[0]) == True

    def test_CreateNew_Variant(self, user_login):
        self.driver = user_login
        self.variantprop = Variant(self.driver)
        self.variantprop.clickProjectTab()
        self.driver.implicitly_wait(4)
        self.variantprop.clickVariantTab()
        self.variantprop.ClickNewVariantButton()
        rand_new_variant = ''.join((random.choice('aeiournstlcp')for i in range(5)))

        self.variantprop.setNewVariantName(rand_new_variant)
        self.variantprop.setNewVariantDesc(self.NewVariantDesc)
        self.variantprop.NewVariantClickSaveButton()
        time.sleep(2)
        assert 'Updated Successfully.' in self.driver.page_source

    def test_Edit_Variant(self, user_login):
        self.driver = user_login
        self.variantprop = Variant(self.driver)
        self.variantprop.clickProjectTab()
        self.driver.implicitly_wait(4)
        self.variantprop.clickVariantTab()
        self.variantprop.ClickVariantEditButton()
        rand_edit_variant = ''.join((random.choice('aeiournstlcp') for i in range(5)))

        self.variantprop.setEditVariantName(rand_edit_variant)
        self.variantprop.setEditVariantDesc(self.EditVariantDesc)
        self.variantprop.EditVariantClickSaveButton()
        time.sleep(2)
        assert "Updated Successfully." in self.driver.page_source

    def test_Copy_Variant(self, user_login):
        self.driver = user_login
        self.variantprop = Variant(self.driver)
        self.variantprop.clickProjectTab()
        self.driver.implicitly_wait(4)
        self.variantprop.clickVariantTab()
        self.variantprop.ClickVariantCopyButton()
        rand_copy_variant = ''.join((random.choice('aeiournstlcp') for i in range(5)))

        self.variantprop.setCopyVariantName(rand_copy_variant)
        self.variantprop.CopyVariantClickSaveButton()
        time.sleep(2)
        assert "Data Added Successfully." in self.driver.page_source

    def test_Variant_Delete(self, user_login):

        self.driver = user_login
        self.variantprop = Variant(self.driver)
        self.variantprop.clickProjectTab()
        self.driver.implicitly_wait(4)
        self.variantprop.clickVariantTab()
        self.variantprop.VariantClickDeleteButton()
        self.variantprop.VariantConfirmDelete()
        time.sleep(2)
        assert "Deleted Successfully." in self.driver.page_source
