from telnetlib import EC
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time
from PageObjects.LoginPage import Login
from PageObjects.Systempage import Sys
from PageObjects.Systempage import Dev
from PageObjects.Systempage import Var
from PageObjects.Systempage import ErrorCode


# class Test_Settings:
#
#     filename = "Log_Files_PPT"
#     value1   = "101"
#     value2   = "102"
#
#     def test_Database_Elements(self, user_login):
#         self.driver = user_login
#         self.ss = Sys(self.driver)
#         self.ss.clicksystem()
#         self.driver.implicitly_wait(4)
#         self.ss.Settings()
#         time.sleep(2)
#
#         Database = []
#         Database = self.driver.find_elements(By.XPATH, "//*[@id='collapseOne']/div")
#         for dat in Database:
#             print(dat.text)
#
#
#     def test_DatabaseData(self, user_login):
#         self.driver = user_login
#         self.ss = Sys(self.driver)
#         self.ss.clicksystem()
#         self.ss.Settings()
#         time.sleep(2)
#
#         expected_data1 = ['Name', 'Base Directory', 'User', 'Password']
#         data_base_data1 = self.driver.find_elements(By.XPATH, "//*[@id='layoutSidenav_content']/main/div[3]/div/div")
#         for idx, base_data1 in enumerate(data_base_data1):
#             print(idx, base_data1.text)
#             assert (expected_data1[idx] == base_data1.text)
#
#     def test_TestReport(self, user_login):
#         self.driver = user_login
#         self.ss = Sys(self.driver)
#         time.sleep(2)
#         self.ss.clicksystem()
#         self.ss.Settings()
#         self.ss.TestReport()
#         time.sleep(2)
#         self.ss.TRclickEdit()
#         time.sleep(2)
#         dropdown = self.driver.find_element(By.ID, 'optionValue')
#         drp = Select(dropdown)
#         time.sleep(2)
#         drp.select_by_visible_text('By Month')
#         self.ss.setValue1(self.value1)
#         self.ss.TRclickSave()
#         time.sleep(2)
#         assert "Data Added Successfully" in self.driver.page_source
#
#
#     def test_SystemLog(self, user_login):
#         self.driver = user_login
#         self.ss = Sys(self.driver)
#         time.sleep(2)
#         self.ss.clicksystem()
#         self.ss.Settings()
#         self.ss.SystemLog()
#         self.ss.SLclickEdit()
#         self.driver.implicitly_wait(4)
#         dropdown = self.driver.find_element(By.ID, 'optionValue')
#         drp = Select(dropdown)
#         time.sleep(2)
#         drp.select_by_visible_text('Free Space')
#         time.sleep(2)
#         self.ss.setFileName(self.filename)
#         self.ss.setValue2(self.value2)
#         self.ss.SLclickSave()
#         time.sleep(2)
#         assert "Data Added Successfully" in self.driver.page_source
#
#
#     def test_Language(self, user_login):
#         self.driver = user_login
#         self.ss = Sys(self.driver)
#         time.sleep(2)
#         self.ss.clicksystem()
#         self.ss.Settings()
#         self.ss.Language()
#         time.sleep(2)
#         self.ss.Lclick()
#
# class Test_DeviceManager:
#
#     SysGrpName = "System Group -1"
#     SysGrpDesc = "This is the First System Group Description"
#     SysGrpSno = "1"
#     printername = "Printer 1"
#     pptcardpoints = "50"
#     pptcardpointsqty = "1"
#
#     # def test_SystemGroupCreateNew(self, user_login):
#     #     self.driver = user_login
#     #     self.ss = Sys(self.driver)
#     #     self.driver.implicitly_wait(4)
#     #     self.ss.clicksystem()
#     #     self.dm = Dev(self.driver)
#     #     self.dm.DeviceM()
#     #     self.driver.implicitly_wait(4)
#     #     self.dm.SysGroupclickNew()
#     #     self.dm.setSysGrpName(self.SysGrpName)
#     #     self.driver.implicitly_wait(4)
#     #     self.dm.setSysGrpDesc(self.SysGrpDesc)
#     #     self.driver.implicitly_wait(4)
#     #     self.dm.setSysGrpSno(self.SysGrpSno)
#     #     self.driver.implicitly_wait(4)
#     #     self.dm.SysGrpclickSave()
#     #     time.sleep(2)
#     #     assert "Added Successfully." in self.driver.page_source
#
#     def test_SystemGroupClickProperties(self, user_login):
#         self.driver = user_login
#         self.ss = Sys(self.driver)
#         self.driver.implicitly_wait(4)
#         self.ss.clicksystem()
#         time.sleep(2)
#         self.dm = Dev(self.driver)
#         self.dm.DeviceM()
#         time.sleep(2)
#         self.dm.SysGrpClick()
#         time.sleep(2)
#
#         sysgrpprop = self.driver.find_elements(By.XPATH, "//*[@id='collapseSysDescBelow']/div")
#         print(len(sysgrpprop))
#         expected = ['Description', 'Serial Number']
#         contents = []
#         for sg in sysgrpprop:
#             contents.append(sg.text)
#         for sgp in expected:
#             assert (sgp in contents[0]) == True
#
#     def test_SystemGroupDevices(self, user_login):
#         self.driver = user_login
#         self.ss = Sys(self.driver)
#         self.driver.implicitly_wait(4)
#         self.ss.clicksystem()
#         time.sleep(2)
#         self.dm = Dev(self.driver)
#         self.dm.DeviceM()
#         time.sleep(2)
#
#         sysgrpprop = self.driver.find_elements(By.XPATH, "//*[@id='ViewDevices']/ul")
#         print(len(sysgrpprop))
#         expected = ['Raspberry pi 4', 'Serial Port', 'Printer', 'PPT Master Card', 'PPT Test Point Card', 'Loudspeaker', 'Operation Buttons']
#         contents = []
#         for sg in sysgrpprop:
#             contents.append(sg.text)
#         for sgp in expected:
#             assert (sgp in contents[0]) == True
#
#     def test_RaspberyPi4Prop(self, user_login):
#         self.driver = user_login
#         self.ss = Sys(self.driver)
#         self.driver.implicitly_wait(4)
#         self.ss.clicksystem()
#         time.sleep(2)
#         self.dm = Dev(self.driver)
#         self.dm.DeviceM()
#         self.dm.RaspberryPiClick()
#         time.sleep(2)
#
#         rasppiprop = self.driver.find_elements(By.XPATH, "//*[@id='raspberryPiBody']/div")
#         print(len(rasppiprop))
#         expected = ['Raspberry Pi 4', 'HostName', 'Linux Version', 'IP Address']
#         contents = []
#         for rp in rasppiprop:
#             contents.append(rp.text)
#         for rpp in expected:
#             assert ('Raspberry Pi 4' in []) == True
#         time.sleep(1)
#         self.dm.RaspBerryPiclickDelete()
#         time.sleep(1)
#         self.dm.RaspBerryPiDeleted()
#         time.sleep(1)
#         assert "Deleted Successfully." in self.driver.page_source
#
#
#     def test_SerialPort1Properties(self, user_login):
#         self.driver = user_login
#         self.ss = Sys(self.driver)
#         self.driver.implicitly_wait(4)
#         self.ss.clicksystem()
#         time.sleep(1)
#         self.dm = Dev(self.driver)
#         self.dm.DeviceM()
#         self.dm.SerialPort1Click()
#         time.sleep(1)
#
#         serialportprop = self.driver.find_elements(By.XPATH, "//*[@id='divDeviceProperty']")
#         print(len(serialportprop))
#         expected = ['Port Name', 'Baud Rate', 'Data Bits', 'Stop Bits', 'Parity', 'FlowControl']
#         contents = []
#         for sp in serialportprop:
#             contents.append(sp.text)
#         for spp in expected:
#             assert (spp in contents[0]) == True
#
#     def test_SerialPort1Edit(self, user_login):
#         self.driver = user_login
#         self.ss = Sys(self.driver)
#         self.driver.implicitly_wait(4)
#         self.ss.clicksystem()
#         time.sleep(2)
#         self.dm = Dev(self.driver)
#         self.dm.DeviceM()
#         self.driver.implicitly_wait(4)
#         self.dm.SerialPort1Click()
#         time.sleep(2)
#         self.dm.SerialPort1clickEdit()
#         time.sleep(2)
#
#         dropdown1 = self.driver.find_element(By.CLASS_NAME, 'cdrdport')
#         drp1 = Select(dropdown1)
#         time.sleep(2)
#         drp1.select_by_visible_text('19200')
#         time.sleep(2)
#
#         dropdown2 = self.driver.find_element(By.ID, 'databits128')
#         drp2 = Select(dropdown2)
#         time.sleep(2)
#         drp2.select_by_visible_text('5')
#         time.sleep(1)
#
#         dropdown3 = self.driver.find_element(By.ID, 'stopbits128')
#         drp3 = Select(dropdown3)
#         time.sleep(2)
#         drp3.select_by_visible_text('2')
#
#         dropdown4 = self.driver.find_element(By.ID, 'parity128')
#         drp4 = Select(dropdown4)
#         time.sleep(2)
#         drp4.select_by_visible_text('Even')
#
#         dropdown5 = self.driver.find_element(By.ID, 'flowcontrol128')
#         drp5 = Select(dropdown5)
#         time.sleep(2)
#         drp5.select_by_visible_text('Xon/Xoff')
#         time.sleep(2)
#         self.dm.SerialPort1clickSave()
#         time.sleep(2)
#         assert "Updated Successfully." in self.driver.page_source
#
#     def test_PrinterProp(self, user_login):
#         self.driver = user_login
#         self.ss = Sys(self.driver)
#         self.driver.implicitly_wait(4)
#         self.ss.clicksystem()
#         time.sleep(2)
#         self.dm = Dev(self.driver)
#         self.dm.DeviceM()
#         self.dm.PrinterClick()
#         time.sleep(2)
#
#         printerprop = self.driver.find_elements(By.XPATH, "//*[@id='divDeviceProperty']")
#         print(len(printerprop))
#         expected = ['Printer Selection', 'Printer Name', 'Printer Type', 'Serial Port']
#         contents = []
#         for pp in printerprop:
#             contents.append(pp.text)
#         for pps in expected:
#             assert (pps in contents[0]) == True
#
#     def test_PrinterPropEdit(self, user_login):
#         self.driver = user_login
#         self.ss = Sys(self.driver)
#         self.driver.implicitly_wait(4)
#         self.ss.clicksystem()
#         time.sleep(2)
#         self.dm = Dev(self.driver)
#         self.dm.DeviceM()
#         self.driver.implicitly_wait(4)
#         self.dm.PrinterClick()
#         time.sleep(2)
#         self.dm.PrinterclickEdit()
#         time.sleep(2)
#         self.dm.setPrinterName(self.printername)
#         time.sleep(2)
#
#         dropdown1 = self.driver.find_element(By.ID, 'PrinterTypeId64')
#         drp1 = Select(dropdown1)
#         time.sleep(2)
#         drp1.select_by_visible_text('Serial printer')
#
#         dropdown2 = self.driver.find_element(By.ID, 'SerialPortId64')
#         drp2 = Select(dropdown2)
#         time.sleep(2)
#         drp2.select_by_visible_text('ttyUSB0')
#         time.sleep(2)
#         self.dm.PrinterclickSave()
#         time.sleep(2)
#         assert "Updated Successfully." in self.driver.page_source
#
#     def test_PPTMasterCardProp(self, user_login):
#         self.driver = user_login
#         self.ss = Sys(self.driver)
#         self.driver.implicitly_wait(4)
#         self.ss.clicksystem()
#         time.sleep(2)
#         self.dm = Dev(self.driver)
#         self.dm.DeviceM()
#         self.dm.PPTMasterCardClick()
#         time.sleep(2)
#
#     def test_PPTTestPointCardProp(self, user_login):
#         self.driver = user_login
#         self.ss = Sys(self.driver)
#         self.driver.implicitly_wait(4)
#         self.ss.clicksystem()
#         time.sleep(2)
#         self.dm = Dev(self.driver)
#         self.dm.DeviceM()
#         self.dm.PPTMasterCardClick()
#         time.sleep(2)
#         self.dm.PPTTestPointCardClick()
#         time.sleep(2)
#
#         ppttestpointcardprop = self.driver.find_elements(By.XPATH, "//*[@id='divDeviceProperty']")
#         print(len(ppttestpointcardprop))
#         expected = ['PPT Test Point Card', 'Test Points', 'Quantity']
#         contents = []
#         for pptc in ppttestpointcardprop:
#             contents.append(pptc.text)
#         for pptcs in expected:
#             assert (pptcs in contents[0]) == True
#
#     def test_PPTTestPointCardPropEdit(self, user_login):
#         self.driver = user_login
#         self.ss = Sys(self.driver)
#         self.driver.implicitly_wait(4)
#         self.ss.clicksystem()
#         time.sleep(2)
#         self.dm = Dev(self.driver)
#         self.dm.DeviceM()
#         self.driver.implicitly_wait(4)
#         self.dm.PPTMasterCardClick()
#         time.sleep(2)
#         self.dm.PPTTestPointCardClick()
#         time.sleep(2)
#         self.dm.PPTTestPointCardclickEdit()
#         time.sleep(2)
#         self.dm.setPPTTestPointCardPoints(self.pptcardpoints)
#         time.sleep(2)
#         self.dm.setPPTTestPointCardQty(self.pptcardpointsqty)
#         time.sleep(2)
#         self.dm.PPTTestPointCardclickSave()
#         time.sleep(2)
#         assert "Updated Successfully." in self.driver.page_source
#
#     def test_ExistingSystemGroupDelete(self, user_login):
#         self.driver = user_login
#         self.ss = Sys(self.driver)
#         self.driver.implicitly_wait(4)
#         self.ss.clicksystem()
#         self.dm = Dev(self.driver)
#         self.dm.DeviceM()
#         self.driver.implicitly_wait(4)
#         self.dm.SysGrpClickDelete()
#         time.sleep(2)
#         self.dm.SysGrpDelete()
#         time.sleep(2)
#         assert "Deleted Successfully." in self.driver.page_source
#
# class Test_Variables:
#
#     def test_System_Variables_Header(self, user_login):
#
#         self.driver = user_login
#         self.ss = Sys(self.driver)
#         self.driver.implicitly_wait(4)
#         self.ss.clicksystem()
#         self.sv = Var(self.driver)
#         self.sv.SysVariables()
#         time.sleep(2)
#         table = self.driver.find_element(By.ID, "tblSystemGlobalVar")
#         header = table.find_elements(By.TAG_NAME, "th")
#         for headerEl in header:
#             print(headerEl.text)
#         time.sleep(2)
#
#
#     def test_System_Variables_Data(self, user_login):
#
#         self.driver = user_login
#         self.ss = Sys(self.driver)
#         self.driver.implicitly_wait(4)
#         self.ss.clicksystem()
#         self.sv = Var(self.driver)
#         self.sv.SysVariables()
#         time.sleep(2)
#         table = self.driver.find_element(By.ID, "tblSystemGlobalVar")
#         body = table.find_element(By.TAG_NAME, "tbody")
#         cells = body.find_elements(By.TAG_NAME, "tr")
#         for cell in cells:
#             print(cell.text)
#
# class Test_ErrorCode:
#
#     ErrorCodeDecno = "7"
#     ErrorCodeName = "ERR_Global"
#     ErrorCodeName_1 = "Global_ERR"
#     ErrorCodeDesc = "This is the Global Error Code"
#     ErrorCodeDesc_1 = "This is the Global Error Code of the system"
#
#     HardwareErrCodeDecNo = "203"
#     HardwareErrCodeName = "ERR_SERIAL_NOTFOUND"
#     HardwareErrCodeName_1 = "Err_Serial_No_NotFound"
#     HardwareErrCodeDesc = "This is the Hardware Error Code"
#     HardwareErrCodeDesc_1 = "This is system hardware error"
#
#     SoftwareErrCodeDecNo = "403"
#     SoftwareErrCodeName = "SFT_Error"
#     SoftwareErrCodeName_1 = "Error_SFT"
#     SoftwareErrCodeDesc = "This is the error Occured by Software"
#     SoftwareErrCodeDesc_1 = "This is PPT Software error"
#
#
#     def test_GlobalErrCode_Header(self, user_login):
#
#         self.driver = user_login
#         self.ss = Sys(self.driver)
#         self.driver.implicitly_wait(4)
#         self.ss.clicksystem()
#         self.ec = ErrorCode(self.driver)
#         self.ec.ErrorCodes()
#         time.sleep(2)
#         table = self.driver.find_element(By.ID, "tblGlobalErrorCodes")
#         header = table.find_elements(By.TAG_NAME, "th")
#         for headerEl in header:
#             print(headerEl.text)
#         time.sleep(2)
#
#
#     def test_GlobalErrCode_Data(self, user_login):
#
#         self.driver = user_login
#         self.ss = Sys(self.driver)
#         self.driver.implicitly_wait(4)
#         self.ss.clicksystem()
#         self.ec = ErrorCode(self.driver)
#         self.ec.ErrorCodes()
#         time.sleep(2)
#         table = self.driver.find_element(By.ID, "tblGlobalErrorCodes")
#         body = table.find_element(By.TAG_NAME, "tbody")
#         cells = body.find_elements(By.TAG_NAME, "tr")
#         for cell in cells:
#             print(cell.text)
#
#
#     def test_GlobalErrCode_CreateNew(self, user_login):
#         self.driver = user_login
#         self.ss = Sys(self.driver)
#         self.driver.implicitly_wait(4)
#         self.ss.clicksystem()
#         self.ec = ErrorCode(self.driver)
#         self.ec.ErrorCodes()
#         time.sleep(2)
#         self.ec.GlobalErrorCodeNew()
#         time.sleep(1)
#         self.ec.setErrorCodeDecno(self. ErrorCodeDecno)
#         time.sleep(1)
#         self.ec.setErrorCodeNewName(self.ErrorCodeName)
#         time.sleep(1)
#         self.ec.setErrorCodeNewDesc(self.ErrorCodeDesc)
#         time.sleep(1)
#         self.ec.GlobalErrorclickSave()
#         time.sleep(1)
#         assert "Updated Successfully." in self.driver.page_source
#
#
#     def test_GlobalErrCode_Edit(self, user_login):
#         self.driver = user_login
#         self.ss = Sys(self.driver)
#         self.driver.implicitly_wait(4)
#         self.ss.clicksystem()
#         self.ec = ErrorCode(self.driver)
#         self.ec.ErrorCodes()
#         time.sleep(2)
#         self.ec.GlobalErrorCodeSelectCheckbox()
#         time.sleep(2)
#         self.ec.GlobalErrorCodeEdit()
#         time.sleep(1)
#         self.ec.setErrorCodeEditName(self.ErrorCodeName_1)
#         time.sleep(2)
#         self.ec.setErrorCodeEditDesc(self.ErrorCodeDesc_1)
#         time.sleep(2)
#         self.ec.GlobalErrorEditSave()
#         time.sleep(1)
#         assert "Updated Successfully." in self.driver.page_source
#
#
#     def test_HardwareErrCode_Header(self, user_login):
#
#         self.driver = user_login
#         self.ss = Sys(self.driver)
#         self.driver.implicitly_wait(4)
#         self.ss.clicksystem()
#         self.ec = ErrorCode(self.driver)
#         self.ec.ErrorCodes()
#         time.sleep(2)
#         table = self.driver.find_element(By.ID, "tblTestHardwareErrorCodes")
#         header = table.find_elements(By.TAG_NAME, "th")
#         for headerEl in header:
#             print(headerEl.text)
#         time.sleep(2)
#
#
#     def test_HardwareErrCode_Data(self, user_login):
#         self.driver = user_login
#         self.ss = Sys(self.driver)
#         self.driver.implicitly_wait(4)
#         self.ss.clicksystem()
#         self.ec = ErrorCode(self.driver)
#         self.ec.ErrorCodes()
#         time.sleep(2)
#         table = self.driver.find_element(By.ID, "tblTestHardwareErrorCodes")
#         body = table.find_element(By.TAG_NAME, "tbody")
#         cells = body.find_elements(By.TAG_NAME, "tr")
#         for cell in cells:
#             print(cell.text)
#
#     def test_HardwareErrCode_CreateNew(self, user_login):
#         self.driver = user_login
#         self.ss = Sys(self.driver)
#         self.driver.implicitly_wait(4)
#         self.ss.clicksystem()
#         self.ec = ErrorCode(self.driver)
#         self.ec.ErrorCodes()
#         time.sleep(2)
#         self.ec.HardwareErrorCodeNew()
#         time.sleep(2)
#         self.ec.setHardwareErrorCodeDecno(self.HardwareErrCodeDecNo)
#         time.sleep(2)
#         self.ec.setHardwareErrorCodeName(self.HardwareErrCodeName)
#         time.sleep(2)
#         self.ec.setHardwareErrorCodeDesc(self.HardwareErrCodeDesc)
#         time.sleep(2)
#         self.ec.HardwareErrorclickSave()
#         time.sleep(2)
#         assert "Updated Successfully." in self.driver.page_source
#
#
#     def test_HardwareErrCode_Edit(self, user_login):
#         self.driver = user_login
#         self.ss = Sys(self.driver)
#         self.driver.implicitly_wait(4)
#         self.ss.clicksystem()
#         self.ec = ErrorCode(self.driver)
#         self.ec.ErrorCodes()
#         time.sleep(2)
#         self.ec.HardwareErrorCodeSelectCheckbox()
#         time.sleep(2)
#         self.ec.HardwareErrorCodeEdit()
#         time.sleep(1)
#         self.ec.setHardwareErrorCodeEditName(self.HardwareErrCodeName_1)
#         time.sleep(2)
#         self.ec.setHardwareErrorCodeEditDesc(self.HardwareErrCodeDesc_1)
#         time.sleep(2)
#         self.ec.HardwareErrorEditSave()
#         time.sleep(1)
#         assert "Updated Successfully." in self.driver.page_source
#
#
#     def test_SoftwareErrCode_Header(self, user_login):
#         self.driver = user_login
#         self.ss = Sys(self.driver)
#         self.driver.implicitly_wait(4)
#         self.ss.clicksystem()
#         self.ec = ErrorCode(self.driver)
#         self.ec.ErrorCodes()
#         time.sleep(2)
#         table = self.driver.find_element(By.ID, "tblPPTSoftwareErrorCodes")
#         header = table.find_elements(By.TAG_NAME, "th")
#         for headerEl in header:
#             print(headerEl.text)
#         time.sleep(2)
#
#
#     def test_SoftwareErrCode_Data(self, user_login):
#         self.driver = user_login
#         self.ss = Sys(self.driver)
#         self.driver.implicitly_wait(4)
#         self.ss.clicksystem()
#         self.ec = ErrorCode(self.driver)
#         self.ec.ErrorCodes()
#         time.sleep(2)
#         table = self.driver.find_element(By.ID, "tblPPTSoftwareErrorCodes")
#         body = table.find_element(By.TAG_NAME, "tbody")
#         cells = body.find_elements(By.TAG_NAME, "tr")
#         for cell in cells:
#             print(cell.text)
#
#
#     def test_SoftwareErrCode_CreateNew(self, user_login):
#         self.driver = user_login
#         self.ss = Sys(self.driver)
#         self.driver.implicitly_wait(4)
#         self.ss.clicksystem()
#         self.ec = ErrorCode(self.driver)
#         self.ec.ErrorCodes()
#         time.sleep(2)
#         self.ec.SoftwareErrorCodeNew()
#         time.sleep(2)
#         self.ec.setSoftwareErrorCodeDecno(self.SoftwareErrCodeDecNo)
#         time.sleep(2)
#         self.ec.setSoftwareErrorCodeName(self.SoftwareErrCodeName)
#         time.sleep(2)
#         self.ec.setSoftwareErrorCodeDesc(self.SoftwareErrCodeDesc)
#         time.sleep(2)
#         self.ec.SoftwareErrorclickSave()
#         time.sleep(2)
#         assert "Updated Successfully." in self.driver.page_source
#
#
#     def test_SoftwareErrCode_Edit(self, user_login):
#
#         self.driver = user_login
#         self.ss = Sys(self.driver)
#         self.driver.implicitly_wait(4)
#         self.ss.clicksystem()
#         self.ec = ErrorCode(self.driver)
#         self.ec.ErrorCodes()
#         time.sleep(2)
#         self.ec.SoftwareErrorCodeSelectCheckbox()
#         time.sleep(2)
#         self.ec.SoftwareErrorCodeEdit()
#         time.sleep(2)
#         self.ec.setSoftwareErrorCodeEditName(self.SoftwareErrCodeName_1)
#         time.sleep(2)
#         self.ec.setSoftwareErrorCodeEditDesc(self.SoftwareErrCodeDesc_1)
#         time.sleep(2)
#         self.ec.SoftwareErrorEditSave()
#         time.sleep(2)
#         assert "Updated Successfully." in self.driver.page_source
