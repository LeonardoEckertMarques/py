# https://docs.python.org
# 7.2.1. Métodos de objetos arquivo
# leitura de todo o arquivo - readlines()

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
        print("3) Criar arquivo TXT")
        print("4) Ler arquivo TXT")
        escolha = int(input("Digite a opção: "))
        self.menu(escolha)
        self.pergunta_opcao()

    def adicionar_jogador(self):
        self.limpar_tela()
        nome = input("Nome do Jogador: ")
        codigo = random.randint(1, 999)
        jogador = Jogador(codigo, nome, 0.0)
        self.jogadores.append(jogador)
        self.limpar_tela()

    def imprime_jogadores(self):
        self.limpar_tela()
        if self.jogadores:
            for jogador in self.jogadores:
                print(jogador)
        else:
            print("Nenhum jogador ativo.")

    def criar_arquivo(self):
        with open('jogadores.txt', "w") as arch:
            if not self.jogadores:
                arch.writelines("Nenhum jogador ativo. \n")
            else:
                for jogador in self.jogadores:
                    arch.writelines(str(jogador) + '\n')

    def ler_arquivo(self):
        try:
            with open('jogadores.txt', "r") as arch:
                for linha in arch:
                    print(linha, end='')
        except FileNotFoundError:
            print("Nenhum arquivo encontrado.")

    def menu(self, escolha):
        if escolha == 1:
            self.adicionar_jogador()
        elif escolha == 2:
            self.imprime_jogadores()
        elif escolha == 3:
            self.criar_arquivo()
            self.limpar_tela()
        elif escolha == 4:
            self.limpar_tela()
            self.ler_arquivo()
        else:
            quit()

    def limpar_tela(self):
        os.system('cls')

gerenciador = GerenciarJogadores()
gerenciador.pergunta_opcao()
