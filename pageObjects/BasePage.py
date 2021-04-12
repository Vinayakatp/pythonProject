import time

from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_DatePicker(self, Month, Year, exDay):
        self.driver.find_element_by_xpath("//span[@class='k-select']").click()
        time.sleep(5)
        monthYearValue = self.driver.find_element_by_xpath("//body/div[4]/div[1]/div[1]/div[1]/a[2]").text
        print(monthYearValue)
        month = monthYearValue.split(" ")[0].strip()
        year = monthYearValue.split(" ")[1].strip()
        while not (month == Month and year == Year):
            self.driver.find_element_by_xpath("//a[@aria-label='Previous']").click()
            monthYearValue = self.driver.find_element_by_xpath("//body/div[4]/div[1]/div[1]/div[1]/a[2]").text
            print(monthYearValue)
            month = monthYearValue.split(" ")[0].strip()
            year = monthYearValue.split(" ")[1].strip()
        # self.driver.find_element_by_xpath("//a[text()='11']").click()
        b = self.driver.find_element_by_xpath("//a[text()='" + exDay + "']")
        self.driver.execute_script("arguments[0].click();", b)

    def clickOn(self, Locator):
        element = self.driver.find_element(By.XPATH, Locator)
        return element

    def setField(self, Locator, plaintext):
        element = self.driver.find_element(By.ID, Locator)
        element.clear()
        return element.send_keys(plaintext)
