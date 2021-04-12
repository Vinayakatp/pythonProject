from pageObjects.BasePage import BasePage


class LoginPage(BasePage):
    email_id = "Email"
    password_id = "Password"
    login_xpath = "//button[@type='submit']"
    logout_xpath = "//a[text()='Logout']"

    # def __init__(self, driver):
    #     self.driver = driver

    # def set_email(self, email):
    #     self.driver.find_element_by_id(self.email_id).clear()
    #     self.driver.find_element_by_id(self.email_id).send_keys(email)
    #
    # def set_password(self, password):
    #     self.driver.find_element_by_id(self.password_id).clear()
    #     self.driver.find_element_by_id(self.password_id).send_keys(password)
    #
    # def click_login(self):
    #     self.driver.find_element_by_xpath(self.login_xpath).click()

    # def get_title(self):
    #     var = self.driver.title

    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout_xpath).click()
