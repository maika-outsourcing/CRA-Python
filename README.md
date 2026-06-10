# CRA-Python

Application de Compte Rendu d'Activité avec un backend Python/SQLAlchemy et un frontend React TypeScript.

## 🚀 Fonctionnalités
- Gestion des tâches
- API backend avec FastAPI
- Frontend React TypeScript pour la saisie et le suivi des WorkLogs

## 📂 Structure du projet
- `main.py` : point d’entrée du backend
- `models.py` : définition des modèles de données
- `database.py` : connexion et gestion MySQL
- `cra-frontend/` : interface React TypeScript

## ⚙️ Installation
### Backend
```bash
git clone git@github.com-stage:kidtit/CRA-Python.git
cd CRA-Python
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
