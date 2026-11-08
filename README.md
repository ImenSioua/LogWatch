# LogWatch

Plateforme SaaS de monitoring et d'analyse de logs, construite avec la stack ELK, MongoDB, Redis et une interface web Flask.

Mini-projet de génie logiciel - IT Business School
Encadrant : M. Mohamed Najeh Issaoui - Réalisé par : Imen Sioua

## Prérequis

- Docker Desktop (avec Docker Compose v2)
- Git
- 8 Go de RAM disponibles pour Docker (recommandé)

## Démarrage rapide

1. Cloner le dépôt :

        git clone https://github.com/ImenSioua/LogWatch.git
        cd LogWatch

2. Créer le fichier de configuration à partir du modèle :

        copy .env.example .env

   Ouvrir ensuite `.env` et remplacer les valeurs `change_me` par de vrais mots de passe (sans espaces ni les caractères `$`, `#`, `"`).

3. Lancer toute la stack avec une seule commande :

        docker compose up -d --build

4. Vérifier que les 6 services sont "healthy" (1 à 2 minutes au premier démarrage) :

        docker compose ps

## Services et accès

| Service | Rôle | Accès |
|---|---|---|
| webapp | Application Flask (interface web) | http://localhost:8000 |
| elasticsearch | Stockage et recherche des logs | http://localhost:9200 |
| kibana | Visualisation et dashboards | http://localhost:5601 |
| logstash | Collecte et transformation des logs | ports 5044 (Beats) et 9600 (API) |
| mongodb | Base NoSQL (données applicatives) | localhost:27017 |
| redis | Cache | localhost:6379 |

## Commandes utiles

- Voir l'état des services : `docker compose ps`
- Voir les logs d'un service : `docker compose logs -f webapp`
- Arrêter la stack (données conservées) : `docker compose down`
- Tout supprimer, données comprises : `docker compose down -v`

## Structure du projet

    LogWatch/
    |-- docker-compose.yml      orchestration des 6 services
    |-- .env.example            modèle de configuration (le vrai .env n'est pas versionné)
    |-- webapp/                 application Flask (Dockerfile, app.py, requirements.txt)
    |-- logstash/pipeline/      configuration du pipeline Logstash
    |-- docs/                   documents d'analyse et de conception
    |-- figures/                diagrammes et captures

## Gestion de projet

- Méthode : Scrum, 6 sprints (26 octobre - 5 décembre 2026)
- Suivi : Jira, espace LogWatch (clé LW)
- Code : GitHub, branche main