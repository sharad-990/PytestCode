import pytest
import time
import yaml
from utils.yamlReader import getValue
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.xlsxReader import excel_data
from selenium import webdriver

# browser = ["chrome", "firefox"]
locatorPath = "C:\\Users\\SharadKumar\\OneDrive - Round the clock technologies\\Desktop\\Test_Google\\test\\locators\\locators.yaml"
with open(locatorPath, "r") as file:
    locators = yaml.safe_load(file)

@pytest.fixture()
def driver():
    # if request.param == "chrome":
    driver = webdriver.Chrome("C:\\Users\\SharadKumar\\OneDrive - Round the clock technologies\\Desktop\\Test_Google\\chromedriver.exe")
    driver.maximize_window()
    # elif request.param=="firefox":
    #     driver = webdriver.Edge("C:\\Users\\SharadKumar\\OneDrive - Round the clock technologies\\Desktop\\Test_Google\\msedgedriver.exe")
    yield driver

def test_login_Outlook(driver, getValue, excel_data):
    url = getValue["url"]
    driver.get(url)
    driver.implicitly_wait(2)
    driver.find_element_by_xpath(locators["HomePage"]["InputEmailBox"]%"Email").send_keys("sharadkumar@rtctek.com")
    driver.find_element_by_xpath(locators["HomePage"]["NextButton"]).click()
    driver.find_element_by_xpath(locators["HomePage"]["InputEmailBox"]%"Password").send_keys("Ashi@990")
    driver.find_element_by_xpath(locators["HomePage"]["NextButton"]).click()
    driver.find_element_by_xpath(locators["HomePage"]["NextButton"]).click()
    time.sleep(5)
    driver.find_element_by_xpath(locators["HomePage"]["NewMail"]).click()
    driver.find_element_by_xpath(locators["HomePage"]["MailTo"]).send_keys("sharadKumar@rtctek.com")
    time.sleep(5)
    driver.find_element_by_xpath(locators["HomePage"]["MailTo"]).send_keys(Keys.ENTER)
    driver.find_element_by_xpath(locators["HomePage"]["MailSubject"]).click()
    driver.find_element_by_xpath(locators["HomePage"]["MailSubject"]).send_keys(456)
    time.sleep(3)
    driver.find_element_by_xpath(locators["HomePage"]["MailTextBox"]).click()
    # for i in range(len(excel_data)-1):
    driver.find_element_by_xpath(locators["HomePage"]["MailTextBox"]).send_keys(excel_data)
        # print(excel_data[i].__str__)
    driver.execute_script("scroll(0, -250);")
    time.sleep(2)
    driver.find_element_by_xpath(locators["HomePage"]["MailSendButton"]).click()
    time.sleep(5)

# def test_Create_DSR(driver, excel_data):
    # data = excel_data()
    # driver.find_element_by_xpath("//input[@id = 'topSearchInput']").click
    # driver.find_element_by_xpath("//input[@id = 'topSearchInput']").send_keys(excel_data.__str__)
    # time.sleep(50)
    # for line in excel_data:
    # for excel_data in excel_data:
    #     driver.find_element_by_xpath("//input[@id = 'topSearchInput']").click
    #     driver.find_element_by_xpath("//input[@id = 'topSearchInput']").send_keys(excel_data.__str__)
    #     print(excel_data.__str__)
    #     time.sleep(150)



# def test_flipkart(driver, getValue):
#     url = getValue["url1"]
#     driver.get(url)
