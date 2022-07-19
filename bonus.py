import pandas as pd
from twilio.rest import Client

#Your Account SID from twilio.com/console
account_sid ="AC759ef3511a2adbd8578dd35fe1ec2d3e"
# Your Auth Token from twilio.com/console
auth_token  = "d29f76ca4d31a9cd2c1c88dbb3dc63e8"
client = Client(account_sid, auth_token)

lista_meses = ['janeiro','fevereiro','março','abril','maio','junho']

for mes in lista_meses:
    tabela_vendas =  pd.read_excel(f'{mes}.xlsx')
    if( tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendedor'].values[0]
        venda = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendas'].values[0]
        print(f'No mes {mes} alguem bateu a meta. Vendedor: {vendedor} , Vendas: {venda}')
        message = client.messages.create(
            to="+5511957243743",
            from_="+17262244594",
            body=f'Olá Gestor no mes {mes} alguem da sua equipe bateu a meta! Vendedor: {vendedor} , vendeu R$: {venda}')
        print(message.sid)

#Para cada arquivo, verificar se algum valor( coluna vendas) é maior 55 mil
# Se for maior de 55 mil--> a gente envia sms com o nome o mes e as vendas do vendedor






