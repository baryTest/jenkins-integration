import unittest
import time
# virtualenv myVirtualPython
#  ou
# python -m venv myVirtualPython
#
# pip install -U selenium
# pip install webdriver-manager
from unittest import result
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import pytest 
from webdriver_manager.chrome import ChromeDriverManager

browser = ''

def testErreur( ):
    div = browser.find_element(By.ID, 'erreur' )
    if div.get_attribute( 'innerHTML' ) == 'ERREUR !!!' :
        return True
    return False

def lireResultat( ):
    div = browser.find_element(By.ID, 'resultat' )
    return div.get_attribute( 'innerHTML' )

def saisirSomme( somme ):
    elem = browser.find_element(By.ID, 'saisie' )
    elem.clear()
    elem.send_keys( somme )

def clickADD( ):
    bouton = browser.find_element(By.ID, 'add' )
    bouton.click()

def clickRAZ( ):
    bouton = browser.find_element(By.ID, 'raz' )
    bouton.click()



#print( disBonjour( 'toto' ) )

class mesTest( unittest.TestCase ):

    def test_add2chiffre( self ):
        saisirSomme( 12 )
        clickADD()
        saisirSomme( 13 )
        clickADD()
        result = lireResultat()
        self.assertEqual( result, '25,00&nbsp;€' )

    def test_add2chiffre2( self ):
        saisirSomme( 13 )
        clickADD()
        saisirSomme( 17 )
        clickADD()
        result = lireResultat()
        self.assertEqual( result, '55,00&nbsp;€' )
    


if __name__ == '__main__' :
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get('http://10.115.57.132/additione.html')
    unittest.main()
    browser.quit()