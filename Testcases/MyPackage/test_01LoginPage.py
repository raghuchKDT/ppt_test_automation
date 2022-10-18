from telnetlib import EC
from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.by import By
from PageObjectModules.LoginPage import Login

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

    @pytest.mark.sanity()
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
