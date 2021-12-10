'''It is commonly said that one human year is equivalent to 7 dog years. However this
simple conversion fails to recognize that dogs reach adulthood in approximately two
years. As a result, some people believe that it is better to count each of the first two
human years as 10.5 dog years, and then count each additional human year as 4 dog
years.

Write a program that implements the conversion from human years to dog years
described in the previous paragraph. Ensure that your program works correctly for
conversions of less than two human years and for conversions of two or more human
years. Your program should display an appropriate error message if the user enters
a negative number.'''

def from_dog_to_human ( dog_years) :
    if dog_years >= 0 :
        
        if dog_years <= 2 :
            human_years = dog_years*10.5
            
        else :
            human_years = 10.5*2 + dog_years*4
        
        return human_years
        
    else :
        print('Do not enter a negative age!')

def from_human_to_dog ( human_years ) :
    
    while human_years >= 0 :
        if human_years <= 21 :
            dog_years = human_years/10.5
                        
        else :
            dog_years = 21 + human_years/4
        
        return dog_years
                
    else :
        print('Do not enter a negative age!')


print('Escribe "H" para convertir una edad de perro a edad humana.')
print('Escribe "P" para convertir una edad humana a edad de perro.')

mode = 'ask'
while mode not in ['h','H','p','P'] :
    
    mode = input('Tipo de edad: ')
    if mode not in ['h','H','p','P'] :
        print('¡Tipo de conversión no válida!')
        print('\n')

age = -1
while age < 0 :
    age = int ( input('Edad: ') )
    if age < 0:
        print ('¡¡La edad no puede ser un número negativo!!\n')
    
if mode == 'h' or mode =='H' :
    print('La edad del perro es',from_dog_to_human(age),'años humanos.')

elif mode == 'p' or mode =='P' :
    print('La edad es',from_human_to_dog(age),'años de perro.')
    
else : print('Modo de conversión no válido.')



