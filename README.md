# Password-Generator
print("Welcome to password generator")
import random
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()<>?/{}[]:;"
password_length = int(input("What lenght would you like your password to be? "))
password = ""
for x in range(0,password_length):
    password_char = random.choice(chars)
    password = password + password_char
print ("Here is your password : ", password)
choice=input("If you wanna save your password say y or Y: ")
if ((choice=='y') or (choice=='Y')):
    a=input("Enter use of the password?")
    f = open('f:\\PASSWORD.txt', 'w+')
    f.write(password)
    f.close()
b=input("If you wanna see saved password say y or Y: ")
if ((b=='y') or (b=='Y')):
    f=open('f:\\PASSWORD.txt','r')
    print(f.read())
else:
    print ("ok")
