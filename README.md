# ldapAccounts

Project dedicated for a TEST

This project consists in you add a CSV file with (Name, Surname and Email) and with the application it will be created in OpenLdap with a Random password

This application consists in an app to populate a OpenLdap Database with a csv file and send a notification to the user who was add in the DB, also populates a MySQL database with the uid (openLDAP), name, last_name and the password in MD5.

Follow the steps to use the application:

1 - Just rename the file config.py.sample to config.py
2 - After this, add the variables values in the config.py (Values of LDAP to login, csv file path, database credentials etc).
3 - Execute python main.py to use the application

Enjoy it :)
