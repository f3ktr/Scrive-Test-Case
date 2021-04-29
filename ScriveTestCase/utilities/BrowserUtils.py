import time
from PIL import Image
from io import BytesIO

def take_screenshot(element, driver, filename='screenshot.png'):

  time.sleep(3)

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