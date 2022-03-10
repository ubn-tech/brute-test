import random
from termcolor import colored

def banner(): # banner section
	print(colored("""

 	 db db  
 	C88888D # Password Tester
     88 88  #  		v1
 	C88888D # Developer: Ubn-Tech 
  	 YP YP  Github: https://github.com/ubn-tech/
 
		""", 'yellow'))

banner()

# Main Program

chars = "AaBbCcddeeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789!@#$%^&*()_-+={}[]:;|?/~`±§" #Almost al chars

char_list = list(chars)

password = input(colored("Enter the password you want to test: ", 'red'))

guest_password = ""

while(guest_password != password):
	guest_password = random.choices(char_list, k=len(password))

	print(colored("[Password attempt:]" + str(guest_password)+ "", 'green'))

	if(guest_password == list(password)):
		print("# got the password: "+ "".join(guest_password))
		break