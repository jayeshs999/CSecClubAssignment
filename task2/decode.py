import numpy as np

none = np.zeros((7,1))

sym_dict = {}
with open('output.txt','r') as f:
	lines = f.readlines()
	lis1 = []
	lis2 = []
	lis3 = []
	lis4 = [] 
	for j in range(7):
		lis1.append([int(c) for c in lines[j][0:-1]])
		lis2.append([int(c) for c in lines[8+j][0:-1]])
		lis3.append([int(c) for c in lines[16+j][0:-1]])
		lis4.append([int(c) for c in lines[24+j][0:-1]])

	
	arr1 = np.array(lis1)
	arr2 = np.array(lis2)
	arr3 = np.array(lis3)
	arr4 = np.array(lis4)


	sym_dict['('] = arr1[:,0:3]
	sym_dict[')'] = arr1[:,272:275]
	sym_dict['0'] = arr3[:,18:23]
	sym_dict['1'] = arr2[:,12:17]
	sym_dict['2'] = arr1[:,24:29]
	sym_dict['3'] = arr1[:,18:23]
	sym_dict['4'] = arr1[:,36:41]
	sym_dict['5'] = arr2[:,30:35]
	sym_dict['6'] = arr2[:,84:89]
	sym_dict['7'] = arr2[:,24:29]
	sym_dict['8'] = arr1[:,12:17]
	sym_dict['9'] = arr1[:,42:47]
	sym_dict['+'] = arr3[:,51:56]
	sym_dict['-'] = arr1[:,51:56]
	sym_dict['/'] = arr4[:,51:56]
	sym_dict['*'] = arr2[:,51:56]

def get_symbol(a):
	for i in sym_dict.keys():
		if sym_dict[i].shape == a.shape:
			if (sym_dict[i]==a).all():
				return i	





with open('output.txt','r') as f:
	with open('easy.txt','a') as f1:
		lines = f.readlines()
		
		for i in range(int(len(lines)/8)):
			lis = []
			s = ""
			
			for j in range(7):
				lis.append([int(c) for c in lines[8*i+j][0:-1]])
			
			array = np.array(lis)

			for i in range(len(lis[0])):
				if (array[:,i]==none).all():
					continue

				if get_symbol(array[:,i:i+3]):
					s = s + get_symbol(array[:,i:i+3]) 
					i += 2
				elif get_symbol(array[:,i:i+5]):
					s = s + get_symbol(array[:,i:i+5])
					i += 4

			s_new = s[0]

			for i in range(1,len(s)):
				if s[i-1].isnumeric() and s[i].isnumeric():
					s_new += s[i]
				else:
					s_new = s_new + " " + s[i]  

			f1.write(s_new+'\n')
