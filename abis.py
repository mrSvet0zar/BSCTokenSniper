# abis.py
# Ce fichier contient les ABIs des contrats intelligents utilisés dans BSCTokenSniper.py

# ABI de PancakeSwap Router (pour les fonctions d'achat comme swapExactETHForTokens)
pancake_abi = [
    {
        "inputs": [
            {"internalType": "address", "name": "_factory", "type": "address"},
            {"internalType": "address", "name": "_WETH", "type": "address"}
        ],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "inputs": [],
        "name": "WETH",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "address", "name": "tokenA", "type": "address"},
            {"internalType": "address", "name": "tokenB", "type": "address"},
            {"internalType": "uint256", "name": "amountADesired", "type": "uint256"},
            {"internalType": "uint256", "name": "amountBDesired", "type": "uint256"},
            {"internalType": "uint256", "name": "amountAMin", "type": "uint256"},
            {"internalType": "uint256", "name": "amountBMin", "type": "uint256"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "deadline", "type": "uint256"}
        ],
        "name": "addLiquidity",
        "outputs": [
            {"internalType": "uint256", "name": "amountA", "type": "uint256"},
            {"internalType": "uint256", "name": "amountB", "type": "uint256"},
            {"internalType": "uint256", "name": "liquidity", "type": "uint256"}
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "address", "name": "token", "type": "address"},
            {"internalType": "uint256", "name": "amountTokenDesired", "type": "uint256"},
            {"internalType": "uint256", "name": "amountTokenMin", "type": "uint256"},
            {"internalType": "uint256", "name": "amountETHMin", "type": "uint256"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "deadline", "type": "uint256"}
        ],
        "name": "addLiquidityETH",
        "outputs": [
            {"internalType": "uint256", "name": "amountToken", "type": "uint256"},
            {"internalType": "uint256", "name": "amountETH", "type": "uint256"},
            {"internalType": "uint256", "name": "liquidity", "type": "uint256"}
        ],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "factory",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "amountOut", "type": "uint256"},
            {"internalType": "uint256", "name": "reserveIn", "type": "uint256"},
            {"internalType": "uint256", "name": "reserveOut", "type": "uint256"}
        ],
        "name": "getAmountIn",
        "outputs": [{"internalType": "uint256", "name": "amountIn", "type": "uint256"}],
        "stateMutability": "pure",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "amountIn", "type": "uint256"},
            {"internalType": "uint256", "name": "reserveIn", "type": "uint256"},
            {"internalType": "uint256", "name": "reserveOut", "type": "uint256"}
        ],
        "name": "getAmountOut",
        "outputs": [{"internalType": "uint256", "name": "amountOut", "type": "uint256"}],
        "stateMutability": "pure",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "amountOut", "type": "uint256"},
            {"internalType": "address[]", "name": "path", "type": "address[]"}
        ],
        "name": "getAmountsIn",
        "outputs": [{"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "amountIn", "type": "uint256"},
            {"internalType": "address[]", "name": "path", "type": "address[]"}
        ],
        "name": "getAmountsOut",
        "outputs": [{"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "amountA", "type": "uint256"},
            {"internalType": "uint256", "name": "reserveA", "type": "uint256"},
            {"internalType": "uint256", "name": "reserveB", "type": "uint256"}
        ],
        "name": "quote",
        "outputs": [{"internalType": "uint256", "name": "amountB", "type": "uint256"}],
        "stateMutability": "pure",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "address", "name": "tokenA", "type": "address"},
            {"internalType": "address", "name": "tokenB", "type": "address"},
            {"internalType": "uint256", "name": "liquidity", "type": "uint256"},
            {"internalType": "uint256", "name": "amountAMin", "type": "uint256"},
            {"internalType": "uint256", "name": "amountBMin", "type": "uint256"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "deadline", "type": "uint256"}
        ],
        "name": "removeLiquidity",
        "outputs": [
            {"internalType": "uint256", "name": "amountA", "type": "uint256"},
            {"internalType": "uint256", "name": "amountB", "type": "uint256"}
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "address", "name": "token", "type": "address"},
            {"internalType": "uint256", "name": "liquidity", "type": "uint256"},
            {"internalType": "uint256", "name": "amountTokenMin", "type": "uint256"},
            {"internalType": "uint256", "name": "amountETHMin", "type": "uint256"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "deadline", "type": "uint256"}
        ],
        "name": "removeLiquidityETH",
        "outputs": [
            {"internalType": "uint256", "name": "amountToken", "type": "uint256"},
            {"internalType": "uint256", "name": "amountETH", "type": "uint256"}
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "address", "name": "token", "type": "address"},
            {"internalType": "uint256", "name": "liquidity", "type": "uint256"},
            {"internalType": "uint256", "name": "amountTokenMin", "type": "uint256"},
            {"internalType": "uint256", "name": "amountETHMin", "type": "uint256"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "deadline", "type": "uint256"}
        ],
        "name": "removeLiquidityETHSupportingFeeOnTransferTokens",
        "outputs": [{"internalType": "uint256", "name": "amountETH", "type": "uint256"}],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "address", "name": "token", "type": "address"},
            {"internalType": "uint256", "name": "liquidity", "type": "uint256"},
            {"internalType": "uint256", "name": "amountTokenMin", "type": "uint256"},
            {"internalType": "uint256", "name": "amountETHMin", "type": "uint256"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "deadline", "type": "uint256"},
            {"internalType": "bool", "name": "approveMax", "type": "bool"},
            {"internalType": "uint8", "name": "v", "type": "uint8"},
            {"internalType": "bytes32", "name": "r", "type": "bytes32"},
            {"internalType": "bytes32", "name": "s", "type": "bytes32"}
        ],
        "name": "removeLiquidityETHWithPermit",
        "outputs": [
            {"internalType": "uint256", "name": "amountToken", "type": "uint256"},
            {"internalType": "uint256", "name": "amountETH", "type": "uint256"}
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "address", "name": "token", "type": "address"},
            {"internalType": "uint256", "name": "liquidity", "type": "uint256"},
            {"internalType": "uint256", "name": "amountTokenMin", "type": "uint256"},
            {"internalType": "uint256", "name": "amountETHMin", "type": "uint256"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "deadline", "type": "uint256"},
            {"internalType": "bool", "name": "approveMax", "type": "bool"},
            {"internalType": "uint8", "name": "v", "type": "uint8"},
            {"internalType": "bytes32", "name": "r", "type": "bytes32"},
            {"internalType": "bytes32", "name": "s", "type": "bytes32"}
        ],
        "name": "removeLiquidityETHWithPermitSupportingFeeOnTransferTokens",
        "outputs": [{"internalType": "uint256", "name": "amountETH", "type": "uint256"}],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "address", "name": "tokenA", "type": "address"},
            {"internalType": "address", "name": "tokenB", "type": "address"},
            {"internalType": "uint256", "name": "liquidity", "type": "uint256"},
            {"internalType": "uint256", "name": "amountAMin", "type": "uint256"},
            {"internalType": "uint256", "name": "amountBMin", "type": "uint256"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "deadline", "type": "uint256"},
            {"internalType": "bool", "name": "approveMax", "type": "bool"},
            {"internalType": "uint8", "name": "v", "type": "uint8"},
            {"internalType": "bytes32", "name": "r", "type": "bytes32"},
            {"internalType": "bytes32", "name": "s", "type": "bytes32"}
        ],
        "name": "removeLiquidityWithPermit",
        "outputs": [
            {"internalType": "uint256", "name": "amountA", "type": "uint256"},
            {"internalType": "uint256", "name": "amountB", "type": "uint256"}
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "amountOut", "type": "uint256"},
            {"internalType": "address[]", "name": "path", "type": "address[]"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "deadline", "type": "uint256"}
        ],
        "name": "swapETHForExactTokens",
        "outputs": [{"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "amountOutMin", "type": "uint256"},
            {"internalType": "address[]", "name": "path", "type": "address[]"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "deadline", "type": "uint256"}
        ],
        "name": "swapExactETHForTokens",
        "outputs": [{"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "amountOutMin", "type": "uint256"},
            {"internalType": "address[]", "name": "path", "type": "address[]"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "deadline", "type": "uint256"}
        ],
        "name": "swapExactETHForTokensSupportingFeeOnTransferTokens",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "amountIn", "type": "uint256"},
            {"internalType": "uint256", "name": "amountOutMin", "type": "uint256"},
            {"internalType": "address[]", "name": "path", "type": "address[]"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "deadline", "type": "uint256"}
        ],
        "name": "swapExactTokensForETH",
        "outputs": [{"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "amountIn", "type": "uint256"},
            {"internalType": "uint256", "name": "amountOutMin", "type": "uint256"},
            {"internalType": "address[]", "name": "path", "type": "address[]"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "deadline", "type": "uint256"}
        ],
        "name": "swapExactTokensForETHSupportingFeeOnTransferTokens",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "amountIn", "type": "uint256"},
            {"internalType": "uint256", "name": "amountOutMin", "type": "uint256"},
            {"internalType": "address[]", "name": "path", "type": "address[]"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "deadline", "type": "uint256"}
        ],
        "name": "swapExactTokensForTokens",
        "outputs": [{"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "amountIn", "type": "uint256"},
            {"internalType": "uint256", "name": "amountOutMin", "type": "uint256"},
            {"internalType": "address[]", "name": "path", "type": "address[]"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "deadline", "type": "uint256"}
        ],
        "name": "swapExactTokensForTokensSupportingFeeOnTransferTokens",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "amountOut", "type": "uint256"},
            {"internalType": "uint256", "name": "amountInMax", "type": "uint256"},
            {"internalType": "address[]", "name": "path", "type": "address[]"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "deadline", "type": "uint256"}
        ],
        "name": "swapTokensForExactETH",
        "outputs": [{"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "amountOut", "type": "uint256"},
            {"internalType": "uint256", "name": "amountInMax", "type": "uint256"},
            {"internalType": "address[]", "name": "path", "type": "address[]"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "deadline", "type": "uint256"}
        ],
        "name": "swapTokensForExactTokens",
        "outputs": [{"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {"stateMutability": "payable", "type": "receive"}
]

# ABI de PancakeSwap Factory (pour écouter les événements PairCreated)
listening_abi = [
    {
        "inputs": [
            {"internalType": "address", "name": "_feeToSetter", "type": "address"}
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "anonymous": False,
        "inputs": [
            {"indexed": True, "internalType": "address", "name": "token0", "type": "address"},
            {"indexed": True, "internalType": "address", "name": "token1", "type": "address"},
            {"indexed": False, "internalType": "address", "name": "pair", "type": "address"},
            {"indexed": False, "internalType": "uint256", "name": "", "type": "uint256"}
        ],
        "name": "PairCreated",
        "type": "event"
    },
    {
        "constant": True,
        "inputs": [
            {"internalType": "uint256", "name": "", "type": "uint256"}
        ],
        "name": "allPairs",
        "outputs": [
            {"internalType": "address", "name": "", "type": "address"}
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "allPairsLength",
        "outputs": [
            {"internalType": "uint256", "name": "", "type": "uint256"}
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {"internalType": "address", "name": "tokenA", "type": "address"},
            {"internalType": "address", "name": "tokenB", "type": "address"}
        ],
        "name": "createPair",
        "outputs": [
            {"internalType": "address", "name": "pair", "type": "address"}
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "feeTo",
        "outputs": [
            {"internalType": "address", "name": "", "type": "address"}
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "feeToSetter",
        "outputs": [
            {"internalType": "address", "name": "", "type": "address"}
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {"internalType": "address", "name": "", "type": "address"},
            {"internalType": "address", "name": "", "type": "address"}
        ],
        "name": "getPair",
        "outputs": [
            {"internalType": "address", "name": "", "type": "address"}
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {"internalType": "address", "name": "_feeTo", "type": "address"}
        ],
        "name": "setFeeTo",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {"internalType": "address", "name": "_feeToSetter", "type": "address"}
        ],
        "name": "setFeeToSetter",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

# ABI minimal pour les tokens BEP-20 (pour récupérer le nom et le symbole)
token_name_abi = [
    {
        "anonymous": False,
        "inputs": [
            {"indexed": True, "internalType": "address", "name": "owner", "type": "address"},
            {"indexed": True, "internalType": "address", "name": "spender", "type": "address"},
            {"indexed": False, "internalType": "uint256", "name": "value", "type": "uint256"}
        ],
        "name": "Approval",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {"indexed": True, "internalType": "address", "name": "from", "type": "address"},
            {"indexed": True, "internalType": "address", "name": "to", "type": "address"},
            {"indexed": False, "internalType": "uint256", "name": "value", "type": "uint256"}
        ],
        "name": "Transfer",
        "type": "event"
    },
    {
        "constant": True,
        "inputs": [
            {"internalType": "address", "name": "_owner", "type": "address"},
            {"internalType": "address", "name": "spender", "type": "address"}
        ],
        "name": "allowance",
        "outputs": [
            {"internalType": "uint256", "name": "", "type": "uint256"}
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {"internalType": "address", "name": "spender", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"}
        ],
        "name": "approve",
        "outputs": [
            {"internalType": "bool", "name": "", "type": "bool"}
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {"internalType": "address", "name": "account", "type": "address"}
        ],
        "name": "balanceOf",
        "outputs": [
            {"internalType": "uint256", "name": "", "type": "uint256"}
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "decimals",
        "outputs": [
            {"internalType": "uint256", "name": "", "type": "uint256"}
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "getOwner",
        "outputs": [
            {"internalType": "address", "name": "", "type": "address"}
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "name",
        "outputs": [
            {"internalType": "string", "name": "", "type": "string"}
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "symbol",
        "outputs": [
            {"internalType": "string", "name": "", "type": "string"}
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [
            {"internalType": "uint256", "name": "", "type": "uint256"}
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {"internalType": "address", "name": "recipient", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"}
        ],
        "name": "transfer",
        "outputs": [
            {"internalType": "bool", "name": "", "type": "bool"}
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {"internalType": "address", "name": "sender", "type": "address"},
            {"internalType": "address", "name": "recipient", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"}
        ],
        "name": "transferFrom",
        "outputs": [
            {"internalType": "bool", "name": "", "type": "bool"}
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    }
]