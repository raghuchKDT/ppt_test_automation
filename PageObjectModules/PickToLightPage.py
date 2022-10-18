from selenium.webdriver.common.by import By
import time

class PickToLight:

    NewPickToLightName_id = "txtNewPickToLight"
    EditPickToLightName_id = "txtPickName"
    CopyPickToLightName_id = "txtCopyNewPickToLight"
    NewPickToLightDescrption_id = "txtPickToLightDescription"
    EditPickToLightDescrption_id = "txtPickDesc"
    CopyPickToLightDescrption_id = "txtCopyPickToLightDescription"
    NewPickToLightLEDNo_id = "txtLightLed"
    EditPickToLightLEDNo_id = "txtPickNum"
    text_projectTab_xpath = "//*[@id='three']"
    text_PickToLightTab_xpath = "/html/body/div[1]/div[2]/main/div[2]/div/ul/li[3]/a"
    text_select_PickToLight_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[4]/div/div/div[1]/span[1]/div/ul/li[1]"
    btn_new__PickToLight_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[4]/div/div/div[1]/div[2]/div/button[1]"
    btn_new__PickToLightSave_xpath = "/html/body/div[1]/div[2]/main/div[4]/div/div/div[2]/div/button[2]"
    btn_edit__PickToLight_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[4]/div/div/div[1]/div[2]/div/button[2]"
    btn_edit__PickToLightSave_xpath = "/html/body/div[1]/div[2]/main/div[6]/div/div/div[2]/div/button[2]"
    btn_copy__PickToLight_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[4]/div/div/div[1]/div[2]/div/button[3]"
    btn_copy__PickToLightSave_xpath = "/html/body/div[1]/div[2]/main/div[5]/div/div/div[2]/div/button[2]"
    btn_delete_PickToLight_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[4]/div/div/div[1]/div[2]/div/button[4]"
    btn_confirmdelete_PickToLight_xpath = "/html/body/div[1]/div[2]/main/div[7]/div/div/div[2]/div/button[2]"

    def __init__(self, driver):
        self.driver = driver

    def clickProjectTab(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.text_projectTab_xpath).click()

    def clickPickToLightTab(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.text_PickToLightTab_xpath).click()

    def SelectPickToLightFromTable(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.text_select_PickToLight_xpath).click()

    def ClickNewPickToLightButton(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_new__PickToLight_xpath).click()

    def setNewPickToLighteName(self, NewPickToLightName):
        time.sleep(2)
        self.driver.find_element(By.ID, self.NewPickToLightName_id).clear()
        self.driver.find_element(By.ID, self.NewPickToLightName_id).send_keys(NewPickToLightName)

    def setNewPickToLightDesc(self, NewPickToLightDescrption):
        time.sleep(2)
        self.driver.find_element(By.ID, self.NewPickToLightDescrption_id).clear()
        self.driver.find_element(By.ID, self.NewPickToLightDescrption_id).send_keys(NewPickToLightDescrption)

    def setNewPickToLightLED_No(self, NewPickToLightLEDNo):
        time.sleep(2)
        self.driver.find_element(By.ID, self.NewPickToLightLEDNo_id).clear()
        self.driver.find_element(By.ID, self.NewPickToLightLEDNo_id).send_keys(NewPickToLightLEDNo)

    def NewPickToLightClickSaveButton(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_new__PickToLightSave_xpath).click()

    def SelectPickToLightEdit(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.text_select_PickToLight_xpath).click()

    def ClickEditButton(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_edit__PickToLight_xpath).click()

    def setEditPickToLightName(self, EditPickToLightName):
        time.sleep(2)
        self.driver.find_element(By.ID, self.EditPickToLightName_id).clear()
        self.driver.find_element(By.ID, self.EditPickToLightName_id).send_keys(EditPickToLightName)

    def setEditPickToLightDesc(self, EditPickToLightDescrption):
        time.sleep(2)
        self.driver.find_element(By.ID, self.EditPickToLightDescrption_id).clear()
        self.driver.find_element(By.ID, self.EditPickToLightDescrption_id).send_keys(EditPickToLightDescrption)

    def setEditPickToLightLED_No(self, EditPickToLightLEDNo):
        time.sleep(2)
        self.driver.find_element(By.ID, self.EditPickToLightLEDNo_id).clear()
        self.driver.find_element(By.ID, self.EditPickToLightLEDNo_id).send_keys(EditPickToLightLEDNo)

    def EditPickToLightClickSaveButton(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_edit__PickToLightSave_xpath).click()

    def SelectPickToLightCopy(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.text_select_PickToLight_xpath).click()

    def PickToLightClickCopyButton(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_copy__PickToLight_xpath).click()

    def setCopyPickToLightName(self, CopyPickToLightName):
        time.sleep(2)
        self.driver.find_element(By.ID, self.CopyPickToLightName_id).clear()
        self.driver.find_element(By.ID, self.CopyPickToLightName_id).send_keys(CopyPickToLightName)

    def setCopyPickToLightDesc(self, CopyPickToLightDescrption):
        time.sleep(2)
        self.driver.find_element(By.ID, self.CopyPickToLightDescrption_id).clear()
        self.driver.find_element(By.ID, self.CopyPickToLightDescrption_id).send_keys(CopyPickToLightDescrption)

    def CopyPickToLightClickSaveButton(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_copy__PickToLightSave_xpath).click()

    def SelectPickToLightDelete(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.text_select_PickToLight_xpath).click()

    def PickToLightClickDeleteButton(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_delete_PickToLight_xpath).click()

    def PickToLightConfirmDelete(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_confirmdelete_PickToLight_xpath).click()
