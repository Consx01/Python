
def encrypt_text(plain_text,shift_value):
    cipher_value = ""
    for char in plain_text:
        if char.isalpha():
            ascii_value= 65 if char.isupper() else 97
            character_code = (ord(char)-ascii_value)
            key = (character_code+shift_value)%26
            encrypt_char = chr(key+ascii_value)
            cipher_value += encrypt_char
        else:
            cipher_value += char
    return cipher_value

def decrypt_text(cipher_text,shift_value):
    plain_text = ""
    for char in cipher_text:
        if char.isalpha():
            ascii_value= 65 if char.isupper() else 97
            character_code = (ord(char)-ascii_value)
            key = (character_code-shift_value)%26
            decrypt_char = chr(key+ascii_value)
            plain_text += decrypt_char
        else:
            plain_text += char
    return plain_text

def input_text():
    print("\n********Caesar Cipher Program********")
    print("| Press [1] to Encrypt")
    print("| Press [2] to Decrypt")
    print("| Press [3] to Quit")
    print("|************************************")
    choice = int(input(("| Enter choice      : ")))
    print("|------------------------------------")
    return choice


cipher_text1 = ""           
while 4==4 :
    choice = input_text()
    if choice == 1:
        plain_text = input("| Enter plain text  : ")
        shift_value = int(input("| Enter shift value : "))
        if shift_value <= 26:
            cipher_text1 = encrypt_text(plain_text,shift_value)
            print("| Cipher text       :",cipher_text1)
        else:
            print("| Invalid shift value\n| Please enter shift value within 27.")
            break             
    elif choice == 2:
        if cipher_text1=="":
            print("| No message to decrypt.")
            print("| Please choose 1 to encrypt first."\n")  
        else:
            print("| Cipher text :",cipher_text1)
            print("| Plain text  :",decrypt_text(cipher_text1,shift_value),"\n")
    elif choice == 3:
        quit()
    else :
        print("| Sorry! Wrong choice\n| Please enter valid number\n\n")
        
        
