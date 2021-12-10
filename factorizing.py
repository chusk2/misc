#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def is_factor(x,y):		#Define si a es divisor de b
	if y % x ==0:
		return True
	else:
		return False

def is_prime(x):
	prime=True
	for i in range(2,x): #prueba con todos los números menores de num hasta el 2
		if x%i==0: # si es divisible por un número distinto de 1 o él mismo, no es primo
			prime=False
			break
		else:
			prime=True
	return prime		

primes_list=[] # array para guardar los factores primos
primes_not_repeated={}
b=int(input('Introduce un número entero para factorizar en números primos: '))

if is_prime(b):
	print(b,' es de por sí número primo.')

else:
	primes_not_repeated={}
	count=0
	for i in range(2,b):	#comienza a probar factores a partir de 2
		if is_factor(i,b):
			if is_prime(i):
				primes_list.append(i)

				# try:
				# 	if i.index(prime_list):		#factor primo repetido, no añadir, solo contarlo una vez más
				# 		count=count+1
				# 		repeated_primes.append(i.index(prime_list):count)
				# except ValueError:
				# 	prime_list.append(i)	#factor primo nuevo
	# limpiamos lista de números primos de los repetidos
	for i in primes_list:
		if not i in primes_not_repeated:
			primes_not_repeated[i]=primes_list.count(i)
	
	print('La descomposición de ', b, ' en factores primos es:')
	for i in primes_not_repeated:
		print(i,'**',primes_not_repeated[i],end="*")
	print('\n',primes_not_repeated)
	print(primes_list)
