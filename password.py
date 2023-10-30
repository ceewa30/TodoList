import re

password = input("Enter new password : ")

result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for dig in password:
    if dig.isdigit():
        digit = True

result["digits"] = digit

uppercase = False
for upper in password:
    if upper.isupper():
        uppercase = True

result["uppercase"] = uppercase


special_char = False
regexp = re.compile('[^0-9a-zA-Z]+')
if regexp.search(password):
    special_char = True

# specialchar = False
# # special_char = re.compile('!@#$%^&*()~:;{[}]|\?/<,>.}')

# for special in password:
#     special_char=re.compile('[@_!$%^&*()<>?/\|}{~:]#')
#     # print(special)
#     if special_char.search(special) == None:
#        print("string is accepted")
#     else:
#         print(special)
    
    # if special_char.search(special) == True:
    #     specialchar = True

print(special_char)

result["special_char"] = special_char

print(result)
print(all(result))

if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password")



# using function

def strength(password):
    result = {}
    
    if len(password) > 8:
        result["length"] = True
    else:
        result["length"] = False
    
    digit = False
    uppercase = False
    
    for i in password:
        if i.isdigit():
            digit = True
            
        if i.isupper():
            uppercase = True
    
    result["digit"] = digit
    
    result["uppercase"] = uppercase
    
    if all(result.values()):
        return "Strong Password"
    else:
        return "Weak Password"
    
password = input("Enter the password: ")

result = strength(password)
print(result)


  