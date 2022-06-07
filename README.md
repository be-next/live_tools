# live_tools

Fork du projet [live_tools](https://github.com/CryptoRobotFr/live_tools) de [CryptoRobotFr](https://github.com/CryptoRobotFr).
L'objectif de ce fork est de proposer une version live du `trix` avec des paramètres optimisés.

## Fonctionnement du TRIX
`bot` simple conçu pour s'exécuter toutes les heures (i.e. sur la base de l'analyse des bougies horaires).

La stratégie prend en compte le `trix` et le `stochastic RSI` 
(La stratégie est présentée dans cette vidéo [Le TRIX la stratégie la plus RENTABLE ?! 1000$ to 1M$ sur ETH en 4 ans | TrueStrategy#4](https://youtu.be/uE04UROWkjs)) 
avec des paramètres optimisés pour le TRX et le SOL (cf. [Optimiser vos BOT de TRADING afin de gagner en RENTABILITÉ ! Guide python d'optimisation du TRIX](https://youtu.be/jm-UfVPqUQo)).

Le `bot` utilise l'exchage FTX :
> Lien d'affiliation FTX : https://ftx.com/eu/profile#a=121892334
> (*utiliser ce lien permet d'économiser 5% sur les frais de transaction*).


## Installation
Liste des commandes pour set-up le projet.

### Cloner le projet
Lancer la commande à la racine du compte :
> `$> git clone https://github.com/be-next/live_tools.git`

### Préparation de l'environnement
Permet de mettre à jour l'OS, d'installer la commande `pip` et d'installer les librairies `python` nécessaires l'exécution des `bots`.
> `$> bash ./live_tools/install.sh`

## Trix optimisé pour TRON (TRX)
Pour exécuter le `bot` `trix_trx` toutes les heures (et 1 minute), il faut ajouter la ligne suivante dans la cron tab (`crontab -e`):
> `1 * * * * python3 ./live_tools/strategies/trix/trix_trx.py >> trix_trx.log 2>&1`

## Trix optimisé pour SOLANA (SOL)
Pour exécuter le `bot` `trix_sol` toutes les heures (et 2 minutes), il faut ajouter la ligne suivante dans la cron tab (`crontab -e`):
> `1 * * * * python3 ./live_tools/strategies/trix/trix_sol.py >> trix_sol.log 2>&1`
