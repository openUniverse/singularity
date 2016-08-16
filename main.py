"""Softmax."""

import numpy as np
scores = [3.0, 1.0, 0.2]
scores = np.array([[1, 2, 3, 6],
                   [2, 4, 5, 6],
                   [3, 8, 7, 6]])



def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    eToTheInput = np.exp(x)
    return np.divide(eToTheInput, np.sum( eToTheInput, axis=0 ))


print(softmax(scores*10))

# # Plot softmax curves
# import matplotlib.pyplot as plt
# x = np.arange(-2.0, 6.0, 0.1)
# scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])
#
# plt.plot(x, softmax(scores).T, linewidth=2)
# plt.show()


# class StoneCost:
#     def __init__(self, thatch, wood, stone):
#         self.thatch = thatch
#         self.wood = wood
#         self.stone = stone
#
#     def __mul__(self, other):
#         return StoneCost(self.thatch * other, self.wood * other, self.stone * other)
#
#     def __add__(self, other):
#         return StoneCost(self.thatch + other.thatch, self.wood + other.wood, self.stone + other.stone )
#
#     def __str__(self):
#         return "thatch: " + str(self.thatch) + " wood: " + str(self.wood) + " stone: " + str(self.stone)
#
# class ArcBuilding:
#     wall = StoneCost(15, 20, 40)
#     ceiling = StoneCost(20, 30, 60)
#     floor = StoneCost(30, 40, 80)
#
#     def __init__(self, width, height, length):
#         self.width = width
#         self.height = height
#         self.length = length
#
#     def __str__(self):
#         return "Wall * " + str(self.NumberOfWalls()) + " Materials: " + str(self.WallCost()) + \
#                "\n Floor"
#
#     def TotalCost(self):
#         return self.WallCost() + self.CielingCost() + self.FloorCost()
#
#     def WallCost(self):
#         return self.wall * self.NumberOfCielings()
#
#     def CielingCost(self):
#         return self.ceiling * self.NumberOfFloors()
#
#     def FloorCost(self):
#         return self.floor * self.NumberOfWalls()
#
#     def NumberOfCielings(self):
#         return self.Area()
#
#     def NumberOfFloors(self):
#         return self.Area()
#
#     def Area(self):
#         return self.length * self.width
#
#     def NumberOfWalls(self):
#         return 2 * self.width + 2 * self.height
#
#
#
# mainBuild = ArcBuilding(width=100, length=100, height=100)
# summerHome = ArcBuilding(100, 10, 10)
#
# costOfMainBuilding = mainBuild.TotalCost()
# costOfSummerHome = summerHome.TotalCost()
#
# print( mainBuild )