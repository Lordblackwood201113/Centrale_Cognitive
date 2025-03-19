import streamlit as st
import leafmap.foliumap as leafmap
from folium import WmsTileLayer

st.set_page_config(layout="wide", page_title="Vegstat", page_icon="💻")

# Barre latérale
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
st.logo("Logo_Centrale_Cognitive.jpeg", size = "medium")

st.subheader("Centrale Geospatial Applications")
st.title("SplitMap Visualisation 💻")

# Mise en cache des définitions des couches WMS
@st.cache_data
def get_layers_dict():
    elevation = WmsTileLayer(
        url="http://localhost:8080/geoserver/Centrale/wms?",
        name="elevation",
        fmt="image/png",
        layers="elevation",
        transparent=True,
        overlay=True,
        control=True,
    )

    agb_2024 = WmsTileLayer(
        url="http://localhost:8080/geoserver/Centrale/wms?",
        name="agb_2024",
        fmt="image/png",
        layers="predicted_agbd_2024",
        transparent=True,
        overlay=True,
        control=True,
    )

    agb_2023 = WmsTileLayer(
        url="http://localhost:8080/geoserver/Centrale/wms?",
        name="agb_2023",
        fmt="image/png",
        layers="predicted_agbd_2023",
        transparent=True,
        overlay=True,
        control=True,
    )

    agb_2022 = WmsTileLayer(
        url="http://localhost:8080/geoserver/Centrale/wms?",
        name="agb_2022",
        fmt="image/png",
        layers="predicted_agbd_2022",
        transparent=True,
        overlay=True,
        control=True,
    )

    pente = WmsTileLayer(
        url="http://localhost:8080/geoserver/Terrain/wms?",
        name="pente",
        fmt="image/png",
        layers="pente_13_ok",
        transparent=True,
        overlay=True,
        control=True,
    )

    ombrage = WmsTileLayer(
        url="http://localhost:8080/geoserver/Terrain/wms?",
        name="ombrage_13",
        fmt="image/png",
        layers="ombrage_13",
        transparent=True,
        overlay=True,
        control=True,
    )

    exposition_massif_forestier = WmsTileLayer(
        url="http://localhost:8080/geoserver/Terrain/wms?",
        name="exposition_massif_forestier",
        fmt="image/png",
        layers="exposition_massif_forestier",
        transparent=True,
        overlay=True,
        control=True,
    )

    return {
        "Elevation": elevation,
        "AGB 2022": agb_2022,
        "AGB 2023": agb_2023,
        "AGB 2024": agb_2024,
        "exposition_massif_forestier": exposition_massif_forestier,
        "ombrage_13": ombrage,
        "pente": pente
    }

layers_dict = get_layers_dict()

# Sélections de couches via des dropdown dans deux colonnes
col1, col2 = st.columns(2)
with col1:
    left_key = st.selectbox("Sélectionnez la couche pour le côté gauche", list(layers_dict.keys()))
with col2:
    right_key = st.selectbox("Sélectionnez la couche pour le côté droit", list(layers_dict.keys()))

left_layer = layers_dict[left_key]
right_layer = layers_dict[right_key]

# Création de la carte avec split_map
m = leafmap.Map(
    location=[43.296482, 5.36978],
    zoom_start=10,
    tiles="cartodb positron",
    measure_control=False,
    draw_control=False,
    search_control=False
)

m.split_map(
    left_layer=left_layer,
    right_layer=right_layer,
    left_label=left_key,
    right_label=right_key
)

# Ajout de la légende pour le côté droit
legend_url = f"http://localhost:8080/geoserver/Centrale/wms?REQUEST=GetLegendGraphic&FORMAT=image/png&LAYER={right_layer}"
m.add_wms_legend(url=legend_url)

m.to_streamlit(height=500)
