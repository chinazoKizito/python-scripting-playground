import re


while True:
    password = input("please create your password: ")
    if re.fullmatch("^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$", password):
        print('Password created successfully')
        break
    else:
        print('Password must be at least 8 letters long and must contain  uppercase and lower case letters as well as '
              'characters')