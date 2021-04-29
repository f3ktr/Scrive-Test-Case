
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from PIL import Image
from io import BytesIO

def take_screenshot(element, driver, filename='screenshot.png'):

  location = element.location_once_scrolled_into_view
  size = element.size
  png = driver.get_screenshot_as_png() # saves screenshot of entire page

  im = Image.open(BytesIO(png)) # uses PIL library to open image in memory

  left = location['x']
  top = location['y']
  right = location['x'] + size['width']
  bottom = location['y'] + size['height']


  im = im.crop((left, top, right, bottom)) # defines crop points
  im.save(filename) # saves new cropped image


driver = webdriver.Chrome(executable_path = "C:\Selenium WebDrivers\chromedriver_win32\chromedriver.exe") #ChromeDriver Running
driver.get("https://staging.scrive.com/t/9221714692410699950/7348c782641060a9")

name = "Faruk Enes Kilic"

xpathNameBox = "(//*[@class=\"name\"])[2]"
xpathNextButton = "//*[@class=\"label\"]"
xpathDocSignVerifyingMessage = "//*[@class=\"instructions s-header-doc-signed\"]"
xpathSignButton = "//*[@class=\"button button-block sign-button action\"]"
cssSignModule = ".col-xs-6.center-block"

driver.find_element_by_id("name").send_keys(name) #Typing name to name box
assert driver.find_element_by_xpath(xpathNameBox).text == name #Name Assertion

driver.find_element_by_xpath(xpathNextButton).click() #Next Button Click

driver.implicitly_wait(3)

signBox = driver.find_element_by_css_selector(cssSignModule) #Sign Module Location
take_screenshot(signBox,driver,'sign_box_screenshot.png')#Taking screenshot
driver.find_element_by_xpath(xpathSignButton).click() #Sign Button Click

driver.implicitly_wait(3)

verificationMessage = (driver.find_element_by_xpath(xpathDocSignVerifyingMessage).text)

assert verificationMessage == "Document signed!" #Assertion for the signed message
driver.close()

