#import requests
import streamlit as st
from bs4 import BeautifulSoup
import urllib.request
URL = "https://rk9.gg/pairings/worlds-2022-vgc#P2"
html = urllib.request.urlopen(URL).read()
soup = BeautifulSoup(html, "html.parser")

results = soup.get_text()
lista = results.split()
indexes = []

st.title("Pokémon WCS'22 records by country")
st.markdown("Data from [RK9 Labs](https://rk9.gg/pairings/worlds-2022-vgc#P2). Developed with :heart: by [@miniherrera11](https://twitter.com/miniherrera11).")
country = st.text_input("Write the tag (e.g.: [ES])")

for i in range(len(lista)):
    if lista[i] == country:
        indexes.append(i)

data = []
jugadores = []
partidas = []

data = list(set(data))


datos_buenos = []
records = []
for num in indexes:
    records.append(lista[num + 1])
    jugadores.append(lista[num - 2] + " " + lista[num - 1])

jugadores_unique = list(set(jugadores))

for jugador in jugadores_unique:
    lista_ind = []
    for i in range(len(jugadores)):
        if jugadores[i] == jugador:
            lista_ind.append(i)
    for j in lista_ind:
        indice = max(lista_ind)
    st.markdown(jugador + " " + records[indice])
