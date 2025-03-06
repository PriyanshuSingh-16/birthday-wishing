# 1) Importing the necessary file.
import reset_options as ro

# 2) Creating a function for importinf the correct function.
def func(n):
    if(n==1):
        ro.complete_reset()
    elif(n==2):
        ro.partial_reset()
    elif(n==3):
        ro.birth_date_checking()
    elif(n==4):
        ro.chatless_conatcts()
    elif(n==5): 
        ro.chatless_contacts_manually()
    elif(n==6):
        ro.update_contact() 
    elif(n==7):
        ro.update_contact_manually()     
    elif(n==8):
        ro.correcting_name()    
    elif(n!=0):
        print("Invalid Input")             
   

# 3) Giving choices to the user.

print("Reset".center(100,"."))
print("\n")

list1=["Complete reset","Partial Reset","Rectifying Birth Dates","Exporting chats of already listed contacts", "Manually adding Birthday of already listed contacts","Updating contact list by adding chats","Updating Contact list Manually","Rectifying Contact Names"]
for idx,e in enumerate(list1,1):
    print(f"{idx}: {e}")
    
print()    
print("Choose the option which u wish to use.")
print("Give the input as 0 if u wish to exit.")   
print() 

a=1
while(a):
    a=int(input("Enter your choice: "))
    print()
    func(a)
    print()
    

print("Reset completed.".center(100,"."))

