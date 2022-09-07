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

from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

browser.get('http://10.115.57.132/additione.html')


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


#scénario
def scenarAdd2chiffre():
    print( 'test de 2 addition'  )
    saisirSomme( 12 )
    clickADD()
    saisirSomme( 13 )
    clickADD()
    result = lireResultat()
    #print( result )
    if result == '25,00&nbsp;€':
        print( 'OK' )
    else:
        print( 'KO' )


def scenarTestErreur():
    print( "test de l'erreur"  )
    saisirSomme( 'toto' )
    clickADD()
    if testErreur() :
        print( 'OK' )
    else:
        print( 'KO' )


def scenarTestSelect():
    elem = browser.find_element(By.ID, 'select-paiement' )
    #listOption = elem.first_selected_option
    listOption = Select( elem )    
    #print selected_option.text
    #for opt in listOption.options:
    #    print( opt.text )
    if listOption.options[0].text == 'Espèce':
        print( 'OK' )
    else:
        print( 'KO' )

    if listOption.options[1].text == 'Carte bancaire':
        print( 'OK' )
    else:
        print( 'KO' )

    if listOption.options[2].text == 'Cheque':
        print( 'OK' )
    else:
        print( 'KO' )

def scenarTestUL():
    elem = browser.find_element( By.XPATH, "/html/body/ul" )
    items = elem.find_elements( By.TAG_NAME, "li")
    if items[0].text == '+100€ 5%':
        print( 'OK' )
    else:
        print( 'KO' )

    if items[1].text == '+300€ 7%':
        print( 'OK' )
    else:
        print( 'KO' )

    if items[2].text == '+500€ 10%':
        print( 'OK' )
    else:
        print( 'KO' )


def scenarTestTable():
    elem = browser.find_element( By.XPATH, "/html/body/table" )
    items = elem.find_elements( By.TAG_NAME, "tr")
    if items[0].text == '+100€ 5%':
        print( 'OK' )
    else:
        print( 'KO' )

    if items[1].text == '+300€ 7%':
        print( 'OK' )
    else:
        print( 'KO' )

    if items[2].text == '+500€ 10%':
        print( 'OK' )
    else:
        print( 'KO' )

def scenarTestTable2():
    for ligne in range( 1,4):
        for colone in range( 1,3 ):
            elem = browser.find_element( By.XPATH, "/html/body/table/tbody/tr["+str(ligne)+"]/td["+str(colone)+"]" )
            print( elem.text )


#scenarAdd2chiffre()
#scenarTestErreur()
#scenarTestSelect()
#scenarTestUL()
scenarTestTable2()

browser.quit()
time.sleep(40)