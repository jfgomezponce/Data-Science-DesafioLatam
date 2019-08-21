'''
3. La función letra_x(n), la cual al ser llamada, dibujará una letra "x" según el ejemplo
letra_x(5)

n = 5
				() al medio
0 5		*...*	3 (n-2)
1 4		.*.*.	1 (n-4)
2 3		..*  	0 (n-n) o (n-1/2)
3 2		.*.*	1 (n-4)
4 1		*...*	3 (n-2)


-----------------
n = 7

0 7	*.....* (*)+ ( )(n-2) +(*)				5 (n-2)
1 6	.*...*. 1()+(*)+( )(n-2-2)+(*)+()1		3 (n-2-2)
2 5	..*.*.. 2()+(*)+( )(n-2-2-2)+(*)+()2	1
#########################
3 4	...*... 3()+(*)+( )0 +()3		0
######## MITAD ##########
#########################
i								resta (al medio)	espacios
4 3	..*.*.. 2()+(*)+( )1+(*)+()2	1					2 (resta+2) (i-3)
5 2	.*...*. 1()+(*)+( )3+(*)+()1	3					1 (resta-2) (i-4)
6 1	*.....* (*)+ ( )(n-2) +(*)		5					0 (resta-4) (i-5)




'''

def letra_x(n):
	asteriscos = ''
	resta = n-2
	
	for i in range(n):
		
		if i == 0 or i == n-1: #inicio o final
			asteriscos += '*' + (' '*(n-2)) + '*' + '\n'
		elif i == ((n-1)/2):
			asteriscos += i*' '+'*'+' '*i+'\n'
		elif i < ((n-1)/2):
			resta -= 2
			asteriscos += (' '*i) +'*' + (' '*(resta)) + '*' + (' '*i) + '\n'
		#########################
		elif i > ((n-1)/2):
			#print(i,resta)
			asteriscos += (' '*(i-resta-1)) +'*'+ (' '*resta) +'*'+ (' '*(i-resta-1)) +'\n'
			resta += 2
	#print(asteriscos)
	return asteriscos
string_asteriscos = letra_x(int(input()))