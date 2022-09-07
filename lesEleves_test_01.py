from sre_constants import NOT_LITERAL_IGNORE
import statistics


notes = [ 7, 14, 17, 11, 12, 1, 16, 7, 4, 13, 7, 7 ]
#notes = [ 5 ]
#notes = [  ]



moyenne = sum( notes ) / len( notes )

# un boucle nous chercons les deux en même temps
noteMax = -99999
noteMin = 99999
for note in notes:
    if note < noteMin:
        noteMin = note
    if note > noteMax:
        noteMax = note




def statEcole( notes ):
    noteMax = -99999
    noteMin = 99999  
    moyenne = sum (notes)/ len( notes )
    for note in notes:
        if note < noteMin :
             noteMin = note
        if note > noteMax:
             noteMax = note
    return ( noteMax , noteMin, moyenne)






print ( statEcole ( notes ))


