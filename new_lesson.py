# print('Welcome to AskPython Quiz')
# answer=input('Are you ready to play the Quiz ? (yes/no) :')
# score=0
# total_questions=3
 
# if answer.lower()=='yes':
#     answer=input('Question 1: What is your Favourite programming language?')
#     if answer.lower()=='python':
#         score += 1
#         print('correct')
#     else:
#         print('Wrong Answer :(')
 
 
#     answer=input('Question 2: Do you follow any author on AskPython? ')
#     if answer.lower()=='yes':
#         score += 1
#         print('correct')
#     else:
#         print('Wrong Answer :(')
 
#     answer=input('Question 3: What is the name of your favourite website for learning Python?')
#     if answer.lower()=='askpython':
#         score += 1
#         print('correct')
#     else:
#         print('Wrong Answer :(')
 
# print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
# mark=(score/total_questions)*100
# print('Marks obtained:',mark)
# print('BYE!')

# squares = {i: i * i for i in range(10)}
# print(squares)

# squares ={i: i*i for i in range(10) if i % 2!= 0 }
# print(squares)

# values = ["a", "b", "c"]

# for count, value in enumerate(values, start=1):
#     print(count, value)

# def even_items(numbers: list):
#     return [v for i, v in enumerate(numbers, start=1) if not i % 2 == 0] 

#        -//-

# def even_itmes(numbers: list):
#     new_list = []
#     for i,v in enumerate(numbers, start=1):
#         if not i % 2:
#             new_list.append(v)
#     return new_list
# seq = list(range(10, 31))

# print(even_itmes(seq))

# seq = list(range(15, 21))

# print(even_items(seq))   

# def even_items(numbers: list):
#     return [v for i, v in enumerate(numbers, start=1) if i % 2 == 0]

# seq = list(range(15, 21))

# print(even_items(seq))   #parasyti paprastesniu budu nd

# import math #visokius matematinius veiksmus galima daryti
# print(math.factorial(7))

#1 Find all of the numbers from 1-1000 that are divisible by 6.

# div6 = [n for n in range(1,1000) if n % 6 == 0] 
# print(div6)

#2 Find all number from 1-1000 that have 9 in them.

# nine = [n for n in range(0,1000) if '9' in str(n)]
# print(nine)

#3
# text = 'In this lecture we will review some additional functionalities of python built-in data structures.'
# new_text = text.split()
# print([word for word in new_text if "e" in word])


#                          -//-

# for word in new_text:
#     if "e" in word:
#         print(word)



#4
# print(len(word for word in new_text if len(word) > 5))

#5 Given the same string calculate the occurrence of each letter in the string. (HINT: store everything in dictionary)



# letter_dict = {}
# text = 'In this lecture we will review some additional functionalities of python built-in data structures.'

# new_text = text.split() #and text.isalpha()
# # just_letters = text.isalpha()

# for word in new_text:
#     for letter in word:
#         if letter.isalpha():
#             if letter in letter_dict:
#                 letter_dict[letter] +=1
#             else:
#                 letter_dict[letter] = 1
        
        
# # print(new_text)

# # print(dict(sorted(letter_dict.items)))
# print(letter_dict)
# print(type(new_text))

#6

