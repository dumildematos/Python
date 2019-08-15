from models.aluno import Aluno
from models.disciplina import Disciplina
from models.matricula import Matricula

def menuStart():
    print("Seja Bem-Vindo \n"
          "*** MENU PRINCIPAL *** \n"
          "- CADASTRO ALUNO - \n"
          "1  - Cadastro aluno \n"
          "2  - Alterar dados \n "
          "3  - Ver Alunos \n "
          "4  - Excluir Aluno \n"
          "- CADASTRO DISCIPLINAS - \n"
          "5  - Cadastrar Disciplina \n "
          "6  - Alterar Disciplina \n "
          "7 - Consultar Disciplinas\n"
          "8 - Excluir Disciplina\n"
          "-MATRICULA ALUNO - DISCIPLINA -\n "
          "9 - Matrícular aluno em uma disciplina\n "
          "- RELATÓRIOS -\n"
          "10 - Relatório de Alunos \n"
          "11 - Relatório Aniversariantes do mês \n "
          "12 - Para encerrar o programa\n")
    opt = input('Coloque a Opção: ')

    if int(opt) == 1:
        print('Cadastrar Aluno')
        cont = 'S'

        while cont is not 'N':

            matricula = input('Digite o código de Matricula: ')
            nome = input('Digite o nome do Aluno: ')
            sexo = input('Digite o sexo do Aluno: ')
            nascimento = input('Digite a data de Nascimento do Aluno: ')
            telefone = input('Digite o número de telefone do Aluno: ')
            Aluno.criar(Aluno,matricula,nome,sexo,nascimento,telefone)
            cont = input('Deseja continuar a matricular alunos? - S - SIM / N - Não: ')

        menuStart()
    if int(opt) == 2:
        print('Alterar Dados')
        matricula = input('Digite o código de Matricula: ')
        Aluno.alterar(Aluno,int(matricula))
        menuStart()

    if int(opt) == 3:
        print('Exibir Dado')
        cont = 'S'

        while cont is not 'N':
            matricula = input('Digite o código de Matricula: ')
            dado = Aluno.consulta(Aluno,int(matricula))
            print(dado)
            cont = input('Deseja continuar a exibir os dados dos alunos? - S - SIM / N - Não: ')

        menuStart()

    if int(opt) == 4:
        print('Excluir Aluno')
        cont = 'S'
        while cont is not 'N':
            matricula = input('Digite o código de Matricula: ')
            Aluno.remover(Aluno, int(matricula))
            cont = input('Deseja continuar a exibir os dados dos alunos? - S - SIM / N - Não: ')
        menuStart()

    if int(opt) == 5:
        print('Cadastrar Disciplina')
        cont = 'S'

        while cont is not 'N':
            codigo = input('Digite o código da disciplina: ')
            horario = input('Digite o horário: ')
            sala = input('Digite a o número da sala: ')
            total_vagas = input('Digite o total de vagas: ')
            Disciplina.criar(Aluno, codigo, horario, sala, total_vagas)
            cont = input('Deseja continuar a cadastrar disciplinas? - S - SIM / N - Não: ')
        menuStart()

    if int(opt) == 6:
        print('Alterar Dados')
        codigo = input('Digite o código da Disciplina: ')
        Disciplina.alterar(Disciplina,int(codigo))
        menuStart()

    if int(opt) == 7:
        print('Exibir Disciplina')
        cont = 'S'

        while cont is not 'N':
            codigo = input('Digite o código da disciplina: ')
            dado = Disciplina.consulta(Disciplina,int(codigo))
            print(dado)
            cont = input('Deseja continuar a exibir os dados dos alunos? - S - SIM / N - Não: ')
        menuStart()

    if int(opt) == 8:
        print('Excluir Disciplina')
        cont = 'S'
        while cont is not 'N':
            matricula = input('Digite o código de Matricula: ')
            Aluno.remover(Aluno, int(matricula))
            cont = input('Deseja continuar a exibir os dados dos alunos? - S - SIM / N - Não: ')
        menuStart()

    if int(opt) == 9:
        print('Matrícular aluno em uma disciplina')
        disc_codg = input('Digite o código da Disciplina que pretende Matricular o aluno: ')
        matr_aluno = input('Digite o número da Patricula do aluno: ')
        Matricula.matricular(Matricula,int(disc_codg), int(matr_aluno))