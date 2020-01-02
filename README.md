# polyglot-python
flask API to check two sided prime number-
An number is a Two-sided Prime if 
1.	The number is itself a prime number. 
e.g. 3797
2.	Removing 1 digit at a time from left hand side from the original number gives you prime numbers. 
e.g. 797, 97, 7 are all prime numbers.
3.	Removing 1 digit at a time from right hand side from the original number gives you prime numbers. 
e.g. 379, 37, 3 are all prime numbers.

# installation and setup
Using command line run below-
1. python -m pip install -r requirements.txt
2. cd flask-app
3. api.py

Application will start running on http://127.0.0.1:5000/

# how to run api
Go to browser and hit below links -

http://127.0.0.1:5000/api - Welcome to Flask API demo : Two sided prime number.
http://127.0.0.1:5000/api/33 - 33 is a number that needs to be checked. Give response {"33 is two sided prime? ":"false"}
