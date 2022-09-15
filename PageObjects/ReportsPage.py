from selenium.webdriver.common.by import By
import time

class reports:
    btn_reports_xpath = "//*[@id='five']/span"
    btn_checkmarkreport_xpath = "//*[@id='tblReport']/tbody/tr[1]/td[1]/label/span"
    btn_newreport_xpath = "//*[@id='bntGoToCreateReport']"
    btn_savereport_xpath = "//*[@id='btn-reportSave']"
    btn_editreport_xpath = "//*[@id='btn-reportEdit']"
    btn_checkmark2_xpath = "//*[@id='tblReport']/tbody/tr[2]/td[1]/label/span"
    btn_deletereport_xpath = "//*[@id='btn-reportdelete']"
    btn_popupdeletereport_xpath = "//*[@id='btn-delete-report']"
    btn_checkmarkreport3_xpath = "//*[@id='tblReport']/tbody/tr[4]/td[1]/label/span"
    btn_multipledelete_xpath = "//*[@id='tblReport']/thead/tr/th[1]/label/span"

    def __init__(self,driver):
        time.sleep(1)
        self.driver = driver

    def clickreports(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btn_reports_xpath).click()

    def clickcheckmark(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btn_checkmarkreport_xpath).click()

    def clicknew(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btn_newreport_xpath).click()

    def clicksave(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btn_savereport_xpath).click()

    def clickedit(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btn_editreport_xpath).click()

    def clickcheckmark2(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btn_checkmark2_xpath).click()

    def clickdelete(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btn_deletereport_xpath).click()

    def clickpopdelete(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btn_popupdeletereport_xpath).click()

    def clickreportmaskdelete(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='ViewReportMasks']/div[2]/ul/li/div/span/ul/div[5]/svg").click()

    def clickcheckmarkreport(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btn_checkmarkreport3_xpath).click()

    def clickmultipledelete(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_multipledelete_xpath).click()
