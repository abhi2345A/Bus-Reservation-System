# Bus-Reservation-System

It's a **Django framework** based web developement project. It allows users to book bus tickets which are open.<br/>

### Features
```
* Admin - Login . . . Allows admin to login
* Admin - Reset Tickets . . . Allows admin to reset all the tickets to open
* Admin - Check passengers,seats . . . Allows admin to check passenger and seats details
* User - Register . . . Allows user to register 
* User - Login . . . Allows user to login
* User - Add Details ( passenger ) . . . Allows user to add its details as a passenger 
* User - Update Details ( passenger ) . . . Allows user to update its details as a passenger
* User - Check Seat Layout . . . Allows user to check bus seat layout i.e. window, inner and booked seats
* User - Select Seat . . . Allows user to select a seat. If the seat ticket is closed show alert !
* User - Check Open Tickets . . . Allows user to check open seat tickets
* User - Check Closed Tickets . . . Allows user to check closed seat tickets
```
### Built With
```
* Frontend - HTML / CSS / JavaScript
* Backend -  Django Framework (Python) / SQLite 
* Testing  - Selenium / Chromedriver
```
### Deployed Using
 Server is configured on my system , so i need to host before you can access the project on http://52.73.20.196
```
* AWS EC2 Instance
```
### Steps to run on the local server
```
* Install Python and set path
* Install pip
```
Install **Virtual environment**
```
* sudo apt install virtualenv OR
* pip install virtualenv
```
Create a **Virtual Environment**
```
virtualenv venv
```
Move to venv and **activate virtual environment**
```
cd venv/Scripts
& .\activate
```
**Clone the project** inside venv folder
```
git clone https://github.com/abhi2345A/Bus-Reservation-System.git
cd Bus-Reservation-System
```
Install the project **Requirements**
```
pip install -r requirements.txt
```
Apply **migrations** for the database and **migrate** changes
```
python manage.py makemigrations selection
python manage.py migrate
```
Launch the **localserver**
```
python manage.py runserver
```
Go to browser and on **127.0.0.1:8000/**   home page of project will appear
</br>
![Alt text](Screenshots/home.png?raw=true "home")
</br>
passenger's screen after login and entering details

![Alt text](Screenshots/select.png?raw=true "select")


 Click on **Status** to see the seat layout like this 
 </br>
 ![Alt text](Screenshots/layout1.png?raw=true "layout")
 
 ### Create superuser ( Admin )
 Inside **Terminal** type - 
 ```
 python manage.py createsuperuser
 ```
 and provide
 ```
 * Username
 * Email
 * Password
 * Confirm- Password
 ```
 Already created **Admin** credentials for project
 ```
 username -abhi
 password -jeet
 ```
 
 ### Testing
 
 To execute **unit tests** ( selection/tests )
 
 ```
 python manage.py test selection
 ```
 
 To execute **functional tests** ( functional_tests )
 ```
 python manage.py test functional_tests
 ```
 
 
