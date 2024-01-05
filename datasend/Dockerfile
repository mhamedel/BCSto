# Utilisez une image de base avec Python
FROM python:3.8

# Créez un répertoire de travail
WORKDIR /app

# Copiez le code de votre application dans le conteneur
COPY . .

# Copiez le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installez les dépendances
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Exposez le port sur lequel votre application Flask s'exécute

# Exposez le port sur lequel votre application Flask s'exécute
EXPOSE 5000

# Commande pour exécuter l'application Flask
CMD ["python", "serveur.py"]
