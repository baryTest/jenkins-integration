# auteur Toto@gmail.com
# calcule la moyenne d'une classe d'éleve
# 20/07/2022
#
import statistics

def add ( a, b ):
    somme = a + b
    return somme

resultat = add( 5, 9 )
print( resultat )
#14

print(  20 * 'X' )

notes = [ 7, 14, 17, 11, 12, 0, 16, 7, 4, 13, 7, 7 ]
somme = 0
for note in notes:
    print( note )
    somme = somme + note

moyenne = somme / len( notes )
print( 'somme :', somme )
print( 'moyenne :', moyenne )

moyenne = sum( notes ) / len( notes )
print( 'moyenne :', moyenne )

moyenne = statistics.mean( notes )
print( 'moyenne :', moyenne )


print( 'min :', ...  )
print( 'max :', ...  )








