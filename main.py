import random


from task import TwoListsNum


def main():
    avg_lists = TwoListsNum(random.sample(range(100), 10), random.sample(range(100), 10))

    avg_1 = avg_lists.average_first_list
    avg_2 = avg_lists.average_second_list

    print(f"Первый список : {avg_lists.first_list}")
    print(f"Второй список : {avg_lists.second_list}")

    # Сравниваем средние значения списков и выводим соответствующее сообщение
    if avg_1 > avg_2:
        print(f"Первый список имеет большее среднее значение ({avg_1}), чем второй список ({avg_2})")
    elif avg_2 > avg_1:
        print(f"Второй список имеет большее среднее значение ({avg_2}), чем первый список ({avg_1})")
    else:
        print(f"Средние значения первого и второго списка равны {avg_1}")

if __name__ == "__main__":
    main()

