import PySimpleGUI as sg
from cotacao_lira import pegar_cotacoes
from temp import notifica_email
from datetime import datetime



sg.change_look_and_feel('DarkGray2')
layout = [
    [sg.Text('Nome', size=(5,0)),sg.Input(size=(25,0),key='nometela')],
    [sg.Text('E-mail',size=(5,0)),sg.Input(size=(40,0),key='emailtela')],
    [sg.Text('Escolha a moeda que deseja obter a cotação atual')],
    #[sg.Checkbox('Dolar',key='USD', default=False),sg.Checkbox('Euro',key='EUR'),sg.Checkbox('Bitcoin',key='BTC')],
    [sg.Combo(['USD', 'EUR', 'BTC'], key='moeda', size=(6, 3))],
    #[sg.Text('Enviar e-mail?')],
    #[sg.Radio('Sim','envia_email',key='envia_sim'),sg.Radio('Não','envia_email_nao',key='envia_nao')],
    [sg.Button('Cotação'),sg.Button('Enviar e-mail'),sg.CloseButton('Cancelar')],
    [sg.Text("",key="texto_cotacao")],
    [sg.Text("",key="texto_email")],
    #[sg.Output(size=(50,5))]
    
        ]

janela = sg.Window("Sistema de Cotações", layout)

while True:

    #fecha janela
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == "Cancelar":
        break
    #recupera cotação
    if evento == "Cotação":
        data_now= datetime.now()
        data_format =  data_now.strftime("%d/%m/%Y %H:%M")  
        codigo_cotacao = valores["moeda"]
        cotacao = pegar_cotacoes(codigo_cotacao)
        nome = valores["nometela"]
        janela["texto_cotacao"].update(f"Olá {nome}, a cotação do {codigo_cotacao} é de R${cotacao} em {data_format}")
        
    #envia email
    if evento == "Enviar e-mail":
        data_now= datetime.now()
        data_format =  data_now.strftime("%d/%m/%Y %H:%M")  
        codigo_cotacao = valores["moeda"]
        cotacao = pegar_cotacoes(codigo_cotacao)
        nome = valores["nometela"]
        janela["texto_cotacao"].update(f"Olá {nome}, a cotação do {codigo_cotacao} é de R${cotacao} em {data_format}")
        email = valores["emailtela"]
        envia_email = notifica_email(codigo_cotacao, nome, email)


        janela["texto_email"].update(f"Email enviado com sucesso para {email}")

    

       
janela.close() 