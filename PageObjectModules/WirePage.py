from selenium.webdriver.common.by import By
import time

class Wire:

    NewWire_id = "txtNewWireId"
    PushMinValue_id = "txtNewPushMinValue"
    PushMaxValue_id = "txtNewPushMaxValue"
    PullMinValue_id = "txtNewPullMinValue"
    PullMaxValue_id = "txtNewPullMaxValue"
    EditWire_id = "txtNewWireId"
    EditPushMinValue_id = "txtNewPushMinValue"
    EditPushMaxValue_id = "txtNewPushMaxValue"
    EditPullMinValue_id = "txtNewPullMinValue"
    EditPullMaxValue_id = "txtNewPullMaxValue"
    CopyWire_id = "txtCopyNewWireId"
    text_projectTab_link_text = "Project"
    text_wireTab_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[1]/div/ul/li[3]/a"
    checkbox_select_wire_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/div/input"
    btn_new_wire_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[1]/div[1]/button[1]"
    NewWiregroup_id = "drdGrpId"
    list_select_new_color1_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[3]/div[3]/div/div/div[2]/select[1]/option[4]"
    list_select_new_color2_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[3]/div[3]/div/div/div[2]/select[2]/option[5]"
    list_select_new_color3_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[3]/div[3]/div/div/div[2]/select[3]/option[3]"
    list_select_new_picktolight_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[3]/div[3]/div/div/div[2]/select[4]/option[4]"
    list_select_new_WLEDPinName_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[3]/div[3]/div/div/div[2]/select[5]/option[5]"
    btn_new_wireSave_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[3]/div[3]/div/div/div[2]/div/button[3]"
    btn_edit_wire_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[1]/div[1]/button[2]"
    list_select_edit_wireGroupID_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[3]/div[3]/div/div/div[2]/select[1]/option[3]"
    list_select_edit_color1_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[3]/div[3]/div/div/div[2]/select[2]/option[3]"
    list_select_edit_color2_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[3]/div[3]/div/div/div[2]/select[3]/option[2]"
    list_select_edit_color3_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[3]/div[3]/div/div/div[2]/select[4]/option[1]"
    list_select_edit_picktolight_xpath = "//*[@id='drdPickToLightId']"
    list_select_edit_WLEDPinName_xpath = "//*[@id='txtNewWledPinName']"
    btn_edit_wireUpdate_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[3]/div[3]/div/div/div[2]/div/button[2]"
    btn_copy_wire_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[1]/div[1]/button[3]"
    btn_copy_wireSaveas_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[3]/div[5]/div/div/div[2]/div/button[2]"
    btn_delete_wire_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[1]/div[1]/button[4]"
    btn_confirmdelete_wire_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[3]/div[6]/div/div/div[2]/div/button[2]"

    def __init__(self, driver):
        self.driver = driver

    def clickProjectTab(self):
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, self.text_projectTab_link_text).click()

    def clickVariantTab(self):
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Variant").click()

    def clickWireTab(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.text_wireTab_xpath).click()

    def SelectWire(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.checkbox_select_wire_xpath).click()

    def ClickNewWireButton(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_new_wire_xpath).click()

    def setNewWireID(self, NewWireID):
        time.sleep(2)
        self.driver.find_element(By.ID, self.NewWire_id).clear()
        self.driver.find_element(By.ID, self.NewWire_id).send_keys(NewWireID)

    def SelectGroupIDFromList(self, NewwireGroupID):
        time.sleep(2)
        self.driver.find_element(By.ID, self.NewWiregroup_id).clear()
        self.driver.find_element(By.ID, self.NewWiregroup_id).send_keys(NewwireGroupID)

    def SelectColor1(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.list_select_new_color1_xpath).click()

    def SelectColor2(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.list_select_new_color2_xpath).click()

    def SelectColor3(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.list_select_new_color3_xpath).click()

    def setPushMinValue(self, PushMinValue):
        time.sleep(2)
        self.driver.find_element(By.ID, self.PushMinValue_id).clear()
        self.driver.find_element(By.ID, self.PushMinValue_id).send_keys(PushMinValue)

    def setPushMaxValue(self, PushMaxValue):
        time.sleep(2)
        self.driver.find_element(By.ID, self.PushMaxValue_id).clear()
        self.driver.find_element(By.ID, self.PushMaxValue_id).send_keys(PushMaxValue)

    def setPullMinValue(self, PullMinValue):
        time.sleep(2)
        self.driver.find_element(By.ID, self.PullMinValue_id).clear()
        self.driver.find_element(By.ID, self.PullMinValue_id).send_keys(PullMinValue)

    def setPullMaxValue(self, PullMaxValue):
        time.sleep(2)
        self.driver.find_element(By.ID, self.PullMaxValue_id).clear()
        self.driver.find_element(By.ID, self.PullMaxValue_id).send_keys(PullMaxValue)

    def SelectPickToLightFromList(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.list_select_new_picktolight_xpath).click()

    def SelectWLEDPinName(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.list_select_new_WLEDPinName_xpath).click()

    def NewWireClickSaveButton(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_new_wireSave_xpath).click()

    def ClickEditWireButton(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_edit_wire_xpath).click()

    def setEditWireID(self, EditWireID):
        time.sleep(2)
        self.driver.find_element(By.ID, self.EditWire_id).clear()
        self.driver.find_element(By.ID, self.EditWire_id).send_keys(EditWireID)

    def EditGroupIDFromList(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.list_select_edit_wireGroupID_xpath).click()

    def EditColor1(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.list_select_edit_color1_xpath).click()

    def EditColor2(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.list_select_edit_color2_xpath).click()

    def EditColor3(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.list_select_edit_color3_xpath).click()

    def setEditPushMinValue(self, EditPushMinValue):
        time.sleep(2)
        self.driver.find_element(By.ID, self.EditPushMinValue_id).clear()
        self.driver.find_element(By.ID, self.EditPushMinValue_id).send_keys(EditPushMinValue)

    def setEditPushMaxValue(self, EditPushMaxValue):
        time.sleep(2)
        self.driver.find_element(By.ID, self.EditPushMaxValue_id).clear()
        self.driver.find_element(By.ID, self.EditPushMaxValue_id).send_keys(EditPushMaxValue)

    def setEditPullMinValue(self, EditPullMinValue):
        time.sleep(2)
        self.driver.find_element(By.ID, self.EditPullMinValue_id).clear()
        self.driver.find_element(By.ID, self.EditPullMinValue_id).send_keys(EditPullMinValue)

    def setEditPullMaxValue(self, EditPullMaxValue):
        time.sleep(2)
        self.driver.find_element(By.ID, self.EditPullMaxValue_id).clear()
        self.driver.find_element(By.ID, self.EditPullMaxValue_id).send_keys(EditPullMaxValue)

    def EditPickToLightFromList(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.list_select_edit_picktolight_xpath).click()

    def EditWLEDPinName(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.list_select_edit_WLEDPinName_xpath).click()

    def EditWireClickUpdateButton(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_edit_wireUpdate_xpath).click()

    def ClickWireCopyButton(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_copy_wire_xpath).click()

    def setCopyWireID(self, CopyWireID):
        time.sleep(2)
        self.driver.find_element(By.ID, self.CopyWire_id).clear()
        self.driver.find_element(By.ID, self.CopyWire_id).send_keys(CopyWireID)

    def CopyWireClickSaveAsButton(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_copy_wireSaveas_xpath).click()

    def WireClickDeleteButton(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_delete_wire_xpath).click()

    def WireConfirmDelete(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_confirmdelete_wire_xpath).click()

class WireColorScheme:

    NewWireColorSchemeName_id = "txtNewColorSchemeName"
    NewWireColorSchemeAbbreviation_id = "txtColorAbbreviation"
    EditWireColorSchemeName_id = "txtNewColorSchemeName"
    EditWireColorSchemeAbbreviation_id = "txtColorAbbreviation"
    text_projectTab_xpath = "/html/body/div[1]/div[1]/div/div/nav/div/div/div[1]/a[2]"
    text_wireTab_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[1]/div/ul/li[3]/a"
    btn_new_wireschemecolor_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[3]/div[2]/div/div/div[2]/div[1]/div[1]/button[1]"
    text_wirecolorarea_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[3]/div[4]/div/div/div[2]/input[3]"
    btn_new_wireschemecolorSave_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[3]/div[4]/div/div/div[2]/div/button[3]"
    checkbox_select_wirecolorscheme_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div[1]/div/input"
    btn_edit_wirecolorscheme_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[3]/div[2]/div/div/div[2]/div[1]/div[1]/button[2]"
    btn_edit_wirecolorschemeUpdate_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[3]/div[4]/div/div/div[2]/div/button[2]"
    btn_delete_wirecolorscheme_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[3]/div[2]/div/div/div[2]/div[1]/div[1]/button[3]"
    btn_confirmdelete_wirecolorscheme_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[3]/div[7]/div/div/div[2]/div/button[2]"

    def __init__(self, driver):
        self.driver = driver

    def clickProjectTab(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.text_projectTab_xpath).click()

    def clickVariantTab(self):
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Variant").click()

    def clickWireTab(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.text_wireTab_xpath).click()

    def ClickNewWireSchemeColorButton(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_new_wireschemecolor_xpath).click()

    def setNewWireColorSchemeName(self, NewWireColorSchemeName):
        time.sleep(2)
        self.driver.find_element(By.ID, self.NewWireColorSchemeName_id).clear()
        self.driver.find_element(By.ID, self.NewWireColorSchemeName_id).send_keys(NewWireColorSchemeName)

    def setNewWireColorSchemeAbbreviation(self, NewWireColorSchemeAbbreviation):
        time.sleep(2)
        self.driver.find_element(By.ID, self.NewWireColorSchemeAbbreviation_id).clear()
        self.driver.find_element(By.ID, self.NewWireColorSchemeAbbreviation_id).send_keys(NewWireColorSchemeAbbreviation)

    def ClickWireColorArea(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.text_wirecolorarea_xpath).click()

    def ClickWireColorSchemeSaveButton(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_new_wireschemecolorSave_xpath).click()

    def SelectWireColorScheme(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.checkbox_select_wirecolorscheme_xpath).click()

    def ClickEditWireSchemeColorButton(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_edit_wirecolorscheme_xpath).click()

    def setEditWireColorSchemeName(self, EditWireColorSchemeName):
        time.sleep(2)
        self.driver.find_element(By.ID, self.EditWireColorSchemeName_id).clear()
        self.driver.find_element(By.ID, self.EditWireColorSchemeName_id).send_keys(EditWireColorSchemeName)

    def setEditWireColorSchemeAbbreviation(self, EditWireColorSchemeAbbreviation):
        time.sleep(2)
        self.driver.find_element(By.ID, self.EditWireColorSchemeAbbreviation_id).clear()
        self.driver.find_element(By.ID, self.EditWireColorSchemeAbbreviation_id).send_keys(EditWireColorSchemeAbbreviation)

    def ClickWireColorSchemeUpdateButton(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_edit_wirecolorschemeUpdate_xpath).click()

    def WireColorSchemeClickDeleteButton(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_delete_wirecolorscheme_xpath).click()

    def WireColorSchemeConfirmDelete(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_confirmdelete_wirecolorscheme_xpath).click()
