from selenium.webdriver.common.by import By
import time

class Variant:

    link_variant_Link_Text = "Variant"
    NewVariantName_id = "varName"
    NewVariantDesc_id = "varDesc"
    EditVariantName_id = "varName"
    EditVariantDesc_id = "varDesc"
    CopyVariantName_id = "txtNewVariantName"
    text_projectTab_xpath = "//*[@id='three']/span"
    btn_variant_link_txt = "Variant"
    checkbox_select_variant_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/div/table/tbody/tr[1]/td[1]/label/span"
    btn_new_variant_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/button[1]"
    btn_new_variantSave_xpath = "//*[@id='btn-VarSave']"
    checkbox_select_editvariant_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/div/table/tbody/tr[2]/td[1]/label/span"
    btn_edit_variant_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/a"
    btn_edit_variantSave_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/button[2]"
    btn_copy_variant_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/button[3]"
    btn_copy_variantSave_xpath = "/html/body/div[1]/div[2]/main/div[14]/div/div/div[2]/div/button[2]"
    checkbox_select_deletevariant_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/div/table/tbody/tr[1]/td[1]/label/span"
    btn_delete_variant_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/button[4]"
    btn_confirmdelete_variant_xpath = "/html/body/div[1]/div[2]/main/div[15]/div/div/div[2]/div/button[2]"

    def __init__(self, driver):
        time.sleep(1)
        self.driver = driver

    def clickProjectTab(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.text_projectTab_xpath).click()

    def clickVariantTab(self):
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, self.btn_variant_link_txt).click()

    def VariantSelectCheckbox(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.checkbox_select_variant_xpath).click()

    def ClickNewVariantButton(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_new_variant_xpath).click()

    def setNewVariantName(self, NewVariantName):
        time.sleep(2)
        self.driver.find_element(By.ID, self.NewVariantName_id).clear()
        self.driver.find_element(By.ID, self.NewVariantName_id).send_keys(NewVariantName)

    def setNewVariantDesc(self, NewVariantDesc):
        time.sleep(2)
        self.driver.find_element(By.ID, self.NewVariantDesc_id).clear()
        self.driver.find_element(By.ID, self.NewVariantDesc_id).send_keys(NewVariantDesc)

    def NewVariantClickSaveButton(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_new_variantSave_xpath).click()

    def SelectVariantEditCheckbox(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.checkbox_select_editvariant_xpath).click()

    def ClickVariantEditButton(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_edit_variant_xpath).click()

    def setEditVariantName(self, EditVariantName):
        time.sleep(2)
        self.driver.find_element(By.ID, self.EditVariantName_id).clear()
        self.driver.find_element(By.ID, self.EditVariantName_id).send_keys(EditVariantName)

    def setEditVariantDesc(self, EditVariantDesc):
        time.sleep(2)
        self.driver.find_element(By.ID, self.EditVariantDesc_id).clear()
        self.driver.find_element(By.ID, self.EditVariantDesc_id).send_keys(EditVariantDesc)

    def EditVariantClickSaveButton(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_edit_variantSave_xpath).click()

    def ClickVariantCopyButton(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_copy_variant_xpath).click()

    def setCopyVariantName(self, CopyVariantName):
        time.sleep(2)
        self.driver.find_element(By.ID, self.CopyVariantName_id).clear()
        self.driver.find_element(By.ID, self.CopyVariantName_id).send_keys(CopyVariantName)

    def CopyVariantClickSaveButton(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_copy_variantSave_xpath).click()

    def SelectVariantDelete(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.checkbox_select_deletevariant_xpath).click()

    def VariantClickDeleteButton(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_delete_variant_xpath).click()

    def VariantConfirmDelete(self):
        time.sleep(2)
        self.driver.find_element("xpath", self.btn_confirmdelete_variant_xpath).click()
