import streamlit as st
from bs4 import BeautifulSoup
import urllib.request

st.title("Pokémon VGC/TCG records by country")
st.markdown(
    "Data from [RK9 Labs](https://rk9.gg/). Developed with :heart: by [@miniherrera11](https://twitter.com/miniherrera11).")

URL = "https://rk9.gg/pairings/NA2MV6cHdbdqvXWs7HAa"
URL_TCG = "https://rk9.gg/pairings/NA1KYsUUz7fBID8XkZHZ"
st.markdown(f"**Default tournament displayed: NAIC'23**")

TCG_checkbox = st.checkbox(
    "To choose TCG, please enable this checkbox. Otherwise, VGC is displayed.")


checkbox = st.checkbox(
    "To choose another tournament, please enable this checkbox and paste the pairings' link from RK9 Labs below.")

if checkbox:
    url = st.text_input("Paste it here")
    if len(url) == 0:
        pass
    else:
        URL = url

if TCG_checkbox:
    URL = URL_TCG

country = st.text_input("Write the tag (e.g.: '[ES]')")

html = urllib.request.urlopen(URL).read()
soup = BeautifulSoup(html, "html.parser")

results = soup.get_text()  # Gets the text from the html
words = results.split()  # Splits results into words
indices = []  # Stores the position inside the 'list' array of all tags from the same country

for i in range(len(words)):  # Checks if words are the tag we wanted
    if words[i] == country:
        indices.append(i)

players = []  # Stores all players from wished country
records = []  # Stores all records from wished country with the same order

for num in indices:  # Appends players and their records from indices
    records.append(words[num + 1])
    players.append(words[num - 2] + " " + words[num - 1])

players_unique = list(set(players))  # Eliminates duplicated names

for player in players_unique:  # Checks from all entries of a players, which is the most recent
    list_ind = []
    for i in range(len(players)):
        if players[i] == player:
            list_ind.append(i)
    index = max(list_ind)
    st.markdown(player + " " + records[index])

st.markdown("Copyright Disclaimer under section 107 of the Copyright Act 1976, allowance is made for “fair use” for "
            "purposes such as criticism, comment, news reporting, teaching, scholarship, education and research. Fair "
            "use is a use permitted by copyright statute that might otherwise be infringing. Non-profit, educational "
            "or personal use tips the balance in favor of fair use.")
