import unittest
import pytest
from utilities.utils import LogtheAutomation
from base.base_driver import PopUps
from pages.login_page import LoginPage

#For file reading
from ddt import data, unpack, ddt, file_data

@pytest.mark.usefixtures("setup")
@ddt
class TestPBLogin(unittest.TestCase):
    log = LogtheAutomation()

    # @data(("Praveen2", "Testing"))
    # @pytest.mark.parametrize("username, password", [
    #     ("praveen2", "testing")])
    # @unpack

    #JSON FILE READ
    # @file_data("../testdata/testdata.json")

    #EXCEL FILE READ
    # @data(*LogtheAutomation.xlsxfilereader("C:\\Users\\balaj\\PycharmProjects\\Test_Framework\\testdata\\testdata.xlsx", "testdata"))


    #CSV FILE READ
    @data(*LogtheAutomation.csvfilereader('C:\\Users\\balaj\\PycharmProjects\\Test_Framework\\testdata\\testdata.csv'))
    @unpack


    def test_loginpage(self, username, password):
        #browser will launch and login screen will be opened
        #login details
        login = LoginPage(self.driver, 10)
        login.login_page_details(username, password)
        self.log.logcatch().info(f"Username and password entered successfully : '{username}'")
        pp = PopUps(self.driver, 20)
        pp.waitingelements()
        pp.logut_from_application()
        self.log.logcatch().info("Logged out success")

# ================================================
# TO RUN THE SCRIPT FOLLOW THESE COMMANDS
# pyest
#
# pytest run in command  prompt:
#     1.[ pytest --browser chrome ] = normal run without reports, only log
#     2. [pytest --browser chrome --html=report.html --self-contained-html] -with html reports
#     3. [pytest --browser chrome --html=/reports/july07.html -  inside directory that we need
# test coverage report - pytest --cov=my_module tests/
# ===================================================




#==========================================

# login_details = LoginPage(self.driver, self.wait)
#
# #username
# login_details.user_name('praveen2')
#
# #password
# login_details.password('testing')
#
# #loginbutton
# login_details.login_button()

# #closing popups
# Popup = Pop_Ups(self.driver, self.wait)
# Popup.popups()

#wait time
# WebDriverWait(self.driver, 20)

# OR
# Wait for an element to ensure the page has loaded after login
# WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, "//button[@id='kt_login_signin_submit']"))
#         )


# import pytest
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
#
# # Apply the setup fixture to the test class
# @pytest.mark.usefixtures("setup")
# class TestPBLogin:
#     def test_loginpage(self):
#         # Perform the login actions
#         self.driver.find_element(By.ID, "username").send_keys('praveen2')
#         self.driver.find_element(By.ID, "password").send_keys('testing')
#         self.driver.find_element(By.XPATH, "//button[@id='kt_login_signin_submit']").click()
#         self.driver.maximize_window()

#         # Wait for an element to ensure the page has loaded after login
#         WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, "//button[@id='kt_login_signin_submit']"))
#         )
