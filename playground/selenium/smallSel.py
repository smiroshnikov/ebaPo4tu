from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("E:\Development\ebaPo4tu\playground\pythonic stuff\chromewriver-win\chromedriver.exe")

driver.get("http://python.org")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "start-shell")))
    print("Element found!")
finally:
    pass
    # driver.quit()
#
# implicit vs explicit wait
# implicit wait - waits before every call (pauses for a certain amount of time for every action
# implicit can be used if a connection is slow / used once per session
# explicit wait wait for a certain condition only

driver.implicitly_wait(10)
driver.get("http://python.org")
we = driver.find_element_by_id('start-shell')
driver.close()
