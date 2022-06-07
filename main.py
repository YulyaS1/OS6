from random import randint
import math as m

memory = [8, 8, 8, 8, 8, 8, 8, 8]
ex_tasks = []
new_file = 0


def add_task():
    global memory, ex_tasks, new_file
    reserv = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(memory)):
        reserv[i] = memory[i]
    rand_task = randint(1, 64)
    place = randint(0, 7)
    new_file = rand_task
    reserv_ex_task = [0]*len(ex_tasks)
    for i in range(len(ex_tasks)):
        reserv_ex_task[i] = ex_tasks[i]
    ex_tasks.append(rand_task)
    if memory[place] == 8:
        if rand_task <= 8:
            memory[place] -= rand_task
        else:
            try:
                memory[place] -= 8
                rand_task -= 8
                for i in range(m.ceil(rand_task / 8)):
                    if rand_task <= 8 and memory[place + i + 1] == 8:
                            memory[place + i + 1] -= rand_task
                            rand_task = 0
                    else:
                        memory[place + i + 1] -= 8
                        rand_task -= 8

            except:
                memory = reserv
                ex_tasks = reserv_ex_task
                add_task()

    else:
        memory = reserv
        ex_tasks = reserv_ex_task
        add_task()


def compression():
    global memory
    sum = 0
    for i in range(len(ex_tasks)):
        sum += ex_tasks[i]
    for i in range(len(memory)):
        if sum > 8:
            memory[i] = 0
            sum -= 8
        elif 0 < sum <= 8:
            memory[i] = 8 - sum
            sum = 0
        elif sum == 0:
            memory[i] = 8
    print("Состояние памяти после сжатия:", memory)


def delete_task():
    global ex_tasks
    del_task = int(input("Введите размер удаляемого файла: "))
    for i in range(len(ex_tasks)):
        if ex_tasks[i] == del_task:
            del ex_tasks[i]
            compression()
            break


def menu():
    print("Выберите пункт: ")
    print("1) Добавить файл и произвести сжатие")
    print("2) Удалить файл")
    print("3) Вывести список исполняемых файлов")
    choose = int(input())
    if choose == 1:
        add_task()
        print("Размер нового файла:", new_file)
        print("Текущее состояние памяти:", memory)
        compression()
        menu()
    if choose == 2:
        delete_task()
        menu()
    if choose == 3:
        print("Исполняемые файлы:", ex_tasks)
        menu()


if __name__ == "__main__":
    menu()
