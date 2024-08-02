import os
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# Setup WebDriver path and options
paths = r"E:\Automation testing\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the IMDb Advanced Name Search page
driver.get("https://www.imdb.com/search/name/")
driver.maximize_window()
driver.execute_script("window.scrollTo(500, 500);")

name_input = driver.find_element(By.XPATH,'//div[@class="sc-6addea7c-0 jfSEAR"]').click()
name_input.send_keys("Bhavani")

# Use WebDriverWait to wait for elements to be present
wait = WebDriverWait(driver, 20)
driver.execute_script("window.scrollTo(700, 700);")
# Fill in the input boxes and select boxes

# filling in the name box
name = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="sc-6addea7c-0 jfSEAR"]'))).click()
driver.find_element(By.XPATH,'//input[@name="name-text-input"]').send_keys("bhavani")

#filling the birthdatebox
b_date = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="birthDateAccordion"]/div[1]/label/span[1]/div'))).click()
driver.find_element(By.XPATH,'//input[@name="birth-date-start-input"]').send_keys("16/03/2002")
driver.find_element(By.XPATH,'//input[@name="birth-date-end-input"]').send_keys("24/06/2023")

#filling the birthdaybox
b_day = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="birthdayAccordion"]/div[1]/label/span[1]/div'))).click()
driver.find_element(By.XPATH,'//input[@aria-label="Enter birthday"]').send_keys("03/16")
driver.execute_script("window.scrollTo(700, 700);")

awards = wait.until(EC.presence_of_element_located((By.XPATH, '//label[@data-testid="accordion-item-awardsAccordion"]'))).click()
driver.execute_script("window.scrollTo(1000, 1000);")

page_topics = wait.until(EC.presence_of_element_located((By.XPATH, '//label[@data-testid="accordion-item-deathDateAccordion"]'))).click()
driver.execute_script("window.scrollTo(1000, 1000);")

d_date = wait.until(EC.presence_of_element_located((By.XPATH, '//label[@aria-controls="accordion-item-deathDateAccordion"]'))).click()
driver.find_element(By.XPATH,'//input[@aria-label="Enter death date from"]').send_keys("11/04/2012")
driver.find_element(By.XPATH,'//input[@aria-label="Enter death date to"]').send_keys("14/05/2021")
driver.execute_script("window.scrollTo(500, 500);")

gender = wait.until(EC.presence_of_element_located((By.XPATH, '//label[@aria-controls="accordion-item-genderIdentityAccordion"]'))).click()
driver.execute_script("window.scrollTo(500, 500);")

credits = driver.find_element(By.XPATH, '//*[@id="filmographyAccordion"]/div[1]/label').click()

# Find the credit input element
credit = driver.find_element(By.XPATH, '//*[@id="accordion-item-filmographyAccordion"]/div/div/div/div[1]/input')

# Use ActionChains to input text and select the first suggestion
actions = ActionChains(driver)
actions.send_keys_to_element(credit, "Holiday")
actions.pause(2)  # Wait for suggestions to appear
actions.send_keys(keys.DOWN)  # Navigate to the first suggestion
actions.pause(1)  # Pause briefly to ensure the selection
actions.send_keys(keys.ENTER)  # Press the Enter key to select
actions.perform()

# Confirmation
print("Search performed successfully.")

a_names = wait.until(EC.presence_of_element_located((By.XPATH, '//label[@class="ipc-accordion__item__label ipc-accordion__item__label--indent-full"]'))).click()
result = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[1]/button/span')))
result.click()

# # # Close the browser
driver.quit()