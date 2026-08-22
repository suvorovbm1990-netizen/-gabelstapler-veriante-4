import streamlit as st
import random
import os

st.set_page_config(page_title="Gabelstapler Quiz", page_icon="🏗️", layout="centered")

# ТВОИ ФАЙЛЫ КАК НА СКРИНЕ - в корне репозитория
QUESTIONS = [
    {"id": 1, "frage": "Wie fährt man mit dem beladenen Gabelstapler ein Gefälle hinunter?", "image": None, "options": ['Die Last wird "bergseitig" geführt;', 'Auf keinen Fall im Leerlauf;', 'Die Last wird "talseitig" geführt;', 'Der Gabelstapler darf beladen kein Gefälle befahren.'], "correct": [0, 1]},
    {"id": 2, "frage": "Eine Kiste mit 1600 kg soll gestapelt werden. Unter welchen Bedingungen ist dies möglich?", "image": "Диаграмма Tragfähigkeit 2000kg.jpg", "options": ['Lastschwerpunkt 600 mm und Höhe 4,5 m;', 'Lastschwerpunkt 600 mm und Höhe 5,5 m;', 'Lastschwerpunkt 700 mm und Höhe 4,0 m;', 'Lastschwerpunkt 500 mm und Höhe 5,0 m.'], "correct": [0, 2]},
    {"id": 3, "frage": "Darf der Gabelstaplerfahrer Arbeitskollegen mitnehmen?", "image": None, "options": ['In keinem Fall;', 'Kurze Strecke;', 'Wenn Kollege in Eile ist;', 'Wenn besonderer Sitz mit Haltegriffen vorhanden ist und Unternehmer das Mitfahren zugelassen hat.'], "correct": [3]},
    {"id": 4, "frage": "Wann ist die nächste Prüfung bei dieser Prüfplakette fällig?", "image": "Pfüfplakette.jpg", "options": ['Februar 2006;', 'August 2006;', 'Februar 2007;', 'August 2007.'], "correct": [0]},
    {"id": 5, "frage": "Welche Aufgaben gehören zu den Pflegearbeiten, die der Fahrer darf?", "image": None, "options": ['Kühlwasserkontrolle;', 'Batteriepflege;', 'Lenkung instandsetzen;', 'Ölstandskontrolle;', 'Bremsbeläge erneuern.'], "correct": [0, 1, 3]},
    {"id": 6, "frage": "Welche Fördermittel sind zu den Flurförderzeugen zu rechnen?", "image": None, "options": ['Gabelhubwagen;', 'Gabelstapler;', 'Schubmaststapler;', 'Bergwerkslore;', 'Kran-Laufkatze.'], "correct": [0, 1, 2]},
    {"id": 10, "frage": "Was tun bei undichtem Hydraulikschlauch?", "image": None, "options": ['Ölstand prüfen;', 'Mit Isolierband abdichten;', 'Nur halbe Tragkraft nutzen;', 'Sofort stilllegen und Schaden melden;', 'Nach Feierabend sagen.'], "correct": [3]},
    {"id": 11, "frage": "Wann darf ein geschulter Fahrer (18 Jahre) Stapler benutzen?", "image": None, "options": ['Nur bei Tag;', 'Immer wenn Schlüssel steckt;', 'Nur bei Nacht;', 'Er muss ausdrücklich beauftragt sein;', 'Immer wenn Ladung schwerer als Diagramm.'], "correct": [3]},
    {"id": 12, "frage": "Was ist beim Befahren von Ladebrücken zu beachten?", "image": "Ladebrücke.jpg", "options": ['Nichts;', 'Nur rückwärts;', 'Tragfähigkeit der Ladebrücke;', 'Tragfähigkeit der Ladefläche;', 'Nach UVV verboten.'], "correct": [2, 3]},
    {"id": 13, "frage": "Welche Bezeichnung ist für das Gebotszeichen blau/weiss richtig?", "image": "Gebotszeichen Schuhe.jpg", "options": ['Fussweg benutzen;', 'Heizraum für Schuhe;', 'Festes Schuhwerk verboten;', 'Schutzschuhe tragen.'], "correct": [3]},
    {"id": 14, "frage": "Auf welche Höhe dürfen Sie Palette 800x1200 mm, 1100 kg heben?", "image": "Tragfähigkeit 1500 kg.jpg", "options": ['4,0 m;', '4,5 m;', '5,0 m;', '5,5 m;', '3,5 m.'], "correct": [2]},
    {"id": 15, "frage": "Welche Verkehrswege dürfen befahren werden?", "image": None, "options": ['Nur die von der Unternehmensleitung festgelegten Wege;', 'Nur Hauptverkehrswege;', 'Keine Vorschrift;', 'Nur ganz ebene Wege;', 'Nur Fusswege.'], "correct": [0]},
    {"id": 16, "frage": "Wann darf Stapler bei hochgefahrener Arbeitsbühne verlassen werden?", "image": None, "options": ['Kurzzeitig;', 'Nur bei Feststellbremse und Motor aus;', 'Nur bei Dienstschluss;', 'Nie;', 'Nur bei ebenem Boden.'], "correct": [3]},
    {"id": 17, "frage": "Welche Flüssigkeit in der Batterie?", "image": None, "options": ['Destilliertes Wasser;', 'Verdünnte Schwefelsäure;', 'Salzsäure;', 'Leitungswasser.'], "correct": [1]},
    {"id": 18, "frage": "Auf welcher Darstellung ist der Lastschwerpunktabstand am größten?", "image": "3 картинки с паллетой.jpg", "options": ['Darstellung a - Last weit vorn', 'Darstellung b - Last nah', 'Darstellung c - Last direkt am Rücken'], "correct": [0]},
    {"id": 19, "frage": "Stellen getränkte Putzlappen Brandgefahr dar?", "image": None, "options": ['Nein, nicht brennbar;', 'Nein, mit Fett brennt nicht;', 'Ja, Selbstentzündung;', 'Ja, Dämpfe bilden explosionsfähiges Gemisch.'], "correct": [2, 3]},
    {"id": 20, "frage": "Was gehört zur Abfahrtskontrolle Diesel-Stapler?", "image": None, "options": ['Waschen;', 'Gabelzinken auf Beschädigung prüfen;', 'Luftfilter reinigen;', 'Motorölstand prüfen.'], "correct": [1, 3]},
]

if "order" not in st.session_state:
    st.session_state.order = random.sample(range(len(QUESTIONS)), len(QUESTIONS))
    st.session_state.current = 0
    st.session_state.score = 0
    st.session_state.show_result = False
    st.session_state.answered = False

def reset_quiz():
    st.session_state.order = random.sample(range(len(QUESTIONS)), len(QUESTIONS))
    st.session_state.current = 0
    st.session_state.score = 0
    st.session_state.show_result = False
    st.session_state.answered = False

total = len(QUESTIONS)
current_idx = st.session_state.current

if current_idx < total:
    st.progress((current_idx)/total, text=f"Frage {current_idx+1} von {total} | Punkte: {st.session_state.score}")

if current_idx >= total:
    st.title("🏁 Fertig!")
    st.metric("Ergebnis", f"{st.session_state.score} / {total}")
    prozent = st.session_state.score / total * 100
    if prozent == 100:
        st.balloons()
        st.success("Perfekt! 100%")
    elif prozent >= 80:
        st.success(f"{prozent:.0f}% - Sehr gut!")
    else:
        st.warning(f"{prozent:.0f}% - Noch üben!")
    if st.button("🔄 Nochmal starten", type="primary"):
        reset_quiz()
        st.rerun()
else:
    q_global_idx = st.session_state.order[current_idx]
    q = QUESTIONS[q_global_idx]

    st.subheader(f"Frage {current_idx+1}: {q['frage']}")

    # --- ПОКАЗ КАРТИНКИ ---
    if q["image"]:
        if os.path.exists(q["image"]):
            st.image(q["image"], use_container_width=True)
        else:
            # пробуем найти похожий файл
            found = False
            for f in os.listdir('.'):
                if os.path.splitext(f)[0].lower() in os.path.splitext(q["image"])[0].lower() or os.path.splitext(q["image"])[0].lower() in f.lower():
                    if f.lower().endswith(('.jpg','.jpeg','.png')):
                        st.image(f, use_container_width=True)
                        found = True
                        break
            if not found:
                st.error(f"Bild nicht gefunden: {q['image']} - Dateien im Repo: {', '.join([f for f in os.listdir('.') if f.endswith('.jpg')])}")

    st.write("---")
    is_multi = len(q["correct"]) > 1
    if is_multi:
        st.caption("⚠️ Mehrere Antworten möglich!")

    user_selection = []
    for i, opt in enumerate(q["options"]):
        key = f"q_{current_idx}_{i}_{q['id']}"
        if st.checkbox(opt, key=key, disabled=st.session_state.answered):
            user_selection.append(i)

    col1, col2 = st.columns([1,1])
    with col1:
        if not st.session_state.answered:
            if st.button("✅ Antworten", type="primary", use_container_width=True):
                if not user_selection:
                    st.warning("Bitte wähle eine Antwort!")
                else:
                    st.session_state.answered = True
                    st.session_state.last_selection = user_selection
                    if set(user_selection) == set(q["correct"]):
                        st.session_state.score += 1
                        st.session_state.last_correct = True
                    else:
                        st.session_state.last_correct = False
                    st.rerun()
                    if st.session_state.answered:
        if st.session_state.last_correct:
            st.success("✅ RICHTIG!")
        else:
            st.error("❌ FALSCH!")
            correct_text = "\n".join([f"✔️ {q['options'][c]}" for c in q["correct"]])
            st.info(f"**Richtige Antwort:**\n{correct_text}")
        with col2:
            if st.button("➡️ Nächste Frage", type="primary", use_container_width=True):
                st.session_state.current += 1
                st.session_state.answered = False
                st.rerun()

    st.divider()
    if st.button("🔀 Neu mischen"):
        reset_quiz()
        st.rerun()
