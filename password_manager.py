#This is a simple program for creating and managing unqiue passwords

#import tools and libaries
import os, random, sys, shelve
from string import digits
from string import punctuation
from string import ascii_letters

passwordShelve = shelve.open('encryptedpasswords')
passwordShelve['passwords'] = ''
#encave the code in a try and except clause to handle general error
try:
	if (sys.argv[1] == 'SET'):
		chars = digits + punctuation + ascii_letters
		secure_random = random.SystemRandom()
		password = "".join(secure_random.choice(chars) for i in range(int(sys.argv[3])))
		shelfFile = shelve.open('encryptedpasswords')
		passwordShelve[sys.argv[2]] = password
		shelfFile['passwords'] = passwordShelve
		print(sys.argv[2], ':',passwordShelve[sys.argv[2]])
		shelfFile.close()
	elif (sys.argv[1] == 'GET'):
		try:
			print(sys.argv[2], ':',passwordShelve[sys.argv[2]])
		except:
			print('You should SET before you attempt to get.')
except:
	print('Read the docs, you are not getting something right!!!')