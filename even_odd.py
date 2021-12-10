'''Write a program that reads an integer from the user. Then your program should
display a message indicating whether the integer is even or odd.'''

number = int( float( input('Dame un número entero: ')) )

if number % 2 == 0:
    print (f'{number} es un número par.')
else :
    print (f'{number} es un número impar.')