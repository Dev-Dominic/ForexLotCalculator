# Forex Lot Calculator

Forex Lot Calculator uses risk(%), account balance and stop loss

## How to Use

```bash
$ ./fxLotCal.py <risk(%)> <account_balance> <stop_loss(pips)>
$ ./fxLotCal.py 3 100 30 
```

### Output

```bash
$ Risk (USD): 3
$ Lot: 0.01
```

## Issues 

Only major issue is the fact that this calculator only takes into account USD pairs, as such LOT sizes don't reflect non-USD pairs
