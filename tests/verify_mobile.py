
from playwright.sync_api import sync_playwright
import time
import os

def run():
    with sync_playwright() as p:
        # Test mobile device
        iphone_13 = p.devices['iPhone 13']
        browser = p.webkit.launch()
        context = browser.new_context(**iphone_13)
        page = context.new_page()

        # Navigate to the app
        page.goto('http://localhost:3000')

        # Wait for fonts and canvas to load
        page.wait_for_timeout(2000)

        # Take a screenshot of the initial mobile state
        page.screenshot(path='mobile_initial.png')

        # Personalize
        page.fill('#nameInput', 'Mobile User')
        page.click('button:has-text("generate link")')

        # Wait a bit for the "link copied" state
        page.wait_for_timeout(1000)
        page.screenshot(path='mobile_after_generate.png')

        # Navigate to the personalized URL manually (since clipboard is hard to test in headless)
        page.goto('http://localhost:3000?name=Mobile%20User')
        page.wait_for_timeout(2000)
        page.screenshot(path='mobile_final_greeting.png')

        browser.close()

if __name__ == "__main__":
    run()
