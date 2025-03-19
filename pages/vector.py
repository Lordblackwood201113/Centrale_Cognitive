import streamlit as st
import leafmap.foliumap as leafmap
from folium import WmsTileLayer
import pandas as pd
import plotly.express as px
import geopandas as gpd
import pygwalker as pyg
import streamlit.components.v1 as components

# Configuration de la page
st.set_page_config(layout="wide", page_title="Vegstat", page_icon="💻")
st.logo("Logo_Centrale_Cognitive.jpeg", size = "medium")

# Barre latérale Contact
st.sidebar.title("Contact")
st.sidebar.info(
    """
    [LinkedIn](https://compte-linkedin) |
    [Email](mailto:contact@AgriXtech.com) |
    [GitHub repository](https://github.com/centrale_cognitive/) |
    [Téléphone](tel:+2250759788597)
    """
)
st.sidebar.image("Logo_Centrale_Cognitive.jpeg", use_container_width=True)

# Titres principaux
st.subheader("Centrale Geospatial Applications")
st.title("Vectors visualisation 💻")

# Définition des couches WMS
massif_forestier_wms = WmsTileLayer(
    url="http://localhost:8080/geoserver/Centrale/wms?",
    name="massif forestier",
    fmt="image/png",
    layers="massif_forestier",
    transparent=True,
    overlay=True,
    control=True,
)

statistiques_de_zones_wms = WmsTileLayer(
    url="http://localhost:8080/geoserver/Centrale/wms?",
    name="statistiques de zones",
    fmt="image/png",
    layers="statistiques_de_zones",
    transparent=True,
    overlay=True,
    control=True,
)

# Dictionnaire des couches (si besoin de les utiliser plus tard)
layers_dict = {
    "massif_forestier": massif_forestier_wms,
    "statistiques_de_zones": statistiques_de_zones_wms
}

# ----------------------- Fonctions avec mise en cache ----------------------- #

@st.cache_data
def load_state_zone():
    """Lecture et mise en cache du shapefile state_zone."""
    return gpd.read_file("state_zone/state_zone.shp")

@st.cache_data
def load_massif_forestier():
    """Lecture et mise en cache du shapefile du Massif Forestier."""
    return gpd.read_file("Massifs/Massif Forestier.shp")

def plot_graph(df):
    """
    Génère un graphique à barres empilées représentant la somme des AGB
    par massif et par essence.
    """
    # Calcul de la somme par groupe
    df_sum = df.groupby(["nom_maf", "ESSENCE"])["_sum"].sum().reset_index()

    # Création du graphique avec plotly.express
    fig = px.bar(
        df_sum,
        x="nom_maf",
        y="_sum",
        color="ESSENCE",
        barmode="stack",
        title="Somme des AGB par massif et par essence"
    )
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="black"),
        yaxis=dict(showgrid=True, gridcolor='#cecdcd'),
        xaxis=dict(showgrid=True, gridcolor='#cecdcd'),
        paper_bgcolor='rgba(0, 0, 0, 0)',
    )
    st.plotly_chart(fig, use_container_width=True)

@st.cache_data
def get_pygwalker_html(df):
    """
    Génère et met en cache le code HTML de pygwalker
    pour la dataframe fournie (sans géométrie).
    """
    return pyg.walk(df, return_html=True)

# ----------------------- Interface principale ----------------------- #

# Affichage de quelques métriques (valeurs statiques ici)
total1, total2, total3 = st.columns(3, gap='small')
with total1:
    st.info('Nombre de Massifs Forestiers')
    st.metric(label="Nbr Massifs", value=25)

with total2:
    st.info('Somme des surfaces ha')
    st.metric(label="Sum Surface", value=182102.909)

with total3:
    st.info('Nombre de Feux (2000-2024)')
    st.metric(label="Nbr Feux", value=519)

# Chargement des shapefiles via les fonctions mises en cache
state_zone_df = load_state_zone()
massif_gdf = load_massif_forestier()

# Mise en page en deux colonnes
col1, col2 = st.columns(2)

with col1:
    # Création de la carte avec Leafmap
    m = leafmap.Map(
        location=[43.296482, 5.36978],
        zoom_start=10,
        tiles="cartodb positron",
        measure_control=False,
        draw_control=False,
        search_control=False
    )
    # Ajout du shapefile du Massif Forestier à la carte
    m.add_gdf(massif_gdf, layer_name="Massif Forestier", info_mode='on_click')
    m.to_streamlit(height=500)

with col2:
    # Affichage du graphique
    plot_graph(state_zone_df)

# Section expander pour pygwalker
with st.expander("⏰ VISUALISATION & GRAPHIQUE "):
    # Suppression de la colonne géométrie pour pygwalker
    df_no_geom = state_zone_df.drop(columns="geometry")
    pyg_html = get_pygwalker_html(df_no_geom)
    components.html(pyg_html, height=1000, scrolling=True)
