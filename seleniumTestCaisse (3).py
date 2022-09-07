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
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

browser.get('http://localhost//test//caisse.html')



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

def testRemise():
    div = browser.find_element(By.ID, 'resultat' )
    montant = div.get_attribute( 'innerHTML' )
    montantTotal= montant.split('&')
    montantTem = montantTotal[0].split(',')
    montantDec = float(montantTem[0]) + (float(montantTem[1]) /10)

    div = browser.find_element(By.ID, 'remise' )
    remise = div.get_attribute( 'innerHTML' )
    remiseTotal= remise.split('&')
    remiseTem = remiseTotal[0].split(',')
    remiseDec = float(remiseTem[0]) + (float(remiseTem[1]) /10)
    
    print('Montant : ', montantDec)

    if  montantDec<100 :
        remiseAttendu = montantDec * 0.05
    else :
        remiseAttendu = montantDec * 0.1

    print('remiseAttendu : ', remiseAttendu)
    print('remiseDec : ', remiseDec)

    if (remiseAttendu == remiseDec) :
        print ('OK')
    else :
        print ('KO')

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
    result = lireResultat()
    if testErreur() :
        print( 'OK' )
    else:
        print( 'KO' )


#scénario pour un montant <100
def scenarTestRemiseMoins():
    print( 'test de remise -100'  )
    saisirSomme( 50 )
    clickADD()
    result = lireResultat()
    #print( result )
    if result == '50,00&nbsp;€':
        print( 'OK' )
    else:
        print( 'KO' )
    testRemise()

    #scénario pour un montant >100
def scenarTestRemisePlus():
    print( 'test de remise -100'  )
    saisirSomme( 150 )
    clickADD()
    result = lireResultat()
    #print( result )
    if result == '50,00&nbsp;€':
        print( 'OK' )
    else:
        print( 'KO' )
    testRemise()

#scenarAdd2chiffre()
#scenarTestErreur()
scenarTestRemiseMoins()
scenarTestRemisePlus()


browser.quit()
time.sleep(40)