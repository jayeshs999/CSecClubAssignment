import numpy as np

a = np.array(np.ones((256,256,256)),dtype = bool)

for i in range(1,5):
	
	with open(f"part{i}",'rb') as file:

		while True:

			byte = file.read(3)
			if not byte:
				break

			a[byte[0],byte[1],byte[2]] = False
			
			byte = file.read(1)
			if not byte:
				break

i,j,k = np.nonzero(a)

print(i,j,k)	

for c in range(len(i)):
	print(chr(i[c]),chr(j[c]),chr(k[c]),sep = '')

print("All We ask for is creative problem solving")

with open("answer.txt","w") as f:
	f.write("All We ask for is creative problem solving")



