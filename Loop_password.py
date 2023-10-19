# The program should show numbers of times you tried to enter both credentials.
#For storing account information use dict , all data should be lowercase and extra symbols (@, %, $ etc and numbers). 
#If in password numbers or symbols are not provided, the program should add additional value to dictionary as a value, names 'improved password'
# Create a program witch takes 5 different (minmum)  variables containing strings for username and password.
# The string should look like : "username='', password=''; username='',password='';....etc"
# Start Endless loop allowing to enter username and password and 
# check if credentials are correct stop endless loop and print greeting message, otherwise print 'wrong credentials' and ask to enter password and username again. 


credentials = input("username='juozas007', password='hello11111'; username='gerlix', password='gggg!4'; username='matrix999', password='neoliks'; username='traukinys', password='garvezis'; username='BX500', password='History'")
username= input("Enter your username: ")
password= input("Enter your password: ") 

split_list = credentials.split("; ")
my_dict ={}
my_dict = split_list

while True:
    if username in my_dict:
        if password in my_dict:
            print(f'Greetings, {username}')
        break    
    else:
        print(f'Try another username or password')