# 1) Importing the necessary modules.
import os



# 2) Obtaining the list of contacts whose files are present.
directory_path=os.getcwd()
contact_list_path=os.path.join(directory_path,"Contacts List With Chats.txt")   
                       
with open(contact_list_path,"r") as f:
    contact_list_with_chats=f.read().splitlines()
    
    
    
# 3) Defining the list of elements that should be searched.
wishes=["happy birthday","many many returns of this day","may god bless u with long life"]    



# 4) Function for searching for wishes in all the files and getting the birthdates.
def obtain_birthdate(string,contact_name):
    
    for e in wishes:
        if e in string.lower() and string.split("-")[1].split(":")[0].strip()!=contact_name:
            length=len(string)
            str1=string[0:length-1]
            date=str1.split("-")[0].split(",")[0]
            message=str1.split("-")[1].split(":")[1]
            return(date,message)
        return None
    
    
    
# 5) Searching for wishes in all the files and getting the birthdates.
date_of_birth_file_path=os.path.join(directory_path,"Birth Date") 

with open(date_of_birth_file_path,"w",encoding="utf-8") as file1:        # Creating a file with birth dates
        
    for e in contact_list_with_chats:
        file_path1=os.path.join(directory_path,rf"Contacts\{e}\WhatsApp Chat with {e}.txt")
        file_path_2=os.path.join(directory_path,rf"Contacts\{e}\Wishes.txt")
        
        with open(file_path_2,"w",encoding="utf-8") as file2:             # Creating a file with wishes.
            
            with open(file_path1,"r+",encoding="utf-8") as file3:            # Reading the chats
                readlin=1
                flag=False
                
                while(readlin):
                    readlin=file3.readline()
                    result=obtain_birthdate(readlin,e)
                    
                    if not result == None and flag==False:
                        print(f"{e}:{result[0]}",file=file1)
                        print(f"{result[1].strip()}",file=file2)
                        flag=True
                        
                    elif  not result == None:
                        print(f"{result[1].strip()}",file=file2)  
             
                
                
                