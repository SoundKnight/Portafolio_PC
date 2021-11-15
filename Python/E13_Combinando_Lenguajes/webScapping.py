#Ibrahim Zavala Hernandez, Julio Gerardo Cazares Gonzales, Pedro Saldaña Vazquez
import requests
from bs4 import BeautifulSoup

def get_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    return BeautifulSoup(response.content, "html.parser")

def images():
    soup = get_soup(link)
    images = soup.find_all("img")
    t = [{"src": image.get("src"), "alt": image.get("alt")} for image in images]
    for i in range(0,len(t)):
        X = str( t[i] )
        archivo.write( X +"\n")
        

    
if __name__=="__main__":
    link="https://es.wikipedia.org/wiki/Queen"
    print("La página a la que se le realizará el ws es: " +link) #El link se puede cambiar para así extraer info de distintas páginas
    print("Realizando Web Scrapping...")
    archivo=open("ws_images.txt","w")
    images()
    archivo.close()
    print("Web Scrapping realizado con éxito")

