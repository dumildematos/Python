from models.autenticacao import Logar
from models.menu import menuStart

user = input('Digite o nome de usuário: ')
senha = input('Digite a sua Senha: ')

if Logar(user,senha):
    menuStart()

