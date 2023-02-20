import re
from playwright.sync_api import Page, expect
import pytest

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("Loading Katalon homepage...")
    page.goto("https://www.katalon.com")

    yield
    print("Test finished\n")

def test_successful_login(page: Page):
    login = page.get_by_role('link', name='Log in')
    expect(login).to_have_attribute('href', re.compile('.*/sign-in'))

    login.click()

    expect(page).to_have_url(re.compile('.*/sign-in'))
    
    form_title = page.get_by_text('Welcome back')
    expect(form_title).to_be_visible()

    form_logo = page.get_by_alt_text('Katalon Logo')
    expect(form_logo).to_be_visible()

    email_input = page.get_by_placeholder("Email", exact=True)
    expect(email_input).to_be_editable()

    email_input.fill('anh.ng.hcm@gmail.com')

    password_input = page.get_by_placeholder("Password", exact=True)
    expect(password_input).to_be_editable()
    password_input.fill("Test123$")

    sign_in_btn = page.get_by_role('button', name="Sign in", exact=True)
    expect(sign_in_btn).to_be_visible()
    sign_in_btn.click()

    expect(page).to_have_url(re.compile('.*/testops.katalon.io'))



def test_homepage_has_katalon_in_title_and_view_demo_link_linking_to_the_demo_page(page: Page):
    expect(page).to_have_title(re.compile("katalon", re.IGNORECASE))
    
    view_demo = page.get_by_role('link', name="View a demo")
    expect(view_demo).to_have_attribute('href', re.compile('.*/view.*demo'))

    view_demo.click()
    expect(page).to_have_url(re.compile('.*demo'))
    

    play_btn = page.locator("[id=\"wistia_132\\.big_play_button_graphic\"]")
    expect(play_btn).to_be_visible()

