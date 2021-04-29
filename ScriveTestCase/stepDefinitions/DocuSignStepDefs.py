from selenium import webdriver
from utilities import Driver as dr
from utilities import BrowserUtils as brow_util
from pages import DocumentSignPage as d_s_p

import configparser

def verify_that_document_signed(browser,sendingName):

    if browser.lower() == "chrome":
        path = dr.chromePath
        driver = webdriver.Chrome(executable_path=path)
    elif browser.lower() == "firefox":
        path = dr.firefoxPath
        driver = webdriver.Firefox(executable_path=path)
    else:
        print("Unsupported browser!")

    url = "https://staging.scrive.com/t/9221714692410699950/7348c782641060a9"

    driver.get(url)
    driver.find_element_by_id("name").send_keys(sendingName)

    assert driver.find_element_by_xpath(d_s_p.xpathNameBox).text == sendingName

    driver.find_element_by_xpath(d_s_p.xpathNextButton).click()
    driver.implicitly_wait(5)

    signModule = driver.find_element_by_css_selector(d_s_p.cssSignModule)
    if(browser.lower() == "firefox"):
        brow_util.take_screenshot(signModule,driver,r'..\Screenshots\(Firefox)doc_sign_page_box_screenshot.png')
    else:
        brow_util.take_screenshot(signModule, driver, r'..\Screenshots\(Chrome)doc_sign_page_box_screenshot.png')
    driver.find_element_by_xpath(d_s_p.xpathSignButton).click()
    driver.implicitly_wait(5)



    verificationMessage = (driver.find_element_by_xpath(d_s_p.xpathDocSignVerifyingMessage).text)

    assert verificationMessage == "Document signed!"

    driver.close()




