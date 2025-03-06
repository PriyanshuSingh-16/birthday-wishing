# 1)# 1) Importing the necessary modules
import os

# 2) Obtaining the necessary path.
directory_file_path=os.getcwd()
contact_list_with_birthdate_path=os.path.join(directory_file_path,"Birth Date")


# 3) Function which organises the data properly.
def organise_data(path):
    def storing_the_data(path):
        
        with open(path,"r",encoding="utf-8") as f:
            complete_data=f.read()

        data_in_list=complete_data.split("\n")
        data_in_list=list(set(data_in_list))
        data_in_list.remove("") 
         
        
        return data_in_list


    def arranging_the_data_1(list_of_infos):
        arranged_list=[]
        
        for e in list_of_infos:
            x=e.split(":")
            y=x[1].split("/")
            y.pop(2)
            y.append(x[0])
            
            i=0
            while(i<2):
                y[i]=int(y[i])
                i=i+1
            temp=y[0]    
            y[0]=y[1]
            y[1]=temp
            
            arranged_list.append(y)
            arranged_list.sort()
            
        return(arranged_list)


    def  arranging_the_data_2(data_1):   
        data_2={}
        
        for i in range(1,13):
            data_2[i]=[e for e in data_1 if e[0]==i]
            
            
        return (data_2)
    
    
    def arranging_the_data_3(data_2):
        data_3={}
        datas1=list(data_2.keys())
        datas2=list(data_2.values())
        
        for key,value in zip(datas1,datas2) :
            d1={}
            
            for e in value:
                key1=e[1]
                e.pop(1)
                if (key1 in d1.keys()):
                    d1[key1].append(str(e[1]))
                else:
                    d1[key1]=[(e[1])]
                
                
            data_3[key]=d1    
            
        return data_3        
        
    
    #1) Data is stored in a list and all the duplicate data is removed. 
    list_of_infos=list(storing_the_data(path))

    #2) We would store the data in the form of list with each individual elements seperated. 
    #   Sorting the data on the basis of month,date,year and finally name.
    data_1=arranging_the_data_1(list_of_infos)

    #3) We would form a dictionary based on month
    #   The dictionary is made in such a way that it stores the information of each month
    data_2=arranging_the_data_2(data_1)

    #4) The dictionary is formed with each month as key and a list as value which contains key value pair of name and date of birth 
    data_3=arranging_the_data_3(data_2)
    return data_3



# 4) Calling the function to organiise the data.
organised_data=organise_data(contact_list_with_birthdate_path)



# 5) Creating a function to be called from another module.
def get_data():
    return organised_data




