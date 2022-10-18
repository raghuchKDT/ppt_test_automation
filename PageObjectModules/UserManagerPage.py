from selenium.webdriver.common.by import By
import time

class usermanager:
    textbox_User_id = "userName"
    textbox_Pass_id = "password"
    btn_usermanager_xpath = "//*[@id='four']/span"
    btn_level2bar_xpath = "//*[@id='pills-user-tab']"
    btn_newuser_xpath = "//*[contains(text(),'New')]"
    btn_checkmark3_xpath =  "//*[@id='tblUser']/tbody/tr[3]/td[1]/label/span"
    btn_save_xpath = "//*[contains(text(), 'Save')]"
    btn_delete_id = "collapsesubadmin"
    btn_checkmark2_xpath = "//*[@id='tblUser']/tbody/tr[2]/td[4]/label/span"
    btn_edit_xpath = "//*[@id='btn-userEdit']"
    btn_popupdelete_xpath = "//*[@id='btn-delete-user']"
    btn_role_xpath =  "//*[contains(text(),'Role')]"
    btn_newrole_xpath = "//*[@id='bntGoToCreateRole']"
    btn_saverole_xpath =  "//*[@id='btn-roleSave']"
    btn_chechmarkrole_xpath = "//*[@id='tblRole']/tbody/tr[2]/td[1]/label/span"
    btn_editrole_xpath = "//*[@id='btn-roleEdit']"
    btn_deleterole_xpath = "//*[@id='btn-roledelete']"
    btn_popdeleterole_xpath = "//*[@id='btn-delete-role']"
    textbox_roleName_id = "roleName"
    textbox_useR_id = "username"
    textbox_pasS_id = "pasSword"
    textbox_rolename_id = "rolename"

    def __init__(self, driver):
        time.sleep(1)
        self.driver = driver

    def clickusermanager(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btn_usermanager_xpath).click()

    def clickleve2menusermanager(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH,self.btn_level2bar_xpath ).click()

    def clickNew(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH,self.btn_newuser_xpath ).click()

    def clickcheckkk(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH,self.btn_checkmark3_xpath).click()

    def User(self, User):
        time.sleep(1)
        self.driver.find_element(By.ID, self.textbox_User_id).clear()
        self.driver.find_element(By.ID, self.textbox_User_id).send_keys(User)

    def Pass(self, Pass):
        time.sleep(1)
        self.driver.find_element(By.ID, self.textbox_Pass_id).clear()
        self.driver.find_element(By.ID, self.textbox_Pass_id).send_keys(Pass)

    def clicksave(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH , self.btn_save_xpath ).click()

    def clickaccesscheck(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='tblUser']/tbody/tr[3]/td[1]/label/span").click()

    def clickaccessdelete(self):
        time.sleep(1)
        self.driver.find_element(By.ID, self.btn_delete_id).click()

    def clickcheckmark(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btn_checkmark2_xpath ).click()

    def clickedit(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btn_edit_xpath ).click()


    def useR(self,useR):
        time.sleep(1)
        self.driver.find_element(By.ID, self.textbox_useR_id).clear()
        self.driver.find_element(By.ID, self.textbox_useR_id).send_keys(useR)

    def pasS (self,pasS):
        time.sleep(1)
        self.driver.find_element(By.ID, self.textbox_pasS_id).clear()
        self.driver.find_element(By.ID, self.textbox_pasS_id).send_keys(pasS)

    def clickcheckkmark(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[@id='tblUser']/tbody/tr[2]/td[1]/label/span").click()

    def clickdelete(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[contains(text(), 'Delete')]").click()

    def clickdeletepopup(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btn_popupdelete_xpath).click()

    def clickuusermanager(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btn_usermanager_xpath).click()

    def clickRole(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH,self.btn_role_xpath).click()

    def clickrolenew(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH,  self.btn_newrole_xpath ).click()

    def setroleName(self, roleName):
        time.sleep(1)
        self.driver.find_element(By.ID, self.textbox_roleName_id).clear()
        self.driver.find_element(By.ID, self.textbox_roleName_id).send_keys(roleName)

    def clicksaverole(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btn_saverole_xpath).click()

    def clickcheck(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btn_chechmarkrole_xpath).click()

    def clickeditrole(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btn_editrole_xpath ).click()

    def editrolename(self, rolename):
        time.sleep(1)
        self.driver.find_element(By.ID, self.textbox_rolename_id).clear()
        self.driver.find_element(By.ID, self.textbox_rolename_id).send_keys(rolename)

    def clickroledelete(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btn_deleterole_xpath ).click()

    def deletepopup(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btn_popdeleterole_xpath ).click()
