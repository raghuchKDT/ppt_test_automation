from selenium.webdriver.common.by import By
import time

class XCode:

    link_variant_Link_Text = "Variant"
    NewXCodeName_id = "txtNewXcodeName"
    NewXCodeCustomer_id = "txtXcodeCustomerId"
    NewXCodeDesc_id = "txtXcodeDescription"
    EditXCodeName_id = "txtNewXcodeName1"
    EditXCodeCustomer_id = "txtXcodeCustomerId1"
    EditXCodeDesc_id = "txtXcodeDescription1"
    EditXCodeCTPPin1Name_id = "ctp-1"
    EditXCodeCTPPin2Name_id = "ctp-2"
    CopyXCodeName_id = "txtCopyXcodeName"
    CopyXCodeCustomer_id = "txtCopyXcodeCustomerId"
    CopyXCodeDesc_id = "txtCopyXcodeDescription"
    text_projectTab_link_txt = "Project"
    text_xcodeTab_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[1]/div/ul/li[2]/a"
    checkbox_select_xcode_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[3]/div/div[2]/div[1]/a/div/div[1]/div"
    btn_new_xcode_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/button[1]"
    list_select_new_xCodeModule_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/select/option[3]"
    btn_new_choosefile_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/input[3]"
    btn_new_xcodeSave_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div/button[2]"
    btn_edit_xcode_xpath = "//*[@id='btn-XEdit']"
    btn_edit_choosefile_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[2]/div[3]/div/div/div[2]/input[3]"
    btn_edit_xcodeSave_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[2]/div[3]/div/div/div[2]/div/button[2]"
    list_select_SwitchStatus_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div/div[4]/div/div[3]/select/option[2]"
    checkbox_select_switch_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div/div[4]/div/div[4]/input"
    btn_SwitchUpdate_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[3]/input[4]"
    btn_copy_xcode_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/button[2]"
    list_select_xcode_xpath = "//*[@id='xcodd-52']/a"
    btn_copy_xcodeSave_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div/div[2]/div/button[1]"
    checkbox_select_delete_xcode_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[3]/div/div[2]/div[1]/a/div/div[1]/div"
    btn_delete_xcode_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/button[3]"
    btn_confirmdelete_xcode_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[4]/div/div/div[2]/div/button[2]"

    def __init__(self, driver):
        self.driver = driver

    def clickProjectTab(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.text_projectTab_link_txt).click()

    def clickVariantTab(self):
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Variant").click()

    def clickXCodeTab(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.text_xcodeTab_xpath).click()

    def SelectXCode(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.checkbox_select_xcode_xpath).click()

    def ClickNewXCodeButton(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_new_xcode_xpath).click()

    def setNewXCodeName(self, NewXCodeName):
        time.sleep(2)
        self.driver.find_element(By.ID, self.NewXCodeName_id).clear()
        self.driver.find_element(By.ID, self.NewXCodeName_id).send_keys(NewXCodeName)

    def setNewXCodeCustomerID(self, NewXCodeCustomerID):
        time.sleep(2)
        self.driver.find_element(By.ID, self.NewXCodeCustomer_id).clear()
        self.driver.find_element(By.ID, self.NewXCodeCustomer_id).send_keys(NewXCodeCustomerID)

    def setNewXCodeDesc(self, NewXCodeDesc):
        time.sleep(2)
        self.driver.find_element(By.ID, self.NewXCodeDesc_id).clear()
        self.driver.find_element(By.ID, self.NewXCodeDesc_id).send_keys(NewXCodeDesc)

    def SelectXCodeModulefromDropDownList(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.list_select_new_xCodeModule_xpath).click()

    def ClickNewChooseFile(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_new_choosefile_xpath).send_keys("C:\\Users\\KnoDTec\\Downloads\\Picture.png")

    def NewXCodeClickSaveButton(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_new_xcodeSave_xpath).click()

    def ClickXCodeEditButton(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_edit_xcode_xpath).click()

    def setEditXCodeName(self, EditXCodeName):
        time.sleep(2)
        self.driver.find_element(By.ID, self.EditXCodeName_id).clear()
        self.driver.find_element(By.ID, self.EditXCodeName_id).send_keys(EditXCodeName)

    def setEditXCodeCustomerID(self, EditXCodeCustomerID):
        time.sleep(2)
        self.driver.find_element(By.ID, self.EditXCodeCustomer_id).clear()
        self.driver.find_element(By.ID, self.EditXCodeCustomer_id).send_keys(EditXCodeCustomerID)

    def setEditXCodeDesc(self, EditXCodeDesc):
        time.sleep(2)
        self.driver.find_element(By.ID, self.EditXCodeDesc_id).clear()
        self.driver.find_element(By.ID, self.EditXCodeDesc_id).send_keys(EditXCodeDesc)

    def ClickEditChooseFile(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_edit_choosefile_xpath).send_keys("C:\\Users\\KnoDTec\\Downloads\\Picture.png")

    def EditXCodeClickSaveButton(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_edit_xcodeSave_xpath).click()

    def setEditXCodeCTPPin1Name(self, EditXCodeCTPPin1Name):
        time.sleep(2)
        self.driver.find_element(By.ID, self.EditXCodeCTPPin1Name_id).clear()
        self.driver.find_element(By.ID, self.EditXCodeCTPPin1Name_id).send_keys(EditXCodeCTPPin1Name)

    def setEditXCodeCTPPin2Name(self, EditXCodeCTPPin2Name):
        time.sleep(2)
        self.driver.find_element(By.ID, self.EditXCodeCTPPin2Name_id).clear()
        self.driver.find_element(By.ID, self.EditXCodeCTPPin2Name_id).send_keys(EditXCodeCTPPin2Name)

    def SelectXCodeSwitchStatusFromList(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.list_select_SwitchStatus_xpath).click()

    def XCodeSwitchSelectCheckbox(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.checkbox_select_switch_xpath).click()

    def XCodeClickUpdateButton(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_SwitchUpdate_xpath).click()

    def ClickXCodeCopyButton(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_copy_xcode_xpath).click()

    def SelectXCodeFromList(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.list_select_xcode_xpath).click()

    def setCopyXCodeName(self, CopyXCodeName):
        time.sleep(2)
        self.driver.find_element(By.ID, self.CopyXCodeName_id).clear()
        self.driver.find_element(By.ID, self.CopyXCodeName_id).send_keys(CopyXCodeName)

    def setCopyXCodeCustomerID(self, CopyXCodeCustomerID):
        time.sleep(2)
        self.driver.find_element(By.ID, self.CopyXCodeCustomer_id).clear()
        self.driver.find_element(By.ID, self.CopyXCodeCustomer_id).send_keys(CopyXCodeCustomerID)

    def setCopyXCodeDesc(self, CopyXCodeDesc):
        time.sleep(2)
        self.driver.find_element(By.ID, self.CopyXCodeDesc_id).clear()
        self.driver.find_element(By.ID, self.CopyXCodeDesc_id).send_keys(CopyXCodeDesc)

    def CopyXCodeClickSaveButton(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_copy_xcodeSave_xpath).click()

    def SelectXCodeDelete(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.checkbox_select_delete_xcode_xpath).click()

    def XCodeClickDeleteButton(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_delete_xcode_xpath).click()

    def XCodeConfirmDelete(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_confirmdelete_xcode_xpath).click()
