import re
from playwright.sync_api import Playwright, sync_playwright, TimeoutError
from menuitemextractor import extract_menu_item
from menuitem import MenuItem
import pandas as pd
import os

def tullyscraper(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={'width': 1280, 'height': 720})
    page = context.new_page()
    
    try:
        # Set a longer timeout
        page.set_default_timeout(90000)  # 90 seconds
        
        # Navigate to the page
        page.goto("https://web.archive.org/web/20241111165815/https://www.tullysgoodtimes.com/menus/")
        
        # Add a small delay to ensure page loads
        page.wait_for_timeout(5000)
        
        extracted_items = []
        titles = page.query_selector_all("h3.foodmenu__menu-section-title")
        print(f"Found {len(titles)} menu sections")
        
        for title in titles:
            title_text = title.inner_text()
            print("MENU SECTION:", title_text) 
            
            # Get the container of menu items
            row = title.evaluate_handle("el => el.nextElementSibling.nextElementSibling")
            menu_items = row.query_selector_all("div.foodmenu__menu-item")
            
            for item in menu_items:
                item_text = item.inner_text()
                if item_text.strip():
                    extracted_item = extract_menu_item(title_text, item_text)
                    print(f"  MENU ITEM: {extracted_item.name}")
                    extracted_items.append(extracted_item.to_dict())

        # Ensure cache directory exists
        os.makedirs("cache", exist_ok=True)
        
        df = pd.DataFrame(extracted_items)
        df.to_csv("cache/tullys_menu.csv", index=False)    
        print(f"Total menu items extracted: {len(extracted_items)}")
        
    except TimeoutError as e:
        print(f"Timeout error: {e}")
        raise
    except Exception as e:
        print(f"An error occurred: {e}")
        raise
    finally:
        context.close()
        browser.close()

if __name__ == "__main__":
    with sync_playwright() as playwright:
        tullyscraper(playwright)
