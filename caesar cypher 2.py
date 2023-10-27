# d e f g h i j k l m n o p q r s t u v w x y z a b c d

# DWKORQH FRPPXQWB FROOJH
# ATHLONE COMMUNTY COLLGE

# 25 possible keys

# What do you get when you cross a snowman with a vampire? Frostbite


message = input("Enter your message: ")
key = int(input("Enter the key number: "))
mode_type = input("Enter 'encode' or 'decode': ")
encode=""
Letters = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for letter in message:
    if letter.upper() in Letters:
        number = Letters.find(letter.upper())
        if mode_type== 'encode':
            number = number + key
            encode=encode + Letters[number]
        elif mode_type == 'decode':
                number= number - key
print(encode)