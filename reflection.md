# Reflection

Student Name: Gabriel Davila
Student Email: gdavil01@syr.edu

`--- Reflection Below This Line ---`

Working on the web scraping project taught me a lot. At first, I struggled with the web archive timing out, but I realized using wait_for_selector with timeouts is way better than just waiting for the page to load. I also had trouble with module imports when menuitemextractor.py couldn’t find the MenuItem class. Switching to from src.menuitem import MenuItem fixed it and taught me how Python finds modules. Cleaning the scraped text was tricky too—I had to make sure important info like 'GS,' 'V,' 'S,' or 'P' tags got filtered out without messing up the menu items. Extracting menu items from nested HTML was another challenge, but I got better at using tools like query_selector and learned how to connect JavaScript DOM tricks with Python, like using evaluate_handle("el => el.nextElementSibling.nextElementSibling"). I also struggled with a test that required exactly 113 menu items with 4 columns, and I fixed it by refining my scraping logic to ensure all the data was extracted and formatted correctly. I also realized I need to get better at handling errors like timeouts and broken HTML. Testing overall really helped me catch problems early and build things the right way.