# Создать программу, которая принимает два списка чисел и выполняет следующие действия:
# a. Рассчитывает среднее значение каждого списка.
# b. Сравнивает эти средние значения и выводит соответствующее сообщение:
# - ""Первый список имеет большее среднее значение"", если среднее значение первого списка больше.
# - ""Второй список имеет большее среднее значение"", если среднее значение второго списка больше.
# - ""Средние значения равны"", если средние значения списков равны.

from statistics import mean
from typing import List


# Создайте программу на Python
class TwoListsNum:

    # Создаем два рандомных списка чисел

    # def create_random_list(global_list, repartition):
    #     g_list = list(global_list)
    #     random.shuffle(g_list)
    #     split_point = round(len(g_list) * repartition)
    #     return g_list[:split_point], g_list[split_point:]

    def __init__(self, first_list: List, second_list: List) -> None:
        self.list_1: List = first_list
        self.list_2: List = second_list
        self.avg_list_1: float = None
        self.avg_list_2: float = None

    @property
    def first_list(self) -> List:
        return self.list_1

    @property
    def second_list(self) -> List:
        return self.list_2

    # Cреднее значение каждого списка
    @property
    def average_first_list(self) -> float:
        if self.avg_list_1 is None:
            self.avg_list_1 = mean(self.list_1)
        return self.avg_list_1

    @property
    def average_second_list(self) -> float:
        if self.avg_list_2 is None:
            self.avg_list_2 = mean(self.list_2)
        return self.avg_list_2

