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


ecole = {
    'CP' : { 'toto' : { 'age' : 12, 'note' :  6 },  
             'tata' : { 'age' : 11, 'note' : 16 },
             'gert' : { 'age' :  9, 'note' : 12 }
           },

    'CE1' :{ 'Marie' : { 'age' : 13, 'note' : 13 },  
             'Lili'  : { 'age' : 10, 'note' : 14 },
             'Karim' : { 'age' : 11, 'note' : 17 }
           },

    'CE2' :{ 'Marc'     : { 'age' : 13, 'note' : 3 },  
             'Louise'   : { 'age' : 11, 'note' : 4 },
             'Sarah'    : { 'age' : 12, 'note' : 1 }
           }
}


def trouverUnEleve( nom ):
    for nomClasse, classe in ecole.items():
        if nom in classe:
            return ecole[ nomClasse ][ nom ]
    return None


def afficherUnEleve( nom ):
    print( nom,  trouverUnEleve(nom) )


afficherUnEleve( 'toto' )
print( 20 * '-' )
afficherUnEleve( 'Karim' )
print( 20 * '-' )

def ajouterUnEleve( nom, classe, age, note=None ):
    ecole[ classe ][ nom ] = { 'age' : age, 'note': note }

def afficherClasse( classe ):
    klass = ecole[ classe ]
    for eleve, info in klass.items():
        print( eleve, info )

    
afficherClasse( 'CP')
ajouterUnEleve( 'Gontrand', 'CP', 6  )
ajouterUnEleve( 'Gontrand', 'CP', 4  )
print( 20 * '-' )
ecole[ 'CP' ][ 'Gontrand' ] = 'gontrand sent des pieds' 
ajouterUnEleve( 'Gertrude', 'CP', 7, 14  )
ajouterUnEleve( 'gertrude', 'CP', 7  )
afficherClasse( 'CP')
print( 20 * '-' )
afficherClasse( 'CE2')

# ces 2 ligne
ecole[ 'CE2' ][ 'Louise' ][ 'note' ] = ecole[ 'CE2' ][ 'Louise' ][ 'note' ] + 1
# equivalent
ecole[ 'CE2' ][ 'Louise' ][ 'note' ] += 1

print( ecole[ 'CE2' ][ 'Louise' ][ 'note' ] )


