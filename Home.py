import streamlit as st
import leafmap.foliumap as leafmap
from folium import *

st.set_page_config(layout="wide", page_title = "Vegstat", page_icon= "💻")

st.sidebar.title("Contact")

st.sidebar.info(
    """
    [LinkedIn](https:// compte linkedin) |
     
    [Email](centralecognitive@gmail.com) |
     
    [GitHub repository](https://github.com/centrale_cognitive/) |
     
    | [Téléphone](+33 0605915679) | 
    """
)
st.logo("Logo_Centrale_Cognitive.jpeg", size = "medium")

st.sidebar.image("Logo_Centrale_Cognitive.jpeg", use_container_width =True)

st.subheader("Centrale Geospatial Applications")
# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

#------- HEADER -------------
with st.container() :
    st.title("ACCUEIL")
    st.write("Bienvenue chez La Centrale Cognitive, Leader en Analyse Géospatiale et Développement d'application WebGIS")
    
#------- BODY -------------
with st.container() :
    st.write("##")
    st.header("NOTRE EXPERTISE")
    c1, c2 = st.columns(2)
    with c1 : 
        st.write("""entrale Cognitive est spécialisée dans l'intégration des Systèmes d’Information Géographique (SIG) et des technologies de télédétection pour répondre aux enjeux environnementaux et forestiers. Nous réalisons des projets de cartographie avancée, d’analyse des masses combustibles et de modélisation des risques d’incendie, en exploitant des outils tels que le LiDAR, l’imagerie multispectrale et les drones.
Notre expertise s’étend également à la gestion durable des écosystèmes forestiers, en intégrant la préservation de la biodiversité, la planification sylvicole et l’optimisation des ressources naturelles. Nous accompagnons collectivités, parcs naturels, organismes publics et entreprises privées avec des solutions adaptées aux spécificités locales et aux exigences réglementaires.
Enfin, Centrale Cognitive se distingue dans l’estimation des stocks de carbone, en combinant télédétection et modélisation pour fournir des évaluations fiables de la biomasse et du carbone stocké dans les forêts. Cette expertise contribue à la prévention des incendies, au suivi des émissions de carbone et à une gestion durable des ressources naturelles, participant ainsi à la transition écologique.
""")
    with c2 :
        st.image("Logo_Centrale_Cognitive.jpeg", use_container_width =True)
        

with st.container() :
    st.write("##")
    st.header("MOTS DU DIRECTEUR")
    c1, c2 = st.columns(2)
    with c1 : 
        st.write("""Bienvenue sur notre site dédié à l’analyse géospatiale. 
                 En tant que directeur de notre entreprise, je suis fier de vous présenter une équipe passionnée qui met au service de vos projets toute son expertise en collecte, traitement et visualisation de données géographiques. 
                 Notre engagement repose sur l’innovation et la rigueur scientifique afin de transformer des données complexes en solutions stratégiques et durables. 
                 Nous croyons fermement que comprendre l’espace et ses dynamiques est la clé pour anticiper les défis de demain et saisir les opportunités d’aujourd’hui. 
                 Merci de votre confiance et n’hésitez pas à nous contacter pour explorer ensemble les multiples potentialités de l’analyse géospatiale.""")
        
    with c2 :
        st.image("Image1.jpg", use_container_width =True)
    


# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("NOUS CONTACTER")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

