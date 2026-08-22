import streamlit as st
import random
import os

st.set_page_config(page_title="Gabelstapler Quiz Variante 4", page_icon="🏗️", layout="centered")

# СТАРЫЕ НАЗВАНИЯ ФАЙЛОВ КАК У ТЕБЯ В РЕПОЗИТОРИИ
QUESTIONS = [
    {"id": 1, "frage": "Wie fahrt man mit dem beladenen Gabelstapler ein Gefalle hinunter?", "file": None, "options": ['Die Last wird "bergseitig" gefuhrt;', 'Auf keinen Fall im Leerlauf;', 'Die Last wird "talseitig" gefuhrt;', 'Kein Gefalle befahren.'], "correct": [0, 1]},
    {"id": 2, "frage": "Eine Kiste mit 1600 kg soll gestapelt werden. Unter welchen Bedingungen ist dies moglich?", "file": "Диаграмма Tragfähigkeit 2000kg.jpg", "options": ['600 mm und 4,5 m;', '600 mm und 5,5 m;', '700 mm und 4,0 m;', '500 mm und 5,0 m.'], "correct": [0, 2]},
    {"id": 4, "frage": "Wann nachste Prufung bei dieser Prufplakette?", "file": "Pfüfplakette.jpg", "options": ['Februar 2006;', 'August 2006;', 'Februar 2007;', 'August 2007.'], "correct": [0]},
    {"id": 12, "frage": "Was beim Befahren von Ladebrucken beachten?", "file": "Ladebrücke.jpg", "options": ['Nichts;', 'Nur ruckwarts;', 'Tragfahigkeit der Ladebrucke;', 'Tragfahigkeit der Ladeflache;', 'Nach UVV verboten.'], "correct": [2, 3]},
    {"id": 13, "frage": "Gebotszeichen blau/weiss?", "file": "Gebotszeichen Schuhe.jpg", "options": ['Fussweg;', 'Heizraum;', 'Festes Schuhwerk verboten;', 'Schutzschuhe tragen.'], "correct": [3]},
    {"id": 14, "frage": "Palette 800x1200 mm, 1100 kg - max Hohe?", "file": "Tragfähigkeit 1500 kg.jpg", "options": ['4,0 m;', '4,5 m;', '5,0 m;', '5,5 m;', '3,5 m.'], "correct": [2]},
    {"id": 18, "frage": "Wo ist Lastschwerpunktabstand am groessten?", "file": "3 картинки с паллетой.jpg", "options": ['a) weit vorn', 'b) nah', 'c) direkt am Rucken'], "correct": [0]},
    {"id": 3, "frage": "Darf Fahrer Kollegen mitnehmen?", "file": None, "options": ['In keinem Fall;', 'Kurze Strecke;', 'Wenn in Eile;', 'Wenn Sitz mit Haltegriffen und erlaubt.'], "correct": [3]},
    {"id": 5, "frage": "Pflegearbeiten die Fahrer darf?", "file": None, "options": ['Kuhlwasser;', 'Batteriepflege;', 'Lenkung;', 'Olstand;', 'Bremsbelage.'], "correct": [0, 1, 3]},
    {"id": 6, "frage": "Welche sind Flurforderzeuge?", "file": None, "options": ['Gabelhubwagen;', 'Gabelstapler;', 'Schubmaststapler;', 'Bergwerkslore;', 'Kran-Laufkatze.'], "correct": [0, 1, 2]},
    {"id": 10, "frage": "Was tun bei undichtem Schlauch?", "file": None, "options": ['Olstand prufen;', 'Isolierband;', 'Halbe Tragkraft;', 'Sofort stilllegen;', 'Nach Feierabend.'], "correct": [3]},
    {"id": 11, "frage": "Wann darf 18jahriger Stapler benutzen?", "file": None, "options": ['Nur bei Tag;', 'Schlussel steckt;', 'Nur bei Nacht;', 'Muss beauftragt sein;', 'Wenn schwerer als Diagramm.'], "correct": [3]},
    {"id": 15, "frage": "Welche Verkehrswege?", "file": None, "options": ['Nur festgelegte Wege;', 'Nur Hauptwege;', 'Keine Vorschrift;', 'Nur ebene;', 'Nur Fusswege.'], "correct": [0]},
    {"id": 16, "frage": "Wann darf Stapler bei hoher Buhne verlassen werden?", "file": None, "options": ['Kurzzeitig;', 'Bremse+Motor aus;', 'Dienstschluss;', 'Nie;', 'Ebenem Boden.'], "correct": [3]},
    {"id": 17, "frage": "Flussigkeit in Batterie?", "file": None, "options": ['Destilliertes Wasser;', 'Verdunnte Schwefelsaure;', 'Salzsaure;', 'Leitungswasser.'], "correct": [1]},
    {"id": 19, "frage": "Brandgefahr Putzlappen?", "file": None, "options": ['Nein, nicht brennbar;', 'Nein, mit Fett nicht;', 'Ja, Selbstentzundung;', 'Ja, explosionsfahig.'], "correct": [2, 3]},
    {"id": 20, "frage": "Abfahrtskontrolle Diesel?", "file": None, "options": ['Waschen;', 'Gabelzinken prufen;', 'Luftfilter;', 'Olstand.'], "correct": [1, 3]},
]

# умный поиск файла - пробует и в корне и в папке images
def get_image(name):
    if not name:
        return None
    candidates = [
        name,
        f"images/{name}",
        f"./{name}",
        f"./images/{name}",
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    return None
    if "order" not in st.session_state:
    st.session_state.order = random.sample(range(len(QUESTIONS)), len(QUESTIONS))
    st.session_state.current = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.last_correct = False

def reset():
    st.session_state.order = random.sample(range(len(QUESTIONS)), len(QUESTIONS))
    st.session_state.current = 0
    st.session_state.score = 0
    st.session_state.answered = False

total = len(QUESTIONS)
cur = st.session_state.current

st.title("🏗️ Gabelstapler Quiz - Variante 4")

if cur < total:
    st.progress(cur/total, text=f"Frage {cur+1}/{total} | Punkte: {st.session_state.score}")

if cur >= total:
    st.success(f"Fertig! Ergebnis: {st.session_state.score}/{total}")
    if st.session_state.score == total:
        st.balloons()
    if st.button("Nochmal starten", type="primary"):
        reset()
        st.rerun()
else:
    q = QUESTIONS[st.session_state.order[cur]]
    st.subheader(f"{cur+1}. {q['frage']}")

    # ПОКАЗ КАРТИНКИ - СТАРЫЕ ИМЕНА
    if q["file"]:
        path = get_image(q["file"])
        if path:
            st.image(path, use_container_width=True)
        else:
            st.error(f"Bild nicht gefunden: {q['file']}")

    if len(q["correct"]) > 1:
        st.caption("Mehrere Antworten möglich!")

    sel = []
    for i, opt in enumerate(q["options"]):
        if st.checkbox(opt, key=f"{cur}_{q['id']}_{i}", disabled=st.session_state.answered):
            sel.append(i)

    c1, c2 = st.columns(2)
    if not st.session_state.answered:
        with c1:
            if st.button("✅ Antworten", type="primary", use_container_width=True):
                if not sel:
                    st.warning("Wähle eine Antwort!")
                else:
                    st.session_state.answered = True
                    st.session_state.last_correct = (set(sel) == set(q["correct"]))
                    if st.session_state.last_correct:
                        st.session_state.score += 1
                    st.rerun()
    else:
        if st.session_state.last_correct:
            st.success("✅ RICHTIG!")
        else:
            st.error("❌ FALSCH!")
            st.info("Richtig: " + ", ".join([q["options"][c] for c in q["correct"]]))
        with c2:
            if st.button("➡️ Nächste Frage", type="primary", use_container_width=True):
                st.session_state.current += 1
                st.session_state.answered = False
                st.rerun()

    st.divider()
    if st.button("🔀 Neu mischen"):
        reset()
        st.rerun()
