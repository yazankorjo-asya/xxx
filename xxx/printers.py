import requests
from bs4 import BeautifulSoup
 
def h1_printer(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    h1_tag = soup.find("h1")
    print(h1_tag.text)

