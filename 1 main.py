# 1) Importing the necessary modules
import os
import project_wish

directory_path=os.getcwd()
file_path=os.path.join(directory_path,"Birth Date")


# 2) Running the permanent program for a single time.
if not os.path.exists(file_path):
    project_wish.permanent()
    

# 3) Running the wishing my contacts program.
project_wish.temporary()    