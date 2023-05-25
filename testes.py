import os
import random

class Jogador:
    def __init__(self, codigo, nome, score):
        self.codigo = codigo
        self.nome = nome
        self.score = score

    def __str__(self):
        return f"[{self.codigo} | {self.nome} | {self.score}]"

class GerenciarJogadores:
    def __init__(self):
        self.jogadores = []

    def pergunta_opcao(self):
        print("1) Adicionar novo Jogador")
        print("2) Ver Jogadores Ativos")
        print("3) Limpar tela")
        print("4) Criar arquivo TXT")
        escolha = int(input("Digite a opção: "))
        self.menu(escolha)
        self.pergunta_opcao()

    def adicionar_jogador(self):
        nome = input("Nome do Jogador: ")
        codigo = random.randint(1, 999)
        jogador = Jogador(codigo, nome, 0.0)
        self.jogadores.append(jogador)
        self.limpar_tela()

    def limpar_tela(self):
        os.system('cls')

    def imprime_jogadores(self):
        if self.jogadores:
            for jogador in self.jogadores:
                print(jogador)
        else:
            print("\nNenhum jogador ativo.")

    def criar_arquivo(self):
        with open('jogadores.txt', "w") as arch:
            for jogador in self.jogadores:
                arch.writelines({str(jogador)})

    def menu(self, escolha):
        if escolha == 1:
            self.adicionar_jogador()
        elif escolha == 2:
            self.imprime_jogadores()
        elif escolha == 3:
            self.limpar_tela()
        elif escolha == 4:
            self.criar_arquivo()
        else:
            quit()

gerenciador = GerenciarJogadores()
gerenciador.pergunta_opcao()
