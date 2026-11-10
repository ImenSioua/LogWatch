"""Generateur de logs factices pour LogWatch (LW-37).

Produit un fichier JSON Lines (une ligne = un log) lu ensuite par Logstash.
Exemple : python scripts/generate_logs.py --count 1000
Le fichier est toujours ecrit dans data/logs/app.log.
"""
import argparse
import json
import os
import random
from datetime import datetime, timedelta, timezone

from faker import Faker

OUTPUT_FILE = os.path.join("data", "logs", "app.log")
MAX_COUNT = 100000

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

rng = random.SystemRandom()


def make_log(fake, now):
    level = rng.choices(LEVELS, weights=WEIGHTS)[0]
    moment = now - timedelta(seconds=rng.randint(0, 24 * 3600))
    return {
        "timestamp": moment.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "level": level,
        "service": rng.choice(SERVICES),
        "message": rng.choice(MESSAGES[level]),
        "ip": fake.ipv4(),
        "user": fake.user_name(),
        "response_time_ms": rng.randint(5, 3000),
    }


def main():
    parser = argparse.ArgumentParser(description="Generateur de logs factices")
    parser.add_argument("--count", type=int, default=1000, help="nombre de logs (max 100000)")
    args = parser.parse_args()
    count = max(1, min(args.count, MAX_COUNT))

    fake = Faker()
    now = datetime.now(timezone.utc)
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        for _ in range(count):
            out.write(json.dumps(make_log(fake, now)) + "\n")
    print(f"{count} logs ecrits dans {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
