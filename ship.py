from random import randint  #Importação de biblioteca para a geração de números pseudo-aleatórios


class Ship(object):

    def __init__(self):  # Construtor do navio
        self.ID = randint(1000, 9999)  # O navio possui um ID
        self.numberCont = randint(1, 16) # O navio possui de 1 a 16 conteiners
        self.averageWait = 0  # Tempo médio de espera do navio na fila
        self.stack1 = [] # Cada pilha tem a capacidade maxima de 4 conteiners
        self.stack2 = []
        self.stack3 = []
        self.stack4 = []

        # Distribuindo os conteiners pelas pilhas
        turn = 1
        for i in range(0, self.numberCont):
            if turn == 1:
                self.stack1.append(1)  # Número 1 representa um conteiner na pilha
                turn = 2
            elif turn == 2:
                self.stack2.append(1)
                turn = 3
            elif turn == 3:
                self.stack3.append(1)
                turn = 4
            elif turn == 4:
                self.stack4.append(1)
                turn = 1
