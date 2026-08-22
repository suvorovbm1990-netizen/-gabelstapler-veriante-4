import streamlit as st
import random
import os

st.set_page_config(page_title="Gabelstapler Quiz", page_icon="🏗️", layout="centered")

QUESTIONS = [
    {"id": 1, "frage": "Wie fahrt man mit dem beladenen Gabelstapler ein Gefalle hinunter?", "image": None, "options": ['Die Last wird "bergseitig" gefuhrt;', 'Auf keinen Fall im Leerlauf;', 'Die Last wird "talseitig" gefuhrt;', 'Der Stapler darf beladen kein Gefalle befahren.'], "correct": [0, 1]},
    {"id": 2, "frage": "Kiste 1600 kg - wann stapeln moglich? (Diagramm)", "image": "Диаграмма Tragfähigkeit 2000kg.jpg", "options": ['Schwerpunkt 600 mm und Hohe 4,5 m;', 'Schwerpunkt 600 mm und Hohe 5,5 m;', 'Schwerpunkt 700 mm und Hohe 4,0 m;', 'Schwerpunkt 500 mm und Hohe 5,0 m.'], "correct": [0, 2]},
    {"id": 3, "frage": "Darf Fahrer Kollegen mitnehmen?", "image": None, "options": ['In keinem Fall;', 'Kurze Strecke;', 'Wenn Kollege in Eile ist;', 'Wenn Sitz mit Haltegriffen vorhanden und Unternehmer erlaubt hat.'], "correct": [3]},
    {"id": 4, "frage": "Wann nachste Prufung bei dieser Prufplakette?", "image": "Pfüfplakette.jpg", "options": ['Februar 2006;', 'August 2006;', 'Februar 2007;', 'August 2007.'], "correct": [0]},
    {"id": 5, "frage": "Pflegearbeiten die Fahrer darf?", "image": None, "options": ['Kuhlwasserkontrolle;', 'Batteriepflege;', 'Lenkung instandsetzen;', 'Olstandskontrolle;', 'Bremsbelage erneuern.'], "correct": [0, 1, 3]},
    {"id": 6, "frage": "Welche sind Flurforderzeuge?", "image": None, "options": ['Gabelhubwagen;', 'Gabelstapler;', 'Schubmaststapler;', 'Bergwerkslore;', 'Kran-Laufkatze.'], "correct": [0, 1, 2]},
    {"id": 10, "frage": "Was tun bei undichtem Hydraulikschlauch?", "image": None, "options": ['Olstand prufen;', 'Mit Isolierband abdichten;', 'Nur halbe Tragkraft;', 'Sofort stilllegen und Schaden melden;', 'Nach Feierabend sagen.'], "correct": [3]},
    {"id": 11, "frage": "Wann darf geschulter Fahrer (18 Jahre) Stapler benutzen?", "image": None, "options": ['Nur bei Tag;', 'Immer wenn Schlussel steckt;', 'Nur bei Nacht;', 'Er muss ausdrucklich beauftragt sein;', 'Immer wenn Ladung schwerer als Diagramm.'], "correct": [3]},
    {"id": 12, "frage": "Was beim Befahren von Ladebrucken beachten?", "image": "Ladebrücke.jpg", "options": ['Nichts;', 'Nur ruckwarts;', 'Tragfahigkeit der Ladebrucke;', 'Tragfahigkeit der Ladeflache;', 'Nach UVV verboten.'], "correct": [2, 3]},
    {"id": 13, "frage": "Gebotszeichen blau/weiss - was bedeutet?", "image": "Gebotszeichen Schuhe.jpg", "options": ['Fussweg benutzen;', 'Heizraum fur Schuhe;', 'Festes Schuhwerk verboten;', 'Schutzschuhe tragen.'], "correct": [3]},
    {"id": 14, "frage": "Palette 800x1200 mm, 1100 kg - max Hohe?", "image": "Tragfähigkeit 1500 kg.jpg", "options": ['4,0 m;', '4,5 m;', '5,0 m;', '5,5 m;', '3,5 m.'], "correct": [2]},
    {"id": 15, "frage": "Welche Verkehrswege durfen befahren werden?", "image": None, "options": ['Nur die von der Unternehmensleitung festgelegten Wege;', 'Nur Hauptverkehrswege;', 'Keine Vorschrift;', 'Nur ebene Wege;', 'Nur Fusswege.'], "correct": [0]},
    {"id": 16, "frage": "Wann darf Stapler bei hochgefahrener Buhne verlassen werden?", "image": None, "options": ['Kurzzeitig;', 'Nur bei Feststellbremse und Motor aus;', 'Nur bei Dienstschluss;', 'Nie;', 'Nur bei ebenem Boden.'], "correct": [3]},
    {"id": 17, "frage": "Welche Flussigkeit in der Batterie?", "image": None, "options": ['Destilliertes Wasser;', 'Verdunnte Schwefelsaure;', 'Salzsaure;', 'Leitungswasser.'], "correct": [1]},
    {"id": 18, "frage": "Wo ist Lastschwerpunktabstand am groessten?", "image": "3 картинки с паллетой.jpg", "options": ['Darstellung a - weit vorn', 'Darstellung b - nah', 'Darstellung c - direkt am Rucken'], "correct": [0]},
    {"id": 19, "frage": "Brandgefahr durch olgetrankte Putzlappen?", "image": None, "options": ['Nein, nicht brennbar;', 'Nein, mit Fett brennt nicht;', 'Ja, Selbstentzundung;', 'Ja, Dampfe bilden explosionsfahiges Gemisch.'], "correct": [2, 3]},
    {"id": 20, "frage": "Abfahrtskontrolle Diesel-Stapler?", "image": None, "options": ['Waschen;', 'Gabelzinken auf Beschadigung prufen;', 'Luftfilter reinigen;', 'Motorolstand prufen.'], "correct": [1, 3]},
]

if "order" not in st.session_state:
    st.session_state.order = random.sample(range(len(QUESTIONS)), len(QUESTIONS))
    st.session_state.current = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.last_correct = False

def reset_quiz():
    st.session_state.order = random.sample(range(len(QUESTIONS)), len(QUESTIONS))
    st.session_state.current = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.last_correct = False

total = len(QUESTIONS)
cur = st.session_state.current

if cur < total:
    st.progress(cur / total, text=f"Frage {cur+1} von {total} | Punkte: {st.session_state.score}")

if cur >= total:
    st.title("Fertig!")
    st.metric("Ergebnis", f"{st.session_state.score} / {total}")
    pct = st.session_state.score / total * 100
    if pct == 100:
        st.balloons()
        st.success("Perfekt 100%!")
    elif pct >= 80:
        st.success(f"{pct:.0f}% Sehr gut!")
    else:
        st.warning(f"{pct:.0f}% Noch uben!")
    if st.button("Nochmal starten", type="primary"):
        reset_quiz()
        st.rerun()
else:
    q_idx = st.session_state.order[cur]
    q = QUESTIONS[q_idx]
    st.subheader(f"Frage {cur+1}: {q['frage']}")

    if q["image"] and os.path.exists(q["image"]):
        st.image(q["image"], use_container_width=True)
    elif q["image"]:
        st.warning(f"Bild fehlt: {q['image']}")

    st.divider()
    if len(q["correct"]) > 1:
        st.caption("Mehrere Antworten moglich!")

    sel = []
    for i, opt in enumerate(q["options"]):
        k = f"q_{cur}_{q['id']}_{i}"
        if st.checkbox(opt, key=k, disabled=st.session_state.answered):
            sel.append(i)

    c1, c2 = st.columns(2)

    if not st.session_state.answered:
        with c1:
            if st.button("Antworten", type="primary", use_container_width=True):
                if not sel:
                    st.warning("Wahle eine Antwort!")
                else:
                    st.session_state.answered = True
                    if set(sel) == set(q["correct"]):
                        st.session_state.score += 1
                        st.session_state.last_correct = True
                    else:
                        st.session_state.last_correct = False
                    st.rerun()
    else:
        if st.session_state.last_correct:
            st.success("RICHTIG!")
        else:
            st.error("FALSCH!")
            txt = ", ".join([q["options"][x] for x in q["correct"]])
            st.info(f"Richtig: {txt}")
        with c2:
            if st.button("Nachste Frage", type="primary", use_container_width=True):
                st.session_state.current += 1
                st.session_state.answered = False
                st.rerun()

    st.divider()
    if st.button("Neu mischen"):
        reset_quiz()
        st.rerun()
