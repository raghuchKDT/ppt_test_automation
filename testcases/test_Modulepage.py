from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time
from PageObjects.LoginPage import Login
from PageObjects.ModulePage import Module
import random

class Test_Module:
    ModuleName = "Module 5"
    ModuleName1 = "Module 501"
    ModuleName2 = "Module 6"
    ModuleDescrption = "This is the fifth Module"
    ModuleDescrption1 = "This is the 501 module"
    ModuleDescrption2 = "This is the sixth Module"
    No_of_Cavity = "3"
    No_of_Cavity1 = "2"
    No_of_Switch = "2"
    No_of_Switch1 = "1"
    No_of_Module_LED = "3"
    No_of_Module_LED1 = "2"

    def test_Module_table_Header(self, user_login):

        self.driver = user_login
        self.projprop = Module(self.driver)
        self.projprop.clickProjectTab()
        self.projprop.clickModuleTab()
        table = self.driver.find_element(By.ID, "loadModuleData")
        header = table.find_elements(By.TAG_NAME, "th")
        for headerEl in header:
            print(headerEl.text)

    def test_Module_Prop(self, user_login):

        self.driver = user_login
        self.projprop = Module(self.driver)
        self.projprop.clickProjectTab()
        time.sleep(2)
        self.projprop.clickModuleTab()
        self.projprop.ClickModule()
        time.sleep(2)
        mprop = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/main/div[3]/div/div[3]/div/div/div[1]/span[2]")
        print(len(mprop))
        expected = ['Module Pin', 'Description', 'Module Board COMM Pin', 'Number of Cavity', 'Number of Switch', 'Module Cavity LED No']
        contents = []
        for mp in mprop:
            contents.append(mp.text)
        for mps in expected:
            assert (mps in contents[0]) == True

    def test_CreateNew_Module(self, user_login):
        self.driver = user_login
        self.projprop = Module(self.driver)
        self.projprop.clickProjectTab()
        self.projprop.clickModuleTab()
        self.projprop.ClickNewModule()
        rand_new_module = ''.join((random.choice('aeiournstlcp') for i in range(5)))
        self.projprop.setNewModuleName(rand_new_module)
        self.projprop.setNewModuleDesc(self.ModuleDescrption)
        rand_newcavity_no = ''.join((random.choice('12345678') for i in range(1)))
        self.projprop.setNewModuleNo_Cavity(rand_newcavity_no)
        rand_newswitch_no = ''.join((random.choice('12345678') for i in range(1)))
        self.projprop.setNewModuleNo_Switch(rand_newswitch_no)
        rand_newcavityled_no = ''.join((random.choice('12345678') for i in range(1)))
        self.projprop.setNewModuleCavityLED_no(rand_newcavityled_no)
        time.sleep(2)
        self.projprop.ClickChooseFile()
        element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div[8]/div/div/div[2]/input[6]")
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.projprop.ClickChooseFile()
        self.projprop.NewModuleclickSave()
        time.sleep(2)
        assert "Module Added successfully" in self.driver.page_source

    def test_Edit_Module(self, user_login):
        self.driver = user_login
        self.projprop = Module(self.driver)
        self.projprop.clickProjectTab()
        self.projprop.clickModuleTab()
        self.projprop.ClickModule()
        self.projprop.ClickEditModule()
        rand_edit_module = ''.join((random.choice('aeiournstlcp') for i in range(5)))
        self.projprop.setEditModuleDesc(rand_edit_module)
        self.projprop.setEditModuleDesc(self.ModuleDescrption)
        rand_editcavity_no = ''.join((random.choice('12345678') for i in range(1)))
        self.projprop.setEditModuleNo_Cavity(rand_editcavity_no)
        rand_editswitch_no = ''.join((random.choice('12345678') for i in range(1)))
        self.projprop.setEditModuleNo_Switch(rand_editswitch_no)
        rand_editcavityled_no = ''.join((random.choice('12345678') for i in range(1)))
        self.projprop.setEditModuleCavityLED_no(rand_editcavityled_no)
        time.sleep(2)
        self.projprop.ClickChooseFile()
        element = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/main/div[10]/div/div/div[2]/input[6]')
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.projprop.ClickEditChooseFile()
        self.projprop.EditModuleclickSave()
        time.sleep(2)
        assert "Module Updated successfully." in self.driver.page_source

    def test_Copy_Module(self, user_login):
        self.driver = user_login
        self.projprop = Module(self.driver)
        time.sleep(1)
        self.projprop.clickProjectTab()
        self.projprop.clickModuleTab()
        self.projprop.ClickModule()
        self.projprop.ModuleClickCopy()
        rand_copy_module = ''.join((random.choice('modulouse') for i in range(5)))
        self.projprop.setCopyModuleName(rand_copy_module)
        self.projprop.setCopyModuleDesc(self.ModuleDescrption2)
        self.projprop.CopyModuleclickSave()
        time.sleep(2)
        assert "Module Added successfully" in self.driver.page_source

    def test_Module_Delete(self, user_login):

        self.driver = user_login
        self.projprop = Module(self.driver)
        time.sleep(1)
        self.projprop.clickProjectTab()
        self.projprop.clickModuleTab()
        self.projprop.ClickModule()
        self.projprop.ModuleclickDelete()
        self.projprop.ModuleDelete()
        time.sleep(2)
        assert "Module deleted successfully" in self.driver.page_source
