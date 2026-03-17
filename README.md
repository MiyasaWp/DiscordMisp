MISP Discord Bot

Un bot Discord conçu pour assurer le pont entre une instance MISP et un serveur Discord. Il permet de surveiller les menaces en temps réel et d'interroger la base de données de menaces directement via des commandes slash.

Architecture du Projet

Le bot repose sur deux piliers principaux :

    Connexion MISP : Communication via l'API REST (PyMISP) pour récupérer les derniers événements et attributs.

    Connexion Discord : Utilisation de la bibliothèque discord.py pour l'envoi de notifications et la gestion des commandes.

Fonctionnalités Clés 

    Polling & Notifications : Surveillance automatique de l'instance MISP toutes les X minutes. Envoi d'alertes détaillées dans un salon spécifique lors de la détection de nouveaux événements.

    Recherche Simple : Commande /misp_search <indicator> permettant de vérifier instantanément si une IP, un domaine ou un hash est déjà présent dans votre instance.

    Filtrage Intelligent : Système de filtrage par tags pour éviter le "bruit". Vous pouvez configurer le bot pour ne notifier que les événements critiques (ex: tlp:red ou threat-level:high).
