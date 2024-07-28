import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
#browser
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
#browserservice
from selenium.webdriver.chrome.service import Service as chromeservice
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService

@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="class", autouse=True)
def setup(request, browser):
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome(service=chromeservice(ChromeDriverManager().install()))
    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise ValueError("Unsupported browser: {browser}")
    driver.maximize_window()
    driver.get("https://prospectboss.com/easycampaignbeta/")
    wait = WebDriverWait(driver, 10)
    request.cls.driver = driver
    request.cls.wait = wait
    yield
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")

#SCREENSHOT

# we can take screenshot in three ways
# driver.save_screenshot()
# driver.get_screenshot_as_file()
# By default it will take screenshots

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extras.url("https://prospectboss.com"))
        xfail = hasattr(report, "wasxfail")
        if(report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            report_directory = os.path.dirname(item.config.option.htmlpath)
            file_name = str(int(round(time.time() * 1000))) + ".png"  #filename based on time
            #file_name = report.nodeid.replace(":", "_") + ".png"  #filename will be on test case name
            destinationFile = os.path.join(report_directory, file_name)
            driver.save_screenshot(destinationFile)
            if file_name:
                html = ('<div><img src="%s" alt="screenshot" style="width:300px;height=200px" ' 
                        'onclick="window.open(this.src)" align="right"/></div>' % file_name)
            extra.append(pytest_html.extras.html(html))
    report.extra = extra

#FOR REPORT
def pytest_html_report_title(report):
    report.title = "Automation_Report"



# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # Define the fixture with class scope
# @pytest.fixture(scope="class")
# def setup(request):
#     # Initialize the Chrome driver
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     driver.get("https://prospectboss.com/easycampaignbeta/")
#     request.cls.driver = driver
#
#     yield
#     driver.quit()
