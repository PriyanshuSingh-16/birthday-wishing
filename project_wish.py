def permanent():
    # 1) Creating Contact list
    import contact_list

    # 2) Collecting all the zipped chats in the same directory.
    with open("Contacts List.txt","r",encoding="utf-8") as f:
        contact_list=f.read()
        print(contact_list)
    print("End".center(50))     
    print("\n")
    print("Go to whatsapp web.")
    print("Export chats of all the contacts individually to this folder.")
    input("Press Enter after doing it.")
        
    # 3) Unzipping the chats and creating individual folders for each contacts.
    import file_manager     

    # 4) Reading the chats and obtaining birth dates and Messages.
    import birth_dates

    # 5) Customising messages for each contact. 
    print("Customize ur wishes according to ur wish.".center(50))
    print("Categorize them.".center(50))
    print("\n")

    import customise

def temporary():
    # 1) Arranging the Birth dates according to months.
    # 2) Wishing Happy Birthday.
    import wish


