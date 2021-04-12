import random
import string
import time

import pytest

# from pageObjects.CustomerPage import CustomerPage
from pageObjects.HomePage import HomePage

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestCommerce_03_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.getLogger()

    @pytest.mark.sanity
    def test_AddNewCustomer(self, setup):
        self.logger.info("############## Verifying login test####################")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setField(self.lp.email_id, self.username)
        self.lp.setField(self.lp.password_id, self.password)
        self.lp.clickOn(self.lp.login_xpath).click()
        home_title = self.driver.title
        self.logger.info(home_title)
        self.homePage = HomePage(self.driver)
        self.homePage.clickOn(self.homePage.customer_menu_xpath).click()
        self.homePage.clickOn(self.homePage.customerButton_xpath).click()
        self.homePage.clickOn(self.homePage.add_button_xpath).click()
        time.sleep(3)
        self.logger.info("********* Entered Add customer Page ****  *****")
        self.email = random_generator() + "@gmail.com"
        self.homePage.setField(self.homePage.txtboxEmail_xpath, self.email)
        self.homePage.setField(self.homePage.txtboxPassword_xpath, "kushal@123")
        self.homePage.setField(self.homePage.txtboxFirstName_xpath, "vini")
        self.homePage.setField(self.homePage.txtboxLastName_xpath, "tp")
        self.homePage.setGender("Male")
        self.homePage.get_DatePicker("May", "2000", "25")
        # self.homePage.setDOB("3/1/2021")
        self.homePage.setField(self.homePage.txtboxCompany_xpath, "Tata Consultancy Services Limited")
        self.homePage.clickOn(self.homePage.cbTaxExempt_xpath).click()
        self.homePage.setField(self.homePage.txtAdminComment_xpath, "Kushal is our god")
        self.homePage.setManagerOfVender("Vendor 1")
        self.homePage.setCustomerRoles("Vendors")
        time.sleep(3)
        self.homePage.clickOn(self.homePage.btnSave_xpath).click()
        time.sleep(3)
        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)

        if 'customer has been added successfully.' in self.msg:
            assert True
            self.driver.close()
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.info("********* Add customer Test Failed ************")
            self.driver.close()
            assert False
        self.logger.info("******* Ending Add customer test **********")

    def test_e2e(self, setup):
        self.driver = setup
        self.logger.info("New Login")
        self.loginPage = LoginPage(self.driver)
        self.logger.info("Entering into Green Kart website")
        self.logger.info(self.driver.title)
        self.driver.get(self.baseURL)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.setField(self.loginPage.email_id, self.username)
        self.loginPage.setField(self.loginPage.password_id, self.password)
        self.loginPage.clickOn(self.loginPage.login_xpath).click()
        time.sleep(3)
        self.logger.info(self.driver.title)
        time.sleep(3)
        self.loginPage.click_logout()
        self.driver.close()


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
