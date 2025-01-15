import streamlit as st
import joblib
import re

# Définir la fonction de nettoyage du texte
def clean_text(text):
    """
    Nettoie le texte en :
    - Convertissant en minuscules.
    - Supprimant les caractères spéciaux.
    - Supprimant les espaces multiples.
    """
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text

# Charger le modèle et le vectoriseur
@st.cache_resource  # Cache pour éviter de recharger à chaque interaction
def load_model():
    model = joblib.load("spam_classifier.pkl")
    vectorizer = joblib.load("tfidf_vectorizer.pkl")
    return model, vectorizer

model, vectorizer = load_model()

# Titre de l'application avec emoji
st.title("📩 Détection de Spam 📩")

# Barre latérale pour des informations supplémentaires
st.sidebar.title("À propos")
st.sidebar.write("""
Cette application utilise un modèle de machine learning pour détecter si un SMS ou un email est un **spam** ou **non-spam**.
- **Modèle** : SVM (Support Vector Machine)
- **Technologie** : Python, Scikit-learn, Streamlit
""")

# Zone de texte pour l'entrée utilisateur
user_input = st.text_area("✉️ Entrez un SMS ou un email :", "")

# Bouton pour lancer la prédiction
if st.button("🔍 Vérifier"):
    if user_input:
        # Nettoyer et vectoriser le texte
        text_cleaned = [clean_text(user_input)]
        text_vectorized = vectorizer.transform(text_cleaned)

        # Faire une prédiction
        prediction = model.predict(text_vectorized)
        result = "Spam" if prediction[0] == 1 else "Non-Spam"

        # Afficher le résultat avec des couleurs et des emojis
        if result == "Spam":
            st.error("🚨 **Résultat : Spam** 🚨")
            st.write("Ce message semble suspect. Méfiez-vous !")
        else:
            st.success("✅ **Résultat : Non-Spam** ✅")
            st.write("Ce message semble légitime. Pas de souci !")
    else:
        st.warning("⚠️ Veuillez entrer un texte pour vérifier s'il s'agit d'un spam.")

# Section supplémentaire pour des conseils
st.markdown("---")
st.subheader("💡 Conseils pour éviter les spams :")
st.write("""
- Ne cliquez pas sur des liens suspects.
- Ne partagez pas vos informations personnelles.
- Utilisez un filtre anti-spam pour votre boîte mail.
""")