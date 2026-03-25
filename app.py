import streamlit as st
import pandas as pd
import plotly.express as px
import statsmodels.api as sm

st.set_page_config(page_title="Observatoire Grand Nokoué", layout="wide")

st.title("🏙️ Analyseur Spatial du Grand Nokoué")
st.sidebar.header("Paramètres d'analyse")

st.sidebar.subheader("Simulateur de trajet")
depart = st.sidebar.selectbox("Lieu de résidence", ["Abomey-Calavi", "Porto-Novo", "Sèmè-Kpodji", "Ouidah"])
km_prix = {"Abomey-Calavi": 16, "Porto-Novo": 32, "Sèmè-Kpodji": 18, "Ouidah": 38}

st.metric(label=f"Distance vers Cotonou", value=f"{km_prix[depart]} km")

st.subheader("Corrélation Distance / Prix du loyer")
data = pd.DataFrame({
    'Commune': ["Cotonou", "Calavi", "Porto-Novo", "Sèmè", "Ouidah"],
    'Distance': [1, 16, 32, 18, 38],
    'Loyer': [300000, 60000, 55000, 50000, 35000]
})

fig = px.scatter(data, x="Distance", y="Loyer", text="Commune", trendline="ols")
st.plotly_chart(fig, use_container_width=True)

st.info("💡 Conseil Géomatique : Le développement du corridor Nord-Ouest (Calavi) nécessite une priorité sur le transport de masse.")
