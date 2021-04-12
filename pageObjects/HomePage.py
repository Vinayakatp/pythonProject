import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from pageObjects.BasePage import BasePage


class HomePage(BasePage):
    customer_menu_xpath = "(//i[@class='right fas fa-angle-left '])[4]"
    customerButton_xpath = "//li[@class='nav-item']/a[@href='/Admin/Customer/List']"
    add_button_xpath = "//a[@class='btn btn-primary']"
    txtboxEmail_xpath = "//input[@id='Email']"
    txtboxPassword_xpath = "//input[@id='Password']"
    txtboxFirstName_xpath = "//input[@id='FirstName']"
    txtboxLastName_xpath = "//input[@id='LastName']"
    txtboxDOB_xpath = "//input[@id='DateOfBirth']"
    rbMale_xpath = "//input[@id='Gender_Male']"
    rbFemale_xpath = "//input[@id='Gender_Female']"
    txtboxCompany_xpath = "//input[@id='Company']"
    cbTaxExempt_xpath = "//input[@id='IsTaxExempt']"
    txtAdminComment_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"
    drpManagerofVender_xpath = "//select[@id='VendorId']"
    drpNewsLetter_xpath = "//div/input[@aria-describedby='SelectedNewsletterSubscriptionStoreIds_taglist']"
    drpCustomerRoles_xpath = "/div/input[@aria-describedby='SelectedCustomerRoleIds_taglist']"
    txtcustomerRoles_xpath = "//input[@aria-labelledby='SelectedCustomerRoleIds_label']"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    textnewsletter_xpath = "//input[@class='k-input k-readonly']"
    dropdownnewsletter = "//select[@id='SelectedNewsletterSubscriptionStoreIds']"

    # def __init__(self, driver):
    #     self.driver = driver
    #

    def clickOnCustomerMainMenu(self):
        return self.driver.find_element_by_xpath(self.customer_menu_xpath)

    # def clickOnMenu(self, menu):
    #     return self.driver.find_element_by_xpath(menu)

    # Method overloading example

    def clickOnCustomerSubMenu(self):
        return self.driver.find_element_by_xpath(self.customerButton_xpath)

    def clickOnCustomerSubMenu(self, ele):
        return self.driver.find_element_by_xpath(ele)

    # Method overrriding
    def setField(self, Locator, plaintext):
        element = self.driver.find_element(By.XPATH, Locator)
        element.clear()
        return element.send_keys(plaintext)

    def clickOnAddNew(self):
        return self.driver.find_element_by_xpath(self.add_button_xpath)

    def setEmail(self, email):
        try:
            return self.driver.find_element_by_xpath(self.txtboxEmail_xpath).send_keys(email)
        except:
            return None

    def setPassword(self, password):
        try:
            return self.driver.find_element_by_xpath(self.txtboxPassword_xpath).send_keys(password)
        except:
            return None

    # def setField(self, ele, passText):
    #     try:
    #         return self.driver.find_element_by_xpath(ele).send_keys(passText)
    #     except:
    #         return None

    def setLastName(self, lastname):
        try:
            return self.driver.find_element_by_xpath(self.txtboxLastName_xpath).send_keys(lastname)
        except:
            return None

    def setDOB(self, dob):
        try:
            return self.driver.find_element_by_xpath(self.txtboxDOB_xpath).send_keys(dob)
        except:
            return None

    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element_by_xpath(self.rbMale_xpath).click()
        elif gender == "Female":
            self.driver.find_element_by_xpath(self.rbFemale_xpath).click()
        else:
            self.driver.find_element_by_xpath(self.rbMale_xpath).click()

    def setCompanyName(self, company):
        try:
            return self.driver.find_element_by_xpath(self.txtboxCompany_xpath).send_keys(company)
        except:
            return None

    def clickTaxExepmt(self):
        return self.driver.find_element_by_xpath(self.cbTaxExempt_xpath)

    def setAdminComment(self, comment):
        return self.driver.find_element_by_xpath(self.txtAdminComment_xpath).send_keys(comment)

    # def clickOnSave(self):
    #     return self.driver.find_element_by_xpath(self.btnSave_xpath).click()

    def setManagerOfVender(self, value):
        Drp = self.driver.find_element_by_xpath(self.drpManagerofVender_xpath)
        sect = Select(Drp)
        sect.select_by_visible_text(value)

    # def setNewsLetter(self, newvalue):
    #     #drp = self.driver.find_element_by_xpath(self.drpNewsLetter_xpath).send_keys(newvalue, Keys.ENTER)
    #     # scet = Select(drp)
    #     # scet.select_by_visible_text(newvalue)
    #
    #     # def setCustomerRoles(self, role):
    #     #     ddl = self.driver.find_element_by_xpath(self.drpCustomerRoles_xpath).send_keys(role, Keys.ENTER)
    #     #     # sct = Select(ddl)
    #     #     # sct.select_by_visible_text(role)
    #     if newvalue == "Male":
    #         self.driver.find_element_by_xpath(self.rbMale_xpath).click()
    #     elif gender == "Female":
    #         self.driver.find_element_by_xpath(self.rbFemale_xpath).click()
    #     else:
    #         self.driver.find_element_by_xpath(self.rbMale_xpath).click()

    def setCustomerRoles(self, role):
        self.driver.find_element_by_xpath(self.txtcustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemAdministrators_xpath)
        elif role == 'Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        time.sleep(3)
        # self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def clickOnSavebutton(self):
        return self.driver.find_element_by_xpath(self.btnSave_xpath)

    # def setCalendarDate(self,date):
