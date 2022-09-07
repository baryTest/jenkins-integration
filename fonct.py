# -*- coding: utf-8 -*-
import statistics

notes = [ 7, 14, 17, 11, 12 ]
somme = 0
for note in notes:
    print( note )
    somme = somme + note

moyene = somme / len( notes )
print( 'somme :', somme )
print( 'moyene :', moyene )

moyenne = sum( notes ) / len( notes )
print( 'moyenne :', moyenne )

moyenne = statistics.mean( notes )
print( 'moyenne :', moyenne )

# une boucle pour chercher la valeur la plus basse
notemin = 20
for note in notes:
      if note < notemin:
          notemin = note

# une boucle pour chercher la valeur la plus haute
notemax = -20
for note in notes:
      if note > notemax:
          notemax = note

print ("La plus petite note", min (notes))
print ("La plus grande note", max (notes))
