from web3 import Web3
import requests
import json
import os

# Charger la configuration
config_file_path = os.path.abspath('') + '/config.json'
with open(config_file_path, 'r') as config_file:
    config = json.load(config_file)

# Variables de configuration
pancakeSwapFactoryAddress = config["pancakeSwapFactoryAddress"]
wBNBAddress = config["wBNBAddress"]
web3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))

# ABI minimal pour la paire PancakeSwap (pour getReserves)
pair_abi = [
    {
        "constant": True,
        "inputs": [],
        "name": "getReserves",
        "outputs": [
            {"internalType": "uint112", "name": "_reserve0", "type": "uint112"},
            {"internalType": "uint112", "name": "_reserve1", "type": "uint112"},
            {"internalType": "uint32", "name": "_blockTimestampLast", "type": "uint32"}
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "token0",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "token1",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    }
]

# ABI minimal pour le factory PancakeSwap (pour getPair)
factory_abi = [
    {
        "constant": True,
        "inputs": [
            {"internalType": "address", "name": "", "type": "address"},
            {"internalType": "address", "name": "", "type": "address"}
        ],
        "name": "getPair",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    }
]

# Fonction pour obtenir le prix (on ne récupère plus la liquidité)
def get_price(token_address):
    """
    Récupère uniquement le prix d'un token en BNB à partir de sa paire de liquidité sur PancakeSwap.
    
    Args:
        token_address (str): Adresse du contrat du token.
    
    Returns:
        float: Prix en BNB par token (0 si erreur ou pas de paire).
    """
    try:
        factory_contract = web3.eth.contract(address=pancakeSwapFactoryAddress, abi=factory_abi)
        pair_address = factory_contract.functions.getPair(token_address, wBNBAddress).call()
        
        if pair_address == "0x0000000000000000000000000000000000000000":
            return 0  # Pas de paire de liquidité

        pair_contract = web3.eth.contract(address=pair_address, abi=pair_abi)
        reserves = pair_contract.functions.getReserves().call()
        token0 = pair_contract.functions.token0().call()
        
        # Déterminer quel token est WBNB et quel token est le token cible
        if token0.lower() == wBNBAddress.lower():
            reserve_bnb = reserves[0] / 1e18  # WBNB (reserve0)
            reserve_token = reserves[1] / 1e18  # Token (reserve1)
        else:
            reserve_bnb = reserves[1] / 1e18  # WBNB (reserve1)
            reserve_token = reserves[0] / 1e18  # Token (reserve0)

        # Calculer le prix (BNB par token)
        if reserve_token == 0:
            price_in_bnb = 0
        else:
            price_in_bnb = reserve_bnb / reserve_token

        return price_in_bnb
    except Exception as e:
        print(f"[Error] Failed to get price: {str(e)}")
        return 0

# Fonction pour formater un nombre en notation scientifique
def to_scientific_notation(number):
    """
    Formate un nombre en notation scientifique avec 2 décimales.
    
    Args:
        number (float): Nombre à formater.
    
    Returns:
        str: Nombre formaté en notation scientifique (ou "0" si le nombre est 0).
    """
    if number == 0:
        return "0"
    return "{:.2e}".format(number)

# Fonction pour envoyer un message Telegram (en anglais, sans liquidité ni holders)
def send_telegram_message(token_name, token_address, price):
    """
    Envoie un message Telegram formaté avec le nom, l'adresse et le prix du token.
    
    Args:
        token_name (str): Nom du token.
        token_address (str): Adresse du contrat du token.
        price (float): Prix en BNB par token.
    """
    try:
        bot_token = config["telegramBotToken"]
        chat_id = config["telegramChatId"]
        enable_notifications = config["enableTelegramNotifications"].lower() == "true"

        if not enable_notifications:
            return

        # Construire le lien BscScan
        bscscan_link = f"https://bscscan.com/address/{token_address}"

        # Formater le message avec Markdown (en anglais)
        message = (
            "🎉 **New Token Detected!** 🎉\n\n"
            f"📛 *Name*: **{token_name}**\n"
            f"🏠 *Address*: [{token_address}]({bscscan_link})\n"
            f"💰 *Price*: _{to_scientific_notation(price)} BNB_ 🚀"
        )

        # URL pour envoyer le message via l'API Telegram
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "Markdown"
        }
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("[Info] Telegram notification sent successfully!")
        else:
            print(f"[Error] Failed to send Telegram notification: {response.text}")
    except Exception as e:
        print(f"[Error] Failed to send Telegram notification: {str(e)}")