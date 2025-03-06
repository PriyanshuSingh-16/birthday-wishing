# 1) Importing the necessary Modules.
import zipfile
import os


# 2) Creating a function to unzip file and save it in a different directory.
current_directory_path=os.getcwd()
new_directory_path=os.path.join(current_directory_path,"Contacts")  # Creating a new directory within this directory for Contacts
os.makedirs(new_directory_path, exist_ok=True)

def unzip_file(zip_file_path, extract_to_dir):
    os.makedirs(extract_to_dir, exist_ok=True)
    
    # Open the zip file in read mode and Extract all the contents into the specified directory
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to_dir)
    

# 3) Unzipping the file for all the possible contacts.
contact_whose_chats_are_present_=[]
with open("Contacts List.txt","r") as f:  # Obtaining Contact List
    contact=f.read().splitlines()
    
    
for e in contact:                            # Unzipping the file
    zip_file_path=os.path.join(current_directory_path,f"WhatsApp Chat with {e}.zip")
    extract_to_dir=os.path.join(new_directory_path,f"{e}")
    
    if os.path.exists(zip_file_path):
        contact_whose_chats_are_present_.append(e)
        unzip_file(zip_file_path, extract_to_dir)
        os.remove(zip_file_path)            # Removing the Zipped file
        

with open("Contacts List With Chats.txt","w") as f:  # Obtaining Contact List whose chats are uploaded
         for e in contact_whose_chats_are_present_:
             print(e,file=f)
