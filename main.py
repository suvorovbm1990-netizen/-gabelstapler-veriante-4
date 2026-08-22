import streamlit as st
import random
import os

st.set_page_config(page_title="Gabelstapler Quiz", page_icon="🏗️", layout="centered")

QUESTIONS = [
    {"f": "Wie fahrt man mit dem beladenen Gabelstapler ein Gefalle hinunter?", "img": None, "opts": ['Die Last wird "bergseitig" gefuhrt', 'Auf keinen Fall im Leerlauf', 'Die Last wird "talseitig" gefuhrt', 'Kein Gefalle befahren'], "c": [0,1]},
    {"f": "Kiste 1600 kg - wann stapeln moglich? (Diagramm beachten)", "img": "Диаграмма Tragfähigkeit 2000kg.jpg", "opts": ['600 mm und 4,5 m', '600 mm und 5,5 m', '700 mm und 4,0 m', '500 mm und 5,0 m'], "c": [0,2]},
    {"f": "Darf Fahrer Kollegen mitnehmen?", "img": None, "opts": ['In keinem Fall', 'Kurze Strecke', 'Wenn in Eile', 'Wenn Sitz mit Griffen und erlaubt'], "c": [3]},
    {"f": "Wann nachste Prufung bei dieser Prufplakette?", "img": "Pfüfplakette.jpg", "opts": ['Februar 2006', 'August 2006', 'Februar 2007', 'August 2007'], "c": [0]},
    {"f": "Welche Aufgaben darf Fahrer bei Pflege machen?", "img": None, "opts": ['Kuhlwasser', 'Batteriepflege', 'Lenkung instandsetzen', 'Olstand', 'Bremsbelage'], "c": [0,1,3]},
    {"f": "Welche sind Flurforderzeuge?", "img": None, "opts": ['Gabelhubwagen', 'Gabelstapler', 'Schubmaststapler', 'Bergwerkslore', 'Kran-Laufkatze'], "c": [0,1,2]},
    {"f": "Was tun bei undichtem Hydraulikschlauch?", "img": None, "opts": ['Olstand prufen', 'Isolierband', 'Halbe Tragkraft', 'Sofort stilllegen und melden', 'Nach Feierabend'], "c": [3]},
    {"f": "Wann darf 18-jahriger geschulter Fahrer Stapler nutzen?", "img": None, "opts": ['Nur bei Tag', 'Schlussel steckt', 'Nur bei Nacht', 'Muss beauftragt sein', 'Wenn schwerer als Diagramm'], "c": [3]},
    {"f": "Was beim Befahren von Ladebrucken beachten?", "img": "Ladebrücke.jpg", "opts": ['Nichts', 'Nur ruckwarts', 'Tragfahigkeit Ladebrucke', 'Tragfahigkeit Ladeflache', 'Nach UVV verboten'], "c": [2,3]},
    {"f": "Gebotszeichen blau/weiss mit Schuh - was bedeutet?", "img": "Gebotszeichen Schuhe.jpg", "opts": ['Fussweg', 'Heizraum', 'Festes Schuhwerk verboten', 'Schutzschuhe tragen'], "c": [3]},
    {"f": "Palette 800x1200 1100kg - max Hohe? (1500kg Diagramm)", "img": "Tragfähigkeit 1500 kg.jpg", "opts": ['4,0 m', '4,5 m', '5,0 m', '5,5 m', '3,5 m'], "c": [2]},
    {"f": "Welche Verkehrswege durfen befahren werden?", "img": None, "opts": ['Nur festgelegte Wege', 'Nur Hauptwege', 'Keine Vorschrift', 'Nur ebene', 'Nur Fusswege'], "c": [0]},
    {"f": "Wann darf Stapler bei hoher Buhne verlassen werden?", "img": None, "opts": ['Kurzzeitig', 'Bremse+Motor aus', 'Dienstschluss', 'Nie', 'Ebener Boden'], "c": [3]},
    {"f": "Flussigkeit in Batterie?", "img": None, "opts": ['Destilliertes Wasser', 'Verdunnte Schwefelsaure', 'Salzsaure', 'Leitungswasser'], "c": [1]},
    {"f": "Wo ist Lastschwerpunktabstand am groessten?", "img": "3 картинки с паллетой.jpg", "opts": ['a) weit vorn', 'b) nah', 'c) direkt am Rucken'], "c": [0]},
    {"f": "Brandgefahr durch olgetrankte Lappen?", "img": None, "opts": ['Nein', 'Nein mit Fett', 'Ja Selbstentzundung', 'Ja Dampfe explosiv'], "c": [2,3]},
    {"f": "Abfahrtskontrolle Diesel-Stapler?", "img": None, "opts": ['Waschen', 'Gabelzinken prufen', 'Luftfilter', 'Olstand'], "c": [1,3]},
]

# --- SESSION ---
if "idx" not in st.session_state:
    st.session_state.idx = 0
    st.session_state.score = 0
    st.session_state.order = random.sample(range(len(QUESTIONS)), len(QUESTIONS))
    st.session_state.answered = False
    st.session_state.correct = False

def next_q():
    st.session_state.idx += 1
    st.session_state.answered = False

def restart():
    st.session_state.idx = 0
    st.session_state.score = 0
    st.session_state.order = random.sample(range(len(QUESTIONS)), len(QUESTIONS))
    st.session_state.answered = False

# --- UI ---
total = len(QUESTIONS)
cur = st.session_state.idx
if cur < total:
    st.progress((cur)/total, text=f"Frage {cur+1} von {total} | Punkte: {st.session_state.score}")
    q = QUESTIONS[st.session_state.order[cur]]
    st.header(f"{q['f']}")
    
    # Bild - sucht in root und in images/
    if q["img"]:
        found = False
        for p in [q["img"], f"images/{q['img']}", f"./{q['img']}"]:
            if os.path.exists(p):
                st.image(p, use_container_width=True)
                found = True
                break
        if not found:
            st.warning(f"Bild {q['img']} nicht gefunden")

    if len(q["c"]) > 1:
        st.caption("Mehrere Antworten moglich!")

    # Antworten
    selected = []
    for i, opt in enumerate(q["opts"]):
        if st.checkbox(opt, key=f"{cur}_{i}", disabled=st.session_state.answered):
            selected.append(i)

    if not st.session_state.answered:
        if st.button("Antworten", type="primary", use_container_width=True):
            if not selected:
                st.warning("Bitte Antwort wahlen!")
            else:
                st.session_state.answered = True
                if set(selected) == set(q["c"]):
                    st.session_state.correct = True
                    st.session_state.score += 1
                else:
                    st.session_state.correct = False
                st.rerun()
    else:
        if st.session_state.correct:
            st.success("✅ RICHTIG!")
        else:
            st.error("❌ FALSCH!")
            richtig = ", ".join([q["opts"][i] for i in q["c"]])
            st.info(f"Richtig ist: {richtig}")
        
        if st.button("Weiter ➡️", type="primary", use_container_width=True):
            next_q()
            st.rerun()

    st.divider()
    if st.button("Neu mischen"):
        restart()
        st.rerun()

else:
    st.title("🏁 Fertig!")
    st.metric("Ergebnis", f"{st.session_state.score}/{total}")
    if st.session_state.score == total:
        st.balloons()
        st.success("Perfekt!")
    if st.button("Nochmal starten", type="primary"):
        restart()
        st.rerun()
