from func_connections import connect_dydx
from func_private import abort_all_positions
from constants import ABORT_ALL_POSITIONS

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

