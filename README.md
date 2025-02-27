# Django CMS – Seznam knih 📚

Tento projekt je jednoduchý CMS (Content Management System) postavený na Django, který zobrazuje seznam knih načítaný z JSON souboru.

## 📌 Funkce
- Zobrazení seznamu knih na homepage
- Detailní stránka každé knihy
- Použití Django šablon (`extends`, `block`) pro organizaci HTML
- Načítání dat ze souboru `data.json`

## 🛠️ Instalace a spuštění
1. Klonuj tento repozitář:
   ```sh
   git clone https://github.com/tvoje_repo/django_cms.git
   cd django_cms

2. Vytvoř a aktivuj virtuální prostředí:
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows

3. Nainstaluj závislosti:
pip install -r requirements.txt

4. Spusť Django server:
python manage.py runserver

