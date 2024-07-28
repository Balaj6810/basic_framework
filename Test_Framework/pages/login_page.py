from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utilities.utils import LogtheAutomation


class LoginPage():
    def __init__(self, driver, wait):
        self.logger = LogtheAutomation.logcatch(self)
        self.driver = driver
        self.wait= WebDriverWait(self.driver,10)

    def user_name(self, username):
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.logger.info("Login user name entered")

    def password(self,password):
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.logger.info("Login password has entered")

    def login_button(self):
        self.driver.find_element(By.XPATH, "//button[@id='kt_login_signin_submit']").click()
        self.logger.info("Clicked on login button done")

    def login_page_details(self, enterusername,enterpassword):
        self.user_name(enterusername)
        self.password(enterpassword)
        self.login_button()
        # self.wait.until(EC.visibility_of(self.driver.find_element(By.XPATH, "//button[@id='viewCampaign']")))
        # self.wait.until(EC.visibility_of_element_located((By.XPATH,"//button[@id='viewCampaign']")))


