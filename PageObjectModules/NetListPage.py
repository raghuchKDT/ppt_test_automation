from selenium.webdriver.common.by import By
import time

class Connectionlist:
    textbox_cln_id = "ListName"
    textbox_cld_id = "ListDesc"
    btn_project_xpath = "//*[@id='three']/span"
    btn_variant_link_txt = "Variant"
    btn_netlist_xpath = "//*[@id='pills-connectionlist-tab']"
    btn_connectionlist_xpath = "//*[@id='pills-connectionlist']/div[1]/a"
    btn_newlist_xpath = "//*[@id='bntCreateConnectionListDetail']"
    btn_savelist_xpath = "//*[@id='btn-add-connectionDet']"
    btn_checkmark_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[5]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div/label/span"
    btn_copylist_xpath = "//*[@id='btn-wire-copy']"
    btn_deletelist_xpath = "//*[@id='btn-connectionlistDetaildelete']"
    btn_popupdeletelist_xpath = "//*[@id='btn-delete-connectionlist']"
    btn_saveaslist_xpath = "//*[@id='btn-copy-connection']"


    def __init__(self, driver):
        time.sleep(1)
        self.driver = driver

    def Project(self):
        self.driver.find_element(By.XPATH, self.btn_project_xpath).click()

    def clickvariant(self):
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT,  self.btn_variant_link_txt).click()

    def clicknetlist(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_netlist_xpath ).click()

    def clickconnectionlist(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.btn_connectionlist_xpath ).click()

    def clicknewlist(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.btn_newlist_xpath ).click()

    def setnewlist(self, ListName):
        time.sleep(2)
        self.driver.find_element(By.ID, self.textbox_cln_id).clear()
        self.driver.find_element(By.ID, self.textbox_cln_id).send_keys(ListName)

    def setnewlistdesc(self, ListDesc):
        time.sleep(2)
        self.driver.find_element(By.ID, self.textbox_cld_id).clear()
        self.driver.find_element(By.ID, self.textbox_cld_id).send_keys(ListDesc)

    def clicksavelist(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_savelist_xpath).click()

    def clickcheckmarklist(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_checkmark_xpath).click()

    def clickcopylist(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_copylist_xpath ).click()

    def clicksaveaslist(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btn_saveaslist_xpath).click()

    def deletelist(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_deletelist_xpath ).click()

    def popupdeletelist(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_popupdeletelist_xpath ).click()
