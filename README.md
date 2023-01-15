# Write Encode
Translates any word or phrase into multiple different styles. Such styles include Binary and Morse code. Capstone group project for Justice Through Code

# Group Members
Ahmad Bright 
ajbright213
Talesa Howell 
talesa365
Jessica Lotto 
jlotto8
Bryan M. Wolf
bmwolf102990

# 1. Create a virtual environment
At the root folder of the repository run:
```
python3 -m venv venv
```
Make sure to call your virtual environment "venv"

# 2. Run virtual environment
## On Windows:
Windows Powershell users:
```
venv\Scripts\activate.bat
```
Bash users:
```
source venv/Scripts/activate
```
## On Unix or MacOS:
```
source venv/bin/activate
```
# 3. Install dependencies

pip install django

pip freeze install
```
pip install -r requirements.txt
```
# 4. Run django
cd into the nyc-guide directory
run the command: python manage.py runserver
And go to `http://localhost:8000`

# To stop running the server/application

# To exit the virtual environment
run the command: deactivate

# The following are used in this project:

Python data structures such as dictionaries and their associated methods
Python Classes and Inheritance
Django URLs to understand how to capture parameters in views
Django Templates
HTML
CSS

# Features

Home page that reveals an input and output field, with two buttons- for the user to choose to translate their input into either Morse or binary code.
<img width="1440" alt="Screenshot 2023-01-12 at 6 09 04 PM" src="https://user-images.githubusercontent.com/111258836/212209490-d83b36e4-dd05-43e9-a584-58665d219448.png">

## Translate to Morse code

Text from the input field translated into binary code
<img width="1440" alt="Screenshot 2023-01-12 at 7 25 59 PM" src="https://user-images.githubusercontent.com/111258836/212209187-3f891fe0-0aad-474f-8bed-46513bd823be.png">

## Translate to binary code

Text from the input field translated into Morse code
<img width="1440" alt="Screenshot 2023-01-12 at 7 56 27 PM" src="https://user-images.githubusercontent.com/111258836/212212558-74e5e210-073d-4d5a-b783-c26b53118096.png">

## History page

History page will reveal the last translations of the session
<img width="1440" alt="Screenshot 2023-01-15 at 11 13 55 AM" src="https://user-images.githubusercontent.com/111258836/212553718-c43f2880-a53e-4162-82ea-d5b548a0c109.png">
