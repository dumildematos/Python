def Logar(nome, senha):

        if nome == 'Admin' and senha == "admin":
            print('Logou')
            return True
        else:
            print('Tente Novamente')
            return False