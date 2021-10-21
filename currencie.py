import requests
import json


id_currencie = ['GBPBRL', 'NOKBRL', 'BTCBRL', 'NZDBRL',
                'CHFBRL', 'ETHBRL', 'DKKBRL', 'COPBRL',
                'RUBBRL', 'CNYBRL', 'INRBRL', 'MXNBRL', 
                'PLNBRL', 'EURBRL', 'SARBRL', 'TRYBRL',
                'PYGBRL', 'AEDBRL', 'HKDBRL', 'XRPBRL',
                'USDBRL', 'CADBRL', 'JPYBRL', 'ILSBRL',
                'SGDBRL', 'SEKBRL', 'THBBRL', 'PENBRL',
                'DOGEBRL', 'TWDBRL', 'LTCBRL', 'AUDBRL', 
                'CLPBRL', 'BOBBRL', 'ARSBRL', 'UYUBRL']

currencie = requests.get("http://economia.awesomeapi.com.br/json/last/GBP-BRL,NOK-BRL,BTC-BRL,NZD-BRL,CHF-BRL,ETH-BRL,DKK-BRL,COP-BRL,RUB-BRL,CNY-BRL,INR-BRL,MXN-BRL,PLN-BRL,EUR-BRL,SAR-BRL,TRY-BRL,PYG-BRL,AED-BRL,HKD-BRL,XRP-BRL,USD-BRL,CAD-BRL,JPY-BRL,ILS-BRL,SGD-BRL,SEK-BRL,THB-BRL,PEN-BRL,DOGE-BRL,TWD-BRL,LTC-BRL,AUD-BRL,CLP-BRL,BOB-BRL,ARS-BRL,UYU-BRL")
currencie_data = currencie.json()

for id in id_currencie:
    print(currencie_data[id], "\n")
