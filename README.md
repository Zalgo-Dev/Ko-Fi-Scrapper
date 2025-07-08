# Ko-Fi Scraper

Un bot Python qui surveille automatiquement une boutique Ko-Fi et envoie des notifications Discord lorsque de nouveaux articles sont ajoutés.

## 🚀 Fonctionnalités

- **Surveillance automatique** : Vérifie une boutique Ko-Fi toutes les minutes pour détecter les nouveaux articles
- **Notifications Discord** : Envoie des messages avec embed riches contenant toutes les informations de l'article
- **Extraction complète** : Récupère le nom, l'image, les tags, la description et le prix de chaque article
- **Évite les doublons** : Stocke les articles déjà traités dans un fichier JSON pour éviter les notifications répétées
- **Mode headless** : Fonctionne en arrière-plan sans interface graphique
- **Logging détaillé** : Journalisation complète pour le suivi et le débogage

## 📋 Prérequis

- Python 3.7+
- Google Chrome installé
- ChromeDriver (doit être dans le PATH)
- Un webhook Discord configuré

## 🛠️ Installation

1. **Cloner le repository**
   ```bash
   git clone https://github.com/votre-username/Ko-Fi-Scrapper.git
   cd Ko-Fi-Scrapper
   ```

2. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

3. **Télécharger ChromeDriver**
   - Téléchargez ChromeDriver depuis [https://chromedriver.chromium.org/](https://chromedriver.chromium.org/)
   - Assurez-vous qu'il correspond à votre version de Chrome
   - Ajoutez-le à votre PATH ou placez-le dans le dossier du projet

## ⚙️ Configuration

Avant d'exécuter le script, vous devez modifier les paramètres de configuration dans `ko-fi.py` :

```python
url = 'https://ko-fi.com/example/shop'  # 🔴 REMPLACEZ par l'URL de la boutique Ko-Fi à surveiller
discord_webhook_url = 'https://discord.com/api/webhooks/YOUR_WEBHOOK_URL'  # 🔴 REMPLACEZ par votre webhook Discord
embed_color = 0x3498db  # Couleur de l'embed Discord (optionnel)
```

### Créer un webhook Discord

1. Allez dans les paramètres de votre serveur Discord
2. Sélectionnez "Intégrations" → "Webhooks"
3. Cliquez sur "Créer un webhook"
4. Copiez l'URL du webhook et remplacez `discord_webhook_url` dans le code

## 🚀 Utilisation

1. **Configurer les paramètres** dans `ko-fi.py`
2. **Lancer le script** :
   ```bash
   python ko-fi.py
   ```

Le script va :
- Effectuer un scan initial de la boutique
- Envoyer des notifications pour tous les articles existants (premier lancement)
- Continuer à surveiller la boutique toutes les 60 secondes
- Envoyer des notifications uniquement pour les nouveaux articles

## 📁 Structure des fichiers

```
Ko-Fi-Scrapper/
│
├── ko-fi.py           # Script principal
├── requirements.txt   # Dépendances Python
├── items.json        # Base de données des articles (créé automatiquement)
├── LICENSE           # Licence du projet
└── README.md         # Ce fichier
```

## 📊 Format des notifications Discord

Chaque notification contient :
- **Titre** : Nom de l'article (avec lien vers la page Ko-Fi)
- **Image** : Photo principale de l'article
- **Tags** : Catégories/mots-clés de l'article
- **Description** : Description complète de l'article
- **Prix** : Prix de l'article
- **Mention** : @everyone pour notifier tous les membres

## 🔧 Personnalisation

### Modifier l'intervalle de vérification
```python
# Changez 60 pour un nombre de secondes différent
time.sleep(60)  # Vérification toutes les 60 secondes
```

### Modifier la couleur de l'embed
```python
embed_color = 0x3498db  # Bleu (défaut)
embed_color = 0xe74c3c  # Rouge
embed_color = 0x2ecc71  # Vert
```

### Désactiver les mentions @everyone
```python
data = {
    "content": "",  # Supprimer "@everyone"
    "embeds": [...]
}
```

## 🐛 Résolution des problèmes

### ChromeDriver non trouvé
```
WebDriverException: 'chromedriver' executable needs to be in PATH
```
**Solution** : Assurez-vous que ChromeDriver est installé et dans votre PATH.

### Erreur de webhook Discord
```
Error sending message for item: /s/shop/item/...
Response status: 400
```
**Solution** : Vérifiez que votre URL de webhook Discord est correcte.

### Éléments non trouvés
```
TimeoutException: Message: 
```
**Solution** : L'URL de la boutique Ko-Fi peut être incorrecte ou la structure de la page a changé.

## 📝 Logs

Le script génère des logs détaillés pour chaque opération :
- Chargement/sauvegarde des articles
- Découverte de nouveaux articles
- Extraction des détails
- Envoi des notifications Discord
- Erreurs et exceptions

## ⚠️ Considérations importantes

- **Respect du site** : Le script inclut des pauses pour éviter de surcharger les serveurs Ko-Fi
- **Utilisation responsable** : Utilisez ce script uniquement pour surveiller vos propres boutiques ou avec permission
- **Données personnelles** : Ne partagez jamais votre URL de webhook Discord

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
- Signaler des bugs
- Proposer de nouvelles fonctionnalités
- Améliorer la documentation
- Soumettre des pull requests

## 📄 Licence

Ce projet est sous licence [MIT](LICENSE).

## 🆘 Support

Si vous rencontrez des problèmes :
1. Vérifiez les logs du script
2. Consultez la section "Résolution des problèmes"
3. Ouvrez une issue sur GitHub avec les détails de l'erreur

---

**Note** : Ce projet est à des fins éducatives et de surveillance personnelle. Respectez les conditions d'utilisation de Ko-Fi et Discord.