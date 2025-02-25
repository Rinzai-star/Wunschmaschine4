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
            st.warning("🔍 Reflexionsübung:\n- Was bedeutet dein höchstes Selbst für dich?\n- Stelle dir vor, dein Wunsch ist erfüllt. Fühlt es sich nach Liebe oder nach Angst an?\n- Frage dich: Würde mein höheres Selbst diesen Wunsch aus tiefstem Herzen wählen?")

    def kausal_pruefung(self):
        antwort = st.radio("Kausale Ebene: Glaubst du zu 100%, dass dein Wunsch möglich ist?", ("Ja", "Nein", "Ich weiß es nicht"))
        if antwort == "Ja":
            self.kausal_check = "✅ Deine innere Überzeugung unterstützt dein Ziel."
        elif antwort == "Nein":
            self.kausal_check = "⚠️ Deine Glaubenssätze blockieren dich."
            self.blockaden += "\n- Gibt es Beweise, dass es nicht geht? Kannst du Gegenbeweise finden?"
        else:
            self.kausal_check = "❓ Du bist unsicher."
            st.warning("🔍 Reflexionsübung:\n- Welche Beweise hast du, dass es klappen könnte?\n- Gibt es Menschen, die das bereits geschafft haben?\n- Welcher kleine erste Schritt würde dir zeigen, dass dein Wunsch möglich ist?")

    def energie_pruefung(self):
        antwort = st.radio("Energie-Ebene: Fühlst du dich bereits so, als wäre dein Wunsch erfüllt?", ("Ja", "Nein", "Ich weiß es nicht"))
        if antwort == "Ja":
            self.energie_check = "✅ Deine Schwingung ist bereits auf der Frequenz deines Wunsches."
        elif antwort == "Nein":
            self.energie_check = "⚠️ Deine Schwingung ist noch nicht auf der Frequenz des Ziels."
            self.blockaden += "\n- Welche Emotionen verbindest du mit deinem Wunsch? Wie kannst du dich mehr in die Erfüllung hineinversetzen?"
        else:
            self.energie_check = "❓ Du bist unsicher."
            st.warning("🔍 Reflexionsübung:\n- Wie fühlt sich dein Leben an, wenn dein Wunsch erfüllt ist?\n- Spiele gedanklich mit dieser Realität – was verändert sich?\n- Mache eine Visualisierungsübung: Schließe die Augen und stelle dir vor, dein Wunsch ist wahr geworden.")

    def physisch_pruefung(self):
        antwort = st.radio("Physische Ebene: Hast du bereits konkrete Handlungen unternommen?", ("Ja", "Nein", "Ich weiß es nicht"))
        if antwort == "Ja":
            self.physisch_check = "✅ Du handelst im Einklang mit deiner Manifestation."
        elif antwort == "Nein":
            self.physisch_check = "⚠️ Du hast noch keine Handlung gesetzt."
            self.blockaden += "\n- Welche ersten konkreten Schritte kannst du setzen?"
        else:
            self.physisch_check = "❓ Du bist unsicher."
            st.warning("🔍 Reflexionsübung:\n- Was wäre der kleinste Schritt, den du heute unternehmen kannst?\n- Gibt es eine inspirierende Person, die du um Rat fragen kannst?\n- Schreibe 3 Ideen auf, wie du deinem Wunsch aktiv näher kommst.")

    def hoeheres_selbst_pruefung(self):
        antwort = st.radio("Höheres Selbst: Vertraust du dem Universum und deiner Führung?", ("Ja", "Nein", "Ich weiß es nicht"))
        if antwort == "Ja":
            self.hoeheres_selbst = "✅ Du bist in völliger Harmonie mit deiner höchsten Führung."
        elif antwort == "Nein":
            self.hoeheres_selbst = "⚠️ Du kämpfst gegen den Fluss des Universums."
            self.blockaden += "\n- Welche Erfahrungen haben dein Vertrauen ins Universum beeinflusst?"
        else:
            self.hoeheres_selbst = "❓ Du bist unsicher."
            st.warning("🔍 Reflexionsübung:\n- Welche Momente in deinem Leben haben dir gezeigt, dass du geführt wirst?\n- Was wäre, wenn das Universum bedingungslos für dich sorgt?\n- Stelle dir vor, dein Wunsch ist bereits erfüllt – wie fühlt sich das an?")

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

if __name__ == "__main__":
    tool = Wunschmaschine()
    tool.manifestieren()
