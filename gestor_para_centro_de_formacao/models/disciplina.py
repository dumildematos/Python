class Disciplina:

    def __init__(self, codigo, horario, sala, total_vagas, vagas_ocupadas,status):
        self.codigo = codigo
        self.horario = horario
        self.sala = sala
        self.total_vagas = total_vagas
        self.vagas_ocupadas = vagas_ocupadas
        self.status = status

    def criar(self, codigo, horario, sala, total_vagas):

        file = open('database/disciplina.txt', 'a')
        file.writelines(codigo + '\t' + horario + '\t' + sala + '\t' + total_vagas + '\t' + '0' + '\t' +  'Activo' + ' \n')
        file.close()

        print('Disciplina criada com Sucesso!')

    def consulta(self, codigo):
        pos = codigo - 1
        with open('database/disciplina.txt') as discs:
            for i , disc in enumerate(discs):
                if i == pos:
                    ver = disc.split('\t')
                    return ver

    def alterar(self, codigo):
        pos = codigo - 1
        disciplina = Disciplina.consulta(Disciplina, codigo)

        opt = input('Qual dado deseja Alterar ? 1 - Horário 2 - Sala 3- Quantidade Total de Vagas: ')

        if int(opt) is 1:
            print('Alterar Horário')
            novo_horario = input('Digite o Novo Horário: ')
            trocarHorario = []

            with open('database/disciplinas.txt') as alunos:
                for i, alun in enumerate(alunos.readlines()):
                    if i == pos:
                        horario = disciplina[1]
                        trocarHorario.append(alun.replace(horario, novo_horario + '(alterado)'))

            print(trocarHorario)
            with open('database/disciplina.txt', 'a+') as discs:
                for hr in trocarHorario:
                    discs.writelines(hr)
            print(trocarHorario)

        elif int(opt) is 2:
            print('Alterar Sala')
            nova_sala = input('Digite o número da Nova Sala: ')
            trocar_sala = []

            with open('database/disciplina.txt', 'a+') as discs:
                for i, disc in enumerate(discs.readlines()):
                    if i == pos:
                        sala = disciplina[2]
                        trocar_sala.append(disc.replace(sala, nova_sala + '(alterado)'))

            with open('database/disciplina.txt', 'a+') as discs:
                for disc in trocar_sala:
                    discs.writelines(disc)

        elif int(opt) is 3:
            print('Alterar quantidade total de vagas')
            nova_qtd_total_vagas = input('Digite o Novo Sexo: ')
            trocar_quantidade = []

            with open('database/disciplina.txt', 'a+') as discs:
                for i, disc in enumerate(discs.readlines()):
                    if i == pos:
                        quantidade_total = disciplina[3]
                        trocar_quantidade.append(disc.replace(quantidade_total, nova_qtd_total_vagas + '(alterado)'))

            with open('database/disciplina.txt', 'a+') as discs:
                for disc in trocar_quantidade:
                    discs.writelines(disc)
        else:
            print('Opção Inválida')

    def remover(self, codigo):
        pos = codigo - 1
        disciplina = Disciplina.consulta(Disciplina, codigo)

        print('Excluir Disciplina')
        trocarEstado = []

        with open('database/disciplina.txt') as discs:
            for i, disc in enumerate(discs.readlines()):
                if i == pos:
                    if int(disciplina[4]) == 0:
                        estado = disciplina[5]
                        trocarEstado.append(disc.replace(estado, 'Excluido' + ' - (alterado)'))

        with open('database/disciplina.txt') as discs:
            for disc in discs:
                discs.writelines(disc)
        print(disciplina)
