from ship import Ship  # Importando a classe do navio
from random import randint  # Importação de biblioteca para a geração de números pseudo-aleatórios
from time import sleep
from docking import DockingArea  # Classe da area de atracamento


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


def crossbeam_load(area, number):
    turn = 1

    for i in range(0, number):
        if turn == 1:
            if len(area.crossbeam1) == 5:
                print('\n\tTravessa 1 descarregada pelo veículo de retirada\n')
                area.crossbeam1.clear()
            area.crossbeam1.append(1)
            turn = 2
        elif turn == 2:
            if len(area.crossbeam2) == 5:
                print('\n\tTravessa 2 descarregada pelo veículo de retirada\n')
                area.crossbeam2.clear()
            area.crossbeam2.append(1)
            turn = 3
        elif turn == 3:
            if len(area.crossbeam3) == 5:
                print('\n\tTravessa 3 descarregada pelo veículo de retirada\n')
                area.crossbeam3.clear()
            area.crossbeam3.append(1)
            turn = 4
        elif turn == 4:
            if len(area.crossbeam4) == 5:
                print('\n\tTravessa 4 descarregada pelo veículo de retirada\n')
                area.crossbeam4.clear()
            area.crossbeam4.append(1)
            turn = 5
        else:
            if len(area.crossbeam5) == 5:
                print('\n\tTravessa 5 descarregada pelo veículo de retirada\n')
                area.crossbeam5.clear()
            area.crossbeam5.append(1)
            turn = 1
    print(f'\tConteiners na travessa 1: {len(area.crossbeam1)}\n')
    print(f'\tConteiners na travessa 2: {len(area.crossbeam2)}\n')
    print(f'\tConteiners na travessa 3: {len(area.crossbeam3)}\n')
    print(f'\tConteiners na travessa 4: {len(area.crossbeam4)}\n')
    print(f'\tConteiners na travessa 5: {len(area.crossbeam5)}\n')
    sleep(2)


def simulation_port():
    """
    Executa a simulação de um porto
    :return: Não possui retorno
    """
    # Criação das areas de atracamento para onde os navios serão direcionados
    area1 = DockingArea()
    area2 = DockingArea()
    area3 = DockingArea()
    area4 = DockingArea()

    timeUnits = 0

    print('*-' * 5, '\tSIMULAÇÃO DE PORTOS', '*-' * 5)
    print('\n\n')
    turn = 1
    while True:
        numberOfShips = randint(0, 3)
        print(f'Número de navios que chegaram ao porto: {numberOfShips}\n', '-' * 30)
        sleep(1)
        for i in range(0, numberOfShips):  # Distribuindo os navios pelas filas
            if turn == 1:
                area1.queue.append(Ship())
                print(f'\nFila 1 recebe o navio {area1.queue[len(area1.queue) - 1].ID} com {area1.queue[len(area1.queue) - 1].numberCont} conteiners')
                sleep(1)
                turn = 2
            elif turn == 2:
                area2.queue.append(Ship())
                print(f'Fila 2 recebe o navio {area2.queue[len(area2.queue) - 1].ID} com {area2.queue[len(area2.queue) - 1].numberCont} conteiners')
                sleep(1)
                turn = 3
            elif turn == 3:
                area3.queue.append(Ship())
                print(f'Fila 3 recebe o navio {area3.queue[len(area3.queue) - 1].ID} com {area3.queue[len(area3.queue) - 1].numberCont} conteiners')
                sleep(1)
                turn = 4
            else:
                area4.queue.append(Ship())
                print(f'Fila 4 recebe o navio {area4.queue[len(area4.queue) - 1].ID} com {area4.queue[len(area4.queue) - 1].numberCont} conteiners')
                sleep(1)
                turn = 1

        if len(area1.queue) != 0:
            cont_number = unload_ship(area1.queue)
            print('-' * 30, f'\nNúmero de conteiners retirados na fila 1 e colocados nas travessas: {cont_number}')
            crossbeam_load(area1, cont_number)
            sleep(1)
        if len(area2.queue) != 0:
            cont_number = unload_ship(area2.queue)
            print(f'Número de conteiners retirados na fila 2 e colocados nas travessas: {cont_number}')
            crossbeam_load(area2, cont_number)
            sleep(1)
        if len(area3.queue) != 0:
            cont_number = unload_ship(area3.queue)
            print(f'Número de conteiners retirados na fila 3 e colocados nas travessas: {cont_number}')
            crossbeam_load(area3, cont_number)
            sleep(1)
        if len(area4.queue) != 0:
            cont_number = unload_ship(area4.queue)
            print(f'Número de conteiners retirados na fila 4 e colocados nas travessas: {cont_number}\n', '-' * 30)
            crossbeam_load(area4, cont_number)
            sleep(1)

        # Verificação se o navio já foi descarregado
        if len(area1.queue) != 0:
            if area1.queue[0].numberCont == 0:
                print(f'\nNavio {area1.queue[0].ID} totalmente descarregado, deixando a fila 1...')
                del area1.queue[0]
        if len(area2.queue) != 0:
            if area2.queue[0].numberCont == 0:
                print(f'\nNavio {area2.queue[0].ID} totalmente descarregado, deixando a fila 2...')
                del area2.queue[0]
        if len(area3.queue) != 0:
            if area3.queue[0].numberCont == 0:
                print(f'\nNavio {area3.queue[0].ID} totalmente descarregado, deixando a fila 3...')
                del area3.queue[0]
        if len(area4.queue) != 0:
            if area4.queue[0].numberCont == 0:
                print(f'\nNavio {area4.queue[0].ID} totalmente descarregado, deixando a fila 4...')
                del area4.queue[0]

        sleep(2)
        print('-' * 30, f'\nNúmero de navios na fila de atracamento 1: {len(area1.queue)}', '\nFila: ')
        for element in area1.queue:
            element.averageWait += 1  # Somando o tempo de espera total do navio
            print(f'{element.ID} -> ', end='')
        print(f'\nTempo médio de espera na fila 1: {calculate_avg_time(area1.queue):.2f} unidades de tempo')
        print('\n')
        sleep(1)

        print(f'\nNúmero de navios na fila de atracamento 2: {len(area2.queue)}', '\nFila: ')
        for element in area2.queue:
            element.averageWait += 1
            print(f'{element.ID} -> ', end='')
        print(f'\nTempo médio de espera na fila 2: {calculate_avg_time(area2.queue):.2f} unidades de tempo')
        print('\n')
        sleep(1)

        print(f'\nNúmero de navios na fila de atracamento 3: {len(area3.queue)}', '\nFila: ')
        for element in area3.queue:
            element.averageWait += 1
            print(f'{element.ID} -> ', end='')
        print(f'\nTempo médio de espera na fila 3: {calculate_avg_time(area3.queue):.2f} unidades de tempo ')
        print('\n')
        sleep(1)

        print(f'\nNúmero de navios na fila de atracamento 4: {len(area4.queue)}', '\nFila: ')
        for element in area4.queue:
            element.averageWait += 1
            print(f'{element.ID} -> ', end='')
        print(f'\nTempo médio de espera na fila 4: {calculate_avg_time(area4.queue):.2f} unidades de tempo')
        print('\n')

        timeUnits += 1
        print('-' * 30, '\n', f'Unidades de tempo decorridas: {timeUnits}')

        input('\n\nPressione <Enter> para continuar a simulação\n\n')
