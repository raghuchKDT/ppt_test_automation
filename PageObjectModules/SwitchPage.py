from selenium.webdriver.common.by import By
import time

class Switch:
    textbox_switchGroup_id = "switchGroup"
    textbox_editsg_id = "SwitchGroup"
    btn_project_xpath = "//*[@id='three']/span"
    btn_switch_xpath = "//*[@id='pills-switch-tab']"
    btn_newswitch_xpath = "//*[@id='bntGoToCreateSwicth']"
    btn_saveswitch_xpath = "//*[@id='btn-switchSave']"
    btn_checkmark1_xpath = "//*[@id='tblswitch']/tbody/tr[1]/td[1]"
    btn_deleteswitch_xpath = "//*[@id='btn-switchdelete']"
    btn_popupdeleteswitch_xpath = "//*[@id='btn-delete-switch']"
    btn_editswitch_xpath = "//*[@id='btn-switchEdit']"
    btn_multipledelete_xpath = "//*[@id='tblswitch']/thead/tr/th[1]/label/span"

    def __init__(self,driver):
        time.sleep(1)
        self.driver = driver

    def Project(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_project_xpath).click()

    def clickswitch(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_switch_xpath).click()

    def clickNew(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_newswitch_xpath ).click()

    def setswitchGroup(self, switchGroup):
        time.sleep(2)
        self.driver.find_element(By.ID, self.textbox_switchGroup_id).clear()
        self.driver.find_element(By.ID, self.textbox_switchGroup_id).send_keys(switchGroup)

    def save(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_saveswitch_xpath ).click()

    def clickcheckmark(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_checkmark1_xpath).click()

    def clickdelete(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_deleteswitch_xpath).click()

    def clickdeleteswitch(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_popupdeleteswitch_xpath).click()

    def clickeditswitch(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_editswitch_xpath).click()

    def seteditswitch(self, SwitchGroup):
        time.sleep(2)
        self.driver.find_element(By.ID, self.textbox_editsg_id).clear()
        self.driver.find_element(By.ID, self.textbox_editsg_id).send_keys(SwitchGroup)

    def clickmultipledelete(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_multipledelete_xpath).click()
