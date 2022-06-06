# live_tools

Fork du projet [live_tools](https://github.com/CryptoRobotFr/live_tools) de [CryptoRobotFr](https://github.com/CryptoRobotFr).

## Installation
Liste des commandes pour set-up le projet.

### Cloner le projet
Lancer la commande à la racine du compte :
> git clone https://github.com/be-next/live_tools.git 

### Préparation de l'environnement
Permet de mettre à jour l'OS, d'installer la commande `pip` et d'installer les librairies `python` nécessaires l'exécution du `bot`.
> bash ./live_tools/install.sh

## Trix optimisé pour TRON (TRX)
Pour exécuter le `bot` `trix_trx` toutes les heures (et 1 minute), il faut ajouter la ligne suivante dans la cron tab (`crontab -e`):
> 1 * * * * python3 ./live_tools/strategies/trix/trix_trx.py >> trix_trx.log 2>&1
