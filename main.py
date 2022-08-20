import streamlit as st
from bs4 import BeautifulSoup
import urllib.request

st.title("Pokémon VGC records by country")
st.markdown("Data from [RK9 Labs](https://rk9.gg/). Developed with :heart: by [@miniherrera11](https://twitter.com/miniherrera11).")

URL = "https://rk9.gg/pairings/worlds-2022-open-vgc"
st.markdown(f"**Default tournament displayed: {URL}**")
checkbox = st.checkbox("To choose another one, please enable this next checkbox and paste the pairings' link from RK9 Labs below.")

if checkbox:
    url = st.text_input("Paste it here")
    if len(url) == 0:
        pass
    else:
        URL = url

country = st.text_input("Write the tag (e.g.: '[ES]')")

html = urllib.request.urlopen(URL).read()
soup = BeautifulSoup(html, "html.parser")

results = soup.get_text()
lista = results.split()
indexes = []

for i in range(len(lista)):
    if lista[i] == country:
        indexes.append(i)

jugadores = []

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
