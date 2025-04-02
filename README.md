# BSCTokenSniper v1.1

A bot written in Python to automatically detect and buy tokens on the Binance Smart Chain as soon as liquidity is provided, with Telegram notifications for new tokens.

BSCTokenSniper is a Python bot designed to detect new `PairCreated` events on the Binance Smart Chain (when a liquidity pair is created) and optionally buy the token. It now includes Telegram notifications to alert users about new tokens that pass the mini-audit (or all tokens if the mini-audit is disabled). The bot is reliable and works well, but if you find any problems, improvements, or suggestions, please let me know by raising an issue.

## Description

The aim of BSCTokenSniper is to detect new tokens on PancakeSwap and optionally buy them with a specified amount of BNB, with the goal of profiting from a price increase. Once the bot detects a `PairCreated` event, it can perform a mini-audit to filter out potential scams. It also sends a Telegram notification with the token's name, address, and price in BNB.

The bot can check if:
- Source code is verified.
- A valid PancakeSwap V2 router is being used.
- A mint function exists.
- The token is a potential honeypot.
- The PancakeSwap V1 router address is not being used.

The user can enable or disable the mini-audit. Be aware that disabling the mini-audit may result in investing in scams. After the mini-audit (or if it's disabled), the bot sends a Telegram notification with the token's details. If the `observeOnly` option is disabled, the bot will attempt to buy the token with the specified amount of BNB.

The bot interacts directly with the Binance Smart Chain using the PancakeSwap V2 router and factory addresses, making it much faster than using the PancakeSwap web interface or Metamask. By avoiding web interfaces and interacting directly with BSC nodes, you can snipe tokens almost instantly. During testing, the bot was typically among the first 3 buy transactions for detected tokens.

The bot uses the user's wallet address and private key to buy tokens. This information is kept secure, stored locally on your computer, and only used for buying tokens (you can review the code to confirm).

The bot does not incur additional fees beyond BSC network transaction fees and PancakeSwap fees.

## New Features in v1.1

- **Telegram Notifications**: The bot now sends Telegram notifications for each detected token that passes the mini-audit (or all tokens if the mini-audit is disabled). The notification includes the token's name, address (with a clickable BscScan link), and price in BNB.
- **Simplified Data**: The bot no longer retrieves the number of holders or liquidity to improve performance. The Telegram notification focuses on essential information: name, address, and price.

## Prerequisites

- Python 3 or later installed.
- Node.js installed (easiest way) – Install the Windows version from [https://nodejs.org/en/download/](https://nodejs.org/en/download/).
- Web3 installed (in Windows command line, type: `npm install web3`).
- BscScan API key (free of charge, create an account on [BscScan](https://bscscan.com/) and generate a free API key).
- BSC wallet address and private key.
- Enough BNB in your wallet to snipe tokens.
- A Telegram bot and chat ID for notifications (see the "Setting Up Telegram Notifications" section below).

## Setup

1. Install all dependencies listed above.
2. Edit the `config.json` file with your wallet address, private key, BscScan API key, and Telegram bot details (see the "Configuration File" section for details).
3. (Optional) If you are on Windows, open the command prompt, right-click the title bar, click ‘Properties,’ and set the screen buffer size height to 2500. This allows you to scroll through the history of your token snipes.
4. In the command prompt (assuming you are using Windows), type `python` and press Enter to check if it is recognized. If you get a message that it isn't recognized, edit the `launchBSCTokenSniper.bat` file and replace `python` with the path to your Python executable file (ensure the filepath is in quotes, e.g., `"C:\Python39\python.exe"`).
5. Run `launchBSCTokenSniper.bat`, and the bot will start!

## Setting Up Telegram Notifications

The bot can send notifications to a Telegram chat whenever a new token is detected. Follow these steps to set up Telegram notifications:

1. **Create a Telegram Bot**:
   - Open Telegram and search for the `@BotFather` bot.
   - Start a chat with `@BotFather` and send the command `/newbot`.
   - Follow the instructions to name your bot (e.g., "BSCTokenSniperBot").
   - Once created, BotFather will provide a **bot token** (e.g., `7607613951:AAFeQb5BW16liTBM9DdyY6NchrrdLSHwhMM`). Copy this token.

2. **Get Your Chat ID**:
   - Create a private chat or group where you want to receive notifications.
   - Add your bot to the chat or group (search for your bot's name and add it).
   - Send a message in the chat (e.g., "Hello").
   - Open a browser and go to the following URL, replacing `<YOUR_BOT_TOKEN>` with your bot token: https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates  
   For example :  
   https://api.telegram.org/bot7607613951:AAFeQb5BW16liTBM9DdyY6NchrrdLSHwhMM/getUpdates  
   - Look for the `chat` object in the JSON response. The `id` field is your chat ID (e.g., `572531500`). Copy this ID.

3. **Add Telegram Details to `config.json`**:
- Open the `config.json` file in a text editor.
- Add the following fields with the values you obtained:
```json
"telegramBotToken": "7607613951:AAFeQb5BW16liTBM9DdyY6NchrrdLSHwhMM",
"telegramChatId": "572531500",
"enableTelegramNotifications": "True"  
"telegramBotToken": "Your bot token from BotFather"  
"telegramChatId": "The chat ID where notifications will be sent"  
"enableTelegramNotifications": "Set to True toenable notifications, or False to disable them"  
```  
4. **Test the notifications:**  
- Run the bot using `launchBSCTokenSniper.bat`.  
- When a new token is detected, you should receive a Telegram message like this:  
```text  
🎉 **New Token Detected!** 🎉

📛 *Name*: **TokenName**
🏠 *Address*: [0x123...](https://bscscan.com/address/0x123...)
💰 *Price*: _1.23e-5 BNB_ 🚀  
```  
## Configuration File  
The `config.json` file contains all the settings for the bot. Edit it with your details before running the bot.  

```json  
"walletAddress": "Your BSC wallet address (e.g., from Metamask)."  
"walletPrivateKey": "The private key of your wallet address (kept secure and only used locally to buy tokens)"  
"telegramBotToken": "Your Telegram bot token (see 'Setting Up Telegram Notifications')."  
"telegramChatId": "The chat ID for Telegram notifications (see 'Setting Up Telegram Notifications')."  
"enableTelegramNotifications": "Set to True to enable Telegram notifications, or False to disable them."  
"pancakeSwapRouterAddress": "The PancakeSwap V2 router address (default: '0x10ED43C718714eb63d5aA57B78B54704E256024E')."  
"pancakeSwapFactoryAddress": "The PancakeSwap factory address (default: '0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73')."  
"wBNBAddress": "The Wrapped BNB (WBNB) address (default: '0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c')."  
"amountToSpendPerSnipe": "The amount of BNB to spend on each new token (e.g., '0.00025' means 0.00025 BNB per snipe)."  
"transactionRevertTimeSeconds": "Time in seconds before a transaction reverts if not confirmed. Recommended to leave at default ('60')."  
"gasAmount": "Maximum gas to use per transaction. Recommended to leave at default ('300000')."  
"gasPrice": "Maximum gas price in Gwei per transaction. Recommended to leave at default ('10')."  
"bscScanAPIKey": "Your API key from BscScan (required for the mini-audit)."  
"observeOnly": "Set to True to disable buying and only observe token detection and notifications. Recommended for initial testing."  
```  

- **Mini-audit options** (set to True or False):  
```json  
"checkSourceCode": "Checks if the source code is verified on BscScan. Required for other audit checks. Recommended."  
"checkValidPancakeV2": "Checks if the correct PancakeSwap V2 router address is used. May reject some valid tokens due to external router settings. Not recommended."  
"checkMintFunction": "Checks if a mint function exists in the code. Recommended."  
"checkHoneypot": "Checks for potential honeypot behavior (where you can buy but not sell). Recommended."  
"checkPancakeV1Router": "Checks if the PancakeSwap V1 router address is used (you won't be able to sell if it is). Highly recommended."  
```  

**Note**: Be careful when editing `config.json`. Ensure you maintain proper JSON syntax (e.g., don't delete commas or quotation marks). For mini-audit options, use True or False with the first letter capitalized.  

## Mini-Audit  

The bot includes an optional mini-audit feature to filter out potential scam tokens (e.g., honeypots, misconfigured contracts). While not as thorough as a professional audit (e.g., CertiK), it helps improve the quality of tokens the bot interacts with, increasing the likelihood that you can sell them later (provided the token isn't rugged).  

Set all mini-audit options to False in config.json to disable the mini-audit, but be aware that you may end up buying many scam tokens.  

## Things to Note  

- **Token Detection Frequency**: Don't worry if no new tokens are detected for a few minutes. On average, 10-20 new tokens are created per minute on BSC, but this can vary.  
- **WBNB Pairing**: The bot only detects tokens paired with Wrapped BNB (WBNB). You can modify the code to detect tokens paired with other currencies if desired.  
- **Sufficient BNB**: Ensure your wallet has enough BNB to cover sniping costs and transaction fees. If not, the bot will fail to buy tokens.  
- **Editing `config.json`**: Be cautious when editing config.json. Missing commas, quotation marks, or incorrect syntax will cause the bot to fail.  
- **Launching the Bot**: Run `launchBSCTokenSniper.bat` to start the bot. It will open in a command prompt window and begin scanning.  
- **Command Prompt Select Mode**: Avoid left-clicking in the command prompt window, as it will enable "Select" mode and pause the output (you'll see "Select" in the title). Right-click to deselect and resume.  

## FAQs  

**I've sniped lots of coins - how can I check which ones have made a profit?**  

- Go to [poocoin.app](https://poocoin.app/), click "Wallet," and connect your Web3 wallet (e.g., Metamask).  
- It will list the tokens in your wallet and show their profit/loss.  
- Sort by balance (descending) to see the highest-value tokens.  
- Manually sell profitable tokens on PancakeSwap.  

**I keep getting 'Transaction failed' - what's going on?**  

This could be due to:  

- Gas amount or price too low.  
- Incorrect wallet address or private key.  
- Insufficient BNB to cover the token cost and transaction fees.  

**The bot isn't sniping that fast (e.g., a couple of seconds between detection and buying).**  

- This is mainly due to internet speed and computer processing power  

## Risks  

Investing in BSC tokens (often called "shitcoins") is highly risky, and you could lose all your money. Only invest what you are prepared to lose.  

Sniping tokens early makes it difficult to avoid rug pulls. When a token is created, liquidity is typically added manually on PancakeSwap, which is when the bot detects it. Even if liquidity is later burned or locked (e.g., by sending LP tokens to a dead address or liquidity locker), the bot cannot guarantee the token isn't a rug pull at the time of detection.  

The mini-audit feature aims to filter out many scams but is not 100% accurate. Sophisticated scams may bypass detection, though this is rare since most tokens are forks of larger projects (e.g., Safemoon) with minimal code changes.  

## Things to Do / Improve / Bug Fixes / Thoughts  

- Clarify Web3 installation, as many users have had issues with it.  
- Improve honeypot detection (currently basic; some tokens rewrite their code to bypass detection). [bscheck.eu](https://bscheck.eu/) does a better job—consider contacting them to learn about their detection algorithm.  
- Improve reliability (the bot can occasionally freeze).  
- Use `WebsocketProvider` instead of `HTTPProvider` for faster token sniping.  
- Implement a feature to only invest in tokens with a minimum amount of liquidity (e.g., 10 BNB).  
- Add a GUI (optional).  
- Explore rug pull detection.  
- Add an auto-sell feature after reaching a certain profit threshold.  
- Create an `ETHTokenSniper` version for the Ethereum blockchain.  
- Optimize the code for faster execution and sniping.  
- Reconsider the assumption that unverified source code always indicates a scam. Some legitimate developers may not verify their code before adding liquidity.  
- Ignore tokens named "test."  
- Add an option to snipe a specific token by providing its contract address, buying as soon as liquidity is added, and optionally selling at a target price (e.g., see the Refinable case, where a bot made significant profits in minutes).  

## Donations  

If you’ve found this bot useful and have profited from it, please consider donating any token to my BSC wallet address: `0x38cc265Ba9Af0deA866277f80eC4e719b6F452B4`.