# bank-security-room

This is an internal repository for Sunshine Bank employees. If you've found this repository by accident, you won't be able to run it as you don't have access to the DB. But you can use the code freely.

Security room is a site that could be connected to the remote database with visit history and passcard holders info.

### How to install

Please contact your manager and request access to the DB. To access the DB you will require host, port, DB name, username and a password. Create a file called `.env` in the project directory. Paste the data in the file:
```
DB_HOST = 'your db host'
DB_PORT = 'your db port'
DB_NAME = 'your db name'
DB_USER = 'username'
DB_PASSWORD = 'password'

```
Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
