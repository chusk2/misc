#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import turtle


#elegir color
print('Opción 1: tablero a color')
print('Opción 2: tablero clásico en blanco y negro')
print('\n')

colores=int(input('Indica el número de la opción elegida: '))
cellsize=int(input('¿Tamaño de casilla? '))

window=turtle.Screen()
window.clear() # borra dibujos anteriores
window.bgcolor("gray")
t=turtle.Turtle()
t.hideturtle()
t.pensize(2)
t.color('black')
t.speed(0)

# función para generar coordenadas letras
def letras():
	x=0.7*cellsize # centrar las coor en las casillas
	letter=97
	t.color('black')
	t.penup()
	for l in range(8):
		t.write(chr(letter+l))
		t.forward(cellsize)
		
#función para mover cursor sin dibujar
def mover(a,b):
	t.penup()
	t.setpos(a,b)
	t.pendown()

# colocamos el cursor arriba del tablero
x=0
y=cellsize*8.5 # 8 filas + 1 fila para coordenadas
mover(x,y)

letras() #dibujamos coor horizontales
y=cellsize*8
mover(0,y) #cursor a principio del tablero

# establecemos color tablero
if colores==1:
	color1="#fabf7c"
	color2="#f88708"
	t.color(color2)
else:
	color1="white"
	color2="black"
	t.color('black')

for i in range(8): #imprime filas de casillas
	
	for j in range(8): # imprime columnas de casillas
		if (i+1)%2!=0: # fila impar
			if (j+1)%2==0: # col par
				t.fillcolor(color2) # oscuro
			else : t.fillcolor(color1) # claro
		
		else : # fila par
			if (j+1)%2==0 : # col par 
				t.fillcolor(color1) # claro
			else: t.fillcolor(color2) # oscuro
		# comienza a dibujar casillas
			
		t.begin_fill()
		for k in range(4):
			t.forward(cellsize)
			t.right(90)
		t.end_fill()
		x=x+cellsize # desplaza 10 unidades a dcha en horizontal
		t.setx(x) # mueve a la siguiente casilla a la derecha
	x=0 # vuelve a dibujar a la izquierda del tablero
	y=y-cellsize # desplaza 10 unidades hacia abajo
	mover(x,y)
mover(0,y-cellsize)
letras()

turtle.mainloop()

