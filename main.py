import requests
import smtplib
import email.message


# pegar a informação que você quer
requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
requisicao_dicionario = requisicao.json()
cotacao = float(requisicao_dicionario['USDBRL']['bid'])
print(cotacao)

# enviar aviso - email

def enviar_email(cotacao):
    corpo_email = f"""
 <p>Dolar está abaixo de R$4.90. Cotação atual: R${cotacao}</p>
   
    """

    msg = email.message.Message()
    msg['Subject'] = "O dolar está abaixo de R$4.90"
    msg['From'] = 'underclany@gmail.com'
    msg['To'] = 'ddg.775@icloud.com'
    password = 'hfujhyiaucrfxgyl'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

if cotacao < 4.90:
    enviar_email(cotacao)



# doploy - heroku