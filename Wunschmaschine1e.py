import streamlit as st

class Wunschmaschine:
    def __init__(self):
        self.ziel = ""
        self.essenz_check = ""
        self.kausal_check = ""
        self.energie_check = ""
        self.physisch_check = ""
        self.hoeheres_selbst = ""
        self.blockaden = ""
        self.ergebnis = ""
        self.reflexion = ""
        self.todo_liste = ""

    def ziel_eingeben(self):
        self.ziel = st.text_input("Was möchtest du manifestieren?")
    
    def essenz_pruefung(self):
        antwort = st.radio("Essenz-Ebene: Entspricht dein Wunsch wirklich deinem höchsten Selbst?", ("Ja", "Nein", "Ich weiß es nicht"))
        if antwort == "Ja":
            self.essenz_check = "✅ Dein Wunsch ist im Einklang mit deinem höchsten Selbst."
        elif antwort == "Nein":
            self.essenz_check = "⚠️ Dein Wunsch könnte aus Ego oder Mangeldenken stammen. Überdenke ihn."
            self.blockaden += "\n- Überlege, ob dein Wunsch aus Freude oder Angst stammt."
        else:
            self.essenz_check = "❓ Du bist unsicher."
            self.blockaden += "\n- Gibt es Aspekte in deinem Leben oder innere Themen, die zuerst geklärt werden müssen?"
    
    def kausal_pruefung(self):
        antwort = st.radio("Kausale Ebene: Glaubst du zu 100%, dass dein Wunsch möglich ist?", ("Ja", "Nein", "Ich weiß es nicht"))
        if antwort == "Ja":
            self.kausal_check = "✅ Deine innere Überzeugung unterstützt dein Ziel."
        elif antwort == "Nein":
            self.kausal_check = "⚠️ Deine Glaubenssätze blockieren dich."
            self.blockaden += "\n- Warum ist es nicht möglich? Gibt es Gegenbeweise?"
        else:
            self.kausal_check = "❓ Du bist unsicher."
            self.blockaden += "\n- Welche Glaubenssätze könnten dahinterstehen?"
    
    def energie_pruefung(self):
        antwort = st.radio("Energie-Ebene: Fühlst du dich bereits so, als wäre dein Wunsch erfüllt?", ("Ja", "Nein", "Ich weiß es nicht"))
        if antwort == "Ja":
            self.energie_check = "✅ Deine Schwingung ist bereits auf der Frequenz deines Wunsches."
        elif antwort == "Nein":
            self.energie_check = "⚠️ Deine Schwingung ist noch nicht auf der Frequenz des Ziels."
            self.blockaden += "\n- Welche Emotionen verbindest du mit deinem Wunsch? Wie fühlt es sich an für dich? Woran erinnert es dich?"
        else:
            self.energie_check = "❓ Du bist unsicher."
            self.blockaden += "\n- Was hindert dich daran, dich bereits jetzt erfüllt zu fühlen?"
    
    def physisch_pruefung(self):
        antwort = st.radio("Physische Ebene: Hast du bereits konkrete Handlungen unternommen?", ("Ja", "Nein", "Ich weiß es nicht"))
        if antwort == "Ja":
            self.physisch_check = "✅ Du handelst im Einklang mit deiner Manifestation."
        elif antwort == "Nein":
            self.physisch_check = "⚠️ Du hast noch keine Handlung gesetzt."
            self.blockaden += "\n- Welche ersten konkreten Schritte kannst du setzen?"
        else:
            self.physisch_check = "❓ Du bist unsicher."
            self.blockaden += "\n- Was hindert dich daran, aktiv zu werden?"
    
    def hoeheres_selbst_pruefung(self):
        antwort = st.radio("Höheres Selbst: Vertraust du dem Universum und deiner Führung?", ("Ja", "Nein", "Ich weiß es nicht"))
        if antwort == "Ja":
            self.hoeheres_selbst = "✅ Du bist in völliger Harmonie mit deiner höchsten Führung."
        elif antwort == "Nein":
            self.hoeheres_selbst = "⚠️ Du kämpfst gegen den Fluss des Universums."
            self.blockaden += "\n- Welche Erfahrungen haben dein Vertrauen ins Universum beeinflusst?"
        else:
            self.hoeheres_selbst = "❓ Du bist unsicher."
            self.blockaden += "\n- Wie könntest du lernen, mehr zu vertrauen?"
    
    def manifestieren(self):
        st.title("✨ Wunschmaschine ✨")
        self.ziel_eingeben()
        if self.ziel:
            self.essenz_pruefung()
            self.kausal_pruefung()
            self.energie_pruefung()
            self.physisch_pruefung()
            self.hoeheres_selbst_pruefung()

            st.subheader("--- WUNSCHMASCHINEN-ANALYSE ---")
            st.write(f"🎯 Ziel: {self.ziel}")
            st.write(self.essenz_check)
            st.write(self.kausal_check)
            st.write(self.energie_check)
            st.write(self.physisch_check)
            st.write(self.hoeheres_selbst)
            
            if "⚠️" not in (self.essenz_check + self.kausal_check + self.energie_check + self.physisch_check + self.hoeheres_selbst):
                self.ergebnis = "🌟 Dein Ziel ist im vollständigen Alignment! Es wird sich schnell materialisieren. 🌟"
            else:
                self.ergebnis = "🔍 Es gibt Blockaden. Arbeite an den Bereichen mit ⚠️ für eine schnellere Manifestation."
                st.warning(self.blockaden)
            
            st.success(self.ergebnis)
            
            self.todo_liste = st.text_area("📌 Notiere deine nächsten Schritte:")
            if st.button("Speichern & Herunterladen"):
                with open("wunsch_protokoll.txt", "w") as f:
                    f.write(f"Ziel: {self.ziel}\n{self.ergebnis}\nBlockaden: {self.blockaden}\nTo-Do-Liste: {self.todo_liste}")
                st.download_button("Download Protokoll", "wunsch_protokoll.txt")

if __name__ == "__main__":
    tool = Wunschmaschine()
    tool.manifestieren()

