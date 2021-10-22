import requests
import json
from tkinter import *

def obter_cotacoes():
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

    cotacao_dolar = currencie_data['USDBRL']['bid']
    cotacao_euro = currencie_data['EURBRL']['bid']
    cotacao_gbp = currencie_data['GBPBRL']['bid']
    cotacao_btc = currencie_data['BTCBRL']['bid']

    text_currencie = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    Libre Esterlina: {cotacao_gbp}
    Bitcoin: {cotacao_btc}\n
    Obrigado por utilizar nosso serviço!\n'''

    text_currencie_gui["text"] = text_currencie

### INTERFACE GRÁFICA ###

root = Tk()
root.title("Cotação de Moedas")
root.geometry("300x210")
root.resizable(False,False)
root.iconbitmap("img/favicon.ico")

text_guide = Label(root,text="\nClique no botão para obter a cotação atual das moedas\n").grid(column=0, row=0)
btn = Button(root, text="Obter", command=obter_cotacoes).grid(column=0, row=1)
text_currencie_gui = Label(root, text="Wait...",foreground="red")
text_currencie_gui.grid(column=0,row=2)



root.mainloop()
