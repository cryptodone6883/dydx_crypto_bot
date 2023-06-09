from dydx3.constants import API_HOST_GOERLI, API_HOST_MAINNET
from decouple import config

# !! Select mode !!
MODE = 'DEV'

# Close all open positions and orders
ABORT_ALL_POSITIONS = False

# Find Cointegrated Pairs
FIND_COINTEGRATED = False

# Place Trades
PLACE_TRADES = True

# Manage Exit
MANAGE_EXITS = True

# Resolution
RESOLUTION = "1HOUR"

# Stats Window
WINDOW = 21

# Thresholds - Opening
MAX_HALF_LIFE = 24
ZSCORE_THRESH = 1.5
USD_PER_TRADE = 40
USD_MIN_COLLATERAL = 1800

# Thresholds - Closing
CLOSE_AT_ZSCORE_CROSS = True

# Eth address
ETHEREUM_ADDRESS = "0x317337c30fF2d9fd17c527911fa9143C09B353Df"

# KEYS production
# mainnet
STARK_PRIVATE_KEY_MAINNET = config("STARK_PRIVATE_KEY_MAINNET")
DYDX_API_KEY_MAINNET = config("DYDX_API_KEY_MAINNET")
DYDX_API_SECRET_MAINNET = config("DYDX_API_SECRET_MAINNET")
DYDX_API_PASSPHRASE_MAINNET = config("DYDX_API_PASSPHRASE_MAINNET")

# KEYS DEVELOPMENT
# testnet
STARK_PRIVATE_KEY_TESTNET = config("STARK_PRIVATE_KEY_TESTNET")
DYDX_API_KEY_TESTNET = config("DYDX_API_KEY_TESTNET")
DYDX_API_SECRET_TESTNET = config("DYDX_API_SECRET_TESTNET")
DYDX_API_PASSPHRASE_TESTNET = config("DYDX_API_PASSPHRASE_TESTNET")

# keys - export
STARK_PRIVATE_KEY = STARK_PRIVATE_KEY_MAINNET if MODE == "PROD" else STARK_PRIVATE_KEY_TESTNET
DYDX_API_KEY = DYDX_API_KEY_MAINNET if MODE == "PROD" else DYDX_API_KEY_TESTNET
DYDX_API_SECRET = DYDX_API_SECRET_MAINNET if MODE == "PROD" else DYDX_API_SECRET_TESTNET
DYDX_API_PASSPHRASE = DYDX_API_PASSPHRASE_MAINNET if MODE == "PROD" else DYDX_API_PASSPHRASE_TESTNET

# Host - export
HOST = API_HOST_MAINNET if MODE == "PROD" else API_HOST_GOERLI

# HTTP Provider
HTTP_PROVIDER_MAINNET = "https://eth-mainnet.g.alchemy.com/v2/V7cYEfJHdt2Pw3Tul4eQqC4itgS4WaDu"
HTTP_PROVIDER_TESTNET = "https://eth-goerli.g.alchemy.com/v2/u0QE79-iNBEa-2akMQPKqDExxiccNaTA"
HTTP_PROVIDER = HTTP_PROVIDER_MAINNET if MODE == "PROD" else HTTP_PROVIDER_TESTNET