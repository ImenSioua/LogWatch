"""Generateur de logs factices pour LogWatch (LW-37).

Produit un fichier JSON Lines (une ligne = un log) lu ensuite par Logstash.
Exemple : python scripts/generate_logs.py --count 1000 --output data/logs/app.log
"""
import argparse
import json
import os
import random
from datetime import datetime, timedelta, timezone

from faker import Faker

SERVICES = ["webapp", "mongodb", "redis", "elasticsearch", "logstash", "nginx"]
LEVELS = ["DEBUG", "INFO", "WARN", "ERROR", "CRITICAL"]
WEIGHTS = [10, 60, 15, 12, 3]

MESSAGES = {
    "INFO": ["Requete traitee avec succes", "Utilisateur connecte", "Tache planifiee executee"],
    "DEBUG": ["Lecture du cache", "Verification de la configuration"],
    "WARN": ["Temps de reponse eleve", "Utilisation memoire elevee", "Tentative de connexion echouee"],
    "ERROR": ["Connexion a la base refusee", "Timeout de la requete", "Erreur interne du serveur"],
    "CRITICAL": ["Service indisponible", "Espace disque insuffisant"],
}


def make_log(fake, now):
    level = random.choices(LEVELS, weights=WEIGHTS)[0]
    moment = now - timedelta(seconds=random.randint(0, 24 * 3600))
    return {
        "timestamp": moment.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "level": level,
        "service": random.choice(SERVICES),
        "message": random.choice(MESSAGES[level]),
        "ip": fake.ipv4(),
        "user": fake.user_name(),
        "response_time_ms": random.randint(5, 3000),
    }


def main():
    parser = argparse.ArgumentParser(description="Generateur de logs factices")
    parser.add_argument("--count", type=int, default=1000, help="nombre de logs")
    parser.add_argument("--output", default="data/logs/app.log", help="fichier de sortie")
    args = parser.parse_args()

    fake = Faker()
    now = datetime.now(timezone.utc)
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as out:
        for _ in range(args.count):
            out.write(json.dumps(make_log(fake, now)) + "\n")
    print(f"{args.count} logs ecrits dans {args.output}")


if __name__ == "__main__":
    main()
