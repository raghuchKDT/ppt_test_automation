import pytest
import time
from selenium import webdriver
from PageObjects.LoginPage import Login
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import InvalidSessionIdException
from PageObjects.Workflowpage import Workflow
import random


class Test007_Workflow:

    def test_workflowscreen(self, user_login):
        self.driver = user_login
        self.wf = Workflow(self.driver)
        self.wf.Project()
        self.wf.clickworkflow()

        element14 = ['Workflow']
        data_base_element14 = self.driver.find_elements(By.XPATH, "//*[@id='pills-workflow-tab']")

        for idx, base_element14 in enumerate(data_base_element14):
            print(idx, base_element14.text)
            assert (element14[idx] == base_element14.text)

    def test_newworkflow(self, user_login):
        self.driver = user_login
        self.wf = Workflow(self.driver)
        self.wf.Project()
        self.wf.clickworkflow()
        self.wf.clicknewworkflow()

        rand_wf_name = ''.join((random.choice('aeiourtsndlcp') for i in range(5)))

        self.driver.find_element(By.XPATH, "//*[@id='workflowName']").clear()
        self.driver.find_element(By.XPATH, "//*[@id='workflowName']").send_keys(rand_wf_name)

        self.driver.find_element(By.XPATH, "//*[@id='workflowDesc']").clear()
        self.driver.find_element(By.XPATH, "//*[@id='workflowDesc']").send_keys("new workflow is created")

        self.wf.clicksaveworkflow()

        element15 = ['Data Added Successfully.']
        data_base_element15 = self.driver.find_elements(By.XPATH, "//*[contains(text(),'Data Added Successfully.')]")

        for idx, base_element15 in enumerate(data_base_element15):
            print(idx, base_element15.text)
            assert (element15[idx] == base_element15.text)

    def test_edit_workflow(self, user_login):
        self.driver = user_login
        self.wf = Workflow(self.driver)
        self.wf.Project()
        self.wf.clickworkflow()
        self.wf.clickcheckmarkworkflow()
        self.wf.clickeditworkflow()

        rand_wfedit_name = ''.join((random.choice('aeiourtsndlcp')for i in range(5)))
        self.driver.find_element(By.XPATH, "//*[@id='workflowName']").clear()
        self.driver.find_element(By.XPATH, "//*[@id='workflowName']").send_keys(rand_wfedit_name)

        self.driver.find_element(By.XPATH, "//*[@id='workflowDesc']").clear()
        self.driver.find_element(By.XPATH, "//*[@id='workflowDesc']").send_keys("the project is created")

        self.wf.clicksaveworkflow()

        element19 = ['Data Added Successfully.']
        data_base_element19 = self.driver.find_elements(By.XPATH, "//*[contains(text(),'Data Added Successfully.')]")

        for idx, base_element19 in enumerate(data_base_element19):
            print(idx, base_element19.text)
            assert (element19[idx] == base_element19.text)

    def test_generalprop_workflow(self, user_login):
        self.driver = user_login
        self.wf = Workflow(self.driver)
        self.wf.Project()
        self.wf.clickworkflow()
        self.wf.clickcheckmarkworkflow()
        
        assert 'Name' in self.driver.page_source
        assert 'Description' in self.driver.page_source

        # element = ['Name']
        # data_base_ele = self.driver.find_elements(By.XPATH, "//*[@id='collapseOne']/div/div[1]/div/div/div[1]/div/h5")
        #
        # for idx, base_ele in enumerate(data_base_ele):
        #     print(idx, base_ele.text)
        #     assert (element[idx] == data_base_ele)
        #
        # element17 = ['Description']
        # data_base_ele17 = self.driver.find_elements(By.XPATH, "//*[@id='collapseOne']/div/div[1]/div/div/div[3]/div/h5")
        #
        # for idx, base_ele17 in enumerate(data_base_ele17):
        #     print(idx, base_ele17.text)
        #     assert (element17[idx] == data_base_ele17)
