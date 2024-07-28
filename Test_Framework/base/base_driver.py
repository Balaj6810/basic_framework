import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class PopUps():
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def popups(self):   #closing the pop-ups
        try:
         # self.driver.wait(self.driver.until.find_element(By.XPATH,"(//button[contains(@aria-label,'Close')])[10]")).click()
         # self.driver.wait(self.driver.until.find_element(By.XPATH, "(//button[@aria-label='Close']").click())

            # Wait for the first pop-up close button to be clickable and then click it
            close_button1 = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[contains(@aria-label,'Close')])[10]")))
            close_button1.click()

            # Wait for the second pop-up close button to be clickable and then click it
            close_button2 = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@aria-label='Close'])")))
            close_button2.click()

        except Exception as e:
            print("We got some exception like ", e)
        else:
            print("No exception came successfully")

    def waitingelements(self):
       dd =self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='viewCampaign']")))
       dd.click()

    def logut_from_application(self):
        profilepop = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='kt-header__topbar-user']")))
        profilepop.click()
        logout = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Sign Out']")))
        logout.click()
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.ID, 'username')))




