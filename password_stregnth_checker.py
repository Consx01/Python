def password_streangth_check(password): 
    #Defined criteria for the password 
    length = len(password) >= 8
    uppercase_letter = any(char.isupper() for char in password)
    lowercase_letter = any(char.islower() for char in password)
    digits = any(char.isdigit() for char in password)
    special_char = any(char in '!@#$%^&*_-<>~`' for char in password)
    
    if length and uppercase_letter and lowercase_letter and digits and special_char:
        return "Strong Password"
    elif length and (uppercase_letter or lowercase_letter) and digits:
        return "Moderate Password"
    elif length and uppercase_letter and lowercase_letter and (digits or special_char):
        return "Moderate Password"
    else:
        return "Weak Password"

#Main program  
print("\n--------------Password Checker----------------")
password = input("| Enter Password    : ")
pass_streangth = password_streangth_check(password)
print("| Password Strength :",pass_streangth)
print("---------------------------------------------")
