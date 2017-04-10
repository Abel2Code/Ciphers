print('Greetings User!\n'
      'This program will encrypt your input. To decrypt it, you must remember the password.\n'
      'This program creates a caesar cipher.\n')

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']
cipher = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']
#We cannot do cipher = alphabet. That does not create a deep copy

isValidPassword = False
while not isValidPassword:
    password = input('Input a number. Remember this password to decrypt your message later.\n')
    if password.strip().isnumeric():
        # isnumeric() is a boolean method that checks whether a String is a number
        # strip() removes spaces at beginning and end of string
        isValidPassword = True

interval = 0
#This loop creates the cipher
for i in range(int(password)):
    cipher.insert(0, cipher[len(cipher)-1]) # inserts last character of string to the front of the array
    cipher.pop() # removes last character in array

validInput = False
while not validInput:
    options = input('\n'
                    'To encrypt a message, type ENCRYPT.\n'
                    'To decrypt a message, type DECRYPT\n').strip().lower()
    if options == 'encrypt' or options == 'decrypt':
        validInput = True
    else:
        print('ERROR: PLEASE TRY AGAIN')

message = input('\nInput the text you would like to ' + options + ':\n')

newMessage = ''
if options == 'encrypt':
    print('Encrypting...\n')
    for letter in message:
        if letter.islower():
            newMessage += cipher[alphabet.index(letter)].lower()
        elif letter.isupper():
            newMessage += cipher[alphabet.index(letter.lower())].upper()
        else:
            newMessage += letter
    print('Here is your encrypted message:\n' + newMessage)

elif options == 'decrypt':
    print('Decrypting...\n')
    for letter in message:
        if letter.islower():
            newMessage += alphabet[cipher.index(letter)].lower()
        elif letter.isupper():
            newMessage += alphabet[cipher.index(letter.lower())].upper()
        else:
            newMessage += letter
    print('Here is your decrypted message:\n' + newMessage)

else:
    print('ERROR: UNKNOWN VALUE.\n'
          'Exiting Program')