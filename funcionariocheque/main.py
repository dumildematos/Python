def calSalarioLiquido():
    contracheque = []
    imponstoINSS = 0
    with open('funcionario.txt') as funcionario:
        for i, funcionario in enumerate(funcionario):

            ver = funcionario.split(' ')

            if float(ver[2]) <= float(1903.98):
                impostoRenda = 0  #print(ver[0] + ' - Inposto de renda é nula' )
            elif float(ver[2]) <= float(1903.99) or float(ver[2]) <= float(2826.65):
                impostoRenda = 142.80  #print(ver[0] + ' - Inposto de renda é de: ', 142.80)
            elif float(ver[2]) <= float(2826.66) or float(ver[2]) <= float(3751.05):
                impostoRenda = 354.80  #print(ver[0] + ' - Inposto de renda é de: ', 354.80)
            elif float(ver[2]) <= float(3751.06) or float(ver[2]) <= float(4664.68):
                impostoRenda = 636.13 #print(ver[0] + ' - Inposto de renda é de: ', 636.13)
            elif float(ver[2]) >= float(4664.68):
                impostoRenda = 869.36  #print(ver[0] + ' - Inposto de renda é de: ', 869.36)
            if float(ver[2]) <= float(1399.12):
                imponstoINSS = float(ver[2]) % 8   #print(ver[0] + ' - Inposto de INSS é de: -8%')
            elif float(ver[2]) <= float(1399.13) or float(ver[2]) <= float(2331.88):
                imponstoINSS = float(ver[2]) % 8   #print(ver[0] + ' - Inposto de INSS é de: -9%')
            elif float(ver[2]) <= float(2331.89) or float(ver[2]) < float(4663.75):
                imponstoINSS = float(ver[2]) % 11   #print(ver[0] + ' - Inposto de INSS é de: - 11%')
            elif float(ver[2]) < float(4663.76):
                imponstoINSS = float(ver[2]) % 12  # print(ver[0] + ' - Inposto de INSS é de: - 12%')

            salLiquid = float(ver[2]) - float(impostoRenda) - imponstoINSS
            contracheque.append(ver[0] + ' - Salário Liquido de : ' + str(salLiquid) + 'R$ \n')
        return contracheque
calSalarioLiquido()

def contraCheque(data):
    file = open('contracheque.txt', 'a', encoding="utf-8")
    file.writelines(data)
    file.close()

contraCheque(calSalarioLiquido())