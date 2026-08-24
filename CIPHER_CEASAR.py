logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
#asci art 
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']  # 26 letters in the alphabet


def caesar(original_text, shift_amount, encode_or_decode):  # defining cipher based on rules of Cesarean ciphers
    output_text = ""  # placeholder for the ciphered result
    if encode_or_decode == "decode":
        shift_amount *= -1  # condition for DE-ciphering
    for letter in original_text:  # to repeat cipher for each character
        if letter not in alphabet:  # in case of characters not present in the alphabet
            output_text += letter

        shifted_position = alphabet.index(letter) + shift_amount  # new index after ciphering
        shifted_position %= len(alphabet)  # to limit index position within the alphabet
        output_text += alphabet[shifted_position]  # updating output after ciphering
    print(f"Here is the {encode_or_decode}d result: {output_text}")  # printing output


output = "yes"  # initializing condition for while loop
while output == "yes":  # to continue ciphering without restarting the program each time
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()  # to determine whether to encode or decode
    text = input("Type your message:\n").lower()  # the text to be decoded taken in from user
    shift = int(input("Type the shift number:\n"))  # the "key" to a cesarean Cipher

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)  # calling the defined function
    output = input("do you want to go again?(yes/no):\n").lower()  # updating condition for while loop from user
print("thank you for using this program")  # generic thank you message
