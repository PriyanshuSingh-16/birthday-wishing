import os

directory_path=os.getcwd()
file_path1=os.path.join(directory_path,"Birth Date")
file_path2=os.path.join(directory_path,"Contacts")

l1=[]



def custom_wish(l):
    for idx,e in enumerate(l,start=1):
        print(f"{idx}: {e}")
    print()
        
    l_modified=[]    
    print("Enter 0 if u want to remove the message.")
    print("Enter 1 if u want to replace the message.")
    print("Enter 2 if u want to keep the message as it is.")
    
    for e in l:
        print()
        print(e)
        print()
        k1=int(input("Enter ur response: "))
        if k1==1:
            q1=input("Enter the wish: ")
            l_modified.append(q1)
        elif k1==2:
            l_modified.append(e)
     
    print()    
    print("Write additional wishes which u would like to add.")
    print("Once done enter 0.")
    print()
    
    while(True):
        q2=input("Enter the wish: ")
        print()
        if q2=="0":
            break
        l_modified.append(q2)
    
    
    return l_modified    
       



with open(file_path1,"r",encoding="utf-8") as f: 
    data=f.read().splitlines()
    
for e in data:
    a=e.split(":")[0]
    l1.append(a)

for idx,e in enumerate(l1,start=1):
    print(f"{idx}: {e}")



print()
print("Enter the index of the contact whose wishes have to be customised.")
print("Enter 0 when done.")
print()


while(True):
    x=int(input("Enter the index: "))
    if x==0:
        break
    file_path3=os.path.join(file_path2,rf"{l1[x-1]}\Wishes.txt")
    
    with open(file_path3,"r",encoding="utf-8") as f: 
        data1=f.read().splitlines()
        
        data2=custom_wish(data1)
        
    with open(file_path3,"w",encoding="utf-8") as f:
        for e in data2:
            print(e,file=f) 
    print()        