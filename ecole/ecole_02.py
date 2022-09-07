"""
ecole

classes
    cp
    ce1
    ce2
    cm1
    cm2

eleves
    nom
    note
    classe




ajouter( 'toto', 'cm2' )
donnerUneNote( 'toto', 'cm2', 12 )
afficherUneClasse( 'cm2' )
afficherUneClasse( 'ce2' )
afficherUnEleve( 2 )
"""


noms    = {  1:'Pierre',  2:'Archibald', 3:'Sigismond', 4:'Symphorien', 5:'Bérénice', 6:'Gertrude',  7:'Elisabeth'  }    
notes   = {  1: 16,       3: 11,         2:17,          4:3,            5:18,         6:11,          7:1            }     
classes = {  1: 'CE2',    2: 'CE2',      3:'CM1',       4:'CP',         5:'CP',       6:'CE2',       7:'CP'         }
ages    = {  1: 30,       2: 1,          3: 8 ,        4:5,            5:5,          6:7,           7:120         }

def afficherUnEleve( num ):
    print( noms[num] )
    print( ages[num], 'ans' )
    print( notes[num], '/20' )
    print( classes[num] )
    print( )

afficherUnEleve( 5 )
print( 20 * '-' )

for i in range( len(noms) ):
    afficherUnEleve( i+1 )
print( 20 * '-' )


def afficherUnClasse( nomClasse ):
    for i in range( len(classes) ):
        if classes[ i+1 ] == nomClasse:
            afficherUnEleve( i+1 )

print( 20 * '-' )

afficherUnClasse( 'CE2' )

print( 20 * '-' )

afficherUnClasse( 'CP' )

print( 20 * '-' )

afficherUnClasse( 'CM1' )

print( 20 * '-' )

def ajouterEleve( nom, age, classe  ):
    numDernierEleve = len( noms )
    numNouveauEleve = numDernierEleve +1   
    noms[numNouveauEleve]    =   nom
    ages[numNouveauEleve]    =   age
    classes[numNouveauEleve] =   classe
    notes[numNouveauEleve]   =   None


ajouterEleve( 'toto', 13, 'CM1' )
afficherUnClasse( 'CM1' )

def getNumEleve( nom ):
    for i in range( len(noms) ):
        if noms[ i+1 ] == nom:
            return i+1
    return None 


def ajouterUneNote( nom, note ):
    num = getNumEleve( nom )
    notes[ num ] = note

print( 20 * '-' )

ajouterUneNote( 'toto', 12 )
afficherUnClasse( 'CM1' )


