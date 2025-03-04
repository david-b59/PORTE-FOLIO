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
            
            width: 80px;
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

    @media(max-width: 272px) {{
        section[data-testid='stSidebar'] > div {{
            width: 15rem;
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
        <div class="icon">
            📄 <b>HTML, CSS, JavaScript</b> : Développement web et bases du front-end.
        </div>
        <div class="icon">
            📊 <b>SQL</b> : Gestion et manipulation des bases de données.
        </div>
        <div class="icon">
            🐍 <b>Python</b> : Analyse de données et automatisation.
        </div>
        <div class="icon">
            🐍 <b>BILIOTHEQUES</b> : BI Numpy, Pandas, MatPlotLib, Seaborn, Plotly, Streamlit, Sci-kit learn, follium, re.
        </div>
        <div class="icon">
            🤖 <b>Machine Learning</b> : Régressions, classifications, clustering non-supervisé, entraînement des modèles, NLP.
        </div>
        <div class="icon">
            🤖 <b>TECHNIQUE</b> : Webscrapping, API Rest, Geocodage.
        </div>
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
    col1, col2 = st.columns(2)

    # Ajouter des boutons dans chaque colonne
    with col1:
        button_toys = st.button("Toys and Models - Dashboard", key="toys_button")
    with col2:
        button_cinema = st.button("Project Recommandation Cinema", key="cinema_button")

    # Initialisation de l'état du projet sélectionné dans st.session_state
    if "selected_project" not in st.session_state:
        st.session_state["selected_project"] = None

    # Vérifier lequel des boutons a été cliqué et mettre à jour l'état
    if button_toys:
        st.session_state["selected_project"] = "toys"
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
