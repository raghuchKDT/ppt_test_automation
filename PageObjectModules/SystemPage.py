import time

from selenium.webdriver.common.by import By

class Sys:

    textbox_filename_id = "names"
    Value1 = "value"
    Value2 = "values"
    text_systemTab_xpath = "/html/body/div/div[1]/div/div/nav/div/div/div[1]/a[4]"
    text_settingsTab_xpath = "/html/body/div/div[2]/main/div[2]/div/ul/li[1]/a"
    text_database_xpath = "/html/body/div/div[2]/main/div[4]/div/div[1]/div/div[1]/div[1]/h4/a"
    text_testreport_xpath = "/html/body/div/div[2]/main/div[4]/div/div[1]/div/div[2]/div[1]/h4/a"
    btn_edit_Testreport_xpath = "/html/body/div/div[2]/main/div[4]/div/div[1]/div/div[2]/div[1]/h4/span/button"
    btn_edit_TestreportSave_xpath = "/html/body/div[1]/div[2]/main/div[9]/div/div/div[2]/div/button[2]"
    btn_edit_TestreportCancel_xpath = "/html/body/div[1]/div[2]/main/div[9]/div/div/div[2]/div/button[1]"
    text_Systemlog_xpath = "/html/body/div/div[2]/main/div[4]/div/div[1]/div/div[3]/div[1]/h4/a"
    btn_edit_Systemlog_xpath = "/html/body/div/div[2]/main/div[4]/div/div[1]/div/div[3]/div[1]/h4/span/button"
    btn_edit_SystemlogSave_xpath = "/html/body/div[1]/div[2]/main/div[10]/div/div/div[2]/div/button[2]"
    btn_edit_SystemlogCancel_xpath = "/html/body/div[1]/div[2]/main/div[10]/div/div/div[2]/div/button[1]"
    text_language_xpath = "/html/body/div/div[2]/main/div[4]/div/div[1]/div/div[4]/div[1]/h4/a"
    radio_btn_Select_language_xpath = "/html/body/div/div[2]/main/div[4]/div/div[1]/div/div[4]/div[2]/div/div/div/div/div[2]/input"

    def __init__(self, driver):
        self.driver = driver

    def clicksystem(self):
        self.driver.find_element("xpath", self.text_systemTab_xpath).click()

    def Settings(self):
        self.driver.find_element("xpath", self.text_settingsTab_xpath).click()

    def Database(self):
        self.driver.find_element("xpath", self.text_database_xpath).click()

    def TestReport(self):
        self.driver.find_element(By.XPATH, self.text_testreport_xpath).click()

    def TRclickEdit(self):
        self.driver.find_element(By.XPATH, self.btn_edit_Testreport_xpath).click()

    def setValue1(self, value1):
        self.driver.find_element(By.ID, self.Value1).clear()
        self.driver.find_element(By.ID, self.Value1).send_keys(value1)

    def TRclickSave(self):
        self.driver.find_element("xpath", self.btn_edit_TestreportSave_xpath).click()

    def TRclickCancel(self):
        self.driver.find_element("xpath", self.btn_edit_TestreportCancel_xpath).click()

    def SystemLog(self):
        self.driver.find_element(By.XPATH, self.text_Systemlog_xpath).click()

    def SLclickEdit(self):
        self.driver.find_element("xpath", self.btn_edit_Systemlog_xpath).click()

    def setFileName(self, filename):
        self.driver.find_element(By.ID, self.textbox_filename_id).clear()
        self.driver.find_element(By.ID, self.textbox_filename_id).send_keys(filename)

    def setValue2(self, value2):
        self.driver.find_element(By.ID, self.Value2).clear()
        self.driver.find_element(By.ID, self.Value2).send_keys(value2)

    def SLclickSave(self):
        self.driver.find_element("xpath", self.btn_edit_SystemlogSave_xpath).click()

    def SLclickCancel(self):
        self.driver.find_element("xpath", self.btn_edit_SystemlogCancel_xpath).click()

    def Language(self):
        self.driver.find_element(By.XPATH, self.text_language_xpath).click()

    def Lclick(self):
        self.driver.find_element("xpath", self.radio_btn_Select_language_xpath).click()

class Dev:

    SysGrpName_id = "txtNewSystemGroup"
    SysGrpNameDesc_id = "txtSysDescription"
    SysGrpSerialNo_id = "txtSysSerialNumber"
    Printer_name_id = "txtPrinterName72"
    PPT_Test_Point_id = "testpoints"
    PPT_Test_Point_Qty_id = "quantity"
    text_systemTab_xpath = "/html/body/div/div[1]/div/div/nav/div/div/div[1]/a[4]"
    text_DeviceManagerTab_xpath = "/html/body/div/div[2]/main/div[2]/div/ul/li[2]/a"
    btn_new_Systemgroup_xpath = "/html/body/div/div[2]/main/div[4]/div/div[2]/div/div/div[1]/div/button[1]"
    btn_new_SystemgroupSave_xpath = "/html/body/div[1]/div[2]/main/div[7]/div/div/div[2]/div/button[2]"
    text_Systemgroup_xpath = "/html/body/div/div[2]/main/div[4]/div/div[2]/div/div/div[1]/span[1]/ul/li/div/div[1]/h6/a"
    text_RaspberryPi_xpath = "/html/body/div/div[2]/main/div[4]/div/div[2]/div/div/div[1]/span[1]/ul/li[1]/div/div[2]/div/span/div/div[2]/div/ul/li/a[1]"
    btn_delete_RaspberryPi_xpath = "/html/body/div/div[2]/main/div[4]/div/div[2]/div/div/div[1]/span[1]/ul/li[1]/div/div[2]/div/span/div/div[2]/div/ul/li/a[2]/svg/path"
    btn_confirmdelete_RaspberryPi_xpath = "/html/body/div[1]/div[2]/main/div[17]/div/div/div[2]/div[2]/button[2]"
    text_SerialPort_xpath = "/html/body/div/div[2]/main/div[4]/div/div[2]/div/div/div[1]/span[1]/ul/li[1]/div/div[2]/div/span/div/div[4]/div/ul/li/a[1]"
    btn_edit_SerialPort_xpath = "/html/body/div/div[2]/main/div[4]/div/div[2]/div/div/div[2]/div/span/div/div/div[1]/div[2]/button[1]"
    btn_edit_SerialPortSave_xpath = "/html/body/div/div[2]/main/div[4]/div/div[2]/div/div/div[2]/div/span/div/div/div[1]/div[2]/button[2]"
    text_Printer_xpath = "/html/body/div/div[2]/main/div[4]/div/div[2]/div/div/div[1]/span[1]/ul/li[1]/div/div[2]/div/span/div/div[6]/div/ul/li/a[1]"
    btn_edit_Printer_xpath = "/html/body/div/div[2]/main/div[4]/div/div[2]/div/div/div[2]/div/span/div/div/div[1]/div[2]/button[1]"
    btn_edit_PrinterSave_xpath ="/html/body/div/div[2]/main/div[4]/div/div[2]/div/div/div[2]/div/span/div/div/div[1]/div[2]/button[2]"
    text_PPTMasterCard_xpath = "/html/body/div/div[2]/main/div[4]/div/div[2]/div/div/div[1]/span[1]/ul/li[1]/div/div[2]/div/span/div/div[7]/h6/a"
    text_PPTtestpointCard_xpath = "/html/body/div/div[2]/main/div[4]/div/div[2]/div/div/div[1]/span[1]/ul/li[1]/div/div[2]/div/span/div/div[8]/div/ul/li"
    btn_edit_PPTtestpointCard_xpath = "/html/body/div/div[2]/main/div[4]/div/div[2]/div/div/div[2]/div/span/div/div/div[1]/div[2]/button[1]"
    btn_edit_PPTtestpointCardPoints_xpath = "/html/body/div/div[2]/main/div[4]/div/div[2]/div/div/div[2]/div/span/div/div/div[2]/div[2]"
    btn_edit_PPTtestpointCardSave_xpath = "/html/body/div/div[2]/main/div[4]/div/div[2]/div/div/div[2]/div/span/div/div/div[1]/div[2]/button[2]"
    btn_delete_SystemGroup_ClassName = "/html/body/div/div[2]/main/div[4]/div/div[2]/div/div/div[1]/span[1]/ul/li/div/div[1]/h6/span"
    btn_Confirmdelete_SystemGroup_xpath = "//*[@id='btn-remove-sysDev']"

    def __init__(self, driver):
        self.driver = driver

    def clicksystem(self):
        self.driver.find_element("xpath", self.text_systemTab_xpath).click()

    def DeviceM(self):
        self.driver.find_element(By.XPATH, self.text_DeviceManagerTab_xpath).click()

    def SysGroupclickNew(self):
        self.driver.find_element("xpath", self.btn_new_Systemgroup_xpath).click()

    def setSysGrpName(self, SysGrpName):
        self.driver.find_element(By.ID, self.SysGrpName_id).clear()
        self.driver.find_element(By.ID, self.SysGrpName_id).send_keys(SysGrpName)

    def setSysGrpDesc(self, SysGrpDesc):
        self.driver.find_element(By.ID, self.SysGrpNameDesc_id).clear()
        self.driver.find_element(By.ID, self.SysGrpNameDesc_id).send_keys(SysGrpDesc)

    def setSysGrpSno(self, SysGrpSno):
        self.driver.find_element(By.ID, self.SysGrpSerialNo_id).clear()
        self.driver.find_element(By.ID, self.SysGrpSerialNo_id).send_keys(SysGrpSno)

    def SysGrpclickSave(self):
        self.driver.find_element("xpath", self.btn_new_SystemgroupSave_xpath).click()

    def SysGrpClick(self):
        self.driver.find_element(By.XPATH, self.text_Systemgroup_xpath).click()

    def RaspberryPiClick(self):
        self.driver.find_element(By.XPATH, self.text_RaspberryPi_xpath).click()

    def RaspBerryPiclickDelete(self):
        self.driver.find_element("xpath", self.btn_delete_RaspberryPi_xpath).click()

    def RaspBerryPiDeleted(self):
        self.driver.find_element("xpath", self.btn_confirmdelete_RaspberryPi_xpath).click()

    def SerialPort1Click(self):
        self.driver.find_element(By.XPATH, self.text_SerialPort_xpath).click()

    def SerialPort1clickEdit(self):
        self.driver.find_element("xpath", self.btn_edit_SerialPort_xpath).click()

    def SerialPort1clickSave(self):
        self.driver.find_element(By.XPATH, self.btn_edit_SerialPortSave_xpath).click()

    def PrinterClick(self):
        self.driver.find_element(By.XPATH, self.text_Printer_xpath).click()

    def PrinterclickEdit(self):
        self.driver.find_element("xpath", self.btn_edit_Printer_xpath).click()

    def setPrinterName(self, printername):
        self.driver.find_element(By.ID, self.Printer_name_id).clear()
        self.driver.find_element(By.ID, self.Printer_name_id).send_keys(printername)

    def PrinterclickSave(self):
        self.driver.find_element("xpath", self.btn_edit_PrinterSave_xpath).click()

    def PPTMasterCardClick(self):
        self.driver.find_element(By.XPATH, self.text_PPTMasterCard_xpath).click()

    def PPTTestPointCardClick(self):
        self.driver.find_element(By.XPATH, self.text_PPTtestpointCard_xpath).click()

    def PPTTestPointCardclickEdit(self):
        self.driver.find_element("xpath", self.btn_edit_PPTtestpointCard_xpath).click()

    def setPPTTestPointCardPoints(self):
        self.driver.find_element("xpath", self.btn_edit_PPTtestpointCardPoints_xpath).click()

    def setPPTTestPointCardQty(self, pptcardpointsqty):
        self.driver.find_element(By.ID, self.PPT_Test_Point_Qty_id).clear()
        self.driver.find_element(By.ID, self.PPT_Test_Point_Qty_id).send_keys(pptcardpointsqty)

    def PPTTestPointCardclickSave(self):
        self.driver.find_element("xpath", self.btn_edit_PPTtestpointCardSave_xpath).click()

    def SysGrpClickDelete(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_delete_SystemGroup_ClassName).click()

    def SysGrpDelete(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_Confirmdelete_SystemGroup_xpath).click()

class Var:

    VariableName1 = "variableName"
    VariableType1 = "variableType"
    Protocol1     = "protocol"
    Format1       = "format"
    DefaultContent1 = "defaultContent"
    text_systemTab_xpath = "/html/body/div/div[1]/div/div/nav/div/div/div[1]/a[4]"
    text_systemVariables_xpath = "/html/body/div/div[2]/main/div[2]/div/ul/li[3]/a"


    def __init__(self, driver):
        self.driver = driver

    def clicksystem(self):
        self.driver.find_element("xpath", self.text_systemTab_xpath).click()

    def SysVariables(self):
        self.driver.find_element(By.XPATH, self.text_systemVariables_xpath).click()

    def GlobalVariableNew(self):
        self.driver.find_element("xpath", '//*[@id="bntGoToCreateGlobalVariable"]').click()

    def setGlobVariableName(self, VariableName):
        self.driver.find_element(By.ID, self.VariableName1).clear()
        self.driver.find_element(By.ID, self.VariableName1).send_keys(VariableName)

    def setGlobVariableType(self, VariableType):
        self.driver.find_element(By.ID, self.VariableType1).clear()
        self.driver.find_element(By.ID, self.VariableType1).send_keys(VariableType)

    def setGlobVariableProtocol(self, Protocol):
        self.driver.find_element(By.ID, self.Protocol1).clear()
        self.driver.find_element(By.ID, self.Protocol1).send_keys(Protocol)

    def setGlobVariableFormat(self, Format):
        self.driver.find_element(By.ID, self. Format1).clear()
        self.driver.find_element(By.ID, self. Format1).send_keys(Format)

    def setGlobVariableDefaualtContent(self, DefaultContent):
        self.driver.find_element(By.ID, self.DefaultContent1).clear()
        self.driver.find_element(By.ID, self.DefaultContent1).send_keys(DefaultContent)


class ErrorCode:

    ErrorCodeDec_No = "noDec"
    ErrorCodeName1 = "txtName"
    ErrorCodeName_id = "geName"
    ErrorCodeDescr1 = "glDescription"
    ErrorCodeDesc_id = "geDescription"
    HardwareErrorCodeDec_No = "testDec"
    HardwareErrorCodeName1 = "testName"
    HardwareErrorCodeName_id = "thName"
    HardwareErrorCodeDescr1 = "testDescription"
    HardwareErrorCodeDescr_id = "thDescription"
    SoftwareErrorCodeDec_No = "pptDec"
    SoftwareErrorCodeName1 = "pptName"
    SoftwareErrorCodeName_id = "psName"
    SoftwareErrorCodeDescr1 = "pptDescription"
    SoftwareErrorCodeDescr_id = "psDescription"
    text_systemTab_xpath = "/html/body/div/div[1]/div/div/nav/div/div/div[1]/a[4]"
    text_errortab_xpath = "/html/body/div/div[2]/main/div[2]/div/ul/li[4]/a"
    btn_new_globalerrorcode_xpath = "/html/body/div/div[2]/main/div[4]/div/div[3]/div/div[1]/div/button"
    btn_new_globalerrorcodeSave_xpath = "/html/body/div[1]/div[2]/main/div[11]/div/div/div[2]/div[4]/button[2]"
    checkbox_select_globalerrorcode_xpath = "/html/body/div/div[2]/main/div[4]/div/div[3]/div/div[2]/div/div[1]/div/table/tbody/tr[1]/td[1]/label/span"
    btn_edit_globalerrorcode_xpath = "/html/body/div/div[2]/main/div[4]/div/div[3]/div/div[1]/div/a"
    btn_edit_globalerrorcodeSave_xpath = "/html/body/div[1]/div[2]/main/div[14]/div/div/div[2]/div[2]/button[2]"
    btn_new_hardwareErrorcode_xpath = "/html/body/div/div[2]/main/div[4]/div/div[3]/div/div[3]/div/button"
    btn_new_hardwareErrorcodeSave_xpath = "/html/body/div[1]/div[2]/main/div[12]/div/div/div[2]/div[4]/button[2]"
    checkbox_select_hardwareErrorcode_xpath = "/html/body/div/div[2]/main/div[4]/div/div[3]/div/div[4]/div/div[1]/div/table/tbody/tr[1]/td[1]/label/span"
    btn_edit_hardwareErrorcode_xpath = "/html/body/div/div[2]/main/div[4]/div/div[3]/div/div[3]/div/a"
    btn_edit_hardwareErrorcodeSave_xpath = "/html/body/div[1]/div[2]/main/div[15]/div/div/div[2]/div[2]/button[2]"
    btn_new_softwareErrorcode_xpath = "/html/body/div/div[2]/main/div[4]/div/div[3]/div/div[5]/div/button"
    btn_new_softwareErrorcodeSave_xpath = "/html/body/div[1]/div[2]/main/div[13]/div/div/div[2]/div[4]/button[2]"
    checkbox_select_softwareErrorcode_xpath = "/html/body/div/div[2]/main/div[4]/div/div[3]/div/div[6]/div/div[1]/div/table/tbody/tr[1]/td[1]/label/span"
    btn_edit_softwareErrorcode_xpath = "/html/body/div/div[2]/main/div[4]/div/div[3]/div/div[5]/div/a"
    btn_edit_softwareErrorcodeSave_xpath = "/html/body/div[1]/div[2]/main/div[16]/div/div/div[2]/div[2]/button[2]"


    def __init__(self, driver):
        self.driver = driver

    def clicksystem(self):
        self.driver.find_element("xpath", self.text_systemTab_xpath).click()

    def ErrorCodes(self):
        self.driver.find_element(By.XPATH, self.text_errortab_xpath).click()

    def GlobalErrorCodeNew(self):
        self.driver.find_element("xpath", self.btn_new_globalerrorcode_xpath).click()

    def setErrorCodeDecno(self, ErrorCodeDecno):
        time.sleep(2)
        self.driver.find_element(By.ID, self.ErrorCodeDec_No).clear()
        self.driver.find_element(By.ID, self.ErrorCodeDec_No).send_keys(ErrorCodeDecno)

    def setErrorCodeNewName(self, ErrorCodeName):
        self.driver.find_element(By.ID, self.ErrorCodeName1).clear()
        self.driver.find_element(By.ID, self.ErrorCodeName1).send_keys(ErrorCodeName)

    def setErrorCodeNewDesc(self, ErrorCodeDesc):
        self.driver.find_element(By.ID, self.ErrorCodeDescr1).clear()
        self.driver.find_element(By.ID, self.ErrorCodeDescr1).send_keys(ErrorCodeDesc)

    def GlobalErrorclickSave(self):
        self.driver.find_element("xpath", self.btn_new_globalerrorcodeSave_xpath).click()

    def GlobalErrorCodeSelectCheckbox(self):
        self.driver.find_element(By.XPATH, self.checkbox_select_globalerrorcode_xpath).click()

    def GlobalErrorCodeEdit(self):
        self.driver.find_element("xpath", self.btn_edit_globalerrorcode_xpath).click()

    def setErrorCodeEditName(self, ErrorCodeName_1):
        self.driver.find_element(By.ID, self.ErrorCodeName_id).clear()
        self.driver.find_element(By.ID, self.ErrorCodeName_id).send_keys(ErrorCodeName_1)

    def setErrorCodeEditDesc(self, ErrorCodeDesc_1):
        self.driver.find_element(By.ID, self.ErrorCodeDesc_id).clear()
        self.driver.find_element(By.ID, self.ErrorCodeDesc_id).send_keys(ErrorCodeDesc_1)

    def GlobalErrorEditSave(self):
        self.driver.find_element("xpath", self.btn_edit_globalerrorcodeSave_xpath).click()

    # Hardware Error Code:
    def HardwareErrorCodeNew(self):
        self.driver.find_element("xpath", self.btn_new_hardwareErrorcode_xpath).click()

    def setHardwareErrorCodeDecno(self, HardwareErrCodeDecNo):
        self.driver.find_element(By.ID, self.HardwareErrorCodeDec_No).clear()
        self.driver.find_element(By.ID, self.HardwareErrorCodeDec_No).send_keys(HardwareErrCodeDecNo)

    def setHardwareErrorCodeName(self, HardwareErrCodeName):
        self.driver.find_element(By.ID, self. HardwareErrorCodeName1).clear()
        self.driver.find_element(By.ID, self. HardwareErrorCodeName1).send_keys(HardwareErrCodeName)

    def setHardwareErrorCodeDesc(self, HardwareErrCodeDesc):
        self.driver.find_element(By.ID, self.HardwareErrorCodeDescr1).clear()
        self.driver.find_element(By.ID, self.HardwareErrorCodeDescr1).send_keys(HardwareErrCodeDesc)

    def HardwareErrorclickSave(self):
        self.driver.find_element("xpath", self.btn_new_hardwareErrorcodeSave_xpath).click()

    def HardwareErrorCodeSelectCheckbox(self):
        self.driver.find_element(By.XPATH, self.checkbox_select_hardwareErrorcode_xpath).click()

    def HardwareErrorCodeEdit(self):
        self.driver.find_element("xpath", self.btn_edit_hardwareErrorcode_xpath).click()

    def setHardwareErrorCodeEditName(self, HardwareErrCodeName_1):
        self.driver.find_element(By.ID, self. HardwareErrorCodeName_id).clear()
        self.driver.find_element(By.ID, self. HardwareErrorCodeName_id).send_keys(HardwareErrCodeName_1)

    def setHardwareErrorCodeEditDesc(self, HardwareErrCodeDesc_1):
        self.driver.find_element(By.ID, self.HardwareErrorCodeDescr_id).clear()
        self.driver.find_element(By.ID, self.HardwareErrorCodeDescr_id).send_keys(HardwareErrCodeDesc_1)

    def HardwareErrorEditSave(self):
        self.driver.find_element("xpath", self.btn_edit_hardwareErrorcodeSave_xpath).click()

    # Software Error Code:
    def SoftwareErrorCodeNew(self):
        self.driver.find_element("xpath", self.btn_new_softwareErrorcode_xpath).click()

    def setSoftwareErrorCodeDecno(self, SoftwareErrCodeDecNo):
        self.driver.find_element(By.ID, self.SoftwareErrorCodeDec_No).clear()
        self.driver.find_element(By.ID, self.SoftwareErrorCodeDec_No).send_keys(SoftwareErrCodeDecNo)

    def setSoftwareErrorCodeName(self, SoftwareErrCodeName):
        self.driver.find_element(By.ID, self.SoftwareErrorCodeName1).clear()
        self.driver.find_element(By.ID, self.SoftwareErrorCodeName1).send_keys(SoftwareErrCodeName)

    def setSoftwareErrorCodeDesc(self, SoftwareErrCodeDesc):
        self.driver.find_element(By.ID, self.SoftwareErrorCodeDescr1).clear()
        self.driver.find_element(By.ID, self.SoftwareErrorCodeDescr1).send_keys(SoftwareErrCodeDesc)

    def SoftwareErrorclickSave(self):
        self.driver.find_element("xpath", self.btn_new_softwareErrorcodeSave_xpath).click()

    def SoftwareErrorCodeSelectCheckbox(self):
        self.driver.find_element(By.XPATH, self.checkbox_select_softwareErrorcode_xpath).click()

    def SoftwareErrorCodeEdit(self):
        self.driver.find_element("xpath", self.btn_edit_softwareErrorcode_xpath).click()

    def setSoftwareErrorCodeEditName(self, SoftwareErrCodeName_1):
        self.driver.find_element(By.ID, self. SoftwareErrorCodeName_id).clear()
        self.driver.find_element(By.ID, self. SoftwareErrorCodeName_id).send_keys(SoftwareErrCodeName_1)

    def setSoftwareErrorCodeEditDesc(self, SoftwareErrCodeDesc_1):
        self.driver.find_element(By.ID, self.SoftwareErrorCodeDescr_id).clear()
        self.driver.find_element(By.ID, self.SoftwareErrorCodeDescr_id).send_keys(SoftwareErrCodeDesc_1)

    def SoftwareErrorEditSave(self):
        self.driver.find_element("xpath", self.btn_edit_softwareErrorcodeSave_xpath).click()

