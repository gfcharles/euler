'''
Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code 
for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, 
taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, 
restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. 
The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is 
impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the 
password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. 
The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher1.txt (right 
click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text 
must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.

Created on Nov 10, 2010

@author: Greg Charles
'''
import itertools
import gregutils
import re

'''
 Reads the encrypted message from the file, which is a comma-separated list of encrypted ASCII values.
'''
def readFile():
    f = open(gregutils.dataDir() + 'cipher1.txt', 'r')
    values = map(int, f.read().split(','))
    return values


'''
Decrypts the array of ASCII values representing the cipher text.
Returns the plain text as a string
'''
def decrypt(values, key):
    length = len(key)
    counter = 0
    chars = []
    keyValues = map(ord, key)
   
    for value in values:
        chars.append(chr(value ^ keyValues[counter % length]))
        counter += 1
        
    return ''.join(chars)
  
'''
Basic test to see if the text is probably English. False positive and negatives are possible.
'''      
def isEnglishText(text):
    return re.search(' the ', text) or re.search(' and ', text)



cipherText = readFile()    

# For each possible key, decrypt the cipher text and see if we have an English plain text message.
for key in itertools.product('abcdefghijklmnopqrstuvwxyz',repeat=3):
    plainText = decrypt(cipherText, key)
    if isEnglishText(plainText):
        print key, plainText
        print sum(map(ord, plainText))
    

