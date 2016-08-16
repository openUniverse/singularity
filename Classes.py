
class StoneCost:
    def __init__(self, thatch, wood, stone):
        self.thatch = thatch
        self.wood = wood
        self.stone = stone

    def __mul__(self, other):
        return StoneCost(self.thatch * other, self.wood * other, self.stone * other)

    def __add__(self, other):
        return StoneCost(self.thatch + other.thatch, self.wood + other.wood, self.stone + other.stone)

    def __str__(self):
        return "thatch: " + str(self.thatch) + " wood: " + str(self.wood) + " stone: " + str(self.stone)

class ArkBuild:
    wall = StoneCost(15, 20, 40)
    ceiling = StoneCost(20, 40, 60)
    floor = StoneCost(30, 40, 80)

    def __init__(self, width, length, height):
        self.width = width
        self.length = length
        self.height = height

    def __str__(self):
        return "# of Walls: " + str(self.NumOfWall()) + " Wall Mats: " + str(self.WallCost()) + \
               "\n # of Floors: " + str(self.NumOfFloor()) + " Floor Mats: " + str(self.FloorCost()) + \
               "\n # of Ceilings: " + str(self.NumOfFloor()) + " Ceiling Mats: " + str(self.CeilCost()) + \
               "\n Total Cost: " +str(self.TotalCost())
    def TotalCost(self):
        return self.WallCost() + self.FloorCost() + self. CeilCost()

    def WallCost(self):
        return self.wall * self.NumOfWall()

    def CeilCost(self):
        return self.ceiling * self.NumOfCeil()

    def FloorCost(self):
        return self.floor * self.NumOfFloor()

    def NumOfCeil(self):
        return self.Area()

    def NumOfFloor(self):
        return self.Area()

    def Area(self):
        return self.length * self.width

    def NumOfWall(self):
        return (2 * self.width + 2 * self.length) * self.height


mainBuild = ArkBuild(width= 21, length= 70, height= 24)
sumBuild = ArkBuild(5, 5, 10)

print (mainBuild)

