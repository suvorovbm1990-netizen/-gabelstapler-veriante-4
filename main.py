import streamlit as st
import random
import os

st.set_page_config(page_title="Gabelstapler Prüfung - Variante 4", page_icon="🏗️", layout="centered")

# --- БАЗА ВОПРОСОВ ---
# correct - список индексов правильных ответов
QUESTIONS = [
    {
        "id": 1,
        "frage": "Wie fährt man mit dem beladenen Gabelstapler ein Gefälle hinunter?",
        "image": None,
        "options": [
            "Die Last wird \"bergseitig\" geführt;",
            "Auf keinen Fall im Leerlauf;",
            "Die Last wird \"talseitig\" geführt;",
            "Der Gabelstapler darf beladen grundsätzlich kein Gefälle befahren."
        ],
        "correct": [0, 1]
    },
    {
        "id": 2,
        "frage": "Eine Kiste mit einem Gewicht von 1600 kg soll gestapelt werden. Unter welchen Bedingungen ist dies möglich?",
        "image": "images/2.jpg",
        "options": [
            "Der Lastschwerpunktabstand beträgt 600 mm und die Stapelhöhe 4,5 m;",
            "Der Lastschwerpunktabstand beträgt 600 mm und die Stapelhöhe 5,5 m;",
            "Der Lastschwerpunktabstand beträgt 700 mm und die Stapelhöhe 4,0 m;",
            "Der Lastschwerpunktabstand beträgt 500 mm und die Stapelhöhe 5,0 m."
        ],
        "correct": [0, 2]
    },
    {
        "id": 3,
        "frage": "Darf der Gabelstaplerfahrer Arbeitskollegen auf dem Gabelstapler mitnehmen?",
        "image": None,
        "options": [
            "In keinem Fall;",
            "Wenn es sich um eine kurze Strecke handelt;",
            "Wenn der Arbeitskollege in Eile ist;",
            "Wenn auf dem Gabelstapler ein besonderer Sitz- oder Stehplatz mit Haltegriffen vorhanden ist und der Unternehmer das Mitfahren ausdrücklich zugelassen hat."
        ],
        "correct": [3]
    },
    {
        "id": 4,
        "frage": "Die am Gabelstapler sichtbar angebrachte Prüfplakette erleichtert es dem Fahrer, die erforderlichen Prüffristen mit zu überwachen. Wann wäre die nächste Sachkundigenprüfung bei der im Bild dargestellten Prüfplakette erforderlich?",
        "image": "images/4.jpg",
        "options": ["Februar 2006;", "August 2006;", "Februar 2007;", "August 2007."],
        "correct": [0]
    },
    {
        "id": 5,
        "frage": "Welche Aufgaben gehören zu den Pflegearbeiten am Gabelstapler, die der Fahrer durchführen darf?",
        "image": None,
        "options": ["Kühlwasserkontrolle;", "Batteriepflege;", "Lenkung instandsetzen;", "Ölstandskontrolle;", "Bremsbeläge erneuern."],
        "correct": [0, 1, 3]
    },
    {
        "id": 6,
        "frage": "Welche der folgenden Fördermittel sind zu den Flurförderzeugen zu rechnen?",
        "image": None,
        "options": ["Gabelhubwagen;", "Gabelstapler;", "Schubmaststapler;", "Bergwerkslore (Schienengefährt);", "Kran-Laufkatze."],
        "correct": [0, 1, 2]
    },
    {
        "id": 10,
        "frage": "Was müssen Sie tun, wenn Sie an einem Gabelstapler einen undichten Hydraulikschlauch entdecken?",
        "image": None,
        "options": [
            "Regelmäßig den Ölstand überprüfen und nachfüllen;",
            "Den Hydraulikschlauch mit Spezial-Isolierband abdichten;",
            "Nur noch die Hälfte der Tragkraft nutzen;",
            "Gabelstapler sofort stilllegen und den Schaden melden;",
            "Nach Feierabend in der Werkstatt Bescheid sagen."
        ],
        "correct": [3]
    },
    {
        "id": 11,
        "frage": "Wann darf ein geschulter Gabelstaplerfahrer, der schon 18 Jahre alt ist, einen Gabelstapler benutzen?",
        "image": None,
        "options": [
            "Nur bei Tag;",
            "Immer, wenn der Zündschlüssel steckt;",
            "Nur bei Nacht;",
            "Er muss ausdrücklich mit der Führung des Gabelstaplers beauftragt sein;",
            "Immer, wenn die Ladung schwerer ist, als das Traglastdiagramm aussagt."

Богдан Суворов, [22.08.2026 16:50]
],
        "correct": [3]
    },
    {
        "id": 12,
        "frage": "Was ist beim Befahren von Ladebrücken zu beachten?",
        "image": "images/12.jpg",
        "options": [
            "Überhaupt nichts;",
            "Darf nur rückwärts befahren werden;",
            "Die Tragfähigkeit der Ladebrücke;",
            "Die Tragfähigkeit der Ladefläche;",
            "Das Befahren von Anhängern mit Flurförderzeugen ist nach UVV grundsätzlich verboten."
        ],
        "correct": [2, 3]
    },
    {
        "id": 13,
        "frage": "Welche Bezeichnung ist für das untenstehende Gebotszeichen richtig? Farben: blau/weiß [Знак - сапоги]",
        "image": "images/13.jpg",
        "options": ["Fußweg benutzen;", "Heizraum für Schuhe;", "Festes Schuhwerk verboten;", "Schutzschuhe tragen."],
        "correct": [3]
    },
    {
        "id": 14,
        "frage": "Auf welche maximale Höhe dürfen Sie mit diesem Gabelstapler eine Palette mit den Maßen 800 x 1200 mm heben, die 1100 kg wiegt?",
        "image": "images/14.jpg",
        "options": ["4,0 m;", "4,5 m;", "5,0 m;", "5,5 m;", "3,5 m."],
        "correct": [2]
    },
    {
        "id": 15,
        "frage": "Welche Verkehrswege dürfen mit Flurförderzeugen befahren werden?",
        "image": None,
        "options": ["Nur die von der Unternehmensleitung festgelegten Wege;", "Nur die Hauptverkehrswege;", "Es gibt keine besondere Vorschrift;", "Nur ganz ebene Wege;", "Nur Fußwege."],
        "correct": [0]
    },
    {
        "id": 16,
        "frage": "Wann darf ein Gabelstapler bei hochgefahrener Arbeitsbühne vom Fahrer verlassen werden?",
        "image": None,
        "options": ["Kurzzeitig;", "Nur bei angezogener Feststellbremse und abgeschaltetem Motor;", "Nur bei Dienstschluss;", "Nie;", "Nur bei völlig ebenem Boden."],
        "correct": [3]
    },
    {
        "id": 17,
        "frage": "Welche Flüssigkeit befindet sich in der Batterie eines Gabelstaplers?",
        "image": None,
        "options": ["Destilliertes Wasser;", "Verdünnte Schwefelsäure;", "Salzsäure;", "Leitungswasser."],
        "correct": [1]
    },
    {
        "id": 18,
        "frage": "Auf welcher Darstellung ist der Lastschwerpunktabstand am größten?",
        "image": "images/18.jpg",
        "options": ["a) Last weit hinten am Gabelrücken", "b) Last flach und nah", "c) Last hochkant direkt am Rücken"],
        "correct": [0]
    },
    {
        "id": 19,
        "frage": "Stellen mit Öl, Fett oder Benzin getränkte Putzlappen eine besonders große Brandgefahr dar?",
        "image": None,
        "options": [
            "Nein, da diese Putzlappen nicht brennbar sind;",
            "Nein, Öl, das mit Fett und Benzin gemischt ist, brennt nicht mehr;",
            "Ja, es kann zur Selbstentzündung kommen;",
            "Ja, es können sich Dämpfe mit dem Luftsauerstoff zu einem explosionsfähigen Gemisch bilden."
        ],
        "correct": [2, 3]
    },
    {
        "id": 20,
        "frage": "Welche Arbeiten gehören zur Abfahrtskontrolle bei einem Diesel-Gabelstapler?",
        "image": None,
        "options": ["Sie waschen Ihren Gabelstapler;", "Sie prüfen die Gabelzinken auf Beschädigung;", "Sie reinigen den Luftfilter;", "Sie prüfen den Motorölstand."],
        "correct": [1, 3]
    },
]

# --- ЛОГИКА ПРИЛОЖЕНИЯ ---
if "order" not in st.session_state:
    st.session_state.order = random.sample(range(len(QUESTIONS)), len(QUESTIONS))
    st.session_state.answers = {}
    st.session_state.checked = False

st.title("🏗️ Übungsfragen Variante 4 - Gabelstapler")

col1, col2 = st.columns(2)
with col1:
    if st.button("🔀 Перемешать вопросы"):
        st.session_state.order = random.sample(range(len(QUESTIONS)), len(QUESTIONS))
        st.session_state.answers = {}
        st.session_state.checked = False
        st.rerun()
with col2:
    if st.button("🔄 Сбросить ответы"):
        st.session_state.answers = {}
        st.session_state.checked = False
        st.rerun()

st.divider()

Богдан Суворов, [22.08.2026 16:50]
score = 0
for idx, q_idx in enumerate(st.session_state.order):
    q = QUESTIONS[q_idx]
    st.subheader(f"{idx+1}. {q['frage']}")

    if q["image"] and os.path.exists(q["image"]):
        st.image(q["image"], width=500)
    elif q["image"]:
        st.info(f"🖼️ Добавь картинку сюда: {q['image']}")

    # checkboxes для множественного выбора
    selected = []
    for i, opt in enumerate(q["options"]):
        key = f"q{q['id']}_{i}_{idx}"
        if st.checkbox(opt, key=key):
            selected.append(i)

    st.session_state.answers[q["id"]] = selected

    if st.session_state.checked:
        correct_set = set(q["correct"])
        selected_set = set(selected)
        if correct_set == selected_set:
            st.success("✅ Правильно")
            score += 1
        else:
            correct_text = ", ".join([q["options"][c] for c in q["correct"]])
            st.error(f"❌ Неправильно. Правильно: {correct_text}")
    st.divider()

if st.button("✅ Проверить результат", type="primary"):
    st.session_state.checked = True
    st.rerun()

if st.session_state.checked:
    st.metric("Итог", f"{score} / {len(QUESTIONS)} правильно")
    if score == len(QUESTIONS):
        st.balloons()
        st.success("Отлично! Ты готов к экзамену.")
    elif score / len(QUESTIONS) > 0.8:
        st.warning("Хорошо, но повтори ошибки!")
    else:
        st.error("Нужно еще подучить.")
