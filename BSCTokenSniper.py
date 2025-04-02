print("Loading...")

import time
from web3 import Web3
import datetime
import requests
import threading
import json
import asyncio
import os
import sys
import ctypes
from utils import get_price, send_telegram_message, to_scientific_notation
from abis import pancake_abi, listening_abi, token_name_abi

# Configuration de la console
os.system("mode con: lines=32766")
os.system("")  # Permet l'utilisation de couleurs dans la console

# Définition des styles de couleur
class style:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

# Affichage du logo
print(style.MAGENTA)
print(" ██████╗ ███████╗ ██████╗    ████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗    ███████╗███╗   ██╗██╗██████╗ ███████╗██████╗ ")
print(" ██╔══██╗██╔════╝██╔════╝    ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║    ██╔════╝████╗  ██║██║██╔══██╗██╔════╝██╔══██╗")
print(" ██████╔╝███████╗██║            ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║    ███████╗██╔██╗ ██║██║██████╔╝█████╗  ██████╔╝")
print(" ██╔══██╗╚════██║██║            ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║    ╚════██║██║╚██╗██║██║██╔═══╝ ██╔══╝  ██╔══██╗")
print(" ██████╔╝███████║╚██████╗       ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║    ███████║██║ ╚████║██║██║     ███████╗██║  ██║")
print(" ╚═════╝ ╚══════╝ ╚═════╝       ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝    ╚══════╝╚═╝  ╚═══╝╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝")
print(style.WHITE)

# Initialisation du titre de la console
ctypes.windll.kernel32.SetConsoleTitleW("BSCTokenSniper | Loading...")

# Variables globales
currentTimeStamp = ""
numTokensDetected = 0
numTokensBought = 0
walletBalance = 0

# Fonction pour obtenir le timestamp
def getTimestamp():
    while True:
        timeStampData = datetime.datetime.now()
        global currentTimeStamp
        currentTimeStamp = "[" + timeStampData.strftime("%H:%M:%S.%f")[:-3] + "]"

# Charger la configuration
config_file_path = os.path.abspath('') + '/config.json'
with open(config_file_path, 'r') as config_file:
    config = json.load(config_file)

# Variables de configuration
bsc = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(bsc))
pancakeSwapRouterAddress = config['pancakeSwapRouterAddress']
pancakeSwapFactoryAddress = config['pancakeSwapFactoryAddress']
wBNBAddress = config['wBNBAddress']
walletAddress = config['walletAddress']
private_key = config['walletPrivateKey']
snipeBNBAmount = float(config['amountToSpendPerSnipe'])
transactionRevertTime = int(config['transactionRevertTimeSeconds'])
gasAmount = int(config['gasAmount'])
gasPrice = int(config['gasPrice'])
bscScanAPIKey = config['bscScanAPIKey']
observeOnly = config['observeOnly'].lower() == "true"
checkSourceCode = config['checkSourceCode'].lower() == "true"
checkValidPancakeV2 = config['checkValidPancakeV2'].lower() == "true"
checkMintFunction = config['checkMintFunction'].lower() == "true"
checkHoneypot = config['checkHoneypot'].lower() == "true"
checkPancakeV1Router = config['checkPancakeV1Router'].lower() == "true"
enableMiniAudit = checkSourceCode and (checkValidPancakeV2 or checkMintFunction or checkHoneypot or checkPancakeV1Router)

# Vérification de la connexion Web3
if web3.is_connected():
    print(currentTimeStamp + " [Info] Web3 successfully connected")
    latest_block = web3.eth.block_number
    print(currentTimeStamp + f" [Info] Latest block number: {latest_block}")
else:
    print(currentTimeStamp + " [Error] Failed to connect to Web3")
    sys.exit(1)

# Mise à jour du titre de la console
def updateTitle():
    global walletBalance
    walletBalance = web3.from_wei(web3.eth.get_balance(walletAddress), 'ether')
    walletBalance = round(walletBalance, -(int("{:e}".format(walletBalance).split('e')[1]) - 4))
    ctypes.windll.kernel32.SetConsoleTitleW(
        f"BSCTokenSniper | Tokens Detected: {numTokensDetected} | Tokens Bought: {numTokensBought} | Wallet Balance: {walletBalance} BNB"
    )

# Initialisation du timestamp
timeStampThread = threading.Thread(target=getTimestamp)
timeStampThread.start()

updateTitle()
print(currentTimeStamp + " [Info] Using Wallet Address: " + walletAddress)
print(currentTimeStamp + " [Info] Using Snipe Amount: " + str(snipeBNBAmount) + " BNB")

# Fonction d'achat d'un token
def Buy(tokenAddress, tokenSymbol):
    if tokenAddress is None:
        return
    tokenToBuy = web3.toChecksumAddress(tokenAddress)
    spend = web3.toChecksumAddress(wBNBAddress)  # WBNB contract address
    contract = web3.eth.contract(address=pancakeSwapRouterAddress, abi=pancake_abi)
    nonce = web3.eth.get_transaction_count(walletAddress)
    pancakeswap2_txn = contract.functions.swapExactETHForTokens(
        0,
        [spend, tokenToBuy],
        walletAddress,
        (int(time.time()) + transactionRevertTime)
    ).buildTransaction({
        'from': walletAddress,
        'value': web3.to_wei(float(snipeBNBAmount), 'ether'),
        'gas': gasAmount,
        'gasPrice': web3.to_wei(gasPrice, 'gwei'),
        'nonce': nonce,
    })

    try:
        signed_txn = web3.eth.account.sign_transaction(pancakeswap2_txn, private_key)
        tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        txHash = str(web3.to_hex(tx_token))
        checkTransactionSuccessURL = f"https://api.bscscan.com/api?module=transaction&action=gettxreceiptstatus&txhash={txHash}&apikey={bscScanAPIKey}"
        checkTransactionRequest = requests.get(url=checkTransactionSuccessURL)
        txResult = checkTransactionRequest.json()['status']

        if txResult == "1":
            print(style.GREEN + currentTimeStamp + f" Successfully bought ${tokenSymbol} for {style.BLUE}{snipeBNBAmount}{style.GREEN} BNB - TX ID: {txHash}")
        else:
            print(style.RED + currentTimeStamp + " Transaction failed: likely not enough gas.")
    except Exception as e:
        print(style.RED + currentTimeStamp + f" Transaction failed: {str(e)}")
    updateTitle()

# Fonction appelée lorsqu'un nouveau token est détecté
def foundToken(event):
    global numTokensDetected, numTokensBought
    try:
        jsonEventContents = json.loads(web3.to_json(event))
        if jsonEventContents['args']['token0'] == wBNBAddress:
            tokenAddress = jsonEventContents['args']['token1']
        elif jsonEventContents['args']['token1'] == wBNBAddress:
            tokenAddress = jsonEventContents['args']['token0']
        else:
            return  # Ignorer si la paire ne contient pas WBNB

        # Récupérer le nom et le symbole du token
        try:
            getTokenName = web3.eth.contract(address=tokenAddress, abi=token_name_abi)
            tokenName = getTokenName.functions.name().call()
            tokenSymbol = getTokenName.functions.symbol().call()
        except Exception as e:
            tokenName = "Unknown"
            tokenSymbol = "Unknown"
            print(style.RED + currentTimeStamp + f" [Error] Failed to get token name/symbol: {str(e)}")

        # Afficher le message de détection
        print(style.YELLOW + currentTimeStamp + " [Token] New potential token detected: " + style.CYAN + tokenName + " (" + tokenSymbol + "): " + style.MAGENTA + tokenAddress + style.RESET)
        numTokensDetected += 1
        updateTitle()

        # Si le mini-audit est désactivé, envoyer directement une notification Telegram
        if not enableMiniAudit:
            price = get_price(tokenAddress)
            send_telegram_message(tokenName, tokenAddress, price)
            if not observeOnly:
                numTokensBought += 1
                Buy(tokenAddress, tokenSymbol)
                updateTitle()
        else:
            # Mini-audit
            print(style.YELLOW + "[Token] Starting Mini Audit...")
            try:
                contractCodeGetRequestURL = f"https://api.bscscan.com/api?module=contract&action=getsourcecode&address={tokenAddress}&apikey={bscScanAPIKey}"
                contractCodeRequest = requests.get(url=contractCodeGetRequestURL)
                tokenContractCode = contractCodeRequest.json()

                if str(tokenContractCode['result'][0]['ABI']) == "Contract source code not verified" and checkSourceCode:
                    print(style.RED + "[FAIL] Contract source code isn't verified.")
                elif "0x05fF2B0DB69458A0750badebc4f9e13aDd608C7F" in str(tokenContractCode['result'][0]['SourceCode']) and checkPancakeV1Router:
                    print(style.RED + "[FAIL] Contract uses PancakeSwap v1 router.")
                elif str(pancakeSwapRouterAddress) not in str(tokenContractCode['result'][0]['SourceCode']) and checkValidPancakeV2:
                    print(style.RED + "[FAIL] Contract doesn't use valid PancakeSwap v2 router.")
                elif "mint" in str(tokenContractCode['result'][0]['SourceCode']) and checkMintFunction:
                    print(style.RED + "[FAIL] Contract has mint function enabled.")
                elif ("function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool)" in str(tokenContractCode['result'][0]['SourceCode']) or "function _approve(address owner, address spender, uint256 amount) internal" in str(tokenContractCode['result'][0]['SourceCode']) or "newun" in str(tokenContractCode['result'][0]['SourceCode'])) and checkHoneypot:
                    print(style.RED + "[FAIL] Contract is a honeypot.")
                else:
                    print(style.GREEN + "[SUCCESS] Token has passed mini audit.")
                    # Récupérer le prix et envoyer une notification Telegram
                    price = get_price(tokenAddress)
                    send_telegram_message(tokenName, tokenAddress, price)
                    if not observeOnly:
                        numTokensBought += 1
                        Buy(tokenAddress, tokenSymbol)
                        updateTitle()
            except Exception as e:
                print(style.RED + currentTimeStamp + f" [Error] Mini-audit failed: {str(e)}")

        print("")  # Saut de ligne

    except Exception as e:
        print(style.RED + currentTimeStamp + f" [Error] Error processing token event: {str(e)}")

# Boucle d'écoute des événements
async def tokenLoop(event_filter, poll_interval):
    while True:
        try:
            for PairCreated in event_filter.get_new_entries():
                foundToken(PairCreated)
            await asyncio.sleep(poll_interval)
        except Exception as e:
            print(style.RED + currentTimeStamp + f" [Error] Error in token loop: {str(e)}")
            break

# Fonction principale pour écouter les tokens
def listenForTokens():
    contract = web3.eth.contract(address=pancakeSwapFactoryAddress, abi=listening_abi)
    print(currentTimeStamp + " [Info] Scanning for new tokens...")
    print("")
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    event_filter = contract.events.PairCreated.create_filter(from_block=web3.eth.block_number - 1000)
    try:
        loop.run_until_complete(tokenLoop(event_filter, 1))
    except Exception as e:
        print(style.RED + currentTimeStamp + f" [Error] Event loop error: {str(e)}")
        listenForTokens()
    finally:
        loop.close()

# Lancer l'écoute des tokens
listenForTokens()

input("")