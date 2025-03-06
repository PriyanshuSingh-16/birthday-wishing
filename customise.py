# 1) Importing the necessary modules
import os



# 2) Storing the contacts with birthdate in a list.
directory_file_path=os.getcwd()
contact_list_with_birthdate_path=os.path.join(directory_file_path,"Birth Date")

with open(contact_list_with_birthdate_path,"r",encoding="utf-8") as f:
    contact_list_with_birthdate=f.read().splitlines()
  
  
  
# 3) Various options to wish happy Birthday.
w1=["Happy Birthday\n","Happy Birthday Bro\n","Happy Birthday Buddy 🙌🥳\n"]
w2=["Happy Birthday\n","Happy Birthday my dear\n","Happy Birthday ❤️\n"] 
w3=["Happy Birthday Sir\n","Happy Birthday dear Sir\n","Happy Birthday 🙏\n"] 



# 4) Getting the contact list.
contact_list=[]
for e in contact_list_with_birthdate:
    k=e.split(":")[0]
    contact_list.append(k)


  
# 5) Asking the User to categorise the contacts and customising the Wishes accordingly.
d1={"1":w1,"2":w2,"3":w3}

print("Category 1: Friends and Collegues")
print("Category 2: Family")
print("Category 3: Seniors")
print("Enter 1 for Category 1 and so on.")
print("\n")

for e in contact_list:
    a=input(f"{e}: ")
    file_path=os.path.join(directory_file_path,rf"Contacts\{e}\Wishes.txt")
    with open(file_path,"a",encoding="utf-8") as f:
        f.writelines(d1[a])
        

    
    
    