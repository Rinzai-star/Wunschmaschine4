import streamlit as st
import pandas as pd
from io import BytesIO

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
        self.reflexionen = {}
        self.todo_liste = []
    
    def ziel_eingeben(self):
        self.ziel = st.text_input("Was möchtest du manifestieren?")
    
    def frage_mit_reflexion(self, frage, key):
        antwort = st.radio(frage, ("Ja", "Nein", "Ich weiß es nicht"), key=key)
        if antwort == "Ja":
            self.reflexionen[key] = "✅ Alles im Einklang."
        elif antwort == "Nein":
            self.reflexionen[key] = "⚠️ Hier gibt es Blockaden. Überdenke dies."
            selbst_reflexion = st.text_area(f"Was hält dich hier zurück? (Notizen für dich)", key=f"notiz_{key}")
            self.reflexionen[key] += f"\n{selbst_reflexion}"
        else:
            self.reflexionen[key] = "❓ Du bist unsicher."
            ind_reflexion = st.text_area(f"Gibt es Aspekte, die zuerst geklärt werden müssen?", key=f"ind_notiz_{key}")
            self.reflexionen[key] += f"\n{ind_reflexion}"
    
    def manifestationsprozess(self):
        st.title("✨ Wunschmaschine ✨")
        self.ziel_eingeben()
        if self.ziel:
            self.frage_mit_reflexion("Essenz-Ebene: Entspricht dein Wunsch wirklich deinem höchsten Selbst?", "essenz")
            self.frage_mit_reflexion("Kausale Ebene: Glaubst du zu 100%, dass dein Wunsch möglich ist?", "kausal")
            self.frage_mit_reflexion("Energie-Ebene: Fühlst du dich bereits so, als wäre dein Wunsch erfüllt?", "energie")
            self.frage_mit_reflexion("Physische Ebene: Hast du bereits konkrete Handlungen unternommen?", "physisch")
            self.frage_mit_reflexion("Höheres Selbst: Vertraust du dem Universum und deiner Führung?", "hoeheres_selbst")

            if "⚠️" not in " ".join(self.reflexionen.values()):
                self.ergebnis = "🌟 Dein Ziel ist im vollständigen Alignment! Es wird sich schnell materialisieren. 🌟"
            else:
                self.ergebnis = "🔍 Es gibt Blockaden. Arbeite an diesen Themen für eine schnellere Manifestation."
                self.todo_liste = [f"📌 {key}: {val}" for key, val in self.reflexionen.items() if "⚠️" in val or "❓" in val]
            
            st.subheader("--- WUNSCHMASCHINEN-ANALYSE ---")
            st.write(f"🎯 Ziel: {self.ziel}")
            for key, val in self.reflexionen.items():
                st.write(val)
            
            st.success(self.ergebnis)
            if self.todo_liste:
                st.subheader("📝 Dein Handlungsplan:")
                for item in self.todo_liste:
                    st.write(item)
                
            self.download_protokoll()
    
    def download_protokoll(self):
        protokoll = f"Ziel: {self.ziel}\n\n"
        for key, val in self.reflexionen.items():
            protokoll += f"{key.capitalize()}: {val}\n\n"
        protokoll += f"Ergebnis: {self.ergebnis}\n\n"
        if self.todo_liste:
            protokoll += "To-Do-Liste:\n"
            for item in self.todo_liste:
                protokoll += f"- {item}\n"
        
        buffer = BytesIO()
        buffer.write(protokoll.encode())
        buffer.seek(0)
        st.download_button("📄 Protokoll als PDF herunterladen", buffer, file_name="Wunschmaschine_Protokoll.txt")

if __name__ == "__main__":
    tool = Wunschmaschine()
    tool.manifestationsprozess()

