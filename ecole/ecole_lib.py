ecole = [
    { 'nom' : 'Toto', 'age' : 6, 'classe' : 'CP', 'note':'A'  },
    { 'nom' : 'Gertrude', 'age' : 8, 'classe' : 'CM1', 'note':11  },
    { 'nom' : 'Emmanuel', 'age' : 14, 'classe' : 'CM2', 'note':17  },
    { 'nom' : 'Brigitte', 'age' : 32, 'classe' : 'CM2', 'note':18  },
    { 'nom' : 'Alphonse', 'age' : 4, 'classe' : 'CP', 'note': 'B'  },
    { 'nom' : 'Alphonse', 'age' : 5, 'classe' : 'CP', 'note': 'C'  },
    { 'nom' : 'Justin',   'age' : 23, 'classe' : 'CM2', 'note': 11  },
    { 'nom' : 'Guildebert',   'age' : 8, 'classe' : 'CM1', 'note': 5  }
]


def trouverEleve( nom ):
    listeResultat = []
    for eleve in ecole:
        if nom == eleve[ 'nom' ]: 
            listeResultat.append( eleve )
    return listeResultat

def trouverUnEleve( nom ):
    for eleve in ecole:
        if nom == eleve[ 'nom' ]: 
            return eleve

def afficherEleve( nom ):
    listeDesEleves = trouverEleve( nom )
    for eleve in listeDesEleves:
        print( eleve )

def afficherUnEleve( nom ):
    print( nom,  trouverUnEleve(nom) )


def afficherUneClasse( classe ):
    for eleve in ecole:
        if classe == eleve[ 'classe' ]: 
            print( eleve )

def ajouterUnEleve( nom, age, classe, note=None  ):
    eleve = {}
    eleve[ 'nom' ] = nom
    eleve[ 'age' ] = age
    eleve[ 'classe' ] = classe
    eleve[ 'note' ] = note
    ecole.append( eleve )
    #ecole.append( { 'nom' : nom, 'age': age, 'classe':classe, 'note' : note } )
