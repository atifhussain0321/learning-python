import random

# Password Generator
print("Welcome to Password Generator,")

len = int(input("What will be the Lenght of Password: "))
char = input("Can use Special Characters[True/False]: ")
special_char = True

# Verifying Details
if char == "True" or char == "T":
    special_char = True
elif char == "False" or char == "F":
    special_char = False
else:
    print("You Entered Wrong Value!!")

# Start Processing
sp_chr = "!@#$%^&*()_+={[}]:;?/>.<}"
chr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
total_chr = sp_chr + chr
num = random.randint(1, 100)

def generate():
    password = 0
    if special_char == True:
        for i in range(len):

# Due to SOME MIND ERROR I'M UNABLE TO COMPLETE THIS CODE SORRY

