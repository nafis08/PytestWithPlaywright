import time

from pytest_playwright.pytest_playwright import browser
from playwright.sync_api import Page, expect


def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com")

def test_playwrightShortCut(page:Page):
    page.goto("https://rahulshettyacademy.com")

def test_login_page(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/#")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("Consultant")
    page.get_by_role("checkbox", name= "terms").check()
    page.get_by_role("button", name= "Sign In").click()
    time.sleep(5)

def test_login_page_wrong_credentials(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/#")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learningsssss")
    page.get_by_role("combobox").select_option("Consultant")
    page.get_by_role("checkbox", name= "terms").check()
    page.get_by_role("button", name= "Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    time.sleep(5)