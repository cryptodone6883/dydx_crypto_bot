from func_connections import connect_dydx
from func_private import abort_all_positions
from constants import ABORT_ALL_POSITIONS, FIND_COINTEGRATED, PLACE_TRADES
from func_public import construct_market_prices, get_candles_historical
from func_cointegration import store_cointegration_results
from func_entry_pairs import open_positions

if __name__ == "__main__":
    
    # connect to client
    try:
        print("Connecting to Client...")
        client = connect_dydx()
    except Exception as e:
        #print(e)
        print("Error connecting to client: ", e)
        exit(1)

    # Abort all open positions
    if ABORT_ALL_POSITIONS:
        try:
            print("Closing all postions...")
            close_orders = abort_all_positions(client)
        except Exception as e:
            print("Error closing all positions: ", e)
            exit(1)


    # Find cointegrated pairs
    if FIND_COINTEGRATED:

        # construct market price
        try:
            print("Fetching market prices, please allow 3 mins ...")
            df_market_prices = construct_market_prices(client)
        except Exception as e:
            print("Error closing all positions: ", e)
            exit(1)

        # store cointegrated pairs
        try:
            print("store cointegrated pairs ...")
            store_result = store_cointegration_results(df_market_prices)
            if store_result != "saved":
                print("Error saving cointegrated pairs")
                exit(1)
        except Exception as e:
            print("Error saving cointegrated pairs", e)
            exit(1)




    # Place trades for opening positions
    if PLACE_TRADES:
        try:
            print("Finding trading opportunity ...")
            open_positions(client)
        except Exception as e:
            print("Error trading pairs", e)
            exit(1)
