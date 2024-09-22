FROM python:3.9-slim

# Working Directory
WORKDIR / app 

# Copie tous les fichiers du répertoire local dans le répertoire de travail du conteneur
COPY . /app

## Copy source code to working directory
COPY requirements.txt /app/

# Install packages from requirements.txt#

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

# Exécute l'application Python
CMD ["python", "app.py"]