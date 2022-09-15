from telnetlib import EC
from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.by import By
from PageObjects.LoginPage import Login


class Test_001_Login:
    baseURL = "http://localhost:5003/"
    username = "Dheeraj"
    password = "admin"

    def test_LoginPageTitle(self, setup):
        self.driver = setup
        act_title = self.driver.title
        print(act_title)
        if act_title == "Push Pull Touch Login":
            assert True
        else:
            assert False



    def test_User_Login_Header(self, setup):
        self.driver = setup
        time.sleep(2)

        assert 'User login' in self.driver.page_source

        # expected_el = ['User login']
        # time.sleep(2)
        # data_base_el = self.driver.find_elements(By.CSS_SELECTOR, "#layoutAuthentication_content > main > div > div.col-sm-12.col-md-12.col-lg-6.order-lg-first.pr-sm-0.mob_bg > div > div > div > h6")
        # for idx, base_el in enumerate(data_base_el):
        #     print(idx, base_el.text)
        #     assert (expected_el[idx] == base_el.text)

    def test_Invalid_User_Login(self, setup):
        self.driver = setup
        self.lp = Login(self.driver)
        time.sleep(2)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(2)
        assert "Invalid Username or Password" in self.driver.page_source
        # self.driver.close()


    def test_Empty_User_Field(self, setup):
        self.driver = setup
        # self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(2)
        assert "Required*" in self.driver.page_source
        # self.driver.close()


    def test_Empty_Password_Field(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.clickLogin()
        time.sleep(2)
        assert "Required*" in self.driver.page_source
        # self.driver.close()

    def test_Signin_Button(self, setup):
        self.driver = setup
        time.sleep(2)
        assert 'Sign in' in self.driver.page_source
        # self.driver.close()


    def test_login(self, user_login):
        self.driver = user_login
        self.driver.implicitly_wait(4)
        title = self.driver.title
        print(title)
        if title == "komax Testing":
            assert True
        else:
            assert False

    def test_logout(self, user_login):
        self.driver = user_login
        self.lp = Login(self.driver)
        self.driver.implicitly_wait(2)
        self.lp.clickuser()
        self.driver.implicitly_wait(2)
        self.lp.clickLogout()
        title = self.driver.title
        print(title)
        if title == "Push Pull Touch Login":
            assert True
        else:
            assert False
