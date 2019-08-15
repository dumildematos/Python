Universidade Federal Rural de Pernambuco
Departamento de Estatística e Informática
Introdução a Programação
Prazo Final: 27/06/2019
Considerações Iniciais:
1. O trabalho deve ser realizado em equipe de 3 (três) alunos;
2. Um aluno da equipe deve assumir a Coordenação do Projeto, e isto deve ser indicado
nos comentários iniciais do programa;
3. Cada aluno da equipe deve fazer, no mínimo, um dos 4 (quatro) primeiros módulos do
projeto (“a” ao “d”), e no início de cada módulo deve haver um comentário indicando
o responsável pela sua autoria;
4. No módulo de Relatórios (d) deve ser utilizado, no mínimo, 2(dois) dos métodos de
ordenação apresentados em sala de aula;
5. Até o prazo final de entrega, deve-se anexar o código do projeto no AVA;
6. O trabalho valerá 5,0 (cinco) pontos para a 2VA.
Descrição do Projeto:
Considere um curso onde os alunos se matriculam em disciplina, desenvolva um projeto com
as seguintes características:
OBS: TUDO DEVE ENVOLVER MANIPULAÇÃO DE ARQUIVOS
(a) Módulo de Alunos
1) Cadastramento:
O cadastro de alunos deve conter os seguintes dados: matrícula, nome, sexo, data
de nascimento (formato: aaaammdd), telefone, quantidade de disciplinas em que
o aluno está matriculado (no cadastramento de novo aluno este valor é zero) e
status (ativo, excluído).
OBS: A matricula do aluno é a chave primária, portanto não podem existir dois
alunos com a mesma matrícula.
2) Alteração:
Alterar os dados de um aluno: nome, sexo, data de nascimento e telefone.OBS: Não podem ser alterados: matricula por ser chave primária; quantidade de
disciplinas por estar relacionado com o módulo de matricula; e status por ser um
atributo alterado apenas durante o cadastramento/remoção;
3) Exibição:
Exibir os dados de um aluno: matricula, nome, sexo, data de nascimento, telefone,
quantidade de disciplinas em que o aluno está matriculado
4) Remoção:
Remover um aluno do cadastro, alterando o status do registro do aluno para
excluído.
OBS: a remoção lógica de um aluno, só pode ser efetivada se o aluno não estiver
matriculado em disciplinas.
5) Consulta:
Função consultar aluno que recebe como entrada a matrícula do aluno e retorna
como saída a posição do arquivo onde o registro do aluno se encontra.
OBS: Essa função deve ser utilizada pelos procedimentos de cadastro, alteração,
exibição e remoção.
(b) Módulo de Disciplinas
1) Cadastramento:
Cadastrar uma nova disciplina. O cadastro de disciplina deve conter os seguintes
dados: código da disciplina, horário, sala onde as aulas ocorrerão, quantidade total
de vagas, quantidade de vagas ocupadas e status do registro (ativo, excluído).
OBS: Não podem existir duas disciplinas com o mesmo código.
2) Alteração:
Alterar dados (horário da disciplina, sala onde as aulas ocorrerão, quantidade total
de vagas) de uma turma.
3) Exibição:
Exibir os dados (código da disciplina, horário, sala onde as aulas ocorrerão,
quantidade de vagas disponíveis) de uma disciplina.
4) Remoção:
Remover uma disciplina do cadastro. Altera o status do registro da disciplina para
excluído. OBS: Para que uma disciplina possa ser removida, é necessário que não
existam alunos matriculados.
5) Consulta:
Função consultar disciplina que recebe como entrada o código da disciplina e
retorna como saída a posição onde o registro se encontra.
OBS: Deverá ser utilizada pelos procedimentos de cadastramento, alteração e
remoção.(c) Módulo de Matrícula:
1) Inclusão de matrícula:
Matricular um aluno em uma disciplina. O cadastro de matrículas deve conter os
seguintes dados: código da disciplina, matrícula do aluno, data da matrícula
(formato: aaaammdd) e status do registro (ativo, excluído).
OBS: Para realizar uma matricula é necessário verificar: se existem vagas na
disciplina solicitada, se o aluno não já está matriculado naquela disciplina ou se o
aluno não atingiu sua cota máxima de disciplinas cursadas por período que é de
5(cinco) disciplinas. Ao realizar a matricula, é necessário atualizar os registros do
aluno e da disciplina envolvidos no processo.
2) Exclusão de matrícula:
Retira um aluno de uma determinada disciplina, alterando o status do registro de
matrícula para excluído. Para excluir um aluno de uma disciplina é necessário que
a matrícula tenha sido realizada há, no máximo, 15 dias. Caso contrário, a exclusão
não será permitida. Ao realizar a exclusão, é necessário atualizar os registros do
aluno e da disciplina envolvidos no processo
3) Trancamento de matrícula:
Tranca a matrícula de um aluno, alterando o status do registro de matrícula para
trancado. Para trancar um aluno, é necessário que a matricula tenha sido feita há
no máximo 30 dias. Caso contrário, o trancamento não será permitido.
OBS: ajustar a quantidade em disciplina.
(d) Módulo de Relatórios:
1) Relatório dos Alunos:
Nesse relatório deve ser emitido todos os alunos ordenados por matrícula.
2) Relatório de Aniversariantes do Mês:
Nesse relatório deve ser emitido os aniversariantes de um determinado mês
ordenado por dia de aniversário.
3) Relatório da Disciplina:
Nesse relatório deve ser emitido os alunos matriculados em uma determinada
disciplina ordenados por matrícula.
(e) Módulo de Manutenção:
1) O programa deverá ter um procedimento para limpeza de cada um dos cadastros:
alunos, turmas e matrícula; removendo fisicamente os registros que foram
excluídos logicamente.