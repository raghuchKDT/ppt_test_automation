from selenium.webdriver.common.by import By
import time

class XCode:

    text_projectTab_xpath = "/html/body/div[1]/div[1]/div/div/nav/div/div/div[1]/a[2]/span"
    text_moduleTab_xpath = "/html/body/div[1]/div[2]/main/div[2]/div/ul/li[2]/a"
    text_variantTab_xpath = "/html/body/div[1]/div[2]/main/div[2]/div/ul/li[5]/a"
    text_xcodeTab_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[1]/div/ul/li[2]/a"
    checkbox_select_xcode_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[3]/div/div[2]/div[1]/a/div/div[1]/div"
    btn_new_xcode_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/button[1]"
    NewXCodeName_id = "txtNewXcodeName"
    NewXCodeCustomer_id = "txtXcodeCustomerId"
    NewXCodeDesc_id = "txtXcodeDescription"
    list_select_new_xCodeModule_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/select"
    EditXCodeName_id = "txtNewXcodeName1"
    EditXCodeCustomer_id = "txtXcodeCustomerId1"
    EditXCodeDesc_id = "txtXcodeDescription1"
    CTPPinName_id = "ctp-1"
    CTPPinName_id2 = "ctp-2"
    CTPPinName_id3 = "ctp-3"
    CTPPinName_id4 = "ctp-4"
    CTPPinName_id5 = "ctp-5"
    CTPPinName_id6 = "ctp-6"
    CTPPinName_id7 = "ctp-7"
    CTPPinName_id8 = "ctp-8"
    CTPPinName_id9 = "ctp-9"
    CTPPinName_id10 = "ctp-10"
    CTPPinName_id11 = "ctp-11"
    CTPPinName_id12 = "ctp-12"
    CTPPinName_id13 = "ctp-13"
    CTPPinName_id14 = "ctp-14"
    CTPPinName_id15 = "ctp-15"
    CTPPinName_id16 = "ctp-16"
    CTPPinName_id17 = "ctp-17"
    CTPPinName_id18 = "ctp-18"
    CTPPinName_id19 = "ctp-19"
    CTPPinName_id20 = "ctp-20"
    CTPPinName_id21 = "ctp-21"
    CTPPinName_id22 = "ctp-22"
    CTPPinName_id23 = "ctp-23"
    CTPPinName_id24 = "ctp-24"
    CTPPinName_id25 = "ctp-25"
    CTPPinName_id26 = "ctp-26"
    CTPPinName_id27 = "ctp-27"
    CTPPinName_id28 = "ctp-28"
    CTPPinName_id29 = "ctp-29"
    CTPPinName_id30 = "ctp-30"
    CTPPinName_id31 = "ctp-31"
    CTPPinName_id32 = "ctp-32"
    CTPPinName_id33 = "ctp-33"
    CopyXCodeName_id = "txtCopyXcodeName"
    CopyXCodeCustomer_id = "txtCopyXcodeCustomerId"
    CopyXCodeDesc_id = "txtCopyXcodeDescription"
    btn_new_choosefile_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/input[3]"
    btn_new_xcodeSave_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div/button[2]"
    btn_edit_xcode_xpath = "//*[@id='btn-XEdit']"
    btn_edit_choosefile_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[2]/div[3]/div/div/div[2]/input[3]"
    btn_edit_xcodeSave_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[2]/div[3]/div/div/div[2]/div/button[2]"
    list_select_SwitchStatus_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div/div[35]/div/div[3]/select"
    checkbox_select_switch_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div/div[35]/div/div[4]/input"
    btn_SwitchUpdate_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[2]/button"
    btn_copy_xcode_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/button[3]"
    list_select_xcode_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div/div[2]/select/option[2]"
    btn_copy_xcodeSave_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div/div[2]/div/button[1]"
    checkbox_select_delete_xcode_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[3]/div/div[2]/div[1]/a/div/div[1]/div"
    btn_delete_xcode_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/button[4]"
    btn_confirmdelete_xcode_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[4]/div/div/div[2]/div/button[2]"

    def __init__(self, driver):
        self.driver = driver

    def clickProjectTab(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.text_projectTab_xpath).click()

    def clickModuleTab(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.text_moduleTab_xpath).click()

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
        self.driver.find_element(By.XPATH, self.btn_new_choosefile_xpath).send_keys("C:\\Users\\KnoDTec - Dheeraj\\Downloads\\Xcode_Module.jpg")

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
        self.driver.find_element(By.XPATH, self.btn_edit_choosefile_xpath).send_keys("C:\\Users\\KnoDTec - Dheeraj\\Downloads\\OCUA.png")

    def EditXCodeClickSaveButton(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_edit_xcodeSave_xpath).click()

    def setNewCTPPinName_test(self, ctp_id, CTPPinName):
        time.sleep(2)
        self.driver.find_element(By.ID, ctp_id).clear()
        self.driver.find_element(By.ID, ctp_id).send_keys(CTPPinName)

    def setNewCTPPinName2(self, CTPPinName2):
        time.sleep(2)
        self.driver.find_element(By.ID, self.CTPPinName_id2).clear()
        self.driver.find_element(By.ID, self.CTPPinName_id2).send_keys(CTPPinName2)

    def setNewCTPPinName3(self, CTPPinName3):
        time.sleep(2)
        self.driver.find_element(By.ID, self.CTPPinName_id3).clear()
        self.driver.find_element(By.ID, self.CTPPinName_id3).send_keys(CTPPinName3)

    def setNewCTPPinName4(self, CTPPinName4):
        time.sleep(2)
        self.driver.find_element(By.ID, self.CTPPinName_id4).clear()
        self.driver.find_element(By.ID, self.CTPPinName_id4).send_keys(CTPPinName4)

    def setNewCTPPinName5(self, CTPPinName5):
        time.sleep(2)
        self.driver.find_element(By.ID, self.CTPPinName_id5).clear()
        self.driver.find_element(By.ID, self.CTPPinName_id5).send_keys(CTPPinName5)

    def setNewCTPPinName6(self, CTPPinName6):
        time.sleep(2)
        self.driver.find_element(By.ID, self.CTPPinName_id6).clear()
        self.driver.find_element(By.ID, self.CTPPinName_id6).send_keys(CTPPinName6)

    def setNewCTPPinName7(self, CTPPinName7):
        time.sleep(2)
        self.driver.find_element(By.ID, self.CTPPinName_id7).clear()
        self.driver.find_element(By.ID, self.CTPPinName_id7).send_keys(CTPPinName7)

    def setNewCTPPinName8(self, CTPPinName8):
        time.sleep(2)
        self.driver.find_element(By.ID, self.CTPPinName_id8).clear()
        self.driver.find_element(By.ID, self.CTPPinName_id8).send_keys(CTPPinName8)

    def setNewCTPPinName9(self, CTPPinName9):
        time.sleep(2)
        self.driver.find_element(By.ID, self.CTPPinName_id9).clear()
        self.driver.find_element(By.ID, self.CTPPinName_id9).send_keys(CTPPinName9)

    def setNewCTPPinName10(self, CTPPinName10):
        time.sleep(2)
        self.driver.find_element(By.ID, self.CTPPinName_id10).clear()
        self.driver.find_element(By.ID, self.CTPPinName_id10).send_keys(CTPPinName10)

    def setNewCTPPinName11(self, CTPPinName11):
        time.sleep(2)
        self.driver.find_element(By.ID, self.CTPPinName_id11).clear()
        self.driver.find_element(By.ID, self.CTPPinName_id11).send_keys(CTPPinName11)

    def setNewCTPPinName12(self, CTPPinName12):
        time.sleep(2)
        self.driver.find_element(By.ID, self.CTPPinName_id12).clear()
        self.driver.find_element(By.ID, self.CTPPinName_id12).send_keys(CTPPinName12)

    def setNewCTPPinName13(self, CTPPinName13):
        time.sleep(2)
        self.driver.find_element(By.ID, self.CTPPinName_id13).clear()
        self.driver.find_element(By.ID, self.CTPPinName_id13).send_keys(CTPPinName13)

    def setNewCTPPinName14(self, CTPPinName14):
        time.sleep(2)
        self.driver.find_element(By.ID, self.CTPPinName_id14).clear()
        self.driver.find_element(By.ID, self.CTPPinName_id14).send_keys(CTPPinName14)

    def setNewCTPPinName15(self, CTPPinName15):
        time.sleep(2)
        self.driver.find_element(By.ID, self.CTPPinName_id15).clear()
        self.driver.find_element(By.ID, self.CTPPinName_id15).send_keys(CTPPinName15)

    def setNewCTPPinName16(self, CTPPinName16):
        time.sleep(2)
        self.driver.find_element(By.ID, self.CTPPinName_id16).clear()
        self.driver.find_element(By.ID, self.CTPPinName_id16).send_keys(CTPPinName16)

    def setNewCTPPinName17(self, CTPPinName17):
        time.sleep(2)
        self.driver.find_element(By.ID, self.CTPPinName_id17).clear()
        self.driver.find_element(By.ID, self.CTPPinName_id17).send_keys(CTPPinName17)

    def setNewCTPPinName18(self, CTPPinName18):
        time.sleep(2)
        self.driver.find_element(By.ID, self.CTPPinName_id18).clear()
        self.driver.find_element(By.ID, self.CTPPinName_id18).send_keys(CTPPinName18)

    def setNewCTPPinName19(self, CTPPinName19):
        time.sleep(2)
        self.driver.find_element(By.ID, self.CTPPinName_id19).clear()
        self.driver.find_element(By.ID, self.CTPPinName_id19).send_keys(CTPPinName19)

    def setNewCTPPinName20(self, CTPPinName20):
        time.sleep(2)
        self.driver.find_element(By.ID, self.CTPPinName_id20).clear()
        self.driver.find_element(By.ID, self.CTPPinName_id20).send_keys(CTPPinName20)

    def setNewCTPPinName21(self, CTPPinName21):
        time.sleep(2)
        self.driver.find_element(By.ID, self.CTPPinName_id21).clear()
        self.driver.find_element(By.ID, self.CTPPinName_id21).send_keys(CTPPinName21)

    def setNewCTPPinName22(self, CTPPinName22):
        time.sleep(2)
        self.driver.find_element(By.ID, self.CTPPinName_id22).clear()
        self.driver.find_element(By.ID, self.CTPPinName_id22).send_keys(CTPPinName22)

    def setNewCTPPinName23(self, CTPPinName23):
        time.sleep(2)
        self.driver.find_element(By.ID, self.CTPPinName_id23).clear()
        self.driver.find_element(By.ID, self.CTPPinName_id23).send_keys(CTPPinName23)

    def setNewCTPPinName24(self, CTPPinName24):
        time.sleep(2)
        self.driver.find_element(By.ID, self.CTPPinName_id24).clear()
        self.driver.find_element(By.ID, self.CTPPinName_id24).send_keys(CTPPinName24)

    def setNewCTPPinName25(self, CTPPinName25):
        time.sleep(2)
        self.driver.find_element(By.ID, self.CTPPinName_id25).clear()
        self.driver.find_element(By.ID, self.CTPPinName_id25).send_keys(CTPPinName25)

    def setNewCTPPinName26(self, CTPPinName26):
        time.sleep(2)
        self.driver.find_element(By.ID, self.CTPPinName_id26).clear()
        self.driver.find_element(By.ID, self.CTPPinName_id26).send_keys(CTPPinName26)

    def setNewCTPPinName27(self, CTPPinName27):
        time.sleep(2)
        self.driver.find_element(By.ID, self.CTPPinName_id27).clear()
        self.driver.find_element(By.ID, self.CTPPinName_id27).send_keys(CTPPinName27)

    def setNewCTPPinName28(self, CTPPinName28):
        time.sleep(2)
        self.driver.find_element(By.ID, self.CTPPinName_id28).clear()
        self.driver.find_element(By.ID, self.CTPPinName_id28).send_keys(CTPPinName28)

    def setNewCTPPinName29(self, CTPPinName29):
        time.sleep(2)
        self.driver.find_element(By.ID, self.CTPPinName_id29).clear()
        self.driver.find_element(By.ID, self.CTPPinName_id29).send_keys(CTPPinName29)

    def setNewCTPPinName30(self, CTPPinName30):
        time.sleep(2)
        self.driver.find_element(By.ID, self.CTPPinName_id30).clear()
        self.driver.find_element(By.ID, self.CTPPinName_id30).send_keys(CTPPinName30)

    def setNewCTPPinName31(self, CTPPinName31):
        time.sleep(2)
        self.driver.find_element(By.ID, self.CTPPinName_id31).clear()
        self.driver.find_element(By.ID, self.CTPPinName_id31).send_keys(CTPPinName31)

    def setNewCTPPinName32(self, CTPPinName32):
        time.sleep(2)
        self.driver.find_element(By.ID, self.CTPPinName_id32).clear()
        self.driver.find_element(By.ID, self.CTPPinName_id32).send_keys(CTPPinName32)

    def setNewCTPPinName33(self, CTPPinName33):
        time.sleep(2)
        self.driver.find_element(By.ID, self.CTPPinName_id33).clear()
        self.driver.find_element(By.ID, self.CTPPinName_id33).send_keys(CTPPinName33)

    # def setEditXCodeCTPPin1Name(self, EditXCodeCTPPin1Name):
    #     time.sleep(2)
    #     self.driver.find_element(By.ID, self.EditXCodeCTPPin1Name_id).clear()
    #     self.driver.find_element(By.ID, self.EditXCodeCTPPin1Name_id).send_keys(EditXCodeCTPPin1Name)
    #
    # def setEditXCodeCTPPin2Name(self, EditXCodeCTPPin2Name):
    #     time.sleep(2)
    #     self.driver.find_element(By.ID, self.EditXCodeCTPPin2Name_id).clear()
    #     self.driver.find_element(By.ID, self.EditXCodeCTPPin2Name_id).send_keys(EditXCodeCTPPin2Name)

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
