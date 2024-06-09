print("Welcome to password generator")
import random
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()<>?/{}[]:;"
password_length = int(input("What length would you like your password to be? "))
password = ""
for x in range(0, password_length):
    password_char = random.choice(chars)
    password += password_char
print ("Here is your password: ", password)
choice = input("If you want to save your password, say 'y' or 'Y': ")
if choice.lower() == 'y':
    use = input("Enter use of the password: ")
    file_path = r'D:\UET\books\1ST SEMESTER FALL 2021\i2c\after mids\I2C FINAL PROJECT\Password_Generator\PASSWORD.txt'
    with open(file_path, 'w+') as f:
        f.write(f"Use: {use}\nPassword: {password}")
        print("Password saved successfully.")
b = input("If you want to see saved password, say 'y' or 'Y': ")
if b.lower() == 'y':
    with open(file_path, 'r') as f:
        print(f.read())
else:
    print("Okay")
