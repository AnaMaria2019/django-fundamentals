This project was created using Pycharm:

- Step 1: Create project
- Step 2: Complete the 'Location' field with the location where you want to create the project
- Step 3: Select in the 'Project Interpreter:New Virtualenv environment' field the 'New environment using Virtualenv'
- Step 4: Add the path, from your computer, to the Python interpreter in the 'Base interpreter' field
- Step 5: Click 'Create'

This project uses the following versions:
- Pycharm Community 2020.1
- Python 3.6
- django 2.2.8

After creating the Pycharm project, to create a Django project follow these steps:

- Step 1: Make sure that when you open 'Terminal' from Pycharm you have the venv activated (if you don't type the following command: 'venv\Scripts\avtivate' and press Enter). If the venv is activated it will appear like this '(venv)' in the front of the line (Example: '(venv) D:\1_Ana\3_Info\13_Learn\1_Python\2_PluralSight\DjangoCourse_2\tictactoe>')
- Step 2: Make sure that the Python interpreter is your local venv. To check this go to 'File' -> 'Settings' -> 'Project: <name_of_the_project>'-> 'Python Interpreter' and here select your venv if it's not selected already.
- Step 3: Go to 'Terminal' and type 'django-admin startproject <name>' (this will create a Django project within the Pycharm Project)