from selenium import webdriver
from pom.login_page import LoginPage
import time

print("🚀 Starting Automation...")

# Initialize WebDriver
driver = webdriver.Chrome()

# Open OrangeHRM site
driver.get("https://opensource-demo.orangehrmlive.com/")
print("🌐 Opened OrangeHRM site")

# Wait for page to load
time.sleep(3)

# Use LoginPage
login = LoginPage(driver)

print("🧑 Entering Username...")
login.enter_username("Admin")

print("🔒 Entering Password...")
login.enter_password("admin123")

print("➡️ Clicking Login...")
login.click_login()

# Optional: wait to observe result before browser closes
time.sleep(10)

# Close browser
driver.quit()
print("✅ Automation Finished.")
