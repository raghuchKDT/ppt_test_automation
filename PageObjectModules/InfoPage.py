from selenium.webdriver.common.by import By
import time

class Info:

    btn_recent_projects_xpath = "/html/body/div/div[2]/main/div[2]/div/ul/li[1]/a"
    btn_clickprojects_xpath = "/html/body/div/div[2]/main/div[4]/div/div/div/div[1]/div[2]/div/div[2]/div/table/tbody/tr/td[1]"
    btn_projheader_xpath = "/html/body/div/div[2]/main/div[4]/div/div/div/div[1]/div[1]/h6"
    btn_versionhis_xpath = "/html/body/div/div[2]/main/div[2]/div/ul/li[2]/a"
    btn_options_xpath = "/html/body/div/div[2]/main/div[2]/div/ul/li[3]/a"

    def __init__(self, driver):
        time.sleep(2)
        self.driver = driver

    def RecentProj(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_recent_projects_xpath).click()

    def proj_tbl_header(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_projheader_xpath).click()

    def clickProject(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_clickprojects_xpath).click()

    def versionhis(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_versionhis_xpath).click()

    def Options(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_options_xpath).click()
