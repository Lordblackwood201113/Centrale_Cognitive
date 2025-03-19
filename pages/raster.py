import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd
import plotly.express as px

st.set_page_config(layout="wide", page_title="Vegstat", page_icon="💻")
st.logo("Logo_Centrale_Cognitive.jpeg", size = "medium")

st.sidebar.title("Contact")
st.sidebar.info(
    """
    [LinkedIn](https:// compte linkedin) |
    [Email](mailto:contact@AgriXtech.com) |
    [GitHub repository](https://github.com/centrale_cognitive/) |
    [Téléphone](+2250759788597)
    """
)
st.sidebar.image("Logo_Centrale_Cognitive.jpeg", use_container_width=True)

st.subheader("Centrale Geospatial Applications")
st.title("Raster Visualisation 💻")

# 📌 Dictionnaire des couches WMS (données statiques)
wms_layers = {
    "AGB 2022": "predicted_agbd_2022",
    "AGB 2023": "predicted_agbd_2023",
    "AGB 2024": "predicted_agbd_2024"
}

# 📌 Fonction de chargement et mise en cache des shapefiles
@st.cache_data
def load_data_dict():
    return {
        "AGB 2022": gpd.read_file("state_zone/agb_zone_2022.shp"),
        "AGB 2023": gpd.read_file("state_zone/agb_zone_2023.shp"),
        "AGB 2024": gpd.read_file("state_zone/agb_zone_2024.shp")
    }

# Chargement des données via la fonction mise en cache
data_dict = load_data_dict()

# 📌 Sélection de la couche WMS via un dropdown
selected_layer_name = st.selectbox("Choisissez une couche WMS :", list(wms_layers.keys()))

# 📌 Création de la carte
m = leafmap.Map(
    location=[43.296482, 5.36978],  # Coordonnées par défaut (Marseille)
    zoom_start=10,
    tiles="cartodb positron",
    measure_control=False,
    draw_control=False,
    search_control=False
)

# 📌 Ajout de la couche WMS sélectionnée
selected_layer = wms_layers[selected_layer_name]
m.add_wms_layer(
    url="http://18.208.148.26:8080/geoserver/Centrale/wms?",
    layers=selected_layer,
    name=selected_layer_name
)

# 📌 Ajout de la légende correspondante
legend_url = f"http://18.208.148.26:8080/geoserver/Centrale/wms?REQUEST=GetLegendGraphic&FORMAT=image/png&LAYER={selected_layer}"
m.add_wms_legend(url=legend_url)

# 📌 Affichage de la carte dans Streamlit
m.to_streamlit(height=500)

# 📌 Récupération du DataFrame sélectionné
selected_df = data_dict[selected_layer_name]

# 📌 Vérification que les colonnes "TFV" et "_sum" existent avant de tracer le graphique
if "TFV" in selected_df.columns and "_sum" in selected_df.columns:
    fig = px.bar(selected_df, x="TFV", y="_sum", title=f"Histogramme de {selected_layer_name}")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning(f"Les colonnes 'TFV' et '_sum' sont introuvables dans {selected_layer_name}. Vérifiez votre fichier CSV.")
