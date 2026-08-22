import streamlit as st
import random
import os

st.set_page_config(page_title="Gabelstapler Variante 4", page_icon="🏗️", layout="centered")

QUESTIONS = [
    {"id": 1, "frage": "Wie fährt man mit dem beladenen Gabelstapler ein Gefälle hinunter?", "image": None, "options": ['Die Last wird "bergseitig" geführt;', 'Auf keinen Fall im Leerlauf;', 'Die Last wird "talseitig" geführt;', 'Der Gabelstapler darf beladen grundsätzlich kein Gefälle befahren.'], "correct": [0, 1]},
    {"id": 2, "frage": "Eine Kiste mit 1600 kg soll gestapelt werden. Unter welchen Bedingungen ist dies möglich?", "image": "images/2.jpg", "options": ['Lastschwerpunkt 600 mm und Höhe 4,5 m;', 'Lastschwerpunkt 600 mm und Höhe 5,5 m;', 'Lastschwerpunkt 700 mm und Höhe 4,0 m;', 'Lastschwerpunkt 500 mm und Höhe 5,0 m.'], "correct": [0, 2]},
    {"id": 3, "frage": "Darf der Gabelstaplerfahrer Arbeitskollegen mitnehmen?", "image": None, "options": ['In keinem Fall;', 'Kurze Strecke;', 'Wenn Kollege in Eile ist;', 'Wenn besonderer Sitz-Stehplatz mit Haltegriffen vorhanden ist und Unternehmer das Mitfahren zugelassen hat.'], "correct": [3]},
    {"id": 4, "frage": "Wann wäre die nächste Prüfung bei der dargestellten Prüfplakette erforderlich?", "image": "images/4.jpg", "options": ['Februar 2006;', 'August 2006;', 'Februar 2007;', 'August 2007.'], "correct": [0]},
    {"id": 5, "frage": "Welche Aufgaben gehören zu den Pflegearbeiten, die der Fahrer durchführen darf?", "image": None, "options": ['Kühlwasserkontrolle;', 'Batteriepflege;', 'Lenkung instandsetzen;', 'Ölstandskontrolle;', 'Bremsbeläge erneuern.'], "correct": [0, 1, 3]},
    {"id": 6, "frage": "Welche Fördermittel sind zu den Flurförderzeugen zu rechnen?", "image": None, "options": ['Gabelhubwagen;', 'Gabelstapler;', 'Schubmaststapler;', 'Bergwerkslore;', 'Kran-Laufkatze.'], "correct": [0, 1, 2]},
    {"id": 10, "frage": "Was tun bei undichtem Hydraulikschlauch?", "image": None, "options": ['Ölstand prüfen und nachfüllen;', 'Mit Isolierband abdichten;', 'Nur halbe Tragkraft nutzen;', 'Sofort stilllegen und Schaden melden;', 'Nach Feierabend Bescheid sagen.'], "correct": [3]},
    {"id": 11, "frage": "Wann darf ein geschulter Fahrer (18 Jahre) einen Gabelstapler benutzen?", "image": None, "options": ['Nur bei Tag;', 'Immer wenn Schlüssel steckt;', 'Nur bei Nacht;', 'Er muss ausdrücklich beauftragt sein;', 'Immer wenn Ladung schwerer als Diagramm.'], "correct": [3]},
    {"id": 12, "frage": "Was ist beim Befahren von Ladebrücken zu beachten?", "image": "images/12.jpg", "options": ['Überhaupt nichts;', 'Darf nur rückwärts;', 'Tragfähigkeit der Ladebrücke;', 'Tragfähigkeit der Ladefläche;', 'Befahren von Anhängern nach UVV verboten.'], "correct": [2, 3]},
    {"id": 13, "frage": "Welche Bezeichnung ist für das Gebotszeichen blau/weiss richtig? (Stiefel)", "image": "images/13.jpg", "options": ['Fussweg benutzen;', 'Heizraum für Schuhe;', 'Festes Schuhwerk verboten;', 'Schutzschuhe tragen.'], "correct": [3]},
    {"id": 14, "frage": "Auf welche maximale Höhe dürfen Sie Palette 800x1200 mm, 1100 kg heben?", "image": "images/14.jpg", "options": ['4,0 m;', '4,5 m;', '5,0 m;', '5,5 m;', '3,5 m.'], "correct": [2]},
    {"id": 15, "frage": "Welche Verkehrswege dürfen mit Flurförderzeugen befahren werden?", "image": None, "options": ['Nur die von der Unternehmensleitung festgelegten Wege;', 'Nur Hauptverkehrswege;', 'Keine besondere Vorschrift;', 'Nur ganz ebene Wege;', 'Nur Fusswege.'], "correct": [0]},
    {"id": 16, "frage": "Wann darf ein Gabelstapler bei hochgefahrener Arbeitsbühne verlassen werden?", "image": None, "options": ['Kurzzeitig;', 'Nur bei Feststellbremse und Motor aus;', 'Nur bei Dienstschluss;', 'Nie;', 'Nur bei ebenem Boden.'], "correct": [3]},
    {"id": 17, "frage": "Welche Flüssigkeit befindet sich in der Batterie?", "image": None, "options": ['Destilliertes Wasser;', 'Verdünnte Schwefelsäure;', 'Salzsäure;', 'Leitungswasser.'], "correct": [1]},
    {"id": 18, "frage": "Auf welcher Darstellung ist der Lastschwerpunktabstand am größten?", "image": "images/18.jpg", "options": ['a) Darstellung a', 'b) Darstellung b', 'c) Darstellung c'], "correct": [0]},
    {"id": 19, "frage": "Stellen mit Öl, Fett, Benzin getränkte Putzlappen große Brandgefahr dar?", "image": None, "options": ['Nein, nicht brennbar;', 'Nein, mit Fett gemischt brennt nicht;', 'Ja, Selbstentzündung möglich;', 'Ja, Dämpfe bilden explosionsfähiges Gemisch.'], "correct": [2, 3]},
    {"id": 20, "frage": "Welche Arbeiten gehören zur Abfahrtskontrolle Diesel-Stapler?", "image": None, "options": ['Waschen;', 'Gabelzinken auf Beschädigung prüfen;', 'Luftfilter reinigen;', 'Motorölstand prüfen.'], "correct": [1, 3]},
]

if "order" not in st.session_state:
    st.session_state.order = random.sample(range(len(QUESTIONS)), len(QUESTIONS))
    st.session_state.checked = False

st.title("🏗️ Gabelstapler - Variante 4")

c1, c2 = st.columns(2)
with c1:
    if st.button("🔀 Перемешать"):
        st.session_state.order = random.sample(range(len(QUESTIONS)), len(QUESTIONS))
        st.session_state.checked = False
        st.rerun()
with c2:
    if st.button("🔄 Сбросить"):
        st.session_state.checked = False
        st.rerun()

st.divider()
score = 0
for idx, q_idx in enumerate(st.session_state.order):
    q = QUESTIONS[q_idx]
    st.subheader(f"{idx+1}. {q['frage']}")
    if q["image"] and os.path.exists(q["image"]):
        st.image(q["image"], width=450)

    selected = []
    for i, opt in enumerate(q["options"]):
        if st.checkbox(opt, key=f"q{q['id']}_{i}_{idx}"):
            selected.append(i)

    if st.session_state.checked:
        if set(selected) == set(q["correct"]):
            st.success("✅ Правильно")
            score += 1
        else:
            corr = ", ".join([q["options"][c] for c in q["correct"]])
            st.error(f"❌ Правильно: {corr}")
    st.divider()

if st.button("✅ Проверить", type="primary"):
    st.session_state.checked = True
    st.rerun()

if st.session_state.checked:
    st.metric("Результат", f"{score} / {len(QUESTIONS)}")
    if score == len(QUESTIONS):
        st.balloons()
