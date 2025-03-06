import os
import win32com.client
import getpass

def create_task(script_path):
    try:
        # Connecting to the Task Scheduler service
        scheduler = win32com.client.Dispatch('Schedule.Service')
        scheduler.Connect()

        # Getting the root task folder
        root_folder = scheduler.GetFolder('\\')
        
        # Creating a new task definition
        task_def = scheduler.NewTask(0)
        
        # Creating a trigger that starts the task at startup
        trigger = task_def.Triggers.Create(1)  # 1 = At startup
        
        # Creating an action that runs the Python script
        action = task_def.Actions.Create(0)  # 0 = Start a program
        action.Path = 'python.exe'
        action.Arguments = f'"{script_path}"'
        
        # Setting task parameters
        task_def.RegistrationInfo.Description = 'Run Python script at startup'
        task_def.Settings.Enabled = True
        task_def.Settings.StopIfGoingOnBatteries = False
        task_def.Settings.DisallowStartIfOnBatteries = False

        # Registering the task
        task_name = 'PythonStartupScript'
        username = getpass.getuser()
        root_folder.RegisterTaskDefinition(
            task_name,        # Task name
            task_def,         # Task definition
            6,                # 6 = Create or update
            None,             # User (None = current user)
            None,             # Password (None = current user's password)
            3                 # Logon interactively
        )
    
    except Exception as e:
        print(f"An error occurred: {e}")


directory_path=os.getcwd()
script_path = os.path.join(directory_path,"1 main.py")
create_task(script_path)
