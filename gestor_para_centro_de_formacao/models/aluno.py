class Aluno:

    def __init__(self, n_matricula, nome, sexo, nascimento, telefone, qtd_disc, status):
        self.n_matricula = n_matricula
        self.nome = nome
        self.sexo = sexo
        self.nascimento = nascimento
        self.telefone = telefone
        self.qtd_disc = qtd_disc,
        self.status = status

    def criar(self, n_matricula, nome, sexo, nascimento, tel):

        file = open('database/alunos.txt', 'a')
        file.writelines(n_matricula + '\t' + nome + '\t' + sexo + '\t' + nascimento + '\t' + tel + '\t' + '0\t' + 'Activo' + ' \n')
        file.close()

        print('Aluno matriculado com Sucesso!')

    def consulta(self, n_matricula):
        pos = n_matricula - 1
        with open('database/alunos.txt') as alunos:
            for i , aluno in enumerate(alunos):
                if i == pos:
                    ver = aluno.split('\t')
                    return ver


    def alterar(self, n_matricula):
        pos = n_matricula - 1
        aluno = Aluno.consulta(Aluno, n_matricula)

        opt = input('Qual dado deseja Alterar ? 1 - Nome 2 - Sexo 3- Data de Nascimento 4 - Telefone: ')

        if int(opt) is 1:
            print('Alterar Nome')
            novo_nome = input('Digite o Novo Nome: ')
            trocarNome = []

            with open('database/alunos.txt') as alunos:
                for i, alun in enumerate(alunos.readlines()):
                    if i == pos:
                        nome = aluno[1]
                        trocarNome.append(alun.replace(nome, novo_nome + '(alterado)'))

            print(trocarNome)
            with open('database/alunos.txt', 'a+') as als:
                for al in trocarNome:
                    als.writelines(al)
            print(aluno)

        elif int(opt) is 2:
            print('Alterar Sexo')
            novo_sexo = input('Digite o Novo Sexo: ')
            trocarSexo = []

            with open('database/alunos.txt') as alunos:
                for i, alun in enumerate(alunos.readlines()):
                    if i == pos:
                        sexo = aluno[2]
                        trocarSexo.append(alun.replace(sexo, novo_sexo + '(alterado)'))

            with open('database/alunos.txt', 'a+') as als:
                for al in trocarSexo:
                    als.writelines(al)

        elif int(opt) is 3:
            print('Alterar Data de Nascimento')
            nova_data_nascimento = input('Digite o Novo Sexo: ')
            trocarData = []

            with open('database/alunos.txt') as alunos:
                for i, alun in enumerate(alunos.readlines()):
                    if i == pos:
                        data = aluno[3]
                        trocarData.append(alun.replace(data, nova_data_nascimento + '(alterado)'))

            with open('database/alunos.txt', 'a+') as als:
                for al in trocarData:
                    als.writelines(al)

        elif int(opt) is 4:
            print('Alterar número de Telefone')
            novo_tel = input('Digite o Novo Sexo: ')
            trocarTel = []

            with open('database/alunos.txt') as alunos:
                for i, alun in enumerate(alunos.readlines()):
                    if i == pos:
                        tel = aluno[4]
                        trocarTel.append(alun.replace(tel, novo_tel + '(alterado)'))

            with open('database/alunos.txt', 'a+') as als:
                for al in trocarTel:
                    als.writelines(al)
        else:
            print('Opção Inválida')

    def remover(self, n_matricula):
        pos = n_matricula - 1
        aluno = Aluno.consulta(Aluno, n_matricula)

        print('Excluir Aluno')
        #novo_nome = input('Digite o Novo Nome: ')
        trocarEstado = []

        with open('database/alunos.txt') as alunos:
            for i, alun in enumerate(alunos.readlines()):
                if i == pos:
                    if int(aluno[5]) == 0:
                        estado = aluno[6]
                        trocarEstado.append(alun.replace(estado, 'Excluido' + ' - (alterado)'))

        with open('database/alunos.txt', 'a+') as als:
            for al in trocarEstado:
                als.writelines(al)
        print(aluno)