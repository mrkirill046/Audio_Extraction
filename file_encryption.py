# Imports
import pyAesCrypt

# Variables
password = input("Enter password: ")

# Code encrypt
pyAesCrypt.encryptFile('token.txt', 'bot.token', password)

# Code decrypt
pyAesCrypt.decryptFile('bot.token', 'really_token.txt', password)
