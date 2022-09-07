# importer la lib de test

from random import randint
from re import M
import unittest
#from unittest import TestCase, main as MAIN
import maLib
#from maLib import main

#   du code à tester

def disBonjour( mes ):
    return 'bonjour ' + mes

def multi( listeDeNombres ):
    res = 1
    if len( listeDeNombres ) > 0:
        for nombre in listeDeNombres:
            res *= nombre
    else:
        res = 0
    return res

def add( a, b):
    try :
        return round(a + b, 10 )
    except:
        return 0


def multiplier( a, b ):
    return a*b

def div( a, b):
    return a/b

print (div)  

def tirageDe():
    res = randint(1, 7)



#print( multi( [ 11, 12, 13 ] )  )
#print( multi( [ 11, 12, 13, 0 ] )  )
#print( multi( [  ] )  )



# section de test
if __name__ == '__main__' :

    # une classe de test dérivée de la class TestCase  
    class MesTest( unittest.TestCase ):
        def test_DisBonjour( self ):
            self.assertEqual( disBonjour( 'tata' ), 'bonjour tata' )
            self.assertNotEqual( disBonjour( 'tata' ), 'bonjour Tata' )

        def test_Multi( self ):
            self.assertEqual(       multi( [ 11, 12, 13 ] ), 1716 )
            self.assertEqual(       multi( [ 11, 12, 13, 0 ] ), 0 )
            self.assertEqual(       multi( [] ), 0 )
            self.assertEqual(       multi( [1] ), 1 )

        def test_Add( self ):
            self.assertEqual(       add( 1, 1 ), 2 )
            self.assertEqual(       add( 0, 0 ), 0 )
            self.assertEqual(       add( -1, 1.2 ), 0.2 )
            self.assertEqual(       add( 1, 0.00002 ), 1.00002 )
            self.assertEqual(       add( 'a', 'b' ), 0 )

        def test_Multiplier( self ):
            self.assertEqual(       multiplier( 1, 1 ), 1 )
            self.assertEqual(       multiplier( 0, 1 ), 0 )
            self.assertEqual(       multiplier( -1.001, 1 ), -1.001 )
            self.assertEqual(       multiplier( -0.001, 0.001 ), -0.000001 )

        def test_Div( self ):
            self.assertEqual(       div( 1, 1 ), 1 )
            self.assertEqual(       div( 0, 1 ), 0 )
            self.assertEqual(       div( -1, 1 ), -1 )
        
        def test_Tirage( self ):
            for i in range( 100):
                res = tirageDe()
                print(res)
                self.assertIn( res,  [1, 2, 3, 4, 5, 6] )
    
    unittest.main()

