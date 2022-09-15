from selenium.webdriver.common.by import By
import time

class Variables:
    btn_project_xpath = "//*[@id='three']/span"
    btn_variant_link_txt = "Variant"
    btn_variables_xpath = "//*[@id='pills-variantglobalvar-tab']"

    def __init__(self, driver):
        time.sleep(1)
        self.driver = driver

    def Project(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btn_project_xpath).click()

    def clickvariant(self):
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, self.btn_variant_link_txt).click()

    def clickvariables(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btn_variables_xpath).click()
