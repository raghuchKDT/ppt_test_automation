from selenium.webdriver.common.by import By
import time

class Module:

    ModuleName_id = "txtNewModule"
    ModuleName_id1 = "txtNewModule1"
    ModuleName_id2 = "txtCopyNewModule"
    ModuleDescrption_id = "txtModuleDescription"
    ModuleDescrption_id1 = "txtModuleDescription1"
    ModuleDescrption_id2 = "txtCopyModuleDescription"
    No_of_Cavity_id = "txtCavity"
    No_of_Cavity_id1 = "txtCavity1"
    No_of_Switch_id = "txtSwitch"
    No_of_Switch_id1 = "txtSwitch1"
    No_of_Module_LED_id = "txtCavityLed"
    No_of_Module_LED_id1 = "txtCavityLed1"
    text_projectTab_xpath = "//*[@id='three']"
    text_moduleTab_xpath = "/html/body/div[1]/div[2]/main/div[2]/div/ul/li[2]/a"
    text_select_module_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[3]/div/div/div[1]/span[1]/div/ul/li[1]/a/h6"
    btn_new_module_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[3]/div/div/div[1]/div[2]/div/button[1]"
    btn_new_Choosefile_module_xpath = "/html/body/div[1]/div[2]/main/div[8]/div/div/div[2]/input[6]"
    btn_new_moduleSave_xpath = "/html/body/div[1]/div[2]/main/div[8]/div/div/div[2]/div/button[2]"
    btn_edit_module_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[3]/div/div/div[1]/div[2]/div/button[2]"
    btn_edit_Choosefile_module_xpath = "/html/body/div[1]/div[2]/main/div[10]/div/div/div[2]/input[6]"
    btn_edit_moduleSave_xpath = "/html/body/div[1]/div[2]/main/div[10]/div/div/div[2]/div/button[2]"
    btn_copy_module_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[3]/div/div/div[1]/div[2]/div/button[3]"
    btn_copy_moduleSave_xpath = "/html/body/div[1]/div[2]/main/div[9]/div/div/div[2]/div/button[1]"
    btn_delete_module_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[3]/div/div/div[1]/div[2]/div/button[4]"
    btn_delete_moduleSave_xpath = "/html/body/div[1]/div[2]/main/div[11]/div/div/div[2]/div/button[2]"

    def __init__(self, driver):
        self.driver = driver

    def clickProjectTab(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.text_projectTab_xpath).click()

    def clickModuleTab(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.text_moduleTab_xpath).click()

    def ClickModule(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.text_select_module_xpath).click()

    def ClickImg(self):
        time.sleep(2)
        self.driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div[3]/div/div[3]/div/div/div[3]/div/img').click()

    def ClickNewModule(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_new_module_xpath).click()

    def setNewModuleName(self, ModuleName):
        time.sleep(2)
        self.driver.find_element(By.ID, self.ModuleName_id).clear()
        self.driver.find_element(By.ID, self.ModuleName_id).send_keys(ModuleName)

    def setNewModuleDesc(self, ModuleDescrption):
        time.sleep(2)
        self.driver.find_element(By.ID, self.ModuleDescrption_id).clear()
        self.driver.find_element(By.ID, self.ModuleDescrption_id).send_keys(ModuleDescrption)

    def setNewModuleNo_Cavity(self, No_of_Cavity):
        time.sleep(2)
        self.driver.find_element(By.ID, self.No_of_Cavity_id).clear()
        self.driver.find_element(By.ID, self.No_of_Cavity_id).send_keys(No_of_Cavity)

    def setNewModuleNo_Switch(self, No_of_Switch):
        time.sleep(2)
        self.driver.find_element(By.ID, self.No_of_Switch_id).clear()
        self.driver.find_element(By.ID, self.No_of_Switch_id).send_keys(No_of_Switch)

    def setNewModuleCavityLED_no(self, No_of_Module_LED):
        time.sleep(2)
        self.driver.find_element(By.ID, self.No_of_Module_LED_id).clear()
        self.driver.find_element(By.ID, self.No_of_Module_LED_id).send_keys(No_of_Module_LED)

    def ClickChooseFile(self):
        self.driver.find_element(By.XPATH, self.btn_new_Choosefile_module_xpath).send_keys("C:\\Users\\KnoDTec\\Downloads\\Picture.png")

    def NewModuleclickSave(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_new_moduleSave_xpath).click()

    def ClickEditModule(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_edit_module_xpath).click()

    def setEditModuleName(self, ModuleName1):
        time.sleep(2)
        self.driver.find_element(By.ID, self.ModuleName_id1).clear()
        self.driver.find_element(By.ID, self.ModuleName_id1).send_keys(ModuleName1)

    def setEditModuleDesc(self, ModuleDescrption1):
        time.sleep(2)
        self.driver.find_element(By.ID, self.ModuleDescrption_id1).clear()
        self.driver.find_element(By.ID, self.ModuleDescrption_id1).send_keys(ModuleDescrption1)

    def setEditModuleNo_Cavity(self, No_of_Cavity1):
        time.sleep(2)
        self.driver.find_element(By.ID, self.No_of_Cavity_id1).clear()
        self.driver.find_element(By.ID, self.No_of_Cavity_id1).send_keys(No_of_Cavity1)

    def setEditModuleNo_Switch(self, No_of_Switch1):
        time.sleep(2)
        self.driver.find_element(By.ID, self.No_of_Switch_id1).clear()
        self.driver.find_element(By.ID, self.No_of_Switch_id1).send_keys(No_of_Switch1)

    def setEditModuleCavityLED_no(self, No_of_Module_LED1):
        time.sleep(2)
        self.driver.find_element(By.ID, self.No_of_Module_LED_id1).clear()
        self.driver.find_element(By.ID, self.No_of_Module_LED_id1).send_keys(No_of_Module_LED1)

    def ClickEditChooseFile(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_edit_Choosefile_module_xpath).send_keys("C:\\Users\\KnoDTec\\Downloads\\Picture.png")

    def EditModuleclickSave(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_edit_moduleSave_xpath).click()

    def ModuleClickCopy(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_copy_module_xpath).click()

    def setCopyModuleName(self, ModuleName2):
        time.sleep(2)
        self.driver.find_element(By.ID, self.ModuleName_id2).clear()
        self.driver.find_element(By.ID, self.ModuleName_id2).send_keys(ModuleName2)

    def setCopyModuleDesc(self, ModuleDescrption2):
        time.sleep(2)
        self.driver.find_element(By.ID, self.ModuleDescrption_id2).clear()
        self.driver.find_element(By.ID, self.ModuleDescrption_id2).send_keys(ModuleDescrption2)

    def CopyModuleclickSave(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_copy_moduleSave_xpath).click()

    def ModuleclickDelete(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_delete_module_xpath).click()

    def ModuleDelete(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_delete_moduleSave_xpath).click()


