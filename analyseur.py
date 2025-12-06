import requests
import sys # Pour pouvoir quitter le programme proprement

# --- CONFIGURATION ---
# La liste des étiquettes de sécurité qu'on recherche
HEADERS_A_VERIFIER = [
    "Strict-Transport-Security",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Content-Security-Policy",
    "Referrer-Policy", # J'en ajoute un petit nouveau utile
    "Server" # Celui-ci, c'est mieux s'il est absent ou générique (comme "nginx" au lieu de "nginx/1.18.0")
]

# --- FONCTIONS ---

def nettoyer_url(url_entree):
    """S'assure que l'URL commence bien par http:// ou https://"""
    url_propre = url_entree.strip() # Enlève les espaces avant/après
    if not url_propre.startswith(("http://", "https://")):
        # On ajoute https par défaut si l'utilisateur l'a oublié
        url_propre = "https://" + url_propre
    return url_propre

# --- PROGRAMME PRINCIPAL ---

print("=== 🕵️‍♂️ Analyseur d'En-têtes de Sécurité Rapide ===")
print("Ce script vérifie passivement la présence des headers HTTP de base.\n")

# 1. On demande l'URL à l'utilisateur
url_input = input("👉 Entrez le domaine à analyser (ex: github.com) : ")

if not url_input:
    print("❌ Erreur : Aucune URL fournie.")
    sys.exit() # On quitte le programme

url_cible = nettoyer_url(url_input)

print(f"\n🔄 Démarrage de l'analyse pour : {url_cible} ...\n")

try:
    # On se connecte
    reponse = requests.get(url_cible, timeout=10)
    
    print(f"✅ Connexion réussie (Code statut : {reponse.status_code})")
    print("--------------------------------------------------")
    print(f" {'HEADER':<35} | RÉSULTAT")
    print("--------------------------------------------------")

    # On boucle sur notre liste de headers
    for header_nom in HEADERS_A_VERIFIER:
        
        if header_nom in reponse.headers:
            valeur = reponse.headers[header_nom]
            # On coupe si c'est trop long pour l'affichage
            if len(valeur) > 50:
                valeur = valeur[:50] + "..."
            
            print(f" [✅] {header_nom:<30} | Trouvé : {valeur}")
        else:
            print(f" [❌] {header_nom:<30} | MANQUANT (Vulnérabilité potentielle)")

    print("--------------------------------------------------")
    print("\n--- Analyse terminée ---")

except requests.exceptions.MissingSchema:
    print("❌ Erreur d'URL : Format invalide.")
except requests.exceptions.ConnectionError:
    print(f"❌ Erreur de connexion : Impossible de joindre {url_cible}.")
except Exception as e:
    print(f"❌ Erreur inattendue : {e}")