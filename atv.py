# -*- coding: utf-8 -*-
import sqlite3

#Criação de um cursor e conector para
conn = sqlite3.connect('atividade.db')
cursor = conn.cursor()

#Criação das tabelas
cursor.execute("""
CREATE TABLE IF NOT EXISTS tb_alunos (
        id_aluno INTEGER NOT NULL PRIMARY KEY,
        nome TEXT NOT NULL,
        cpf     VARCHAR(11) NOT NULL,
        rg      VARCHAR(6) NOT NULL,
        idade INTEGER);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS tb_disciplinas (
        cod   INTEGER NOT NULL PRIMARY KEY,
        disciplina  TEXT NOT NULL,
        id_aluno INTEGER NOT NULL);
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS tb_notas (
        mat_aluno   INTEGER NOT NULL,
        disciplina  TEXT NOT NULL,
        cod INTEGER NOT NULL,
        nota1 FLOAT,
        nota2 FLOAT,
        media FLOAT);
""")

#Criação das classes e métodos necessários para a execução do programa
class Pessoa:
    def __init__(self, nome, cpf, rg, idade):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self, nome, cpf, rg, idade):
        Pessoa.__init__(self, nome, cpf, rg, idade)
        self.id_aluno = id_aluno

class Disciplinas():
    def calcular_nota(self, nota1,nota2):
        self.media = (nota1 + nota2)/2
        return self.media
        
class Database():
    def inserir_dados_aluno(self, id_aluno ,nome, cpf,rg,idade):
        cursor.execute("INSERT INTO tb_alunos VALUES (?,?,?,?,?)", (id_aluno,nome, cpf, rg, idade))
        conn.commit()
    def inserir_dados_disciplina(self,cod,disciplina,id_aluno):
        cursor.execute("INSERT INTO tb_disciplinas VALUES (?,?,?)", (cod,disciplina,id_aluno))
        conn.commit()
    def inserir_notas(self, mat_aluno, disciplina, cod, nota1, nota2, media):
        cursor.execute("INSERT INTO tb_notas VALUES (?,?,?,?,?,?)", (mat_aluno, disciplina,cod,nota1,nota2,media))
        conn.commit()
    def relatorio(self, mat_aluno):
        self.query = """SELECT id_aluno,nome,disciplina,nota1,nota2,media FROM tb_alunos INNER JOIN tb_notas ON id_aluno = mat_aluno WHERE mat_aluno = ?"""
        for linha in cursor.execute(self.query,(mat_aluno,)):
            print("Matrícula: ", linha[0])
            print("Nome: ", linha[1])
            print("Disciplina: ", linha[2])
            print("Nota 1: ", linha[3])
            print("Nota 2: ", linha[4])
            print("Média: ", linha[5])
            if linha[5] > 5:
                print("Aprovado\n")
            elif linha[5] < 5:
                print("Reprovado\n")

#Execução do programa
cadastro = int(input("""***Menu***\n 
1-Cadastrar aluno\n
2-Cadastrar disciplina\n
3-Lançar nota\n
4-Exibir relatório de aluno\n
Escolha uma opção: """))

if cadastro == 1:
    try:
        mydb = Database()
        id_aluno = int(input("Digite a matrícula do aluno: "))
        nome = str(input("Digite o nome: "))
        cpf = int(input("Digite o cpf: "))
        rg = int(input("Digite o rg: "))
        idade = (input("Digite a idade: "))
        mydb.inserir_dados_aluno(id_aluno,nome,cpf,rg,idade)
        print("Dados inseridos com sucesso")
        
    except:
        print("Não foi possível realizar o cadastro")

elif cadastro == 2:
    try:
        mydb = Database()
        cod = int(input("Digite o código da disciplina: "))
        disciplina = str(input("Digite o nome da disciplina: "))
        id_aluno = int(input("Digite a matrícula do aluno: "))
        mydb.inserir_dados_disciplina(cod, disciplina,id_aluno)
        print('Dados inseridos com sucesso')
    except:
        print("Não foi possível realizar o cadastro")

elif cadastro == 3:
    try:
        mydb = Database()
        calculo = Disciplinas()
        id_aluno = str(input("Digite a matrícula do aluno: "))
        disciplina = str(input("Digite o nome da disciplina: "))
        cod = int(input("Digite o código da disciplina: "))
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))   
        media = calculo.calcular_nota(nota1, nota2)
        mydb.inserir_notas(id_aluno, disciplina, cod, nota1, nota2, media)
    except:
        print("Não foi possível realizar o cadastro")
    if media < 5:
        print("Aluno Reprovado")
    elif media >= 5:
        print("Aluno Aprovado")
elif cadastro == 4:
    try:
        mydb = Database()
        mat_aluno = (input("Digite a matrícula do aluno: "))
        mydb.relatorio(mat_aluno)
    except:
        print("Não foi possível realizar a consulta")
