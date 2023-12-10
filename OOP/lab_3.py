import numpy as np

class Array3d:
# метод init задает 3 измерения  dim0, dim1, dim2
# self.data одномерный массив который хранит данные 3х мерного
    def __init__(self, dim0, dim1, dim2):
        self.width = dim0
        self.height = dim1
        self.depth = dim2
        self.data = [0] * (dim0 * dim1 * dim2)
        
# get_index принимает 3х мерные координаты и возвращает одномерный индекс в
# self.data. Преобразовывает 3х - в 1 мерный индекс для доступа к эл массива
    def get_index(self, x, y, z):
        return z * (self.width * self.height) + y * self.width + x
    
#getitem позволяет получить доступ к элементу массива по 3x мерным координатам
#если индексы в пределах, то вызывает нужный элемент    
    def __getitem__(self, index):
        x, y, z = index
        if 0 <= x < self.width and 0 <= y < self.height and 0 <= z < self.depth:
            return self.data[self.get_index(x, y, z)]
        else:
            raise IndexError("Index out of range")
        
# Эти методы принимают одну из 3х координат и возвращают срез массива вдоль нее
    def GetValues0(self, i):
        if 0 <= i < self.width:
            return [self.data[self.get_index(i, y, z)] for y in range(self.height) for z in range(self.depth)]
        else:
            raise IndexError("Index out of range")

    def GetValues1(self, j):
        if 0 <= j < self.height:
            return [self.data[self.get_index(x, j, z)] for x in range(self.width) for z in range(self.depth)]
        else:
            raise IndexError("Index out of range")

    def GetValues2(self, k):
        if 0 <= k < self.depth:
            return [self.data[self.get_index(x, y, k)] for x in range(self.width) for y in range(self.height)]
        else:
            raise IndexError("Index out of range")

    def GetValues01(self, i, j):
        if 0 <= i < self.width and 0 <= j < self.height:
            return [self.data[self.get_index(i, j, z)] for z in range(self.depth)]
        else:
            raise IndexError("Index out of range")

    def GetValues02(self, i, k):
        if 0 <= i < this.width and 0 <= k < self.depth:
            return [self.data[self.get_index(i, y, k)] for y in range(self.height)]
        else:
            raise IndexError("Index out of range")

    def GetValues12(self, j, k):
        if 0 <= j < self.height and 0 <= k < self.depth:
            return [self.data[self.get_index(x, j, k)] for x in range(self.width)]
        else:
            raise IndexError("Index out of range")
        
# эти методы позволяют устанавливать значения в массиве для заданных координат
    def SetValues0(self, i, values):
        if 0 <= i < self.width:
            if len(values) == self.height * self.depth:
                for y in range(self.height):
                    for z in range(self.depth):
                        self.data[self.get_index(i, y, z)] = values[y * self.depth + z]
            else:
                raise ValueError("Invalid number of values")
        else:
            raise IndexError("Index out of range")

    def SetValues1(self, j, values):
        if 0 <= j < self.height:
            if len(values) == self.width * self.depth:
                for x in range(self.width):
                    for z in range(self.depth):
                        self.data[self.get_index(x, j, z)] = values[x * self.depth + z]
            else:
                raise ValueError("Invalid number of values")
        else:
            raise IndexError("Index out of range")

    def SetValues2(self, k, values):
        if 0 <= k < self.depth:
            if len(values) == self.width * self.height:
                for x in range(self.width):
                    for y in range(self.height):
                        self.data[self.get_index(x, y, k)] = values[x * self.height + y]
            else:
                raise ValueError("Invalid number of values")
        else:
            raise IndexError("Index out of range")

    def SetValues01(self, i, j, values):
        if 0 <= i < self.width and 0 <= j < self.height:
            if len(values) == self.depth:
                for z in range(self.depth):
                    self.data[self.get_index(i, j, z)] = values[z]
            else:
                raise ValueError("Invalid number of values")
        else:
            raise IndexError("Index out of range")

    def SetValues02(self, i, k, values):
        if 0 <= i < self.width and 0 <= k < self.depth:
            if len(values) == self.height:
                for y in range(self.height):
                    self.data[self.get_index(i, y, k)] = values[y]
            else:
                raise ValueError("Invalid number of values")
        else:
            raise IndexError("Index out of range")

    def SetValues12(self, j, k, values):
        if 0 <= j < self.height and 0 <= k < self.depth:
            if len(values) == self.width:
                for x in range(self.width):
                    self.data[self.get_index(x, j, k)] = values[x]
            else:
                raise ValueError("Invalid number of values")
        else:
            raise IndexError("Index out of range")
# cоздает массив заполненный 1
    def np_ones(self):
        self.data = [1] * (self.width * self.height * self.depth)
        
# cоздает массив заполненный 0
    def np_zeros(self):
        self.data = [0] * (self.width * self.height * self.depth)
        
# cоздает массив заполненный нужным числом
    def np_fill(self, value):
        self.data = [value] * (self.width * self.height * self.depth)

