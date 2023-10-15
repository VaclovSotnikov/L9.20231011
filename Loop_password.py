
# Create a program witch takes 5 different (minmum)  variables containing strings for username and password.
# The string should look like : "username='', password=''; username='',password='';....etc"
# Start Endless loop allowing to enter username and password and 
# check if credentials are correct stop endless loop and print greeting message, otherwise print 'wrong credentials' and ask to enter password and username again. 
# The program should show numbers of times you tried to enter both credentials.

# credentials = ("username='juozas007', password='hello11111'; username='gerlix', password='gggg!4'; username='matrix999', password='neoliks'; username='traukinys', password='garvezis'; username='BX500', password='History'")
# username= input("Enter your username: ")
# password= input("Enter your password: ") 

# split_list = credentials.split("; ")
# my_dict ={}
# my_dict = split_list

# while True:
#     if username in my_dict:
#         if password in my_dict:
#             print(f'Greetings, {username}')
#         break    
#     else:
#         print(f'Try another username or password')


credentials = ("username='juozas007', password='hello11111'; username='gerlix', password='gggg!4'; username='matrix999', password='neoliks'; username='traukinys', password='garvezis'; username='BX500', password='History'")
print('Enter correct username and password combo to continue')
count=1
while True:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if password=='Hytu76E' and username=='bank_admin':
        print('Access granted')
        break
    else:
        print('Access denied. Try again.')
        count += 1