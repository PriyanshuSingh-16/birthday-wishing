# 0) Importing the important files
import os
import shutil
import time
import zipfile





# 1) COMPLETE RESET

def complete_reset():
    try:
        if(os.path.exists("Whatsapp Files")):
            shutil.rmtree("Whatsapp Files") 
            
        if(os.path.exists("Contacts")):
            shutil.rmtree("Contacts")     

        if(os.path.exists("Contacts List.txt")):
            os.remove("Contacts List.txt") 

        
        if(os.path.exists("Contacts List With Chats.txt")):
            os.remove("Contacts List With Chats.txt") 
        
        if(os.path.exists("Birth Date")):
            os.remove("Birth Date")  

            
    except Exception as e:
        print("There was some error in resetting.")
        




# 2) PARTIAL RESET

def partial_reset():
    try:    
        if(os.path.exists("Contacts")):
            shutil.rmtree("Contacts")     

        if(os.path.exists("Contacts List.txt")):
            os.remove("Contacts List.txt") 

        
        if(os.path.exists("Contacts List With Chats.txt")):
            os.remove("Contacts List With Chats.txt") 
            
        if(os.path.exists("Contacts List Without Chats.txt")):
            os.remove("Contacts List Without Chats.txt")    
        
        if(os.path.exists("Birth Date")):
            os.remove("Birth Date")  

            
    except Exception as e:
        print("There was some error in resetting.")
        
  
        
        
        
# 3) Recheck the Birth date of your contacts.

def birth_date_checking():
    directory_path=os.getcwd()
    file_path=os.path.join(directory_path,"Birth Date")
    
    with open(file_path,"r",encoding="utf-8") as f:
        data=f.read()
        data_processed=data.splitlines()
        
    for idx,e in enumerate(data_processed,start=1):
        print(f"{idx} {e}")
    
    print()
    print("Enter 0 if u have confirmed.")
    print()
    
    a=int(input("Enter your response: ")) 
    if a==0:
        print("The Birthdates have been confirmed.")
    else:      
        while(a):
            print("Enter date and month in two digits.")
            date=input("Enter the date: ")  
            month=input("Enter the month: ") 
             
            contact_path=os.path.join(directory_path,"Contacts") 
            year_path=os.path.join(contact_path,rf"{data_processed[a-1].split(":")[0]}\Year.txt")
            
            if os.path.exists(year_path):
                with open(year_path,"r",encoding="utf-8") as f:
                    f.seek(0)
                    a1=f.read().splitlines()
                    year_1=time.strftime("%Y")
                    if(year_1 in a1):
                        a1.remove(year_1)
                        
                with open(year_path,"w",encoding="utf-8") as f:
                    for e in a1:
                        print(e,file=f)        
                
            year=data_processed[a-1].split("/")[2]
                
            value=data_processed[a-1].split(":")[0] + f":{date}/{month}/{year}"
            data_processed[a-1]=value 
            a=int(input("Enter your response: ")) 
            
            
        with open(file_path,"w",encoding="utf-8") as f:
            for e in data_processed:
                print(e,file=f)
        print("All the birthdates have been fixed.") 
        
  


 
# 4) Getting the list of contacts whose chats are not exported.
 
def chatless_conatcts():
    directory_path=os.getcwd()
    file_path1=os.path.join(directory_path,"Contacts List.txt")
    file_path2=os.path.join(directory_path,"Contacts List With Chats.txt")
    file_path3=os.path.join(directory_path,"Contacts")
    
    with open(file_path1,"r",encoding="utf-8") as f1:
        data1=set(f1.read().splitlines())
        
        
    with open(file_path2,"r",encoding="utf-8") as f2:
        data2=set(f2.read().splitlines())
        
    data3=list(data1.difference(data2)) 
    for idx,e in enumerate(data3,start=1):
        print(f"{idx} {e}")
    
    if data3 !=[]:  
        print()  
        print("Export the chats of the following to this folder in the form of zipped file.")
        print("Once u are done enter 0.")
        print()
            
        while(True):
            a=int(input("Enter 0 when done: "))
            if(a==0):
                break
            else:
                print("Invalid Input.")  
 
        os.rename("Contacts List.txt","Contacts List1.txt")      
        os.rename("Contacts List With Chats.txt","Contacts List With Chats1.txt") 
        os.rename("Birth Date","Birth Date1")  

        with open("Contacts List.txt","w",encoding="utf-8") as f:
            for e in data3:
                print(e,file=f)
        
        # Unzipping the chats and creating individual folders for each contacts.
        import file_manager     

        # Reading the chats and obtaining birth dates and Messages.
        import birth_dates

        # Customising messages for each contact.
        print() 
        print("Customize ur wishes according to ur wish.".center(50))
        print("Categorize them.".center(50))
        print("\n")

        import customise
        
        os.remove("Contacts List.txt")
        
        with open("Birth Date","r",encoding="utf-8") as f:
            a1=f.read()
        with open("Birth Date1","a",encoding="utf-8") as f1:
            f1.write(a1)    
        os.remove("Birth Date")
        os.rename("Birth Date1","Birth Date") 
        
        
        with open("Contacts List With Chats.txt","r",encoding="utf-8") as f:
            a1=f.read()
        with open("Contacts List With Chats1.txt","a",encoding="utf-8") as f1:
            f1.write(a1)    
        os.remove("Contacts List With Chats.txt")
        os.rename("Contacts List With Chats1.txt","Contacts List With Chats.txt")
           
        
        os.rename("Contacts List1.txt","Contacts List.txt") 
                                        
    else:
        print("Chats of all the contacts which are presented in the contact list have been already exported.")             
                




# 5) Getting the list of contacts whose chats are not exported manually.

def chatless_contacts_manually():
    directory_path=os.getcwd()
    file_path1=os.path.join(directory_path,"Contacts List.txt")
    file_path2=os.path.join(directory_path,"Contacts List With Chats.txt")
    file_path3=os.path.join(directory_path,"Contacts")
    
    with open(file_path1,"r",encoding="utf-8") as f1:
        data1=set(f1.read().splitlines())
        
        
    with open(file_path2,"r",encoding="utf-8") as f2:
        data2=set(f2.read().splitlines())
        
    data3=list(data1.difference(data2)) 
    for idx,e in enumerate(data3,start=1):
        print(f"{idx} {e}")
    
    if data3 !=[]:  
        print()  
        print("Enter the sequence no. of the contact which u would like to manually add.")
        print("Once u are done enter 0.")
        print()
        
        a=1
        
        additional_contacts=[]
        additional_contacts_with_birth_date=[]
        while(a):
            a=int(input("Enter the sequence no: "))   
            if a==0:
                break
            date=input("Enter the date in two digits: ")
            month=input("Enter the month in two digits: ")
            print()
            
            year=time.strftime("%Y")
            data_to_be_added=f"{data3[a-1]}:{date}/{month}/{year[2:]}"
            
            additional_contacts.append(data3[a-1])
            additional_contacts_with_birth_date.append(data_to_be_added)
            
        with open("Contacts List Without Chats.txt","a+",encoding="utf-8") as f:
            f.seek(2) 
            for e in additional_contacts:
                print(e,file=f)
                file_path4=os.path.join(file_path3,e)
                file_path5=os.path.join(file_path4,"Wishes.txt")
                os.makedirs(file_path4,exist_ok=True) 
                
                # Various options to wish happy Birthday.
                w1=["Happy Birthday\n","Happy Birthday Bro\n","Happy Birthday Buddy 🙌🥳\n"]
                w2=["Happy Birthday\n","Happy Birthday my dear\n","Happy Birthday ❤️\n"] 
                w3=["Happy Birthday Sir\n","Happy Birthday dear Sir\n","Happy Birthday 🙏\n"] 
                
                # Asking the User to categorise the contacts and customising the Wishes accordingly.
                d1={"1":w1,"2":w2,"3":w3}

                
                print("Category 1: Friends and Collegues")
                print("Category 2: Family")
                print("Category 3: Seniors")
                print("Enter 1 for Category 1 and so on.")
                a=input(f"{e}: ")
                print("\n")
                
                with open(file_path5,"a",encoding="utf-8") as f2:
                    f2.writelines(d1[a])  
                
        with open("Birth Date","a+",encoding="utf-8") as f:
            f.seek(2) 
            for e in additional_contacts_with_birth_date:
                print(e,file=f)   
                
    else:
        print("Chats of all the contacts which are presented in the contact list have been already exported.")            
                         
                
                
                
                              
# 6) Adding New contacts and their date of birth

def update_contact():
    directory_path=os.getcwd()
    file_path1=os.path.join(directory_path,"Contacts List.txt")
    file_path2=os.path.join(directory_path,"Contacts List With Chats.txt")
    file_path3=os.path.join(directory_path,"Contacts")

    os.rename("Contacts List.txt","Contacts List1.txt")      
    os.rename("Contacts List With Chats.txt","Contacts List With Chats1.txt") 
    os.rename("Birth Date","Birth Date1")

    import contact_list
    
    with open(file_path1,"r",encoding="utf-8") as f1:
        data1=set(f1.read().splitlines())
        
        
    with open("Contacts List1.txt","r",encoding="utf-8") as f2:
        data2=set(f2.read().splitlines())
        
    data3=list(data1.difference(data2)) 
    
    with open(file_path1,"w",encoding="utf-8") as f1:
        for e in data3:
            print(e,file=f1)
    
    
    # Collecting all the zipped chats in the same directory.
    with open("Contacts List.txt","r") as f:
        contact_list=f.read()
        print(contact_list)
    print("End".center(50))     
    print("\n")
    print("Go to whatsapp web.")
    print("Export chats of all the contacts individually to this folder.")
    input("Press Enter after doing it.")
        
    # Unzipping the chats and creating individual folders for each contacts.
    import file_manager     

    # Reading the chats and obtaining birth dates and Messages.
    import birth_dates

    # Customising messages for each contact. 
    print("Customize ur wishes according to ur wish.".center(50))
    print("Categorize them.".center(50))
    print("\n")

    import customise

    with open("Birth Date","r",encoding="utf-8") as f:
        a1=f.read()
    with open("Birth Date1","a",encoding="utf-8") as f1:
        f1.write(a1)    
    os.remove("Birth Date")
    os.rename("Birth Date1","Birth Date") 
        
        
    with open("Contacts List With Chats.txt","r",encoding="utf-8") as f:
        a1=f.read()
    with open("Contacts List With Chats1.txt","a",encoding="utf-8") as f1:
        f1.write(a1)    
    os.remove("Contacts List With Chats.txt")
    os.rename("Contacts List With Chats1.txt","Contacts List With Chats.txt")    
     
     
    with open("Contacts List.txt","r",encoding="utf-8") as f:
        a1=f.read()
    with open("Contacts List1.txt","a",encoding="utf-8") as f1:
        f1.write(a1)    
    os.remove("Contacts List.txt")
    os.rename("Contacts List1.txt","Contacts List.txt")  
    



          
# 7) Adding New contacts and their date of birth both manually.

def update_contact_manually():
    print("1 Adding name and chat of the contact.")
    print("2 Adding name and birthdate of the contact.")
    print()
    x=int(input("Enter your choice: "))
    directory_path=os.getcwd()
    file_path1=os.path.join(directory_path,"Contacts List.txt")
    file_path2=os.path.join(directory_path,"Contacts List With Chats.txt")
    file_path3=os.path.join(directory_path,"Contacts")
    
    
    
    if x==1:
        
        print("Enter the name of the contact u wish to add.")
        print("Once u are done,enter 0.")
        print()
        
        l1=[]
        while(True):
            a=input("Enter the Name of the contact: ")
            if a=="0":
                break
            
            l1.append(a)
            
        os.rename("Contacts List.txt","Contacts List1.txt")      
        os.rename("Contacts List With Chats.txt","Contacts List With Chats1.txt") 
        os.rename("Birth Date","Birth Date1")    
            
        with open("Contacts List.txt","w",encoding="utf-8") as f:
            for e in l1:
                print(e,file=f)
        
        with open("Contacts List.txt","r",encoding="utf-8") as f:
            contact_list=f.read()
            print(contact_list)
        print("End".center(50))     
        print("\n")
        print("Go to whatsapp web.")
        print("Export chats of all the contacts individually to this folder.")
        input("Press Enter after doing it.")
            
        # Unzipping the chats and creating individual folders for each contacts.
        import file_manager     

        # Reading the chats and obtaining birth dates and Messages.
        import birth_dates

        # Customising messages for each contact. 
        print("Customize ur wishes according to ur wish.".center(50))
        print("Categorize them.".center(50))
        print("\n")

        import customise    
            
            
        with open("Birth Date","r",encoding="utf-8") as f:
            a1=f.read()
        with open("Birth Date1","a",encoding="utf-8") as f1:
            f1.write(a1)    
        os.remove("Birth Date")
        os.rename("Birth Date1","Birth Date") 
        
        
        with open("Contacts List With Chats.txt","r",encoding="utf-8") as f:
            a1=f.read()
        with open("Contacts List With Chats1.txt","a",encoding="utf-8") as f1:
            f1.write(a1)    
        os.remove("Contacts List With Chats.txt")
        os.rename("Contacts List With Chats1.txt","Contacts List With Chats.txt")    
     
     
        with open("Contacts List.txt","r",encoding="utf-8") as f:
            a1=f.read()
        with open("Contacts List1.txt","a",encoding="utf-8") as f1:
            f1.write(a1)    
        os.remove("Contacts List.txt")
        os.rename("Contacts List1.txt","Contacts List.txt")  
     
     
                
    elif x==2:
        
        print("Enter the name of the contact u wish to add.")
        print("Once u are done,entrer 0.")
        print()
        
        l1=[]
        while(True):
            a=input("Enter the Name of the contact: ")
            if a=="0":
                break
            
            l1.append(a)
        
        with open("Contacts List.txt","a",encoding="utf-8") as f:
            for e in l1:
                print(e,file=f)

        
        additional_contacts_with_birth_date=[]
        for e in l1:
            print(f"Input the Birthdate of {e}")   
        
            date=input("Enter the date in two digits: ")
            month=input("Enter the month in two digits: ")
            print()
            
            year=time.strftime("%Y")
            data_to_be_added=f"{e}:{date}/{month}/{year[2:]}"
            
            additional_contacts_with_birth_date.append(data_to_be_added)
            
        with open("Contacts List Without Chats.txt","a+",encoding="utf-8") as f:
            f.seek(2) 
            for e in l1:
                print(e,file=f)
                file_path4=os.path.join(file_path3,e)
                file_path5=os.path.join(file_path4,"Wishes.txt")
                os.makedirs(file_path4,exist_ok=True) 
                
                # Various options to wish happy Birthday.
                w1=["Happy Birthday\n","Happy Birthday Bro\n","Happy Birthday Buddy 🙌🥳\n"]
                w2=["Happy Birthday\n","Happy Birthday my dear\n","Happy Birthday ❤️\n"] 
                w3=["Happy Birthday Sir\n","Happy Birthday dear Sir\n","Happy Birthday 🙏\n"] 
                
                # Asking the User to categorise the contacts and customising the Wishes accordingly.
                d1={"1":w1,"2":w2,"3":w3}

                
                print("Category 1: Friends and Collegues")
                print("Category 2: Family")
                print("Category 3: Seniors")
                print("Enter 1 for Category 1 and so on.")
                a=input(f"{e}: ")
                print("\n")
                
                with open(file_path5,"a",encoding="utf-8") as f2:
                    f2.writelines(d1[a])  
                
        with open("Birth Date","a+",encoding="utf-8") as f:
            f.seek(2) 
            for e in additional_contacts_with_birth_date:
                print(e,file=f)   
                 
         
        
    else:
        
        print("Invalid input.")
        exit()   
            
    
        


# 8) Rectifying Contact Names
def correcting_name():
    directory_path=os.getcwd()
    file_path1=os.path.join(directory_path,"Contacts List.txt")
    file_path2=os.path.join(directory_path,"Contacts List With Chats.txt")
    file_path3=os.path.join(directory_path,"Contacts List Without Chats.txt")
    file_path4=os.path.join(directory_path,"Birth Date")
    file_path5=os.path.join(directory_path,"Contacts")
    
    with open("Birth Date","r",encoding="utf-8") as f: 
        data_raw=f.read().splitlines()
        data=[]
        
        for e in data_raw:
            k=e.split(":")[0]
            data.append(k)
        
    for idx,e in enumerate(data,start=1):
        print(f"{idx}: {e}")
        
    print()    
    print("Choose the contact name u wish to change.")    
    print("Enter 0 when u are done.")
    print()
    
    d1={}
    while(True):
        a=int(input("Enter your  response: "))
        
        if a==0:
            break
        
        old_name=data[a-1]
        print("Old Name of the Contact:",old_name)
        new_name=input("Enter the correct name: ")
        print("New Name of the Contact:",new_name)
        d1[old_name]=new_name
        file_path=os.path.join(file_path5,old_name)
        file_path_new=os.path.join(file_path5,new_name)
        if os.path.exists(file_path):
            file_path_x=os.path.join(file_path,f"WhatsApp Chat with {old_name}.txt")
            if os.path.exists(file_path_x):
                os.remove(file_path_x)
                
            os.rename(file_path,file_path_new)    
                
    with open(file_path4,"r",encoding="utf-8") as f: 
        data1=f.read()

    for key in d1.keys():
        dat1=data1.replace(key,d1[key])
        
    with open(file_path4,"w",encoding="utf-8") as f: 
        f.write(dat1)    



    with open(file_path2,"r",encoding="utf-8") as f: 
        data1=f.read()

    for key in d1.keys():
        dat1=data1.replace(key,d1[key])
        
    with open(file_path2,"w",encoding="utf-8") as f: 
        f.write(dat1)    



    with open(file_path1,"r",encoding="utf-8") as f: 
        data1=f.read()

    for key in d1.keys():
        dat1=data1.replace(key,d1[key])
        
    with open(file_path1,"w",encoding="utf-8") as f: 
        f.write(dat1)    

    if os.path.exists(file_path3):
        with open(file_path3,"r",encoding="utf-8") as f: 
            data1=f.read()

        for key in d1.keys():
            dat1=data1.replace(key,d1[key])
            
        with open(file_path3,"w",encoding="utf-8") as f: 
            f.write(dat1)          
         