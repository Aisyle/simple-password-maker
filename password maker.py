import random

import os

chars = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

nums = ['1','2','3','4','5','6','7','8','9','0']

alls = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']

print('lenght')

lenghts = int(input('>'))

os.system('cls')

i = 1

for i in range(lenghts) :

	a = random.choice(alls)

	folder = open('a','a')

	folder.write(a)

	folder.close()

	folder = open('a','r')

	print(folder.read())

	folder.close()

os.remove('a')

print('!!press enter to close!!')

input()