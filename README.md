📩 Projet de Détection de Spams avec Machine Learning
Ce projet vise à créer un système de détection de spams en utilisant des techniques de machine learning et de traitement du langage naturel (NLP). Le modèle est capable de classer automatiquement des SMS ou des emails en deux catégories : spam ou non-spam.

📋 Table des Matières
Objectif du Projet

Technologies Utilisées

Structure du Projet

Comment Utiliser ce Projet

Résultats

Améliorations Futures

Auteur

🎯 Objectif du Projet
L'objectif de ce projet est de développer un modèle de machine learning capable de détecter les spams dans les SMS ou les emails. Le modèle est entraîné sur un jeu de données étiqueté et utilise des techniques de NLP pour prétraiter les textes et les transformer en vecteurs numériques.

🛠️ Technologies Utilisées
Langage : Python

Bibliothèques :

pandas : Manipulation des données.

scikit-learn : Machine learning (SVM, Naive Bayes, Random Forest).

nltk : Prétraitement du texte (stopwords, lemmatisation).

streamlit : Création de l'interface utilisateur.

Vectorisation : TF-IDF (Term Frequency-Inverse Document Frequency).

Sauvegarde des Modèles : joblib.

📂 Structure du Projet
Copy
spam-detection/
├── data/                  # Dossier contenant les données
│   └── spam.csv           # Dataset des SMS (spam et non-spam)
├── models/                # Dossier contenant les modèles sauvegardés
│   └── spam_classifier.pkl
│   └── tfidf_vectorizer.pkl
├── app.py                 # Application Streamlit
├── train_model.py         # Script pour entraîner le modèle
├── requirements.txt       # Dépendances du projet
└── README.md              # Fichier README
🚀 Comment Utiliser ce Projet
1. Cloner le Répertoire
bash
Copy
git clone https://github.com/vMonstayys/D-tection-de-Spams-avec-Machine-Learning.git
cd D-tection-de-Spams-avec-Machine-Learning/
2. Installer les Dépendances
pip install -r requirements.txt
3. Entraîner le Modèle
Exécutez le script pour entraîner le modèle et sauvegarder les fichiers 
4. Lancer l'Application Streamlit
Exécutez l'application pour tester le modèle en temps réel :
streamlit run app.py
📊 Résultats
Le modèle SVM a obtenu les performances suivantes :

🎯 Précision : 93%

🔍 Rappel : 92%

⚖️ F1-score : 92.5%

Exemples de Prédictions
Spam :
"Congratulations! You've won a $1000 Walmart gift card. Click here to claim your prize."
Résultat : 🚨 Spam

Non-Spam :
"Hey bro, are we still meeting at 5 PM today?"
Résultat : ✅ Non-Spam

🔮 Améliorations Futures
Améliorer la détection des faux négatifs et faux positifs.

Explorer des techniques avancées comme les réseaux de neurones ou les transformers (BERT).

Déployer l'application sur une plateforme cloud pour la rendre accessible à tous.

👤 Auteur
Nom : Mohamed Sabkari

LinkedIn : https://www.linkedin.com/in/mohamed-sabkari-8b5b47231/


📄 Licence
Ce projet est sous licence MIT. Pour plus de détails, consultez le fichier LICENSE.

🌟 Remerciements
Un grand merci à la communauté open source pour les ressources et bibliothèques utilisées dans ce projet.
