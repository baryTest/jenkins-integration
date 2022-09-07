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
"""

noms    = [ 'Pierre', 'Archibald', 'Sigismond', 'Symphorien', 'Bérénice', 'Gertrude', 'Elisabeth' ]    
notes   = [    16,        17,         11,           3,            18,         11,          1      ]     
classes = [   'CE2',      'CE2',      'CM1',        'CP',         'CP',      'CE2',        'CP'   ]


for i in range( len(noms) ):
    print( noms[i] )
    print( notes[i] )
    print( classes[i] )
    print( )







