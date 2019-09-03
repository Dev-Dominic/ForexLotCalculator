#! /usr/bin/env python
import sys


# python <risk(%)> <account_balance(USD)> <stop_loss(pips)>
if __name__ == "__main__":
    # Getting command line arguments
    risk,account_balance,stop_loss = (int(x) for x in sys.argv[1:])

    # Calculating dollar value of risk
    risk_dollar_val = account_balance * (risk/100) 

    # Calculating lot size
    lot_size = (risk_dollar_val/stop_loss)/10

    print(f"Risk(USD): {risk_dollar_val}\nLot: {lot_size}")
    

