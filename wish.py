# 1) Obtaining the necessary data from previous module.
import organise
data=organise.get_data()

# 2) Obtaining the necessary path.
import os
directory_file_path=os.getcwd()
contact_path=os.path.join(directory_file_path,"Contacts")



# 3) Notification function
def notify(contact_name):
    from plyer import notification
    import time

    notification.notify(
        title='Birthday Wish',
        message=f'Wishing Happy Birthday to {contact_name}',
        app_name='Wishify',
        timeout=5  
    )
    time.sleep(2)
    

# 4) Announcement function
def announce(contact_name):
    import win32com.client 
    import time
    speaker = win32com.client.Dispatch("SAPI.SpVoice") 
    s = f'Wishing Happy Birthday to {contact_name}'
    speaker.Speak(s) 
    time.sleep(2)
  

# 5) Messaging function
def message():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from webdriver_manager.chrome import ChromeDriverManager
    import os
    import time
    import random

    def write_message(contact_name):
        try:
            # 1) Set up Chrome options
            chrome_options = Options()
            
            current_file_directory = os.getcwd()  # Getting the address of current directory
            whatsapp_files_directory = os.path.join(current_file_directory, "Whatsapp Files")  # Creating a directory for WhatsApp files
            
            if not os.path.exists(whatsapp_files_directory):
                os.mkdir(whatsapp_files_directory)
            
            chrome_options.add_argument(f"user-data-dir={whatsapp_files_directory}")
            
            
            # 2) Automatically getting ChromeDriver path and opening WhatsApp Web.
            chrome_driver_path = ChromeDriverManager().install()
            service = Service(executable_path=chrome_driver_path)

            # Initialize WebDriver
            driver = webdriver.Chrome(service=service, options=chrome_options)

            # Open WhatsApp Web
            driver.get("https://web.whatsapp.com")
            print("Opened WhatsApp Web")

            # Wait for the whatsapp web to be downloaded.
            time.sleep(20)
            
            
            # 3) Getting the message.
            file_path=os.path.join(current_file_directory,rf"Contacts\{contact_name}\Wishes.txt")
            with open(file_path,"r",encoding="utf-8") as f:
                mess=f.read().splitlines()
            message=random.choice(mess)



            # 4)Searching for the contact
            search_box = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
            )
            search_box.clear()
            search_box.send_keys(contact_name)
            search_box.send_keys(Keys.RETURN)
            
            

            # 5) Wait for the chat to load
            chat_loaded = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, f'//span[@title="{contact_name}"]'))
            )
            chat_loaded.click()



            # 6)Send message
            message_box = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'))
            )
            message_box.send_keys(message)
            message_box.send_keys(Keys.RETURN)
            time.sleep(5)   
            driver.quit()
            


        except Exception as e:
            print(f"An error occurred: {e}")

            
    # Run the function
    write_message(contact_name)


# 6) Get date/month/year
def date():
    import time
    t1=time.localtime()
    t2=time.strftime("%d:%m:%Y",t1)
    l=t2.split(":")
    return l


# 7) Wishing everyone and storing the date.
l=date()
date=int(l[0])
month=int(int(l[1]))
year=int(int(l[2]))

list1=data[month]
flag1=False
flag2=False

if list1 != []:
    
    if date in list1.keys():
        for e in list1[date]:
            try:
                flag1=True
                contact_name=e
                file_path=os.path.join(contact_path,rf"{contact_name}\Year.txt")
                
                with open(file_path,"a+",encoding="utf-8") as f:
                    f.seek(0)
                    a=f.read().splitlines()
                    
                    if str(year) not in a:
                        notify(contact_name)
                        announce(contact_name)
                        message()
                        flag2=True
                        f.seek(2)
                        f.write(f"{year}\n")
            except Exception as b:
                print("An error occured.",b)            
        
         
if flag1==False:
    print("No one has Birthday today.".center(50))     
elif flag2==False:
    print("All those who have Birthday today have already been wished.".center(50))           
    