from playwright.sync_api import Playwright, sync_playwright, expect
import re



def test_run(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.facebook.com/")
#    print(expect(page).to_have_title(re.compile("Playwright")))
    print(expect(page).to_have_title(re.compile("Facebook")))
    page.get_by_test_id("royal_email").click()
    page.get_by_test_id("royal_email").fill("asmitabisoi@gmail")
    page.get_by_test_id("royal_pass").click()
    page.get_by_test_id("royal_pass").fill("1234")
    page.get_by_test_id("royal_email").click()
    page.get_by_test_id("royal_email").fill("asmitabisoi@gmail.com")
    page.get_by_test_id("royal_login_button").click()
    page.get_by_test_id("assistive_id_dialog").locator("i").click()

    # ---------------------
    context.close()
    browser.close()


#with sync_playwright() as playwright:
#   test_run(playwright)