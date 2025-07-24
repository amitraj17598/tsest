from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('User Launch Chrome browser')
def step_impl(context):
    service = Service(r"C:\Program Files\chrome driver\chromedriver.exe")
    context.driver = webdriver.Chrome(service=service)
    context.driver.maximize_window()

@when('User opens URL "{"https://jugno.racketail.com/"}')
def step_impl(context, url):
    context.driver.get(url)

@when('User enters Email as "{email}" and Password as "{password}"')
def step_impl(context, email, password):
    wait = WebDriverWait(context.driver, 10)

    email_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='email']")))
    email_input.clear()
    email_input.send_keys(email)

    password_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
    password_input.clear()
    password_input.send_keys(password)

@when('Click on Login')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    ).click()

@then('Page Title should be "{title}"')
def step_impl(context, title):
    WebDriverWait(context.driver, 10).until(EC.title_is(title))
    assert context.driver.title == title, f"Expected '{title}', got '{context.driver.title}'"

@when('User click on Log out link')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Logout')]"))
    ).click()

@then('close browser')
def step_impl(context):
    context.driver.quit()
