from datetime import datetime


current = datetime.now()

#print("current time :" , current)


code = int(input("Enter 4-digit code: "))

code_str = str(code)
hour = str(current.hour)
min = str(current.minute)


# print(code_str[:2])
# print(code_str[2:])

# print(current.hour)
# print(current.minute)


try:
    if(hour == code_str[:2] and min == code_str[2:]):
        print("Acess Granted.......")

    else:  
        print("Aecess Denied...!")

except:
    print("error ocurres..")



