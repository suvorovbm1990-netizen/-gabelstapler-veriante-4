import streamlit as st
import random
import os
from PIL import Image, ImageDraw, ImageFont

st.set_page_config(page_title="Gabelstapler Quiz", page_icon="🏗️", layout="centered")

# создаем картинки если их нет - встроенные
def ensure_images():
    os.makedirs("images", exist_ok=True)
    def make(path, title, body):
        if os.path.exists(path):
            return
        img = Image.new('RGB', (700, 500), (255,255,255))
        d = ImageDraw.Draw(img)
        try:
            fb = ImageFont.truetype("DejaVuSans.ttf", 26)
            fs = ImageFont.truetype("DejaVuSans.ttf", 18)
        except:
            fb = ImageFont.load_default()
            fs = ImageFont.load_default()
        d.rectangle([0,0,699,499], outline=(0,0,0), width=3)
        d.text((20,20), title, fill=(0,0,0), font=fb)
        y=70
        for line in body.split("\n"):
            d.text((20,y), line, fill=(20,20,20), font=fs)
            y+=26
        img.save(path)

    make("images/2.jpg", "Tragfahigkeit 2000 kg", "1600kg Kiste\n- 600mm / 4,5m = OK\n- 700mm / 4,0m = OK\n- 600mm / 5,5m = NICHT OK")
    make("images/4.jpg", "Prufplakette 06 -> Pfeil 2", "Mitte: 06 = Jahr 2006\nPfeil auf 2 = Februar\n=> Feb 2006")
    make("images/12.jpg", "Ladebrucke LKW", "Beachten:\n- Tragfahigkeit Brucke\n- Tragfahigkeit Ladeflache")
    make("images/13.jpg", "Gebotszeichen Schuhe", "Blauer Kreis, weisser Schuh\n= SCHUTZSCHUHE TRAGEN")
    make("images/14.jpg", "Traglast 1500kg Palette", "800x1200, 1100kg\nMax 5,0m OK\n5,5m zu hoch")
    make("images/18.jpg", "Lastschwerpunkt Abstand", "a) weit vorn = grosster\nb) mittel\nc) nah am Rucken = kleinster")

ensure_images()

QUESTIONS = [
    {"f": "Kiste 1600 kg - wann stapeln moglich?", "img": "images/2.jpg", "opts": ['600 mm und 4,5 m', '600 mm und 5,5 m', '700 mm und 4,0 m', '500 mm und 5,0 m'], "c": [0,2]},
    {"f": "Wann nachste Prufung bei dieser Prufplakette?", "img": "images/4.jpg", "opts": ['Februar 2006', 'August 2006', 'Februar 2007', 'August 2007'], "c": [0]},
    {"f": "Was beim Befahren von Ladebrucken beachten?", "img": "images/12.jpg", "opts": ['Nichts', 'Nur ruckwarts', 'Tragfahigkeit der Ladebrucke', 'Tragfahigkeit der Ladeflache', 'Nach UVV verboten'], "c": [2,3]},
    {"f": "Gebotszeichen blau/weiss?", "img": "images/13.jpg", "opts": ['Fussweg', 'Heizraum', 'Festes Schuhwerk verboten', 'Schutzschuhe tragen'], "c": [3]},
    {"f": "Palette 800x1200 mm, 1100 kg - max Hohe?", "img": "images/14.jpg", "opts": ['4,0 m', '4,5 m', '5,0 m', '5,5 m', '3,5 m'], "c": [2]},
    {"f": "Wo ist Lastschwerpunktabstand am groessten?", "img": "images/18.jpg", "opts": ['a) weit vorn', 'b) nah', 'c) direkt am Rucken'], "c": [0]},
    {"f": "Wie fahrt man mit beladenem Stapler ein Gefalle hinunter?", "img": None, "opts": ['Last bergseitig', 'Nie im Leerlauf', 'Last talseitig', 'Kein Gefalle befahren'], "c": [0,1]},
    {"f": "Darf Fahrer Kollegen mitnehmen?", "img": None, "opts": ['Nie', 'Kurze Strecke', 'Wenn in Eile', 'Wenn Sitz mit Griffen + erlaubt'], "c": [3]},
    {"f": "Welche Pflege darf Fahrer machen?", "img": None, "opts": ['Kuhlwasser', 'Batterie', 'Lenkung', 'Olstand', 'Bremsen'], "c": [0,1,3]},
    {"f": "Welche sind Flurforderzeuge?", "img": None, "opts": ['Gabelhubwagen', 'Gabelstapler', 'Schubmaststapler', 'Lore', 'Kran-Katze'], "c": [0,1,2]},
    {"f": "Was tun bei undichtem Hydraulikschlauch?", "img": None, "opts": ['Olstand prufen', 'Isolierband', 'Halbe Tragkraft', 'Sofort stilllegen', 'Nach Feierabend'], "c": [3]},
    {"f": "Wann darf 18-jahriger Stapler nutzen?", "img": None, "opts": ['Nur Tag', 'Schlussel steckt', 'Nur Nacht', 'Muss beauftragt sein', 'Wenn schwerer als Diagramm'], "c": [3]},
    {"f": "Welche Verkehrswege?", "img": None, "opts": ['Nur festgelegte Wege', 'Nur Hauptwege', 'Keine Vorschrift', 'Nur ebene', 'Nur Fusswege'], "c": [0]},
    {"f": "Wann darf Stapler bei hoher Buhne verlassen werden?", "img": None, "opts": ['Kurz', 'Bremse+Motor aus', 'Dienstschluss', 'Nie', 'Ebener Boden'], "c": [3]},
    {"f": "Flussigkeit in Batterie?", "img": None, "opts": ['Dest. Wasser', 'Verd. Schwefelsaure', 'Salzsaure', 'Leitungswasser'], "c": [1]},
    {"f": "Brandgefahr Putzlappen?", "img": None, "opts": ['Nein', 'Nein mit Fett', 'Ja Selbstentzundung', 'Ja explosive Dampfe'], "c": [2,3]},
    {"f": "Abfahrtskontrolle Diesel?", "img": None, "opts": ['Waschen', 'Gabelzinken prufen', 'Luftfilter', 'Olstand'], "c": [1,3]},
]

if "idx" not in st.session_state:
    st.session_state.idx = 0
    st.session_state.score = 0
    st.session_state.order = random.sample(range(len(QUESTIONS)), len(QUESTIONS))
    st.session_state.answered = False

def next_q():
    st.session_state.idx += 1
    st.session_state.answered = False

def restart():
    st.session_state.idx = 0
    st.session_state.score = 0
    st.session_state.order = random.sample(range(len(QUESTIONS)), len(QUESTIONS))
    st.session_state.answered = False

total = len(QUESTIONS)
cur = st.session_state.idx

st.title("Gabelstapler - Variante 4")

if cur < total:
    st.progress(cur/total, text=f"Frage {cur+1}/{total} | Punkte: {st.session_state.score}")
    q = QUESTIONS[st.session_state.order[cur]]
    st.subheader(q["f"])
    if q["img"] and os.path.exists(q["img"]):
        st.image(q["img"], use_container_width=True)
    if len(q["c"]) > 1:
        st.caption("Mehrere Antworten moglich!")
    sel=[]
    for i,opt in enumerate(q["opts"]):
        if st.checkbox(opt, key=f"{cur}_{i}", disabled=st.session_state.answered):
            sel.append(i)
    if not st.session_state.answered:
        if st.button("Antworten", type="primary", use_container_width=True):
            if not sel:
                st.warning("Wahle Antwort!")
            else:
                st.session_state.answered=True
                st.session_state.last_ok = (set(sel)==set(q["c"]))
                if st.session_state.last_ok:
                    st.session_state.score+=1
                st.rerun()
    else:
        if st.session_state.last_ok:
            st.success("✅ RICHTIG!")
        else:
            st.error("❌ FALSCH!")
            st.info("Richtig: " + ", ".join([q["opts"][x] for x in q["c"]]))
        if st.button("Weiter ➡️", type="primary", use_container_width=True):
            next_q()
            st.rerun()
    if st.button("Neu mischen"):
        restart()
        st.rerun()
else:
    st.title("Fertig!")
    st.metric("Ergebnis", f"{st.session_state.score}/{total}")
    if st.session_state.score==total:
        st.balloons()
    if st.button("Nochmal", type="primary"):
        restart()
        st.rerun()
