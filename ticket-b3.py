from pandas_datareader import data
import pandas as pd
from IPython.display import display
from datetime import date



ticket_b3 = ['BIDI4.SA','ITSA4.SA', 'ALPK3.SA', 'FLRY3.SA', 'OIBR3.SA']

for ticket in ticket_b3:
    print(ticket)
    cotacao_bovespa = data.DataReader(ticket, data_source='yahoo', start=date.today(), end=date.today())
    display(cotacao_bovespa)
    print("\n")
