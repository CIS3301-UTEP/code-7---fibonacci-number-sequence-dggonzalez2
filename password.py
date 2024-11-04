import re 

password = "UTEP1234%"

if re.findall('"^\S{8,}$"', password):
    print("Your password is Level 0")

elif re.findall('^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', password):
    print("Your password is Level 1")

elif re.findall('^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$',password):
    print("Your password is Level 2")    

elif re.findall('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',password):
    print("Your password is Level 3")
 