from models.aluno import Aluno
from models.disciplina import Disciplina

#def matricular(codigo_disc,n_matri_aluno,data,status):

class Matricula:

    def __init__(self, codigo_disc, n_matri_aluno, data,status):
        self.codigo_disc = codigo_disc
        self.n_matri_aluno = n_matri_aluno
        self.data = data
        self.status = status

    def matricular(self,codigo_disc,n_matri_aluno):
        posD = codigo_disc - 1
        posA = n_matri_aluno - 1
        aluno = Aluno.consulta(Aluno, n_matri_aluno)
        disciplina = Disciplina.consulta(Disciplina,codigo_disc)

        atualizar_disc = []
        atualizar_aluno = []

        print(aluno[5])
        print(disciplina[4])
        if int(disciplina[3]) > 0 and int(aluno[5]) < 5:
            print('matricula pode ser feita')

            with open('database/disciplina.txt') as disciplinas:
                for i, disc in enumerate(disciplinas.readlines()):
                    if i == posD:

                        atualizar_disc.insert(3,int(disciplina[3]) - 1)
                        atualizar_disc.insert(4, int(disciplina[4]) + 1)
                        atualizar_disc.append(disc)

            with open('database/alunos.txt') as alunos:
                for j, alun in enumerate(alunos.readlines()):
                    if j == posA:
                        atualizar_aluno.insert(5, int(aluno[5]) + 1)
                        atualizar_aluno.append(alun)

            with open('database/disciplina.txt', 'a+') as discs:
                for hr in atualizar_disc:
                    discs.writelines(str(hr))

            with open('database/alunos.txt', 'a+') as aluns:
                for al in atualizar_aluno:
                    aluns.writelines(str(al))