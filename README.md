# Basic Password Generator in Kivy 
A basic application in kivy to generate a random password consisting of a keyword given by the user

Simple-Password-Generator provides the user with two functionalities 

	1. Generate 
	2. Retrieve 

In the generate mode a password is generated for the user on the basis length and a specific keyword provided by the user. 
The password will contain Upper case characters,Lower case characters, digits and special character ('_','-').
Along with the password, the user can enter his username which will be used to retrieve the password. 

The password is encrypted and stored in a sqlite databse and copied on the clipboard for the user's use. 

In the Retrieve mode the user enters the username he used to save the password. The password is then decrypted and copied onto the clip board.
