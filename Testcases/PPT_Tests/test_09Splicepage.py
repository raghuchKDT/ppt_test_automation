import pytest
import time
from selenium import webdriver
from PageObjectModules.LoginPage import Login
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import InvalidSessionIdException
from PageObjectModules.SplicePage import Splice
import random

class Test008_Splice:
    SpliceName = 'Splicez'
    Splicename = 'Spliceit'
    spliceName = 'splice10'

    def test_levelmenubar(self, user_login):
        self.driver = user_login
        self.sp = Splice(self.driver)
        self.sp.Project()
        self.sp.clickvariant()
        self.sp.clicksplice()

        element18 = ['Variant']
        data_base_ele18 = self.driver.find_elements(By.LINK_TEXT, "Variant")

        for idx, base_ele18 in enumerate(data_base_ele18):
            print(idx, base_ele18.text)
            assert base_ele18.text in element18

        element19 = ['Splice']
        data_base_ele19 = self.driver.find_elements(By.XPATH, "//*[@id='pills-splice-tab']")

        for idx, base_ele19 in enumerate(data_base_ele19):
            print(idx, base_ele19.text)
            assert base_ele19.text in element19

    def test_level3menubar(self, user_login):
        self.driver = user_login
        self.sp = Splice(self.driver)
        self.sp.Project()
        self.sp.clickvariant()
        self.sp.clicksplice()

        element20 = ['']
        data_base_ele20 = self.driver.find_elements(By.XPATH, "//*[@id='pills-splice']/div[1]/div[1]/div[1]")

        for idx, base_ele20 in enumerate(data_base_ele20):
            print(idx, base_ele20.text)
            assert base_ele20.text in element20

    @pytest.mark.sanity()
    def test_create_newsplice(self, user_login):
        self.driver = user_login
        self.sp = Splice(self.driver)
        self.sp.Project()
        self.sp.clickvariant()
        self.sp.clicksplice()
        self.sp.clicknewsplice()
        time.sleep(2)

        rand_splice_name = ''.join((random.choice('aeiourtsnlchp')for i in range(5)))

        self.driver.find_element(By.XPATH, "//*[@id='spliceName']").clear()
        self.driver.find_element(By.XPATH, "//*[@id='spliceName']").send_keys(rand_splice_name )

        self.sp.clicksavesplice()
        time.sleep(2)

        assert 'Data Added Successfully.' in self.driver.page_source

    def test_copysplice(self, user_login):
        self.driver = user_login
        self.sp = Splice(self.driver)
        self.sp.Project()
        self.sp.clickvariant()
        self.sp.clicksplice()
        self.sp.clickcheckmarksplice()
        self.sp.clickcopysplice()
        time.sleep(2)

        rand_copy_splicename = ''.join((random.choice('aeiournstlcp')for i in range(5)))

        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='txtNewSpliceName']").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='txtNewSpliceName']").send_keys(rand_copy_splicename)

        self.sp.clickcopysave()
        time.sleep(2)

        assert 'Data Added Successfully.' in self.driver.page_source

    def test_edit_splice(self, user_login):
        self.driver = user_login
        self.sp = Splice(self.driver)
        self.sp.Project()
        self.sp.clickvariant()
        self.sp.clicksplice()
        self.sp.clickcheckmark3splice()
        self.sp.clickeditsplice()
        time.sleep(2)

        rand_edit_splice = ''.join((random.choice('aeiournstlcp')for i in range(5)))
        self.sp.seteditsplicename(rand_edit_splice)
        self.sp.clicksavesplice()
        time.sleep(2)
        assert 'Data Added Successfully.' in self.driver.page_source

    def test_deletesplice(self, user_login):
        self.driver = user_login
        self.sp = Splice(self.driver)
        self.sp.Project()
        self.driver.implicitly_wait(4)
        self.sp.clickvariant()
        self.sp.clicksplice()
        self.sp.clickcheckmark3splice()
        self.sp.clickdeletesplice()
        self.sp.clickpopupdeletesplice()
        time.sleep(2)

        assert 'Deleted Successfully.' in self.driver.page_source
