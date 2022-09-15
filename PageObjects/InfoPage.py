from selenium.webdriver.common.by import By
import time

class Info:
    time.sleep(2)
    btn_recent_projects_xpath = "//*[contains(text(),'Recent Projects')]"
    btn_clickprojects_xpath = "//*[@id='tblProject']/tbody/tr[1]"
    btn_versionhis_xpath = "//*[contains(text(),'Version History')]"
    btn_options_xpath = "//*[contains(text(),'Options')]"
    btn_projheader_xpath = "//*[@id ='layoutSidenav_content']/main/div[4]/div/div"

    def __init__(self, driver):
        time.sleep(1)
        self.driver = driver

    def RecentProj(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_recent_projects_xpath).click()

    def clickProject(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_clickprojects_xpath).click()

    def versionhis(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_versionhis_xpath).click()

    def Options(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_options_xpath).click()

    def proj_tbl_header(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_projheader_xpath).click()

