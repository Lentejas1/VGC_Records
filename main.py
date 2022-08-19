import streamlit as st
from bs4 import BeautifulSoup
import urllib.request
URL = "https://rk9.gg/pairings/worlds-2022-vgc#P2"
html = urllib.request.urlopen(URL).read()
soup = BeautifulSoup(html, "html.parser")

results = soup.get_text()
lista = results.split()
print(lista)
indexes = []
country = "[ES]"

for i in range(len(lista)):
    if lista[i] == country:
        indexes.append(i)

data = []
jugadores = []
partidas = []

data = list(set(data))

st.title("Españoles en Pokémon WCS'22")
st.markdown(r"### por Carlos Herrera [(@miniherrera11)](https://twitter.com/miniherrera11)")

datos_buenos = []
records = []
for num in indexes:
    records.append(lista[num + 1])
    jugadores.append(lista[num - 2] + " " + lista[num - 1])

jugadores_unique = list(set(jugadores))
print(jugadores_unique)
print(datos_buenos)
for jugador in jugadores_unique:
    lista_ind = []
    for i in range(len(jugadores)):
        if jugadores[i] == jugador:
            lista_ind.append(i)
    for j in lista_ind:
        indice = max(lista_ind)
    st.markdown(jugador + " " + records[indice])
