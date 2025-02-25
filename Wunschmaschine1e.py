import streamlit as st
import datetime
import pandas as pd

class Wunschmaschine:
    def __init__(self):
        self.ziel = ""
        self.essenz_check = ""
        self.kausal_check = ""
        self.energie_check = ""
        self.physisch_check = ""
        self.hoeheres_selbst = ""
        self.reflexionen = []
        self.handlungsplan = []

    def ziel_eingeben(self):
        self.ziel = st.text_input("Was möchtest du manifestieren?")
    
    def essenz_pruefung(self):
        antwort = st.radio("Essenz-Ebene: Entspricht dein Wunsch wirklich deinem höchsten Selbst?", ("Ja", "Nein", "Ich weiß es nicht"))
        if antwort == "Ja":
            self.essenz_check = "✅ Dein Wunsch ist im Einklang mit deinem höchsten Selbst."
        elif antwort == "Nein":
            self.essenz_check = "⚠️ Dein Wunsch könnte aus Ego oder Mangeldenken stammen. Überdenke ihn."
            self.reflexionen.append("Überlege, ob dein Wunsch aus Freude oder Angst stammt.")
        else:
            self.essenz_check = "❓ Du bist unsicher."
            self.reflexionen.append("Was bedeutet dein höchstes Selbst für dich? Gibt es etwas, das vorher geklärt werden muss?")
    
    def kausal_pruefung(self):
        antwort = st.radio("Kausale Ebene: Glaubst du zu 100%, dass dein Wunsch möglich ist?", ("Ja", "Nein", "Ich weiß es nicht"))
        if antwort == "Ja":
            self.kausal_check = "✅ Deine innere Überzeugung unterstützt dein Ziel."
        elif antwort == "Nein":
            self.kausal_check = "⚠️ Deine Glaubenssätze blockieren dich."
            self.reflexionen.append("Warum ist dein Wunsch nicht möglich? Welche Überzeugungen hast du darüber?")
        else:
            self.kausal_check = "❓ Du bist unsicher."
            self.reflexionen.append("Woher stammt deine Unsicherheit? Kannst du Beispiele für ähnliche Erfolge finden?")
    
    def energie_pruefung(self):
        antwort = st.radio("Energie-Ebene: Fühlst du dich bereits so, als wäre dein Wunsch erfüllt?", ("Ja", "Nein", "Ich weiß es nicht"))
        if antwort == "Ja":
            self.energie_check = "✅ Deine Schwingung ist bereits auf der Frequenz deines Wunsches."
        elif antwort == "Nein":
            self.energie_check = "⚠️ Deine Schwingung ist noch nicht auf der Frequenz des Ziels."
            self.reflexionen.append("Wie fühlt sich die Erfüllung für dich an? Welche alten Emotionen tauchen auf?")
        else:
            self.energie_check = "❓ Du bist unsicher."
            self.reflexionen.append("Was hindert dich daran, dich bereits jetzt erfüllt zu fühlen?")
    
    def physisch_pruefung(self):
        antwort = st.radio("Physische Ebene: Hast du bereits konkrete Handlungen unternommen?", ("Ja", "Nein", "Ich weiß es nicht"))
        if antwort == "Ja":
            self.physisch_check = "✅ Du handelst im Einklang mit deiner Manifestation."
        elif antwort == "Nein":
            self.physisch_check = "⚠️ Du hast noch keine Handlung gesetzt."
            self.reflexionen.append("Welche ersten konkreten Schritte kannst du setzen?")
        else:
            self.physisch_check = "❓ Du bist unsicher."
            self.reflexionen.append("Was hindert dich daran, aktiv zu werden?")
    
    def hoeheres_selbst_pruefung(self):
        antwort = st.radio("Höheres Selbst: Vertraust du dem Universum und deiner Führung?", ("Ja", "Nein", "Ich weiß es nicht"))
        if antwort == "Ja":
            self.hoeheres_selbst = "✅ Du bist in völliger Harmonie mit deiner höchsten Führung."
        elif antwort == "Nein":
            self.hoeheres_selbst = "⚠️ Du kämpfst gegen den Fluss des Universums."
            self.reflexionen.append("Welche Erfahrungen haben dein Vertrauen ins Universum beeinflusst?")
        else:
            self.hoeheres_selbst = "❓ Du bist unsicher."
            self.reflexionen.append("Wie könntest du lernen, mehr zu vertrauen?")
    
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
                ergebnis = "🌟 Dein Ziel ist im vollständigen Alignment! Es wird sich schnell materialisieren. 🌟"
            else:
                ergebnis = "🔍 Es gibt Blockaden. Arbeite an den Reflexionspunkten für eine schnellere Manifestation."
            
            st.success(ergebnis)
            
            if self.reflexionen:
                st.subheader("📌 Reflexionspunkte")
                for punkt in self.reflexionen:
                    st.write("-", punkt)
            
            st.subheader("📝 Dein Handlungsplan")
            aktion = st.text_area("Welche Schritte möchtest du jetzt unternehmen?", "")
            if st.button("Speichern & Downloaden"):
                self.handlungsplan.append(aktion)
                df = pd.DataFrame({"Handlungsschritte": self.handlungsplan})
                df.to_csv("handlungsplan.csv", index=False)
                st.success("Dein Handlungsplan wurde gespeichert. Du kannst ihn jetzt herunterladen.")
                st.download_button("Download Handlungsplan", data=df.to_csv(index=False), file_name="handlungsplan.csv", mime="text/csv")

if __name__ == "__main__":
    tool = Wunschmaschine()
    tool.manifestieren()

