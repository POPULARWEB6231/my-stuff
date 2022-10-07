from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory": r"C:\Users\slpol\python_work\fltp_files\downloads\\"}
chromeOptions.add_experimental_option("prefs", prefs)
chromedriver = "C:/Users/slpol/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriver, options=chromeOptions)

url = "https://dos.elections.myflorida.com/committees/downloadcomlist.asp"
# create a new Chrome session
driver.implicitly_wait(30)
driver.get(url)

# Find download button.
click_field = driver.find_element(By.NAME, 'CanDownload')

# Click that motherfucker.
click_field.click()

# Wait 10 seconds for the load
driver.implicitly_wait(25)

time.sleep(5)

from rename_file_test import rename_file

rename_file()
