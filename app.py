import streamlit as st
import pandas as pd
import plotly.express as px

# Configuration de la page
st.set_page_config(page_title="Observatoire Grand Nokoué", layout="wide")

st.title("🏙️ Analyseur Spatial du Grand Nokoué")
st.sidebar.header("Paramètres d'analyse")

# --- FONCTIONNALITÉ 1 : CALCULATEUR ---
st.sidebar.subheader("Simulateur de trajet")
depart = st.sidebar.selectbox("Lieu de résidence", ["Abomey-Calavi", "Porto-Novo", "Sèmè-Kpodji", "Ouidah"])
km_prix = {"Abomey-Calavi": 16, "Porto-Novo": 32, "Sèmè-Kpodji": 18, "Ouidah": 38}

st.metric(label=f"Distance vers Cotonou", value=f"{km_prix[depart]} km")

# --- FONCTIONNALITÉ 2 : GRAPHIQUE INTERACTIF ---
st.subheader("Corrélation Distance / Prix du loyer")
# Charge ici ton tableau de données consolidées
data = pd.DataFrame({
    'Commune': ["Cotonou", "Calavi", "Porto-Novo", "Sèmè", "Ouidah"],
    'Distance': [1, 16, 32, 18, 38],
    'Loyer': [300000, 60000, 55000, 50000, 35000]
})

fig = px.scatter(data, x="Distance", y="Loyer", text="Commune", trendline="ols")
st.plotly_chart(fig, use_container_width=True)

# --- FONCTIONNALITÉ 3 : RECOMMANDATIONS ---
st.info("💡 Conseil Géomatique : Le développement du corridor Nord-Ouest (Calavi) nécessite une priorité sur le transport de masse.")