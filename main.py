import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Présentation visuelle de mon parcours : Data Scientist & Docteure en IA et Data", layout="wide")

# Sidebar navigation
st.sidebar.title("🧭 Déroulement de la présentation de mon CV")
page = st.sidebar.radio(
    "Naviguer dans le CV :",
    ["🏠 Page d'accueil", "🎓 Parcours académique", "💼 Expérience professionnelle"]
)

with st.sidebar:
    st.markdown("---")
    st.markdown("💡 *L’IA, c’est un peu comme un stagiaire brillant : elle fait des trucs impressionnants… mais seulement si tu passes des heures à tout lui expliquer.*")

def show_accueil():
    st.title("💼 Data Scientist & Docteure en IA et Data")
    st.markdown("### 👩‍💻 Profil")
    st.markdown(""" Oumaima LAGUILI "
                    Docteure en Informatique appliquée à l’IA & à la Data.
                """)
    st.markdown("""
                - Data Scientist passionnée par la **valeur métier** de la donnée et la **création d’impact stratégique** dans les Achats. 
                - Mon objectif est de mobiliser l'IA pour optimiser les décisions, améliorer l’efficacité opérationnelle et renforcer l’expérience client.
                """)
    st.markdown("### 📧 Contact")
    st.markdown("LinkedIn : https://www.linkedin.com/in/oumaima-laguili")
    st.markdown("GitHub : https://github.com/OumaymaAguili")
    st.markdown("GitHub : https://github.com/OumaymaAguili")
    st.markdown("### 📍 Localisation")
    st.markdown("Perpignan, France – ouverte aux opportunités en télétravail ou avec déplacements.")
    st.markdown("### 🌍 Langues")
    st.markdown("- **Français** : Courant")
    st.markdown("- **Anglais** : Professionnel")
    st.markdown("- **Arabe** : Courant")

def show_formation():
    st.header("🎓 Parcours académique")
    st.markdown("- **Ingénieure en Informatique Industrielle** : systèmes intelligents, automatisation, optimisation industrielle.")
    with st.expander("📉 Stage - AirLiquide - Ingénierie"):
        st.markdown("""
        - Développement d’un système de contrôle intelligent des accès à l'usine  
        - **Outils** : Python, MySQL, Raspberry Pi 
    """)
    with st.expander("📉 Stage - EPPM - Ingénierie"):
        st.markdown("""
        - Rédaction d’un cahier des charges pour les actionneurs et capteurs de puits de pétrole.
        - **Outils** : Excel, UML, Documentation technique
        """)
    with st.expander("📉 Stage - INRIA/I3S - R&D"):
        st.markdown("""
        - Conception d’un CNN pour détecter des pathogènes fongiques sur images microscopiques "
        - **Outils** : Data augmentation, Data cleaning, Deepl learning algorithms (U-Net, FasterRCNN), Python, Pytorch, OpenCV, Numpy, Pandas
        """)

    st.markdown("- **Doctorat en Informatique appliquée à l’IA & la Data – PROMES CNRS**")
    with st.expander("🎯 Objectif de la thèse"):
        st.markdown("""
        - Développement d’algorithmes de commande prédictive pour la gestion intelligente de l’énergie solaire dans les logements.
        - Économie de 10 à 20 % sur la facture d’électricité.
        - Confort accru et réduction de l’empreinte carbone.
        """)
    with st.expander("🧠 Compétences techniques"):
        st.markdown("""
        - **Outils** : Python, Pandas, NumPy, Scikit-learn, TensorFlow, Pytorch
        - **Méthodes** : Machine Learning, Deep Learning, Data Mining, Data Visualisation  
        - **Conférences internationales** : Splitech (Croatie), IEEE WCCI (Japon), JNES & SAGIP (France)  
        - **Publications** : 3 articles scientifiques en anglais
        """)
    with st.expander("💼 Compétences transverses"):
        st.markdown("- Gestion de projet, autonomie, collaboration inter-laboratoires, encadrement d’étudiants.")

def show_yper():
    st.header("💼 Expérience – Data Scientist & Docteure en IA/Data chez Yper")
    st.markdown("Start-up tech, environnement agile avec interactions directes avec les équipes métiers.")
    with st.expander("🔐 Automatisation du KYC"):
        st.markdown("- Stack : MongoDB, Python, Git, PyTorch, CircleCI et Sentry (cloud et déploiement), AWS (gestion des images), OCR (EasyOCR, PaddleOCR, OllamaOCR), YOLOv12")
        st.markdown("- Impact : gain d’efficacité de 50 % à 80 % en 2 mois")

    with st.expander("🚚 Prédiction des retards de livraison"):
        st.markdown("- Stack : régression logistique, MongoDB, Skit-learn, Python, GIT, CircleCI et Sentry (cloud et déploiement)")
        st.markdown("- Objectif : fiabiliser les délais et améliorer la satisfaction client")
    with st.expander("📉 Prédiction du churn (magasins)"):
        st.markdown("- Stack : XGBoost, Random Forest, MongoDB, Skit-learn, Python, GIT, CircleCI et Sentry (cloud et déploiement)")
        st.markdown("- Objectif : identifier les magasins à risque de départ")
    with st.expander("📦 Détection de comportements frauduleux (vols)"):
        st.markdown("- Stack : LightGBM, MongoDB, Python, Git, CircleCI et Sentry (cloud et déploiement)")
        st.markdown("- Objectif : prévenir les vols de colis via analyse de profils à risque")
    with st.expander("🤖 Chatbot IA"):
        st.markdown("- Stack : Embeddings OpenAI, HuggingFace (zephyr-1.1b-beta/ Mistral-7B-Instruct-v0.2), Python, Git, CircleCI et Sentry (cloud et déploiement)")
        st.markdown("- Objectif : automatiser la compréhension des messages livreurs")
    with st.expander("📊 Dashboards métiers"):
        st.markdown("""
        - Stack : MongoDB, Pandas, Numpy, Streamlit, MetaBase, SQL, Matplotlib, Python, Git, CircleCI et Sentry (cloud et déploiement)
        - Objectifs :
        - Développement de dashboards interactifs pour les KPIs métiers et les performances IA
        - Faciliter l'accès aux données pour les équipes métiers, permettant une meilleure compréhension des performances et des tendances")
        - Amélioration de la prise de décision stratégique grâce à des visualisations claires et interactives
        - Filtres dynamiques, heatmaps, cartographie, visualisation en temps réel  
        - Préparer des rapports automatisés pour les équipes, permettant un suivi en temps réel des performances et une meilleure réactivité face aux enjeux opérationnels
        - Préparer des COPIL pour les équipes de account et sales, permettant des présentations fluides avec nos clients (Auchan, Carrefour, etc.)
        
        """)

def show_renault():
    st.header("🚗 Pourquoi Renault ?")
    st.markdown("""
    - Renault est un acteur historique fondé en **1898**, avec une forte culture d’ingénierie et d’innovation durable.
    - J’adhère profondément à ses engagements :
        - 🌿 Réduction de l’empreinte carbone dans la chaîne d’approvisionnement
        - 🚺 Égalité professionnelle et inclusion
        - 🔬 Ambition R&D portée sur l'innovation responsable
        - 📉 Contribuer à l’**efficience des achats** et à la **transformation digitale** de Renault
        - 📊 Travailler avec des équipes **multidisciplinaires & orientées impact
    - Je me projette dans cette stratégie à l’intersection de l’**ingénierie, la data, et la transition écologique**.
    """)

def show_questions():
    st.header("🙏 Questions & Remerciements")
    st.markdown("""
    **Questions :**
    - Ce poste est-il une création ? Quelle est votre vision à 6 mois ?
    - Quels sont les projets prioritaires en Data Science chez Renault aujourd’hui ?
    - Comment les équipes Data collaborent-elles avec les équipes métiers/achats ?
    - Quelles perspectives d’évolution sont envisageables à moyen terme ?

    **Remerciements**  
    Merci pour votre attention. J’espère avoir l’opportunité de contribuer à l’innovation data chez Renault.
    """)

# Routing
if page == "🏠 Page d'accueil":
    show_accueil()
elif page == "🎓 Parcours académique":
    show_formation()
elif page == "💼 Expérience professionnelle":
    show_yper()
#elif page == "🚗 Motivations : Pourquoi Renault ?":
 #   show_renault()
#elif page == "📈 Projets et réalisations":
#    pass  # Peut être complété si besoin
#elif page == "🙏 Questions & Remerciements":
#    show_questions()
