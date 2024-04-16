import pytest
import time
import yaml
from utils.yamlReader import getValue
from selenium import webdriver

# browser = ["chrome", "firefox"]
locatorPath = "C:\\Users\\SharadKumar\\OneDrive - Round the clock technologies\\Desktop\\Test_Google\\test\\locators\\locators.yaml"
with open(locatorPath, "r") as file:
    locators = yaml.load()

@pytest.fixture()
def driver():
    # if request.param == "chrome":
    driver = webdriver.Chrome("C:\\Users\\SharadKumar\\OneDrive - Round the clock technologies\\Desktop\\Test_Google\\chromedriver.exe")
    # elif request.param=="firefox":
    #     driver = webdriver.Edge("C:\\Users\\SharadKumar\\OneDrive - Round the clock technologies\\Desktop\\Test_Google\\msedgedriver.exe")
    yield driver

def test_google(driver, getValue):
    url = getValue["url"]
    driver.get(url)
    searchBox = driver.find_element_by_xpath(locators["HomePage"]["InputBoxGoogle"])
    searchBox.send_keys("Hello")
    time.sleep(200)

# def test_flipkart(driver, getValue):
#     url = getValue["url1"]
#     driver.get(url)
