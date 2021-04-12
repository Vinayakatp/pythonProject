import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.getLogger()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("############## test_homePageTitle ####################")
        self.logger.info("############## Verify home page title ####################")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("############## homePageTitle test is passed####################")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("############## homePageTitle test is failed####################")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("############## Verifying login test####################")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setField(self.lp.email_id, self.username)
        self.lp.setField(self.lp.password_id, self.password)
        self.lp.clickOn(self.lp.login_xpath).click()
        home_title = self.driver.title
        if home_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("############## login test is passed####################")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("############## login test is failed####################")
            assert False
