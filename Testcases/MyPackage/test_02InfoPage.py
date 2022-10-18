from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.by import By
from PageObjectModules.LoginPage import Login
from PageObjectModules.InfoPage import Info
from selenium.common.exceptions import InvalidSessionIdException

class Test_Info_Page:

    @pytest.mark.skip(reason=None)
    def test_InfoPageTitle(self, user_login):
        self.driver = user_login
        time.sleep(2)
        self.nf = Info(self.driver)
        title = self.driver.title
        print(title)
        if title == "komax Testing":
            print("Info Page Title verification passed")
        else:
            print("Info Page Title verification Failed")

    @pytest.mark.skip(reason=None)
    def test_Proj_table(self, user_login):
        self.driver = user_login
        time.sleep(2)
        self.nf = Info(self.driver)
        time.sleep(1)
        self.nf.RecentProj()

        # Project Body Data Validations
        table = self.driver.find_element(By.ID, "tblProject")
        body = table.find_element(By.TAG_NAME, "tbody")
        cells = body.find_elements(By.TAG_NAME, "td")
        for cell in cells:
            print(cell.text)

    @pytest.mark.skip(reason=None)
    def test_RecentProj_Properties(self, user_login):
        self.driver = user_login
        self.nf = Info(self.driver)
        time.sleep(1)
        self.nf.RecentProj()
        self.nf.clickProject()

        time.sleep(2)
        rpprop = self.driver.find_elements(By.XPATH, "//*[@id='infoDetails']/div")
        expected = ['Properties', 'Project Name', 'Description', 'Author Name', 'Date Created']
        contents = []
        for rp in rpprop:
            contents.append(rp.text)
        for rps in expected:
            assert (rps in contents[0]) == True

    @pytest.mark.skip(reason=None)
    def test_VersionHistoryElements(self, user_login):
        self.driver = user_login
        self.nf = Info(self.driver)
        time.sleep(1)
        self.nf.versionhis()

        expected_Ver1 = ['Name', 'Version', 'Released Date', 'Licence']
        data_base_Ver1 = self.driver.find_elements(By.XPATH, "//*[@id='layoutSidenav_content']/main/div[3]/div/div")
        for idx, base_Ver1 in enumerate(data_base_Ver1):
            print(idx, base_Ver1.text)
            assert (expected_Ver1[idx] == base_Ver1.text)

    @pytest.mark.skip(reason=None)
    def test_Options_TabData(self, user_login):
        self.driver = user_login
        self.nf = Info(self.driver)
        time.sleep(1)
        self.nf.Options()
        assert 'Software options installed' in self.driver.page_source
        assert 'Graphic setup' in self.driver.page_source
