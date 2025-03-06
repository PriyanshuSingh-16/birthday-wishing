from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os

def get_contacts():
    driver = None
    try:
        # Set up Chrome options
        chrome_options = Options()
        
        current_file_directory = os.getcwd()  # Getting the current directory
        whatsapp_files_directory = os.path.join(current_file_directory, "Whatsapp Files")  # Directory for WhatsApp files
        
        if not os.path.exists(whatsapp_files_directory):
            os.mkdir(whatsapp_files_directory)
        
        chrome_options.add_argument(f"user-data-dir={whatsapp_files_directory}")
        
        # Automatically getting ChromeDriver path and opening WhatsApp Web.
        chrome_driver_path = ChromeDriverManager().install()
        service = Service(executable_path=chrome_driver_path)

        # Initialize WebDriver
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Open WhatsApp Web
        driver.get("https://web.whatsapp.com")
        print("Opened WhatsApp Web")

        # Wait for the user to scan the QR code and the chat panel to load
        input("Press Enter after scanning the QR code and after WhatsApp Web page is completely loaded...")

        # Wait until the contacts panel is visible
        WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.ID, "pane-side"))
        )

        # Get the contacts panel
        contacts_panel = driver.find_element(By.ID, "pane-side")

        # Get the current visible contacts
        contacts = set()  # Using a set to store contacts to avoid duplicates
        contact_elements = contacts_panel.find_elements(By.CSS_SELECTOR, 'span[dir="auto"]')
        for contact_element in contact_elements:
            # Filter elements based on font and color using JavaScript
            font_color = driver.execute_script("return window.getComputedStyle(arguments[0]).color;", contact_element)

            # Assuming we want to filter for a specific color and font-family (replace with your desired values)
            desired_color1 = "rgb(17, 27, 33)"   
            desired_color2="rgb(233, 237, 239)"

            if font_color == (desired_color1):
                name = contact_element.text
                if name:
                    contacts.add(name)

            elif font_color == (desired_color2):
                name = contact_element.text
                if name:
                    contacts.add(name)
                    
        # Storing the contact list into a file
        with open("Contacts List.txt", "w", encoding="utf-8") as f:
            for contact in sorted(contacts):  # Sorting the contacts before writing
                f.write(f"{contact}\n")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if driver:
            driver.quit()

# Run the function
get_contacts()
