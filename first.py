#!/usr/bin/env python3
# -*- coding: utf-8 -*-
num=1 # define previamente num
posit = negat = i = j = 0


while num!=0:
	num=int(input('Dime un número entero: '))
	if num==0:
		break
	elif num>0:
		posit=posit+num
		i=i+1
	else:
		negat=negat+num
		j=j+1

if posit!=0:
		print('La suma de los números positivos es: ' , posit ,
' y su media es: ' , posit/i , '.')
if negat!=0:
	print('La suma de los números negativos es: ' , negat ,
' y su media es: ' , negat/j , '.')
