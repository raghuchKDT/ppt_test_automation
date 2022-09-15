from selenium.webdriver.common.by import By
import time

class Workflow:
    btn_project_xpath = "//*[@id='three']/span"
    btn_workflow_xpath = "//*[@id='pills-workflow-tab']"
    btn_newworkflow_xpath = "//*[@id='bntGoToCreateWorkflow']"
    btn_savewf_xpath = "//*[@id='btn-WorkSave']"
    btn_checkmark1wf_xpath = "//*[@id='tblWorkflow']/tbody/tr[1]/td[1]/label/span"
    btn_editwf_xpath = "//*[@id='btn-WorkEdit']"

    def __init__(self, driver):
        time.sleep(1)
        self.driver = driver

    def Project(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btn_project_xpath).click()

    def clickworkflow(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btn_workflow_xpath).click()

    def clicknewworkflow(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btn_newworkflow_xpath ).click()

    def clicksaveworkflow(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btn_savewf_xpath ).click()

    def clickcheckmarkworkflow(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btn_checkmark1wf_xpath).click()

    def clickeditworkflow(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btn_editwf_xpath ).click()
