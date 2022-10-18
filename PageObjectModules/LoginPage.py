from selenium.webdriver.common.by import By
import time

class Login:

    textbox_username_id = "UserName"
    textbox_password_id = "Password"
    btn_signin_xpath = "//*[contains(text(),'Sign in')]"
    btn_clickuser_xpath = "//*[@id='userDropdown']"
    btn_logout_xpath = "//*[contains(text(), 'Logout')]"

    def __init__(self, driver):
        time.sleep(2)
        self.driver = driver

    def setUserName(self, username):
        time.sleep(1)
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        time.sleep(1)
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btn_signin_xpath).click()

    def clickuser(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btn_clickuser_xpath).click()

    def clickLogout(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btn_logout_xpath).click()


