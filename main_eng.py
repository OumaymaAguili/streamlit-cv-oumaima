import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Visual Resume: Data Scientist & PhD in AI and Data", layout="wide")

# Sidebar navigation
st.sidebar.title("🧭 CV Navigation")
page = st.sidebar.radio(
    "Go to:",
    ["🏠 Home", "🎓 Academic Background", "💼 Professional Experience"]
)

with st.sidebar:
    st.markdown("---")
    st.markdown("💡 *AI is a bit like a brilliant intern: it does impressive things... but only if you spend hours explaining everything first.*")

def show_home():
    st.title("💼 Data Scientist & PhD in AI and Data")
    st.markdown("### 👩‍💻 Profile")
    st.markdown("""Oumaima LAGUILI  
PhD in Computer Science applied to AI & Data.""")

    st.markdown("""
- Passionate Data Scientist focused on **business value** and **strategic impact** in Procurement.
- My goal is to leverage AI to optimize decision-making, enhance operational efficiency, and improve customer experience.
    """)

    st.markdown("### 📧 Contact")
    st.markdown("LinkedIn: https://www.linkedin.com/in/oumaima-laguili")
    st.markdown("GitHub: https://github.com/OumaymaAguili")

    st.markdown("### 📍 Location")
    st.markdown("Perpignan, France – Open to remote or travel-based opportunities.")

    st.markdown("### 🌍 Languages")
    st.markdown("- **French**: Fluent")
    st.markdown("- **English**: Professional")
    st.markdown("- **Arabic**: Fluent")

def show_academic():
    st.header("🎓 Academic Background")
    st.markdown("- **Engineering Degree in Industrial Computer Science**: intelligent systems, automation, industrial optimization.")

    with st.expander("📉 Internship – AirLiquide – Engineering"):
        st.markdown("""
- Developed an intelligent access control system for the factory  
- **Tools**: Python, MySQL, Raspberry Pi
        """)

    with st.expander("📉 Internship – EPPM – Engineering"):
        st.markdown("""
- Drafted technical specifications for oil well actuators and sensors  
- **Tools**: Excel, UML, technical documentation
        """)

    with st.expander("📉 Internship – INRIA/I3S – R&D"):
        st.markdown("""
- Designed a CNN to detect fungal pathogens in microscopic images  
- **Tools**: Data augmentation, Deep Learning (U-Net, FasterRCNN), Python, PyTorch, OpenCV, Numpy, Pandas
        """)

    st.markdown("- **PhD in Computer Science – AI & Data – PROMES CNRS**")
    with st.expander("🎯 Thesis Objective"):
        st.markdown("""
- Developed predictive control algorithms for smart solar energy management in homes  
- Achieved 10–20% electricity savings  
- Enhanced user comfort and reduced carbon footprint
        """)

    with st.expander("🧠 Technical Skills"):
        st.markdown("""
- **Tools**: Python, Pandas, NumPy, Scikit-learn, TensorFlow, PyTorch  
- **Methods**: Machine Learning, Deep Learning, Data Mining, Data Visualization  
- **International Conferences**: Splitech (Croatia), IEEE WCCI (Japan), JNES & SAGIP (France)  
- **Publications**: 3 peer-reviewed scientific articles in English
        """)

    with st.expander("💼 Transversal Skills"):
        st.markdown("- Project management, autonomy, inter-laboratory collaboration, student mentoring.")

def show_experience():
    st.header("💼 Experience – Data Scientist & PhD in AI/Data at Yper")
    st.markdown("Tech start-up with an agile environment and close collaboration with business teams.")

    with st.expander("🔐 KYC Automation"):
        st.markdown("""
- Stack: MongoDB, Python, Git, PyTorch, CircleCI, Sentry, AWS, OCR (EasyOCR, PaddleOCR, OllamaOCR), YOLOv12  
- **Impact**: 50% to 80% efficiency gains within 2 months
        """)

    with st.expander("🚚 Delivery Delay Prediction"):
        st.markdown("""
- Stack: Logistic Regression, MongoDB, Scikit-learn, Python, Git, CircleCI, Sentry  
- **Goal**: Increase reliability of delivery times and improve customer satisfaction
        """)

    with st.expander("📉 Churn Prediction (Stores)"):
        st.markdown("""
- Stack: XGBoost, Random Forest, MongoDB, Scikit-learn, Python, Git, CircleCI, Sentry  
- **Goal**: Identify stores at risk of leaving the platform
        """)

    with st.expander("📦 Fraud Detection (Thefts)"):
        st.markdown("""
- Stack: LightGBM, MongoDB, Python, Git, CircleCI, Sentry  
- **Goal**: Prevent parcel theft by analyzing risky shopper profiles
        """)

    with st.expander("🤖 AI Chatbot"):
        st.markdown("""
- Stack: OpenAI embeddings, HuggingFace (zephyr-1.1b-beta / Mistral-7B), Python, Git, CircleCI, Sentry  
- **Goal**: Automate understanding of delivery agent messages
        """)

    with st.expander("📊 Business Dashboards"):
        st.markdown("""
- Stack: MongoDB, Pandas, Numpy, Streamlit, MetaBase, SQL, Matplotlib, Python, Git, CircleCI, Sentry  
- **Objectives**:
    - Develop interactive dashboards for business KPIs and AI performance  
    - Enable real-time, accessible data insights for operations teams  
    - Support strategic decisions with dynamic filters, heatmaps, mapping  
    - Automate reporting and enable client presentations (Auchan, Carrefour, etc.)
        """)

# Route handling
if page == "🏠 Home":
    show_home()
elif page == "🎓 Academic Background":
    show_academic()
elif page == "💼 Professional Experience":
    show_experience()
