from selenium.webdriver.common.by import By
import time

class Splice:
    textbox_splicename_id = "SpliceName"
    textbox_Splicename_id = "Splicename"
    textbox_spliceName_id = "spliceName"
    btn_project_xpath = "//*[@id='three']/span"
    btn_variant_link_txt = "Variant"
    btn_splice_css_selector = "#pills-splice-tab"
    btn_newsplice_xpath = "//*[@id='bntGoToCreateSplice']"
    btn_savesplice_xpath = "//*[@id='btn-spliceSave']"
    btn_checkmark1splice_xpath = "//*[@id='tblSplice']/tbody/tr[1]/td[1]/label/span"
    btn_copysplice_xpath = "//*[@id='btn-SpliceSaveAs']"
    btn_checkmark3splice_xpath =  "//*[@id='tblSplice']/tbody/tr[1]/td[1]/label/span"
    btn_deletesplice_xpath = "//*[@id='btn-splicedelete']"
    btn_popupdeletesplice_xpath = "//*[@id='btn-delete-splice']"
    btn_editsplice_xpath = "//*[@id='btn-spliceEdit']"
    btn_copysave_xpath = "//*[@id='btn-saveas-splice']"

    def __init__(self, driver):
        time.sleep(1)
        self.driver = driver

    def Project(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_project_xpath).click()

    def clickvariant(self):
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, self.btn_variant_link_txt ).click()

    def clicksplice(self):
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,self.btn_splice_css_selector).click()

    def clicknewsplice(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_newsplice_xpath).click()

    def setsplicename(self, SpliceName):
        time.sleep(2)
        self.driver.find_element(By.ID, self.textbox_splicename_id).clear()
        time.sleep(1)
        self.driver.find_element(By.ID, self.textbox_splicename_id).send_keys(SpliceName)

    def clicksavesplice(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_savesplice_xpath).click()

    def clickcheckmarksplice(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_checkmark1splice_xpath).click()

    def setcopysplicename(self, Splicename):
        time.sleep(2)
        self.driver.find_element(By.ID, self.textbox_Splicename_id).clear()
        self.driver.find_element(By.ID, self.textbox_Splicename_id).send_keys(Splicename)

    def clickcopysave(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_copysave_xpath).click()

    def clickcheckmark3splice(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.btn_checkmark3splice_xpath).click()

    def seteditsplicename(self, spliceName):
        time.sleep(2)
        self.driver.find_element(By.ID, self.textbox_spliceName_id).clear()
        self.driver.find_element(By.ID, self.textbox_spliceName_id).send_keys(spliceName)

    def clickdeletesplice(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_deletesplice_xpath).click()

    def clickpopupdeletesplice(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_popupdeletesplice_xpath).click()

    def clickcopysplice(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_copysplice_xpath).click()

    def clickeditsplice(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_editsplice_xpath ).click()