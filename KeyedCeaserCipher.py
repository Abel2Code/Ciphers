print('Greetings User!\n'
      'This program will encrypt your input. To decrypt it, you must remember the password.\n'
      'This program creates a keyed caesar cipher.\n')

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']
cipher = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']
#We cannot do cipher = alphabet. That does not create a deep copy

password = input('Enter the password for the cipher\n').lower()

tempPassword = ''
#This loop removes any duplicate letters in your password
for letter in password:
    if letter not in tempPassword:
        tempPassword += letter
password = tempPassword

interval = 0
#This loop creates the cipher
for letter in password:
    if (letter.isalpha()):
        cipher.remove(letter)
        cipher.insert(interval,letter)
        interval += 1

validInput = False
while not validInput:
    options = input('\n'
                    'To encrypt a message, type ENCRYPT.\n'
                    'To decrypt a message, type DECRYPT\n').lower()
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