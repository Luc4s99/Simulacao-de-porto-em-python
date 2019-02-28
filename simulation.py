from ship import Ship  # Importando a classe do navio
from random import randint  #Importação de biblioteca para a geração de números pseudo-aleatórios
from time import sleep


def unload_ship(queue):
    removed_cont = 0

    if queue[0].numberCont > 4:
        while removed_cont != 4 and queue[0].numberCont != 0:
            if len(queue[0].stack1) != 0 or removed_cont != 4:
                queue[0].stack1.pop()
                removed_cont += 1
                queue[0].numberCont -= 1
            if len(queue[0].stack2) != 0 or removed_cont != 4:
                queue[0].stack2.pop()
                removed_cont += 1
                queue[0].numberCont -= 1
            if len(queue[0].stack3) != 0 or removed_cont != 4:
                queue[0].stack3.pop()
                removed_cont += 1
                queue[0].numberCont -= 1
            if len(queue[0].stack4) != 0 or removed_cont != 4:
                queue[0].stack4.pop()
                removed_cont += 1
                queue[0].numberCont -= 1

    else:  # Se o numero de conteiners for igual ou menor que 4, pode-se retirar todos os conteiners e retirar o
        # navio da fila
        removed_cont = queue[0].numberCont
        queue[0].stack1.clear()
        queue[0].stack2.clear()
        queue[0].stack3.clear()
        queue[0].stack4.clear()
        queue[0].numberCont = 0  # Retira todos

    return removed_cont


def calculate_avg_time(queue):
    average_time = 0

    if len(queue) == 0:
        return 0
    else:
        for ship in queue:
            average_time += ship.averageWait

        average_time /= len(queue)

        return average_time


def simulation_port():
    """
    Executa a simulação de um porto
    :return: Não possui retorno
    """
    # Criação das filas onde os navios ficarão
    queue1 = []
    queue2 = []
    queue3 = []
    queue4 = []

    numberOfShips = 0
    timeUnits = 0

    turn = 1
    while True:
        numberOfShips = randint(0, 3)
        print(f'Número de navios que chegaram ao porto: {numberOfShips}\n', '-' * 30)
        sleep(1)
        for i in range(0, numberOfShips):  # Distribuindo os navios pelas filas
            if turn == 1:
                queue1.append(Ship())
                print(f'\nFila 1 recebe o navio {queue1[len(queue1) - 1].ID} com {queue1[len(queue1) - 1].numberCont} conteiners')
                sleep(1)
                turn = 2
            elif turn == 2:
                queue2.append(Ship())
                print(f'Fila 2 recebe o navio {queue2[len(queue2) - 1].ID} com {queue2[len(queue2) - 1].numberCont} conteiners')
                sleep(1)
                turn = 3
            elif turn == 3:
                queue3.append(Ship())
                print(f'Fila 3 recebe o navio {queue3[len(queue3) - 1].ID} com {queue3[len(queue3) - 1].numberCont} conteiners')
                sleep(1)
                turn = 4
            else:
                queue4.append(Ship())
                print(f'Fila 4 recebe o navio {queue4[len(queue4) - 1].ID} com {queue4[len(queue4) - 1].numberCont} conteiners')
                sleep(1)
                turn = 1

        if len(queue1) != 0:
            print('-' * 30, f'\nNúmero de conteiners retirados na fila 1: {unload_ship(queue1)}')
            sleep(1)
        if len(queue2) != 0:
            print(f'Número de conteiners retirados na fila 2: {unload_ship(queue2)}')
            sleep(1)
        if len(queue3) != 0:
            print(f'Número de conteiners retirados na fila 3: {unload_ship(queue3)}')
            sleep(1)
        if len(queue4) != 0:
            print(f'Número de conteiners retirados na fila 4: {unload_ship(queue4)}\n', '-' * 30)
            sleep(1)

        # Verificação se o navio já foi descarregado
        if len(queue1) != 0:
            if queue1[0].numberCont == 0:
                print(f'\nNavio {queue1[0].ID} totalmente descarregado, deixando a fila 1...')
                del queue1[0]
        if len(queue2) != 0:
            if queue2[0].numberCont == 0:
                print(f'\nNavio {queue2[0].ID} totalmente descarregado, deixando a fila 2...')
                del queue2[0]
        if len(queue3) != 0:
            if queue3[0].numberCont == 0:
                print(f'\nNavio {queue3[0].ID} totalmente descarregado, deixando a fila 3...')
                del queue3[0]
        if len(queue4) != 0:
            if queue4[0].numberCont == 0:
                print(f'\nNavio {queue4[0].ID} totalmente descarregado, deixando a fila 4...')
                del queue4[0]

        sleep(2)
        print('-' * 30, f'\nNúmero de navios na fila de atracamento 1: {len(queue1)}', '\nFila: ')
        for element in queue1:
            element.averageWait += 1  # Somando o tempo de espera total do navio
            print(f'{element.ID} -> ', end='')
        print(f'\nTempo médio de espera na fila 1: {calculate_avg_time(queue1):.2f} unidades de tempo')
        print('\n')
        sleep(1)

        print(f'\nNúmero de navios na fila de atracamento 2: {len(queue2)}', '\nFila: ')
        for element in queue2:
            element.averageWait += 1
            print(f'{element.ID} -> ', end='')
        print(f'\nTempo médio de espera na fila 2: {calculate_avg_time(queue2):.2f} unidades de tempo')
        print('\n')
        sleep(1)

        print(f'\nNúmero de navios na fila de atracamento 3: {len(queue3)}', '\nFila: ')
        for element in queue3:
            element.averageWait += 1
            print(f'{element.ID} -> ', end='')
        print(f'\nTempo médio de espera na fila 3: {calculate_avg_time(queue3):.2f} unidades de tempo ')
        print('\n')
        sleep(1)

        print(f'\nNúmero de navios na fila de atracamento 4: {len(queue4)}', '\nFila: ')
        for element in queue4:
            element.averageWait += 1
            print(f'{element.ID} -> ', end='')
        print(f'\nTempo médio de espera na fila 4: {calculate_avg_time(queue4):.2f} unidades de tempo')
        print('\n')

        timeUnits += 1
        print('-' * 30, '\n', f'Unidades de tempo decorridas: {timeUnits}')
        # sleep(5)
        input('\n\nPressione <Enter> para continuar a simulação\n\n')
