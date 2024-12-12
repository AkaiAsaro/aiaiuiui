import re

def telesantana(telefone):
    padrao = re.compile(r'^\d{2}\d{8,9}$')
    return padrao.match(str(telefone))

def validaemail(email):
    padrao_email = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    return padrao_email.match(str(email))

def login():
    nome = input("digite seu nome: ")
    telefone = int(input("telefone pra contato: "))
    email = input("digite seu E-mail: ")

    dados = {
    "nome": nome,
    "telefone": telefone,
    "email": email,
    }
    if not telesantana(telefone):
        print("necessário 'DDD' e 9 no começo ")
        return
    if not validaemail(email):
        print("email precisa de '@' e .com' no final")
        return 
    return dados



print(login())

