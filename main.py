import streamlit as st
import random
import os
import glob

st.set_page_config(page_title="Gabelstapler Quiz Variante 4", page_icon="🏗️", layout="centered")

QUESTIONS = [
    {"id": 1, "keywords": [], "frage": "Wie fährt man mit dem beladenen Gabelstapler ein Gefälle hinunter?", "image": None, "options": ['Die Last wird "bergseitig" geführt;', 'Auf keinen Fall im Leerlauf;', 'Die Last wird "talseitig" geführt;', 'Der Gabelstapler darf beladen kein Gefälle befahren.'], "correct": [0, 1]},
    {"id": 2, "keywords": ["2000", "diagramm", "tragf"], "frage": "Eine Kiste mit 1600 kg soll gestapelt werden. Unter welchen Bedingungen ist dies möglich?", "image": "2", "options": ['Lastschwerpunkt 600 mm und Höhe 4,5 m;', 'Lastschwerpunkt 600 mm und Höhe 5,5 m;', 'Lastschwerpunkt 700 mm und Höhe 4,0 m;', 'Lastschwerpunkt 500 mm und Höhe 5,0 m.'], "correct": [0, 2]},
    {"id": 4, "keywords": ["pruf", "plakette", "pfuf", "püf"], "frage": "Wann wäre die nächste Prüfung bei der dargestellten Prüfplakette erforderlich?", "image": "4", "options": ['Februar 2006;', 'August 2006;', 'Februar 2007;', 'August 2007.'], "correct": [0]},
    {"id": 12, "keywords": ["ladebrucke", "ladebrücke"], "frage": "Was ist beim Befahren von Ladebrücken zu beachten?", "image": "12", "options": ['Überhaupt nichts;', 'Darf nur rückwärts;', 'Tragfähigkeit der Ladebrücke;', 'Tragfähigkeit der Ladefläche;', 'Befahren von Anhängern nach UVV verboten.'], "correct": [2, 3]},
    {"id": 13, "keywords": ["gebotszeichen", "schuhe", "stiefel"], "frage": "Welche Bezeichnung ist für das Gebotszeichen blau/weiss richtig?", "image": "13", "options": ['Fussweg benutzen;', 'Heizraum für Schuhe;', 'Festes Schuhwerk verboten;', 'Schutzschuhe tragen.'], "correct": [3]},
    {"id": 14, "keywords": ["1500"], "frage": "Auf welche maximale Höhe dürfen Sie Palette 800x1200 mm, 1100 kg heben?", "image": "14", "options": ['4,0 m;', '4,5 m;', '5,0 m;', '5,5 m;', '3,5 m.'], "correct": [2]},
    {"id": 18, "keywords": ["pallet", "palette", "3 kartinki"], "frage": "Auf welcher Darstellung ist der Lastschwerpunktabstand am größten?", "image": "18", "options": ['a) Last weit vorn - größter Abstand', 'b) Last nah', 'c) Last direkt am Rücken'], "correct": [0]},
    {"id": 3, "keywords": [], "frage": "Darf der Gabelstaplerfahrer Arbeitskollegen mitnehmen?", "image": None, "options": ['In keinem Fall;', 'Kurze Strecke;', 'Wenn Kollege in Eile ist;', 'Wenn besonderer Sitz mit Haltegriffen vorhanden ist und Unternehmer das Mitfahren zugelassen hat.'], "correct": [3]},
    {"id": 5, "keywords": [], "frage": "Welche Aufgaben gehören zu den Pflegearbeiten, die der Fahrer durchführen darf?", "image": None, "options": ['Kühlwasserkontrolle;', 'Batteriepflege;', 'Lenkung instandsetzen;', 'Ölstandskontrolle;', 'Bremsbeläge erneuern.'], "correct": [0, 1, 3]},
    {"id": 6, "keywords": [], "frage": "Welche Fördermittel sind zu den Flurförderzeugen zu rechnen?", "image": None, "options": ['Gabelhubwagen;', 'Gabelstapler;', 'Schubmaststapler;', 'Bergwerkslore;', 'Kran-Laufkatze.'], "correct": [0, 1, 2]},
    {"id": 10, "keywords": [], "frage": "Was tun bei undichtem Hydraulikschlauch?", "image": None, "options": ['Ölstand prüfen;', 'Mit Isolierband abdichten;', 'Nur halbe Tragkraft nutzen;', 'Sofort stilllegen und Schaden melden;', 'Nach Feierabend Bescheid sagen.'], "correct": [3]},
    {"id": 11, "keywords": [], "frage": "Wann darf ein geschulter Fahrer (18 Jahre) einen Gabelstapler benutzen?", "image": None, "options": ['Nur bei Tag;', 'Immer wenn Schlüssel steckt;', 'Nur bei Nacht;', 'Er muss ausdrücklich beauftragt sein;', 'Immer wenn Ladung schwerer als Diagramm.'], "correct": [3]},
    {"id": 15, "keywords": [], "frage": "Welche Verkehrswege dürfen mit Flurförderzeugen befahren werden?", "image": None, "options": ['Nur die von der Unternehmensleitung festgelegten Wege;', 'Nur Hauptverkehrswege;', 'Keine besondere Vorschrift;', 'Nur ganz ebene Wege;', 'Nur Fusswege.'], "correct": [0]},
    {"id": 16, "keywords": [], "frage": "Wann darf ein Gabelstapler bei hochgefahrener Arbeitsbühne verlassen werden?", "image": None, "options": ['Kurzzeitig;', 'Nur bei Feststellbremse und Motor aus;', 'Nur bei Dienstschluss;', 'Nie;', 'Nur bei ebenem Boden.'], "correct": [3]},
    {"id": 17, "keywords": [], "frage": "Welche Flüssigkeit befindet sich in der Batterie?", "image": None, "options": ['Destilliertes Wasser;', 'Verdünnte Schwefelsäure;', 'Salzsäure;', 'Leitungswasser.'], "correct": [1]},
    {"id": 19, "keywords": [], "frage": "Stellen mit Öl, Fett, Benzin getränkte Putzlappen große Brandgefahr dar?", "image": None, "options": ['Nein, nicht brennbar;', 'Nein, mit Fett gemischt brennt nicht;', 'Ja, Selbstentzündung möglich;', 'Ja, Dämpfe bilden explosionsfähiges Gemisch.'], "correct": [2, 3]},
    {"id": 20, "keywords": [], "frage": "Welche Arbeiten gehören zur Abfahrtskontrolle Diesel-Stapler?", "image": None, "options": ['Waschen;', 'Gabelzinken auf Beschädigung prüfen;', 'Luftfilter reinigen;', 'Motorölstand prüfen.'], "correct": [1, 3]},
]

def find_image_smart(q):
    # ищем любой jpg/png в репо который подходит под вопрос
    all_files = glob.glob("**/*.jpg", recursive=True) + glob.glob("**/*.jpeg", recursive=True) + glob.glob("**/*.png", recursive=True) + glob.glob("*.jpg") + glob.glob("*.JPG")
    all_files = list(set(all_files))
    if not q["image"]:
        return None
    # если в вопросе есть keywords - ищем по ним
    for kw in q.get("keywords", []):
        for f in all_files:
            if kw.lower() in f.lower():
                return f
    # ищем по id в имени файла
    for f in all_files:
        fname = os.path.basename(f).lower()
        if f" {q['id']}.jpg" in fname or f"{q['id']}.jpg" == fname or f" {q['id']}" in fname or q["image"] in f:
            return f
    # точные пути
    for cand in [f"images/{q['image']}.jpg", f"images/{q['id']}.jpg", q.get("image")]:
        if cand and os.path.exists(cand):
            return cand
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
    st.progress(cur/total, text=f"Frage {cur+1}/{total} | Score: {st.session_state.score}")

if cur >= total:
    st.success(f"Fertig! {st.session_state.score}/{total}")
    if st.session_state.score == total:
        st.balloons()
    if st.button("🔄 Nochmal", type="primary"):
        reset()
        st.rerun()
else:
    q = QUESTIONS[st.session_state.order[cur]]
    st.subheader(f"{cur+1}. {q['frage']}")

    img_path = find_image_smart(q)
    if img_path and os.path.exists(img_path):
        st.image(img_path, use_container_width=True)
    elif q["image"] is not None:
        st.caption(f"Debug: suche Bild für Frage {q['id']}, gefunden: {img_path} | Dateien: {glob.glob('*.jpg')[:5]}")

    if len(q["correct"]) > 1:
        st.info("Mehrere Antworten möglich!")

    sel = []
    for i, opt in enumerate(q["options"]):
        if st.checkbox(opt, key=f"{cur}_{q['id']}_{i}", disabled=st.session_state.answered):
            sel.append(i)

    col1, col2 = st.columns(2)
    if not st.session_state.answered:
        with col1:
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
        with col2:
            if st.button("➡️ Nächste Frage", type="primary", use_container_width=True):
                st.session_state.current += 1
                st.session_state.answered = False
                st.rerun()

    st.divider()
    if st.button("🔀 Neu mischen"):
        reset()
        st.rerun()
        
