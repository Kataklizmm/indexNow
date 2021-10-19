import string
import random

def keygen(domain):
	if not domain:
		key = input('Введите домен без протокола')
	key = domain
	key = key.replace('.','-')
	for i in range(30):
		key = key + random.choice(string.ascii_letters)
	file = open(f'{key}.txt', 'w', encoding='utf-8')
	file.write(key)
	file.close()
	return key

if __name__ == "__main__":
	keygen()
