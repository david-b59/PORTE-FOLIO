import streamlit as st
import pandas as pd
import numpy as np
from st_on_hover_tabs import on_hover_tabs
from pathlib import Path
import base64
from PIL import Image
import requests
from io import BytesIO


st.set_page_config(layout="wide")



# Convertir l'image locale en base64
image_path = Path("image-background.png")
if image_path.is_file():
    with open(image_path, "rb") as img_file:
        img_base64 = base64.b64encode(img_file.read()).decode()
else:
    st.error(f"L'image '{image_path.name}' est introuvable dans le dossier : {image_path.parent}")

# CSS avec image de fond en base64
css = f'''
<style>

    .stApp {{
        background-image: url("data:image/png;base64,{img_base64}");
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
        background-position: center;
        
    }}

    section[data-testid='stSidebar'] {{
        background-color: #111;
        min-width: unset !important;
        width: unset !important;
        flex-shrink: unset !important;
    }}

    button[kind="header"] {{
        background-color: transparent;
        color: rgb(180, 167, 141);
    }}

    @media(hover) {{
        header[data-testid="stHeader"] {{
            display: none;
        }}

        section[data-testid='stSidebar'] > div {{
            
            width: 100px;
            position: relative;
            z-index: 1;
            top: 0;
            left: 0;
            background-color: #111;
            overflow-x: hidden;
            transition: 0.5s ease;
            padding-top: 60px;
            white-space: nowrap;
        }}

        section[data-testid='stSidebar'] > div:hover {{
            width: 250px;
          
        }}

        button[kind="header"] {{
            display: none;
        }}
    }}

    button, 
    .stButton button, 
    .stDownloadButton button, 
    .st-emotion-cache button {{  
        color: white !important;  /* Texte blanc pour contraste */
        background: linear-gradient(135deg, #2C3E50, #4CA1AF) !important; /* Dégradé bleu-gris pro */
        border: 2px solid #1B2A41 !important; /* Bordure gris foncé */
        padding: 12px 18px !important; /* Agrandir les boutons */
        border-radius: 8px !important; /* Coins arrondis */
        font-size: 16px !important; /* Texte lisible */
        font-weight: bold !important; /* Texte en gras */
        cursor: pointer !important; /* Curseur interactif */
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3) !important; /* Ombre pour effet 3D */
        transition: all 0.3s ease-in-out !important; /* Animation fluide */
    }}
    /* Ajuster les boutons au survol */
    button:hover, 
    .stButton button:hover, 
    .stDownloadButton button:hover, 
    .st-emotion-cache button:hover {{  
        background: linear-gradient(135deg, #1B2A41, #3B6978) !important; /* Dégradé plus foncé au survol */
        transform: scale(1.07) !important; /* Effet zoom léger */
        border-color: #16222A !important;
    }}
    
    
    /* S'assurer que la lisibilité est bonne sur mobile */
    @media (max-width: 768px) {{
        h1, h2, h3, h4, h5, h6, div, p, span {{
            color: black !important;
        }}
        /* Rétablir la couleur d'origine pour les boutons */
    button, 
    .stButton button, 
    .stDownloadButton button, 
    .st-emotion-cache button {{  
        color: white !important;  /* Texte blanc pour contraste */
        background: linear-gradient(135deg, #2C3E50, #4CA1AF) !important; /* Dégradé bleu-gris pro */
        border: 2px solid #1B2A41 !important; /* Bordure gris foncé */
        padding: 12px 18px !important; /* Agrandir les boutons */
        border-radius: 8px !important; /* Coins arrondis */
        font-size: 16px !important; /* Texte lisible */
        font-weight: bold !important; /* Texte en gras */
        cursor: pointer !important; /* Curseur interactif */
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3) !important; /* Ombre pour effet 3D */
        transition: all 0.3s ease-in-out !important; /* Animation fluide */
    }}
    /* Ajuster les boutons au survol */
    button:hover, 
    .stButton button:hover, 
    .stDownloadButton button:hover, 
    .st-emotion-cache button:hover {{  
        background: linear-gradient(135deg, #1B2A41, #3B6978) !important; /* Dégradé plus foncé au survol */
        transform: scale(1.07) !important; /* Effet zoom léger */
        border-color: #16222A !important;
    }}

    /* Rétablir l'affichage normal des icônes et flèches */
    .st-emotion-cache svg,  
    .st-emotion-cache i {{
        color: white !important;  
    }}

    /* Corriger les blocs de code (code copier-coller) */
    pre, code , code span{{
        color: #00ff00 !important;  /* Texte vert clair */
        background-color: #2a2a2a !important; /* Fond gris foncé */
        font-family: 'Courier New', Courier, monospace !important;
        padding: 12px !important;
        border-radius: 6px !important;
        display: block !important;
        overflow-x: auto !important;  /* Permettre le scroll horizontal */
        white-space: pre-wrap !important;  /* Empêcher le débordement */
        word-wrap: break-word !important;  /* Permettre la coupure des mots */
    }}
    }}
    
    @media(max-width: 272px) {{
        section[data-testid='stSidebar'] > div {{
            width: 10rem;
        }}

    }}

    /* Ajouter une image de fond */
</style>
'''
st.markdown(css, unsafe_allow_html=True)


# Barre latérale avec menu interactif
with st.sidebar:
    tabs = on_hover_tabs(
        tabName=['Présentation', 'CV', 'Projets'],
        iconName=['description', 'person', 'folder'],
        default_choice=0
    )

# Contenu affiché selon le choix du menu
if tabs == 'Présentation':
    st.header("Présentation")
    st.write("Bienvenue sur mon portfolio ! Ici, vous pouvez explorer mes compétences et projets.")

    # CSS personnalisé pour le style
    st.markdown(
        """
        <style>
        .title {
            font-size: 2.5em;
            font-weight: bold;
            color: #2c3e50;
            text-align: center;
            margin-bottom: 20px;
        }
        .subtitle {
            font-size: 1.5em;
            font-weight: bold;
            color: #34495e;
            margin-top: 20px;
        }
        .text {
            font-size: 1.2em;
            line-height: 1.6;
            text-align: justify;
        }
        .icon {
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 1.2em;
        }
        .social-icons a {
            text-decoration: none;
            font-size: 1.2em;
            margin-right: 15px;
            color: #0077b5; /* Couleur par défaut (bleu LinkedIn) */
        }
        .social-icons a.github {
            color: #333; /* Couleur pour GitHub (noir) */
        }
        .footer {
            margin-top: 30px;
            text-align: center;
            color: #888888;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Titre principal
    st.markdown('<div class="title">Présentation de David Bauduin</div>', unsafe_allow_html=True)

    # Section "À propos de moi"
    st.markdown('<div class="subtitle">À propos de moi</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="text">
        Je m'appelle <b>David Bauduin</b> et je suis <b>Data Analyst</b>, passionné par l’univers de la donnée.
        Mon parcours a débuté en autodidacte, explorant les fondamentaux du développement
        (<b>HTML, CSS, JavaScript, SQL et Python</b>), avant de consolider mes compétences à travers
        une formation spécialisée en Data Analysis à la <b>Wild Code School</b>.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Section "Compétences Techniques"
    st.markdown('<div class="subtitle">Compétences Techniques</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="icon">💻 <b>Développement Web</b> : HTML, CSS, JavaScript pour créer des interfaces interactives et responsives.</div>
    <div class="icon">🗄️ <b>Gestion des Bases de Données</b> : SQL et MySQL pour l’extraction, la manipulation et la sécurisation des données.</div>
    <div class="icon">🐍 <b>Analyse de Données & Automatisation</b> : Python, R (notions) et Git pour le traitement, l’analyse et l’automatisation des flux de données.</div>
    <div class="icon">📊 <b>Bibliothèques & DataViz</b> : Numpy, Pandas, Matplotlib, Seaborn, Plotly et Streamlit pour la visualisation et l’interprétation des données.</div>
    <div class="icon">🤖 <b>Machine Learning & IA</b> : Régressions, classifications, clustering non supervisé, NLP et intégration de chatbots (LLM) pour des solutions prédictives et interactives.</div>
    <div class="icon">🔍 <b>Techniques d’Intégration</b> : Webscrapping, API Rest, Geocodage et méthodes ELT/ETL pour collecter et intégrer des données provenant de multiples sources.</div>
    <div class="icon">☁️ <b>Cloud & DevOps</b> : Docker, dbt, AWS et Notion Cloud pour le déploiement, la gestion d’infrastructures et l’automatisation des workflows.</div>
    <div class="icon">⚙️ <b>Outils & Méthodologies</b> : PowerBI, Looker Studio, Dax et Agile pour la création de dashboards, la gestion de projets et l’optimisation des processus analytiques.</div>
    """,
    unsafe_allow_html=True,
)

    # Section "Qualités Personnelles"
    st.markdown('<div class="subtitle">Qualités Personnelles</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="text">
        - <b>Curieux</b> : Toujours en quête d'apprentissage.<br>
        - <b>Persévérant</b> : Je ne lâche rien face aux défis.<br>
        - <b>Perfectionniste</b> : J'aime soigner les détails pour garantir des résultats de qualité.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Section "Formation"
    st.markdown('<div class="subtitle">Formation</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="text">
        J'ai suivi une formation en Data Analysis à la <b>Wild Code School</b>, avec une spécialisation
        en <b>Intelligence Artificielle</b> et <b>Machine Learning</b>.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Section "Passions"
    st.markdown('<div class="subtitle">Passions</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="text">
        Toujours en quête d'innovation, j'aime relever de nouveaux défis et transformer
        les données en solutions concrètes et impactantes.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Section "Réseaux Sociaux"
    st.markdown('<div class="subtitle">Réseaux Sociaux</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="social-icons">
            <a href="https://www.linkedin.com/in/david-bauduin-2540a4334/" target="_blank">🔗 LinkedIn</a>
            <a href="https://github.com/david-b59/PROJECTS" target="_blank" class="github">🐙 GitHub</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Footer
    st.markdown(
        """
        <div class="footer">
        Créé par David Bauduin
        </div>
        """,
        unsafe_allow_html=True,
    )



# Ajouter une section pour l'onglet CV
elif tabs == 'CV':

    # CSS pour personnaliser l'interface
    st.markdown("""
        <style>
            .title {
                font-size: 36px;
                font-weight: bold;
                text-align: center;
                color: #2c3e50;
            }
            .subtitle {
                font-size: 20px;
                color: #34495e;
                text-align: center;
                margin-bottom: 20px;
            }
            .pdf-viewer {
                margin: 20px auto;
                display: flex;
                justify-content: center;
            }
        </style>
    """, unsafe_allow_html=True)

    # Titre et sous-titre
    st.markdown('<h1 class="title">📄 Mon CV</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Consultez mon CV directement ou téléchargez-le !</p>', unsafe_allow_html=True)

    # Bouton pour télécharger le CV
    st.markdown(f"📥 [Télécharger mon CV](https://github.com/david-b59/PORTE-FOLIO/raw/main/CV_David_Bauduin_23022025.pdf)")

    st.image("https://david-b59.github.io/PORTE-FOLIO/CV_image.PNG")

           



elif tabs == 'Projets':
    st.header("Projets")
    st.write("Découvrez mes projets réalisés.")
    
    # Créer des colonnes pour les boutons
    col1, col2, col3, col4 = st.columns(4)

    # Ajouter des boutons dans chaque colonne
    with col1:
        button_toys = st.button("Toys and Models - Dashboard", key="toys_button")
    with col2:
        button_telecom = st.button("telecom-attrition - dashboard", key="telecom_button")
    with col3:
        button_cyclistique = st.button("Cyclistique - dashboard", key="Cyclistique_button")
    with col4:
        button_cinema = st.button("Project Recommandation Cinema", key="cinema_button")

    # Initialisation de l'état du projet sélectionné dans st.session_state
    if "selected_project" not in st.session_state:
        st.session_state["selected_project"] = None

    # Vérifier lequel des boutons a été cliqué et mettre à jour l'état
    if button_toys:
        st.session_state["selected_project"] = "toys"
    elif button_telecom:
        st.session_state["selected_project"] = "telecom"
    elif button_cyclistique:
        st.session_state["selected_project"] = "cyclistique"
    elif button_cinema:
        st.session_state["selected_project"] = "cinema"

    # Vérification du projet sélectionné
    if st.session_state["selected_project"] == "toys":
        # Affichage du contenu du projet
        st.write("Projet choisi : Toys and Models - Dashboard")

        # Couleurs et style CSS
        st.markdown(
            """
            <style>
            .title {
                font-size: 2rem;
                color: #3B3B98;
                font-weight: bold;
                text-align: center;
                margin-bottom: 20px;
            }
            .section-title {
                font-size: 1.5rem;
                color: #182C61;
                font-weight: bold;
                margin-bottom: 10px;
                margin-top: 30px;
            }
            .description {
                font-size: 1rem;
                color: #333333;
                text-align: justify;
                margin-bottom: 20px;
            }
            .highlight {
                color: #40739E;
                font-weight: bold;
            }
            </style>
            """, 
            unsafe_allow_html=True
        )

        # Titre principal
        st.markdown('<div class="title">🏎️ Toys and Models Dashboard</div>', unsafe_allow_html=True)

        # Description du projet
        st.markdown('<div class="description">Une entreprise spécialisée dans la vente de modèles et maquettes...</div>', unsafe_allow_html=True)

        # KPI, Fonctionnalités clés, et autres sections...
        st.markdown('<div class="section-title">📊 Les KPI Suivis :</div>', unsafe_allow_html=True)
        st.markdown("""
            - **Ventes** :  
                - Nombre de produits vendus par catégorie et par mois.  
                - Comparaison avec le même mois de l'année précédente et taux de variation.
            - **Finances** :  
                - Chiffre d'affaires des commandes des deux derniers mois par pays.
            - **Logistique** :  
                - Suivi du stock des 5 produits les plus commandés.
            - **Ressources Humaines** :  
                - Chaque mois, les 2 vendeurs ayant réalisé le plus de chiffres d'affaires.
            """, unsafe_allow_html=True)

        # Fonctionnalités et organisation du projet
        st.markdown('<div class="section-title">⚙️ Fonctionnalités clés :</div>', unsafe_allow_html=True)
        st.markdown("""
            - Analyse des KPI principaux avec **SQL**.  
            - Création d’un tableau de bord interactif avec **Power BI**.  
            - Actualisation quotidienne des données pour une gestion dynamique.
            """, unsafe_allow_html=True)

        # Organisation des fichiers
        st.markdown('<div class="section-title">🗂️ Organisation des Fichiers :</div>', unsafe_allow_html=True)
        st.markdown("""
            - **Documentation** :  
                - [Project instructions](https://github.com/david-b59/PROJECTS/blob/main/toys-and-models-dashboard/documentation/project_instructions.pdf)  
                - [Slides présentation](https://github.com/david-b59/PROJECTS/blob/main/toys-and-models-dashboard/documentation/slides_pr%C3%A9sentation.pdf)  
            - **Requêtes SQL** :  
                - [Fichiers SQL](https://github.com/david-b59/PROJECTS/blob/main/toys-and-models-dashboard/queries/kpi_queries.sql)  
            - **Dashboard Power BI** :  
                - [Fichier Power BI](https://github.com/david-b59/PROJECTS/blob/main/toys-and-models-dashboard/power_bi/Projet%201.pbix)  
                - [Screenshots du Dashboard](https://github.com/david-b59/PROJECTS/tree/main/toys-and-models-dashboard/power_bi/screenshots)  
        """, unsafe_allow_html=True)

        # Instructions d'utilisation
        st.markdown('<div class="section-title">📖 Comment utiliser ce projet ?</div>', unsafe_allow_html=True)
        st.markdown("""
            - **Étape 1** : Installez et ouvrez les outils requis :  
                - [MySQL Workbench](https://dev.mysql.com/downloads/workbench/) ou un autre SGBD pour lire les fichiers SQL.  
                - [Power BI Desktop](https://powerbi.microsoft.com/) pour explorer et interagir avec le tableau de bord.  
            - **Étape 2** :  
                - Lisez et exécutez les requêtes SQL pour analyser les KPI.  
                - Ouvrez le fichier Power BI pour visualiser les indicateurs.
        """, unsafe_allow_html=True)

        # ------------------ Ajout d'un titre pour les slides ------------------
        st.markdown("<div class='section-title'>🎥 Découvrez les slides du projet</div>", unsafe_allow_html=True)
        
        # ------------------ Diaporama des images ------------------

        # URL de base pour les images sur GitHub
        repo_url = "https://raw.githubusercontent.com/david-b59/PROJECTS/main/toys-and-models-dashboard/power_bi/screenshots/"
        
        # Liste des noms de tes fichiers
        image_paths = [f"screenshot{i}.png" for i in range(1, 19)]
        
        # Fonction pour charger les images depuis GitHub
        @st.cache_data
        def load_images(image_paths):
            images = []
            for image_name in image_paths:
                image_url = f"{repo_url}{image_name}"
                response = requests.get(image_url)
                if response.status_code == 200:
                    try:
                        img = Image.open(BytesIO(response.content))
                        images.append(img)
                    except Exception as e:
                        st.warning(f"Erreur lors du chargement de l'image {image_name}: {e}")
                else:
                    st.warning(f"Impossible de charger l'image {image_name} (HTTP {response.status_code})")
            return images
        
        # Charger toutes les images
        images = load_images(image_paths)
        
        # Vérifier si des images sont chargées
        if not images:
            st.error("Aucune image valide n'a pu être chargée.")
        else:
            # Initialisation de l'index dans st.session_state
            if "index" not in st.session_state:
                st.session_state.index = 0

            # Créer des boutons pour naviguer
            col1, col2, col3 = st.columns([1, 3, 1])
            with col1:
                if st.button("⬅️ Précédent"):
                    st.session_state.index = (st.session_state.index - 1) % len(images)
            with col3:
                if st.button("➡️ Suivant"):
                    st.session_state.index = (st.session_state.index + 1) % len(images)
        
            # Afficher l'image actuelle
            index = st.session_state.index
            st.image(images[index], caption=f"Image {index + 1}", use_container_width=True)



    


        # Footer
        st.markdown(
            """
            <hr>
            <div style="text-align: center; color: #182C61; font-size: 0.9rem;">
                Réalisé par [Bauduin David].  
            </div>
            """,
            unsafe_allow_html=True
        )

    elif st.session_state["selected_project"] == "telecom":

        # Affichage du projet
        st.write("Projet choisi : Dashboard Business Case – Churn dans les Télécoms")
        
        # Couleurs et style CSS
        st.markdown(
            """
            <style>
            .title {
                font-size: 2rem;
                color: #3B3B98;
                font-weight: bold;
                text-align: center;
                margin-bottom: 20px;
            }
            .section-title {
                font-size: 1.5rem;
                color: #182C61;
                font-weight: bold;
                margin-bottom: 10px;
                margin-top: 30px;
            }
            .description {
                font-size: 1rem;
                color: #333333;
                text-align: justify;
                margin-bottom: 20px;
            }
            .highlight {
                color: #40739E;
                font-weight: bold;
            }
            </style>
            """, 
            unsafe_allow_html=True
        )
        
        # Titre principal
        st.markdown('<div class="title">📊 Dashboard Business Case – Churn dans les Télécoms</div>', unsafe_allow_html=True)
        
        # Description du projet
        st.markdown('<div class="description">Ce dashboard interactif a été réalisé en une journée dans le cadre d’un défi interne. Il traite du churn (résiliation) dans le secteur des télécoms pour le client Pinky, qui souhaite identifier les clients à risque afin de prévenir leur résiliation.</div>', unsafe_allow_html=True)
        
        # Contenu du Dashboard
        st.markdown('<div class="section-title">📊 Contenu du Dashboard :</div>', unsafe_allow_html=True)
        st.markdown("""
        - **Exploration des données** :  
            - Analyse descriptive des variables et identification des facteurs influençant la résiliation.
        - **Visualisations interactives** :  
            - Graphiques clairs et intuitifs pour visualiser les tendances et comparer les comportements clients.
        - **Modélisation du churn** :  
            - Proposition d’un scoring pour identifier les clients à risque, facilitant ainsi les actions commerciales.
        """, unsafe_allow_html=True)
        
        # Fonctionnalités clés
        st.markdown('<div class="section-title">⚙️ Fonctionnalités clés :</div>', unsafe_allow_html=True)
        st.markdown("""
        - Analyse des données à partir d’un **fichier CSV** quasiment nettoyé.
        - Transformations et modifications réalisées directement via **Power Query**.
        - Création d’un tableau de bord interactif avec **Power BI**.
        - Actualisation quotidienne des données pour une gestion dynamique.
        """, unsafe_allow_html=True)
        
        # Organisation des Fichiers
        st.markdown('<div class="section-title">🗂️ Organisation des Fichiers :</div>', unsafe_allow_html=True)
        st.markdown("""
        - **Documentation** :  
            - [PDF Explication du projet](https://github.com/david-b59/PROJECTS/blob/main/telecom-attrition-dashboard/documentation/Churn%20dans%20les%20t%C3%A9l%C3%A9coms.pdf)
        - **Fichier CSV** :  
            - [Données source](LIEN_A_INDIQUER)
        - **Dashboard Power BI** :  
            - [Fichier Power BI](https://github.com/david-b59/PROJECTS/blob/main/telecom-attrition-dashboard/power_bi/telecom.pbix)
        - **Screenshots** :  
            - [Screenshots du Dashboard](https://github.com/david-b59/PROJECTS/tree/main/telecom-attrition-dashboard/power_bi/screenshots)
        """, unsafe_allow_html=True)
        
        # Instructions d'utilisation
        st.markdown('<div class="section-title">📖 Comment utiliser ce projet ?</div>', unsafe_allow_html=True)
        st.markdown("""
        - **Étape 1** : Clonez le dépôt GitHub et ouvrez le projet.
        - **Étape 2** : Consultez le fichier CSV et la documentation PDF pour comprendre les transformations appliquées.
        - **Étape 3** : Ouvrez le fichier Power BI pour explorer le dashboard interactif.
        """, unsafe_allow_html=True)
        
        # ------------------ Ajout d'un titre pour les screenshots ------------------
        st.markdown("<div class='section-title'>🖼️ Découvrez les screenshots du dashboard</div>", unsafe_allow_html=True)
        
        # URL de base pour les images sur GitHub (à adapter ultérieurement)
        repo_url = "https://raw.githubusercontent.com/david-b59/PROJECTS/main/telecom-attrition-dashboard/power_bi/screenshots/"
        
        # Liste des noms de fichiers screenshots (ici, on suppose 10 images)
        image_paths = [f"screen{i}.PNG" for i in range(1, 6)]
        
        # Fonction pour charger les images depuis GitHub
        #@st.cache_data
        def load_images(image_paths):
            images = []
            for image_name in image_paths:
                image_url = f"{repo_url}{image_name}"
                response = requests.get(image_url)
                if response.status_code == 200:
                    try:
                        img = Image.open(BytesIO(response.content))
                        images.append(img)
                    except Exception as e:
                        st.warning(f"Erreur lors du chargement de l'image {image_name}: {e}")
                else:
                    st.warning(f"Impossible de charger l'image {image_name} (HTTP {response.status_code})")
            return images
        
        # Charger toutes les images
        images = load_images(image_paths)
        
        # Vérifier si des images sont chargées
        if not images:
            st.error("Aucune image valide n'a pu être chargée.")
        else:
            # Initialisation de l'index dans st.session_state
            if "index" not in st.session_state:
                st.session_state.index = 0
        
            # Boutons de navigation
            col1, col2, col3 = st.columns([1, 3, 1])
            with col1:
                if st.button("⬅️ Précédent"):
                    st.session_state.index = (st.session_state.index - 1) % len(images)
            with col3:
                if st.button("➡️ Suivant"):
                    st.session_state.index = (st.session_state.index + 1) % len(images)
            
            # Affichage de l'image courante
            index = st.session_state.index
            st.image(images[index], caption=f"Image {index + 1}", use_container_width=True)
        
        # Footer
        st.markdown(
            """
            <hr>
            <div style="text-align: center; color: #182C61; font-size: 0.9rem;">
                Réalisé par [Bauduin David].
            </div>
            """,
            unsafe_allow_html=True
        )


    elif st.session_state["selected_project"] == "cyclistique":

        # ------------------ 1) Titre et Style ------------------
        st.write("Projet choisi : Dashboard Cyclistic – Analyse et Visualisation des Données 2021")
        
        # Couleurs et style CSS
        st.markdown(
            """
            <style>
            .title {
                font-size: 2rem;
                color: #3B3B98;
                font-weight: bold;
                text-align: center;
                margin-bottom: 20px;
            }
            .section-title {
                font-size: 1.5rem;
                color: #182C61;
                font-weight: bold;
                margin-bottom: 10px;
                margin-top: 30px;
            }
            .description {
                font-size: 1rem;
                color: #333333;
                text-align: justify;
                margin-bottom: 20px;
            }
            .highlight {
                color: #40739E;
                font-weight: bold;
            }
            </style>
            """, 
            unsafe_allow_html=True
        )
        
        # Titre principal
        st.markdown('<div class="title">🚴‍♀️ Dashboard Cyclistic – Analyse et Visualisation des Données 2021</div>', unsafe_allow_html=True)
        
        # ------------------ 2) Description Générale ------------------
        st.markdown(
            """
            <div class="description">
            Ce projet est le fruit d'une journée de travail intensif dans le cadre d'un certificat blanc. 
            Il s'inscrit dans le cadre d'une étude de cas business visant à analyser et visualiser les données 
            d'utilisation des vélos de Cyclistic à Chicago pour proposer des recommandations stratégiques.
            </div>
            """, 
            unsafe_allow_html=True
        )
        
        # ------------------ 3) Contexte ------------------
        st.markdown('<div class="section-title">🏙️ Contexte :</div>', unsafe_allow_html=True)
        st.markdown(
            """
            Cyclistic est une entreprise de partage de vélos à Chicago disposant d'une flotte de 5 824 vélos 
            répartis sur 692 stations. Le service est accessible via deux types de clientèle :
            
            - **Cyclistes occasionnels** : Pass pour une course ou une journée complète.
            - **Membres annuels** : Abonnement mensuel ou annuel.
            
            L’objectif est de comprendre comment ces deux groupes utilisent les vélos, afin de convertir 
            davantage de cyclistes occasionnels en membres annuels et de repérer les emplacements stratégiques 
            pour de nouvelles stations.
            """,
            unsafe_allow_html=True
        )
        
        # ------------------ 4) Objectifs de l'Étude ------------------
        st.markdown('<div class="section-title">🎯 Objectifs de l’Étude :</div>', unsafe_allow_html=True)
        st.markdown(
            """
            1. **Usage différencié** : Comment les membres annuels et les cyclistes occasionnels utilisent-ils 
               différemment les vélos ?
            2. **Conversion** : Identifier les leviers pour convertir les cyclistes occasionnels en membres annuels.
            3. **Stratégie digitale** : Exploiter les médias numériques pour améliorer le taux de conversion.
            4. **Nouvelles stations** : Déterminer les emplacements idéaux pour implanter de nouvelles stations, 
               en fonction des habitudes d’utilisation et de la fréquentation.
            """,
            unsafe_allow_html=True
        )
        
        # ------------------ 5) Data & Méthodologie ------------------
        st.markdown('<div class="section-title">🔎 Data & Méthodologie :</div>', unsafe_allow_html=True)
        st.markdown(
            """
            - **Collecte des Données** :  
              - Fichiers CSV publics provenant de Divvy Tripdata (serveur AWS), couvrant l’année 2021.
            - **Pré-traitement & Traitement** :  
              - Nettoyage et suppression des trajets problématiques.  
              - Ajout de colonnes (durée, heure de départ, etc.) pour enrichir l’analyse.  
              - Code de prétraitement et d’analyse dans un notebook <em>Google Colab</em> (voir le dépôt GitHub).
            - **Analyse et Visualisation** :  
              - Création d’un dataset propre pour <strong>Power BI</strong>.  
              - Conception d’un tableau de bord interactif avec cartes géographiques et tableaux croisés dynamiques.
            """,
            unsafe_allow_html=True
        )
        
        # ------------------ 6) Livrables ------------------
        st.markdown('<div class="section-title">📂 Livrables :</div>', unsafe_allow_html=True)
        st.markdown(
            """
            - **Documentation** :  
              - [Présentation (PDF)](https://github.com/david-b59/PROJECTS/tree/main/Cyclistic-ashboard/documentation) exposant la méthodologie, les insights clés et les recommandations.
            - **Notebook Google Colab** :  
              - [Fichier .ipynb](https://github.com/david-b59/PROJECTS/tree/main/Cyclistic-ashboard/notebook) présentant le nettoyage et l’analyse exploratoire.
            - **Fichier Power BI** :  
              - [Fichier .pbit ou .pbix](https://github.com/david-b59/PROJECTS/blob/main/Cyclistic-ashboard/power_bi/certification-blanc-david.pbit) pour visualiser et interagir avec le dashboard.
            - **Screenshots** :  
              - [Captures d’écran](https://github.com/david-b59/PROJECTS/tree/main/Cyclistic-ashboard/power_bi/screenshots) du tableau de bord Power BI disponibles dans le dossier `power_bi/screenshots`.
            """,
            unsafe_allow_html=True
        )
        
        # ------------------ 7) Instructions d’Utilisation ------------------
        st.markdown('<div class="section-title">⚙️ Instructions d’Utilisation :</div>', unsafe_allow_html=True)
        st.markdown(
            """
            1. **Cloner le Dépôt** :  
               <pre><code class="language-bash">git clone https://github.com/david-b59/PROJECTS/tree/main/Cyclistic-dashboard</code></pre>
            2. **Analyse Exploratoire** :  
               - Ouvrez le notebook `.ipynb` dans Google Colab ou Jupyter pour examiner le processus de nettoyage et d’analyse.
            3. **Préparer le Dashboard Power BI** :  
               - Ouvrez le fichier `.pbit` ou `.pbix` dans Power BI Desktop.  
               - Si besoin, spécifiez la source de données (fichier CSV nettoyé) lorsque vous y êtes invité.
            4. **Visualiser le Dashboard** :  
               - Une fois le fichier Power BI chargé, interagissez avec les graphiques et consultez les différentes vues (cartes, tableaux croisés, etc.).
            """,
            unsafe_allow_html=True
        )
        
        # ------------------ 8) Diaporama des Screenshots ------------------
        st.markdown('<div class="section-title">🖼️ Aperçu du Dashboard (Screenshots)</div>', unsafe_allow_html=True)
        
        # URL de base pour les images sur GitHub
        repo_url = "https://raw.githubusercontent.com/david-b59/PROJECTS/main/Cyclistic-ashboard/power_bi/screenshots/"
        
        # Adaptez le nombre d'images et leur nom en fonction de votre dépôt
        # Par exemple, si vous avez 7 captures nommées screen1.PNG, screen2.PNG, ...
        image_paths = [f"screen{i}.PNG" for i in range(1, 8)]
        
        @st.cache_data
        def load_images(image_paths):
            images = []
            for image_name in image_paths:
                image_url = f"{repo_url}{image_name}"
                response = requests.get(image_url)
                if response.status_code == 200:
                    try:
                        img = Image.open(BytesIO(response.content))
                        images.append(img)
                    except Exception as e:
                        st.warning(f"Erreur lors du chargement de l'image {image_name}: {e}")
                else:
                    st.warning(f"Impossible de charger l'image {image_name} (HTTP {response.status_code})")
            return images
        
        images = load_images(image_paths)
        
        if not images:
            st.error("Aucune image valide n'a pu être chargée.")
        else:
            if "index_cyclistic" not in st.session_state:
                st.session_state.index_cyclistic = 0
        
            col1, col2, col3 = st.columns([1, 3, 1])
            with col1:
                if st.button("⬅️ Précédent", key="prev_cyclistic"):
                    st.session_state.index_cyclistic = (st.session_state.index_cyclistic - 1) % len(images)
            with col3:
                if st.button("➡️ Suivant", key="next_cyclistic"):
                    st.session_state.index_cyclistic = (st.session_state.index_cyclistic + 1) % len(images)
        
            index = st.session_state.index_cyclistic
            st.image(images[index], caption=f"Image {index + 1}", use_container_width=True)
        
        # ------------------ 9) Conclusion ------------------
        st.markdown('<div class="section-title">✅ Conclusion</div>', unsafe_allow_html=True)
        st.markdown(
            """
            Ce projet a permis de mettre en évidence les différences d'utilisation des vélos entre les cyclistes 
            occasionnels et les membres annuels. Les insights clés issus de cette analyse fournissent des pistes 
            pour augmenter le taux de conversion vers l’abonnement annuel, ainsi que des recommandations sur 
            l’implantation de nouvelles stations. Le dashboard interactif garantit une approche claire et 
            accessible pour tous les acteurs impliqués.
            """,
            unsafe_allow_html=True
        )
        
        # ------------------ 10) Footer ------------------
        st.markdown(
            """
            <hr>
            <div style="text-align: center; color: #182C61; font-size: 0.9rem;">
                Réalisé par [Bauduin David].
            </div>
            """,
            unsafe_allow_html=True
        )

    
    elif st.session_state["selected_project"] == "cinema":
        st.write("Projet choisi : Project Recommandation Cinema")


        # CSS pour le design
        css = f'''
        <style>
            .stApp {{
                background-image: url("data:image/png;base64,{img_base64}");
                background-size: cover;
                background-attachment: fixed;
                background-repeat: no-repeat;
                background-position: center;
            }}
            .title {{
                font-size: 2rem;
                color: #3B3B98;
                font-weight: bold;
                text-align: center;
                margin-bottom: 20px;
            }}
            .section-title {{
                font-size: 1.5rem;
                color: #182C61;
                font-weight: bold;
                margin-bottom: 10px;
                margin-top: 30px;
            }}
            .description {{
                font-size: 1rem;
                color: #333333;
                text-align: justify;
                margin-bottom: 20px;
            }}
            .highlight {{
                color: #40739E;
                font-weight: bold;
            }}
        </style>
        '''
        st.markdown(css, unsafe_allow_html=True)

        # Titre principal
        st.markdown('<div class="title">🎥 Projet : Moteur de Recommandation pour un Cinéma Local</div>', unsafe_allow_html=True)

        # Lien vers le projet
        st.markdown(
            '<div class="description">Lien vers le projet fini : <a href="https://projet-recommandation-cinema.streamlit.app/" target="_blank">https://projet-recommandation-cinema.streamlit.app/</a></div>',
            unsafe_allow_html=True
        )

        # Contexte du projet
        st.markdown('<div class="section-title">🌟 Contexte :</div>', unsafe_allow_html=True)
        st.markdown('<div class="description">Un cinéma situé dans le <span class="highlight">Nord</span> souhaite revitaliser son activité en se digitalisant. Dans ce cadre, il a sollicité la création d’un moteur de recommandation basé sur une base de données de films (<span class="highlight">IMDB et TMDB</span>) pour personnaliser les séances et attirer un public local. Le projet se concentre sur les situations de <span class="highlight">cold start</span>, où aucune donnée utilisateur n’est disponible au départ.</div>', unsafe_allow_html=True)

        # Missions
        st.markdown('<div class="section-title">🎯 Missions :</div>', unsafe_allow_html=True)
        st.markdown(
            """
            - **Étude de marché** :
                - Analyse des habitudes cinématographiques dans la région de le Nord.
                - Identification des genres, périodes ou autres caractéristiques préférées.
            - **Analyse des données** :
                - Exploration et nettoyage de la base IMDB et TMDB.
                - Analyse des tendances (acteurs les plus présents, durées moyennes des films, périodes populaires, films les mieux notés).
                - Identification des caractéristiques influençant les recommandations.
            - **Création d’un système de recommandation** :
                - Développement d’un modèle basé sur des algorithmes de machine learning.
                - Démonstration de la recommandation sur une sélection de films proposée par le client.
            - **Présentation des résultats** :
                - Construction d’un tableau de bord interactif pour afficher les KPI pertinents.
        - Création d’une présentation synthétique expliquant la démarche, les outils utilisés, les difficultés rencontrées, et les pistes d’amélioration.
            """,
            unsafe_allow_html=True
        )

        # Livrables
        st.markdown('<div class="section-title">📦 Livrables :</div>', unsafe_allow_html=True)
        st.markdown(
            """
            - **Notebook d’analyse et de nettoyage des données** :
                - Documentation complète avec visualisations.
                - Justification des choix et conclusions.
            - **Dashboard interactif (Streamlit)** :
                - Présentation des KPI clés :
                    - Films Français.
                    - Genre Comédie et Action.
                    - 5 dernière année (2020 à 2024).
            """,
            unsafe_allow_html=True
        )

        # Technologies et outils
        st.markdown('<div class="section-title">🛠️ Technologies et Outils :</div>', unsafe_allow_html=True)
        st.markdown(
            """
            - **Exploration et Analyse des données** : Python, Pandas, Matplotlib, Seaborn.
            - **Machine Learning** : Scikit-learn.
            - **Dashboard** : Streamlit.
            - **Base de données** : IMDB et TMDB (fichiers CSV).
            """,
            unsafe_allow_html=True
        )

        # Résultats attendus
        st.markdown('<div class="section-title">✅ Résultats attendus :</div>', unsafe_allow_html=True)
        st.markdown(
            """
            Ce projet vise à fournir une solution personnalisée et adaptée aux attentes locales en intégrant une démarche analytique et technique robuste, et en offrant des outils pratiques pour le cinéma client.
            """,
            unsafe_allow_html=True
        )

        # Footer
        st.markdown(
            """
            <hr>
            <div style="text-align: center; color: #182C61; font-size: 0.9rem;">
                Réalisé par [Bauduin David].
            </div>
            """,
            unsafe_allow_html=True
        )
