# 🕵️‍♂️ Analyseur Passif d'En-têtes de Sécurité HTTP

Un outil en ligne de commande Python (CLI) léger pour effectuer une analyse rapide et non intrusive de la configuration de sécurité d'un site web.

## 🎯 Pourquoi ce projet ?

Dans le cadre de ma montée en compétences en développement Python et en cybersécurité, j'ai voulu créer un outil permettant de vérifier automatiquement les "bonnes pratiques" de base en matière de sécurité web.

Ce script permet de voir en un clin d'œil si un serveur applique les protections essentielles contre des attaques courantes (comme le Clickjacking, le XSS ou le sniffing de type MIME) en inspectant les en-têtes HTTP renvoyés par le serveur.

**Note :** Il s'agit d'une analyse *passive*. Le script n'effectue aucune attaque ni scan intrusif, il ne fait que lire les informations publiques envoyées par le site.

## 🚀 Fonctionnalités

* ✅ **Vérification des Headers Clés :** Contrôle la présence de :
    * `Strict-Transport-Security` (HSTS)
    * `X-Frame-Options`
    * `X-Content-Type-Options`
    * `Content-Security-Policy` (CSP)
    * `Referrer-Policy`
* 🔍 **Détection du Serveur :** Affiche la bannière `Server` si elle est présente (information utile pour la reconnaissance).
* 🛡️ **Gestion d'erreurs :** Gère les URL invalides ou les sites inaccessibles sans faire planter le programme.
* ✨ **Interface CLI propre :** Affichage clair des résultats avec des indicateurs visuels.

## 🛠️ Stack Technique

* **Langage :** Python 3.x
* **Bibliothèques :**
    * `requests` (pour les appels HTTP)
    * `sys` (bibliothèque standard)

## 💻 Comment utiliser ce projet ?

### Prérequis

Avoir Python installé sur votre machine.

### Installation

1. Clonez ce dépôt :
   ```bash
   git clone [https://github.com/VOTRE-NOM-UTILISATEUR/analyseur-securite-http.git](https://github.com/VOTRE-NOM-UTILISATEUR/analyseur-securite-http.git)