# Caesar Cypher

import pyperclip

#The string to be encrypted
#print ('Please enter the message: ')
#message = input()
message = 'fVDaOPZDPZDHTHgPUNDKVVN'

# The encryption key
key = 7

#Wheter the program encrypts or decrypts:
mode = 'decrypt' # Set to either 'encrypt' or 'decrypt'

#Every possible symbol 
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

#Store the encrypted message 
translated = ''

for symbol in message:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        #Perform encryption/decryption of message
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key

        #Handle wraparound
        if translatedIndex >= len(SYMBOLS):
            translatedIndex -= len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex += len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]
    else:
        # Append the symbol without encrypting/decrypting
        translated = translated + symbol

#Output the translated string:
print(translated)
pyperclip.copy(translated)
