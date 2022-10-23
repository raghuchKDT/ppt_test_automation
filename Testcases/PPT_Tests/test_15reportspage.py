import pytest
import time
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from PageObjectModules.LoginPage import Login
from PageObjectModules.ReportPage import reports
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import InvalidSessionIdException
import random

class Test_005_reports:
    User = "push"
    Pass = "pull"
    useR = "antony"
    pasS = "admin"

    def test_reportscreen(self, user_manager):
        self.driver = user_manager
        self.driver.implicitly_wait(2)
        self.rp = reports(self.driver)
        self.rp.clickreports()
        self.driver.implicitly_wait(2)

        # Validation of Report in Side Menu Bar
        exp_ele = ['Report']
        data_bas_ele = self.driver.find_elements(By.XPATH, "//*[@id='five']/span")

        for idx, bas_ele in enumerate(data_bas_ele):
            print(idx, bas_ele.text)
            assert (exp_ele[idx] == bas_ele.text)

    def test_level2menubar(self, user_manager):
        self.driver = user_manager
        self.driver.implicitly_wait(2)
        self.rp = reports(self.driver)
        self.rp.clickreports()
        self.driver.implicitly_wait(2)

        assert 'Report' in self.driver.page_source

        assert 'Report Mask' in self.driver.page_source

        assert 'Global Variable' in self.driver.page_source

    def test_level3menubar(self, user_manager):
        self.driver = user_manager
        self.driver.implicitly_wait(2)
        self.rp = reports(self.driver)
        self.rp.clickreports()
        self.driver.implicitly_wait(2)
        # self.rp.clickcheckmark()

        # Validation of Report in Level3 Menu Bar
        exp_ele4 = ['Report Name']
        data_bas_ele4 = self.driver.find_elements(By.XPATH, "//*[@id='tblReport']/thead/tr/th[2]")

        for idx, bas_ele4 in enumerate(data_bas_ele4):
            print(idx, bas_ele4.text)
            assert (exp_ele4[idx] == bas_ele4.text)

        # Validation of Report in Level3 Menu Bar
        exp_ele5 = ['Index\nVariable Name']
        data_bas_ele5 = self.driver.find_elements(By.XPATH, "//*[@id='pills-report']/div/div/div[2]/div")

        for idx, bas_ele5 in enumerate(data_bas_ele5):
            print(idx, bas_ele5.text)
            assert (exp_ele5[idx] == bas_ele5.text)

        # Validation of Report in Level3 Menu Bar
        exp_ele6 = ['VariableName\nType\nProtocol']
        data_bas_ele6 = self.driver.find_elements(By.XPATH, "//*[@id='ViewAllGlobalVariable']/div/div[1]")

        for idx, bas_ele6 in enumerate(data_bas_ele6):
            print(idx, bas_ele6.text)
            assert (exp_ele6[idx] == bas_ele6.text)

    def test_globalvar(self, user_manager):
        self.driver = user_manager
        self.driver.implicitly_wait(2)
        self.rp = reports(self.driver)
        self.rp.clickreports()
        self.driver.implicitly_wait(2)

        # table = self.driver.find_element(By.ID, "tblreportglobal")
        # body = table.find_element(By.TAG_NAME, "tbody")
        # cells = body.find_elements(By.TAG_NAME, "td")
        # for cell in cells:
        #     print(cell.text)

        # Validation of Report in Level3 Menu Bar
        exp_ele7 = ['VariableName\nType\nProtocol\ncount_pass\nvar\n@countpass@\ncount_fail\nvar\n@countfail@\nlot_size\nvar\n@lotsize@\nlot_counter\nvar\n@lotcounter@\ntext1\nvar\n@text1@\ntext2\nvar\n@text2@\ntext3\nvar\n@text3@\ntext4\nvar\n@text4@\ntext5\nvar\n@text5@\nbarcode1\nvar\n@barcode1@\nbarcode2\nvar\n@barcode2@\nbarcode3\nvar\n@barcode3@\nWire_ID\nvar\n@wireID@\nmeasure_push_min_value\nvar\n@push_min_value@\nmeasure_push_max_value\nvar\n@push_max_value@\nmeasure_pull_min_value\nvar\n@pull_min_value@\nmeasure_pull_max_value\nvar\n@pull_max_value@\ndate\nsys\n@date@\ntime\nsys\n@time@\nvariant_name\nsys\n@variant@\nproject_name\nsys\n@project@\nuser_name\nsys\n@username@\ntotal_test_pass\nsys\n@test_pass@\ntotal_test_fail\nsys\n@test_fail@']
        data_bas_ele7 = self.driver.find_elements(By.XPATH, "//*[@id='pills-report']/div/div/div[3]/div")

        for idx, bas_ele7 in enumerate(data_bas_ele7):
            print(idx, bas_ele7.text)
            assert (exp_ele7[idx] == bas_ele7.text)

    @pytest.mark.sanity()
    def test_new_report(self,user_manager):
        self.driver = user_manager
        self.driver.implicitly_wait(2)
        self.rp = reports(self.driver)
        self.rp.clickreports()
        self.driver.implicitly_wait(2)
        self.rp.clicknew()

        rand_report_name = ''.join((random.choice('aeiournsltchp')for i in range(5)))

        user_manager.find_element(By.XPATH, "//*[@id='reportName']").clear()
        user_manager.find_element(By.XPATH, "//*[@id='reportName']").send_keys(rand_report_name)
        time.sleep(2)

        user_manager.find_element(By.XPATH, "//*[@id='description']").clear()
        user_manager.find_element(By.XPATH, "//*[@id='description']").send_keys("desc")
        time.sleep(2)
        self.rp.clicksave()
        time.sleep(1)

        assert 'Updated Successfully.' in self.driver.page_source

    def test_report_edit(self, user_manager):
        self.driver = user_manager
        self.driver.implicitly_wait(2)
        self.rp = reports(self.driver)
        self.rp.clickreports()
        self.driver.implicitly_wait(2)
        self.rp.clickcheckmark()
        self.rp.clickedit()
        time.sleep(1)
        rand_edit_report = ''.join((random.choice('aeioursnltchp')for i in range(5)))

        user_manager.find_element(By.XPATH, "//*[@id='reportName']").clear()
        user_manager.find_element(By.XPATH, "//*[@id='reportName']").send_keys(rand_edit_report)
        time.sleep(1)

        user_manager.find_element(By.XPATH, "//*[@id='description']").clear()
        user_manager.find_element(By.XPATH, "//*[@id='description']").send_keys("description")
        self.rp.clicksave()
        time.sleep(2)

        assert 'Updated Successfully.' in self.driver.page_source

    def test_report_delete(self,user_manager):
        self.driver = user_manager
        self.driver.implicitly_wait(2)
        self.rp = reports(self.driver)
        self.rp.clickreports()
        self.driver.implicitly_wait(2)
        self.rp.clickcheckmark2()
        self.rp.clickdelete()
        self.rp.clickpopdelete()

        time.sleep(2)
        assert 'Deleted Successfully.' in self.driver.page_source

        # exp_ele8 = ['Deleted Successfully.']
        # data_bas_ele8 = self.driver.find_elements(By.XPATH, "/*[contains(text(),'Deleted Successfully.')]")
        #
        # for idx, bas_ele8 in enumerate(data_bas_ele8):
        #     print(idx, bas_ele8.text)
        #     assert (exp_ele8[idx] == bas_ele8.text)

    def test_geneprop_report(self,user_manager):
        self.driver = user_manager
        self.driver.implicitly_wait(2)
        self.rp = reports(self.driver)
        self.rp.clickreports()
        self.driver.implicitly_wait(2)
        self.rp.clickcheckmark()

        exp_ele9 = ['Name']
        data_bas_ele9 = self.driver.find_elements(By.XPATH, "//*[@id='collapseOne']/div/div[1]/div/div/div[1]/div/h5")

        for idx, bas_ele9 in enumerate(data_bas_ele9):
            print(idx, bas_ele9.text)
            assert (exp_ele9[idx] == bas_ele9.text)

    def test_multiple_deletereports(self, user_manager):
        self.driver = user_manager
        self.driver.implicitly_wait(2)
        self.rp = reports(self.driver)
        self.rp.clickreports()
        self.driver.implicitly_wait(2)
        self.rp.clickmultipledelete()
        time.sleep(1)

        self.rp.clickdelete()
        self.rp.clickpopdelete()
        time.sleep(2)
        assert 'Deleted Successfully.' in self.driver.page_source