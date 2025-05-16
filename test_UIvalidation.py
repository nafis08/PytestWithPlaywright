import time

from playwright.sync_api import Page, expect


def test_UIValidation(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/#")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("Consultant")
    page.get_by_role("checkbox", name="terms").check()
    page.get_by_role("button", name="Sign In").click()
    iphoneProduct = page.locator("app-card").filter(has_text="iphone X")
    iphoneProduct.get_by_role("button").click()
    nokiaProduct = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaProduct.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)
    time.sleep(5)


def test_newTab(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/#")

    with page.expect_popup() as newTabWindow:
        page.locator("//a[contains(text(), 'Free')]").click()
        newPage = newTabWindow.value
        textVarification = newPage.locator(".red").text_content()
        print(textVarification)
        strings = textVarification.split("at")
        email = strings[1].strip().split(" ")[0]
        assert email == "mentor@rahulshettyacademy.com"
    time.sleep(5)