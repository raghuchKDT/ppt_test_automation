import random
from selenium.common.exceptions import NoSuchElementException
import pytest
import time
from selenium import webdriver
from PageObjectModules.LoginPage import Login
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import InvalidSessionIdException
from PageObjectModules.LabelPage import Label

class Test006_Label:
    LabelName = "Label10"
    labeldesc = "print this label"

    def test_Label_screen(self, user_login):
        self.driver = user_login
        self.lb = Label(self.driver)
        self.lb.Project()
        self.lb.clicklabel()

        element6 = ['Label']
        data_base_element6 = self.driver.find_elements(By.XPATH, "//*[@id='pills-label-tab']")

        for idx, base_element6 in enumerate(data_base_element6):
            print(idx, base_element6.text)
            assert (element6[idx] == base_element6.text)

    @pytest.mark.sanity()
    def test_create_newlabel(self, user_login):
        self.driver = user_login
        self.lb = Label(self.driver)
        self.lb.Project()
        self.lb.clicklabel()
        self.lb.createnewlabel()
        time.sleep(1)
        rand_label_name = ''.join((random.choice('aeiourtnsclp')for i in range(5)))

        self.driver.find_element(By.XPATH, "//*[@id='labelName']").clear()
        self.driver.find_element(By.XPATH, "//*[@id='labelName']").send_keys(rand_label_name)

        time.sleep(2)

        self.driver.find_element(By.XPATH, "//*[@id='reportDescription']").clear()
        self.driver.find_element(By.XPATH, "//*[@id='reportDescription']").send_keys("desc")

        self.lb.clicksavelabel()
        time.sleep(2)

        assert 'Updated Successfully.' in self.driver.page_source

    def test_level2_menulabel(self, user_login):
        self.driver = user_login
        self.lb = Label(self.driver)
        self.lb.Project()
        self.lb.clicklabel()

        element8 = ['']
        data_base_ele8 = self.driver.find_elements(By.XPATH, "//*[@id='pills-label']/div[1]/div/div[2]/h6")

        for idx, base_ele8 in enumerate(data_base_ele8):
            print(idx, base_ele8.text)
            assert (element8[idx] == base_ele8.text)

        element9 = ['']
        data_base_ele9 = self.driver.find_elements(By.XPATH, "//*[@id='pills-label']/div[1]/div/div[3]/div/h6")

        for idx, base_ele9 in enumerate(data_base_ele9):
            print(idx, base_ele9.text)
            assert (element9[idx] == base_ele9.text)

    def test_globalvariables(self, user_login):
        self.driver = user_login
        self.lb = Label(self.driver)
        self.lb.Project()
        self.lb.clicklabel()

        element10 = ['']
        data_base_ele10 = self.driver.find_elements(By.XPATH, "//*[@id='tblLabelglobal']/thead/tr")

        for idx, base_ele10 in enumerate(data_base_ele10):
            print(idx, base_ele10.text)
            assert (element10[idx] == base_ele10.text)

    def test_dynamicdata(self, user_login):
        self.driver = user_login
        self.lb = Label(self.driver)
        self.lb.Project()
        self.lb.clicklabel()

        table = self.driver.find_element(By.ID, "tblLabelglobal")
        body = table.find_element(By.TAG_NAME, "tbody")
        cells = body.find_elements(By.TAG_NAME, "td")
        for cell in cells:
            print(cell.text)

    def test_edit_label(self, user_login):
        self.driver = user_login
        self.lb = Label(self.driver)
        self.lb.Project()
        self.lb.clicklabel()
        self.lb.clickchecklabel()
        self.lb.clickeditlabel()

        self.driver.find_element(By.XPATH, "//*[@id='labelName']").clear()
        self.driver.find_element(By.XPATH, "//*[@id='labelName']").send_keys("dfg")

        self.driver.find_element(By.XPATH, "//*[@id='reportDescription']").clear()
        self.driver.find_element(By.XPATH, "//*[@id='reportDescription']").send_keys("happy")

        self.lb.clicksavelabel()

        element = ['Updated Successfully.']
        data_base_element = self.driver.find_elements(By.XPATH, "//*[contains(text(),'Updated Successfully.')]")

        for idx, base_element in enumerate(data_base_element):
            print(idx, base_element.text)
            assert (element[idx] == base_element.text)

    def test_Genprop_label(self, user_login):
        self.driver = user_login
        self.lb = Label(self.driver)
        self.lb.Project()
        self.lb.clicklabel()
        self.lb.clickchecklabel()

        assert "Label Name" in self.driver.page_source
        assert "Label Description" in self.driver.page_source


    def test_label_delete(self, user_login):
        self.driver = user_login
        self.lb = Label(self.driver)
        self.lb.Project()
        self.lb.clicklabel()
        self.lb.clickchecklabel()
        self.lb.clickdeletelabel()
        self.lb.popupdeletelabel()

        element = ['Deleted Successfully.']
        data_base_element = self.driver.find_elements(By.XPATH, "//*[contains(text(),'Deleted Successfully.')]")

        for idx, base_element in enumerate(data_base_element):
            print(idx, base_element.text)
            assert (element[idx] == base_element.text)