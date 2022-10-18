from selenium.webdriver.common.by import By
import time

class Label:
    textbox_labelname_id = "LabelName"
    textbox_labeldesc_id = "Labeldesc"
    btn_project_xpath = "//*[@id='three']/span"
    btn_label_xpath = "//*[@id='pills-label-tab']"
    btn_newlabel_xpath = "//*[@id='bntGoToCreateLabel']"
    btn_savelabel_xpath = "//*[@id='btn-labelSave']"
    btn_editlabel_xpath = "//*[@id='btn-LabelEdit']"
    btn_checkmark1label_xpath = "//*[@id='tblLabel']/tbody/tr[1]/td[1]/label/span"
    btn_deletelabel_xpath = "//*[@id='btn-labeldelete']"
    btn_popupdeletelabel_xpath = "//*[@id='btn-delete-label']"

    def __init__(self, driver):
        time.sleep(1)
        self.driver = driver

    def Project(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btn_project_xpath).click()

    def clicklabel(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btn_label_xpath).click()

    def createnewlabel(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btn_newlabel_xpath).click()

    def setlabelname(self, LabelName):
        time.sleep(1)
        self.driver.find_element(By.ID, self.textbox_labelname_id).clear()
        self.driver.find_element(By.ID, self.textbox_labelname_id).send_keys(LabelName)

    def setlabeldesc(self, labeldesc):
        time.sleep(1)
        self.driver.find_element(By.ID, self.textbox_labeldesc_id).clear()
        self.driver.find_element(By.ID, self.textbox_labeldesc_id).send_keys(labeldesc)

    def clicksavelabel(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btn_savelabel_xpath ).click()

    def clickeditlabel(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btn_editlabel_xpath).click()


    def clickchecklabel(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btn_checkmark1label_xpath).click()

    def clickdeletelabel(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btn_deletelabel_xpath).click()

    def popupdeletelabel(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btn_popupdeletelabel_xpath).click()