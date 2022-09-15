from selenium.webdriver.common.by import By
import time


class Settings:
    textbox_projnam_id = "projectname"
    textbox_pd_id = "projdesc"
    textbox_ProjName_id = "ProjName"
    textbox_Projdesc_id = "Projdesc"
    btn_project_xpath = "//*[@id='three']/span"
    btn_newproject_xpath = "//*[@id='bntGoToCreateProject']"
    btn_checkmark1proj_xpath = "//*[@id='tblProject']/tbody/tr[3]/td[1]/label/span"
    btn_editproj_xpath = "//*[@id='btn-Edit']"
    btn_deleteproj_xpath = "//*[@id='btn-delete']"
    btn_popupdeleteproj_xpath = "//*[@id='btn-delete-project']"
    btn_saveproj_xpath = "//*[contains(text(), 'Save')]"
    btn_saveasproj_xpath = "//*[@id='btn-saveas-project']"
    btn_multipledeleteproj_xpath = "//*[@id='tblProject']/thead/tr/th[1]/label/span"

    def __init__(self, driver):
        time.sleep(1)
        self.driver = driver

    def Project(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_project_xpath).click()

    def clickcheck(self):
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "#tblProject > tbody > tr.odd > td.sorting_1 > label > span").click()

    def setprojname(self, projectname):
        time.sleep(2)
        self.driver.find_element(By.ID, self.textbox_projnam_id).clear()
        self.driver.find_element(By.ID, self.textbox_projnam_id).send_keys(projectname)

    def setprojdesc(self,projdesc ):
        time.sleep(2)
        self.driver.find_element(By.ID, self.textbox_pd_id).clear()
        self.driver.find_element(By.ID, self.textbox_pd_id).send_keys(projdesc)

    def clicknew(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_newproject_xpath).click()

    def clickcheckmarkproj(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_checkmark1proj_xpath ).click()

    def setpn(self, ProjName):
        time.sleep(2)
        self.driver.find_element(By.ID, self. textbox_ProjName_id).clear()
        self.driver.find_element(By.ID, self. textbox_ProjName_id).send_keys(ProjName)

    def setpd(self, Projdesc):
        time.sleep(2)
        self.driver.find_element(By.ID, self. textbox_Projdesc_id).clear()
        self.driver.find_element(By.ID, self. textbox_Projdesc_id).send_keys(Projdesc)

    def clickedit(self):
        self.driver.find_element(By.XPATH, self.btn_editproj_xpath ).click()

    def deleteproj(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_deleteproj_xpath ).click()

    def popupdeleteproj(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_popupdeleteproj_xpath).click()

    def clickSave(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_saveproj_xpath).click()

    def clicksave(self):
        self.driver.find_element(By.XPATH, self.btn_saveasproj_xpath).click()

    def clickmultipledelete(self):
        self.driver.find_element(By.XPATH, self.btn_multipledeleteproj_xpath).click()
