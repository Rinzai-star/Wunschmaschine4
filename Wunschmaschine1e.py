import streamlit as st
import pandas as pd
import io

class Wunschmaschine:
    def __init__(self):
        self.ziel = ""
        self.essenz_check = ""
        self.kausal_check = ""
        self.energie_check = ""
        self.physisch_check = ""
        self.hoeheres_selbst = ""
        self.blockaden = []
        self.ergebnis = ""

        self.reflexionsdaten = []

    def ziel_eingeben(self):
        self.ziel = st.text_input("🌀 Was möchtest du manifestieren?")
    
    def essenz_pruefung(self):
        antwort = st.radio("🌟 Essenz-Ebene: Entspricht dein Wunsch wirklich deinem höchsten Selbst?",
                           ("Ja", "Nein", "Ich weiß es nicht"))
        if antwort == "Ja":
            self.essenz_check = "✅ Dein Wunsch ist im Einklang mit deinem höchsten Selbst."
        elif antwort == "Nein":
            self.essenz_check = "⚠️ Dein Wunsch könnte aus Ego oder Mangeldenken stammen. Überdenke ihn."
            self.blockaden.append("Überlege, ob dein Wunsch aus Freude oder Angst stammt.")
        else:
            self.essenz_check = "❓ Du bist unsicher."
            reflexion = st.text_area("🔍 Was bedeutet dein höchstes Selbst für dich?")
            self.blockaden.append(reflexion)
    
    def kausal_pruefung(self):
        antwort = st.radio("🧠 Kausale Ebene: Glaubst du zu 100%, dass dein Wunsch möglich ist?",
                           ("Ja", "Nein", "Ich weiß es nicht"))
        if antwort == "Ja":
            self.kausal_check = "✅ Deine innere Überzeugung unterstützt dein Ziel."
        elif antwort == "Nein":
            self.kausal_check = "⚠️ Deine Glaubenssätze blockieren dich."
            reflexion = st.text_area("🔎 Warum ist es nicht möglich?")
            self.blockaden.append(reflexion)
        else:
            self.kausal_check = "❓ Du bist unsicher."
            reflexion = st.text_area("🧐 Woher stammt deine Unsicherheit?")
            self.blockaden.append(reflexion)
    
    def energie_pruefung(self):
        antwort = st.radio("💫 Energie-Ebene: Fühlst du dich bereits so, als wäre dein Wunsch erfüllt?",
                           ("Ja", "Nein", "Ich weiß es nicht"))
        if antwort == "Ja":
            self.energie_check = "✅ Deine Schwingung ist bereits auf der Frequenz deines Wunsches."
        elif antwort == "Nein":
            self.energie_check = "⚠️ Deine Schwingung ist noch nicht auf der Frequenz des Ziels."
            reflexion = st.text_area("🎭 Wie fühlt sich dein Wunsch für dich an? Woran erinnert er dich?")
            self.blockaden.append(reflexion)
        else:
            self.energie_check = "❓ Du bist unsicher."
            reflexion = st.text_area("🌀 Was hindert dich daran, dich bereits jetzt erfüllt zu fühlen?")
            self.blockaden.append(reflexion)
    
    def physisch_pruefung(self):
        antwort = st.radio("🔨 Physische Ebene: Hast du bereits konkrete Handlungen unternommen?",
                           ("Ja", "Nein", "Ich weiß es nicht"))
        if antwort == "Ja":
            self.physisch_check = "✅ Du handelst im Einklang mit deiner Manifestation."
        elif antwort == "Nein":
            self.physisch_check = "⚠️ Du hast noch keine Handlung gesetzt."
            reflexion = st.text_area("🚀 Welche ersten konkreten Schritte kannst du setzen?")
            self.blockaden.append(reflexion)
        else:
            self.physisch_check = "❓ Du bist unsicher."
            reflexion = st.text_area("🏁 Was hindert dich daran, aktiv zu werden?")
            self.blockaden.append(reflexion)
    
    def hoeheres_selbst_pruefung(self):
        antwort = st.radio("👁️ Höheres Selbst: Vertraust du dem Universum und deiner Führung?",
                           ("Ja", "Nein", "Ich weiß es nicht"))
        if antwort == "Ja":
            self.hoeheres_selbst = "✅ Du bist in völliger Harmonie mit deiner höchsten Führung."
        elif antwort == "Nein":
            self.hoeheres_selbst = "⚠️ Du kämpfst gegen den Fluss des Universums."
            reflexion = st.text_area("🌊 Welche Erfahrungen haben dein Vertrauen ins Universum beeinflusst?")
            self.blockaden.append(reflexion)
        else:
            self.hoeheres_selbst = "❓ Du bist unsicher."
            reflexion = st.text_area("🔮 Wie könntest du lernen, mehr zu vertrauen?")
            self.blockaden.append(reflexion)

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
            st.write(f"🎯 **Ziel:** {self.ziel}")
            st.write(self.essenz_check)
            st.write(self.kausal_check)
            st.write(self.energie_check)
            st.write(self.physisch_check)
            st.write(self.hoeheres_selbst)
            
            if "⚠️" not in (self.essenz_check + self.kausal_check + self.energie_check + self.physisch_check + self.hoeheres_selbst):
                self.ergebnis = "🌟 Dein Ziel ist im vollständigen Alignment! Es wird sich schnell materialisieren. 🌟"
            else:
                self.ergebnis = "🔍 Es gibt Blockaden. Arbeite an den Bereichen mit ⚠️ für eine schnellere Manifestation."
                st.warning("\n".join(self.blockaden))
            
            st.success(self.ergebnis)

            self.protokoll_download()

    def protokoll_download(self):
        st.subheader("📜 Manifestations-Protokoll herunterladen")
        
        protokoll_text = f"""
        ✨ **Wunschmaschine Protokoll** ✨

        🎯 **Ziel:** {self.ziel}

        🌟 **Essenz-Ebene:** {self.essenz_check}
        🧠 **Kausale Ebene:** {self.kausal_check}
        💫 **Energie-Ebene:** {self.energie_check}
        🔨 **Physische Ebene:** {self.physisch_check}
        👁️ **Höheres Selbst:** {self.hoeheres_selbst}

        🔍 **Erkannte Blockaden:**
        {"\n".join(self.blockaden)}

        🌟 **Endergebnis:** {self.ergebnis}
        """

        # Protokoll als Datei bereitstellen
        buffer = io.BytesIO()
        buffer.write(protokoll_text.encode())
        buffer.seek(0)

        st.download_button(
            label="📥 Protokoll als Textdatei herunterladen",
            data=buffer,
            file_name="wunschmaschine_protokoll.txt",
            mime="text/plain"
        )


if __name__ == "__main__":
    tool = Wunschmaschine()
    tool.manifestieren()
