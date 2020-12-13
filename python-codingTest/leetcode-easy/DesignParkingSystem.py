# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

# Test
class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small
        self.check_big = True
        self.check_medium = True
        self.check_small = True

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big != 0:
                self.big -= 1
                return True
            else :
                return False
        elif carType == 2:
            if self.medium != 0:
                self.medium -= 1
                return True
            else :
                return False
        else :
            if self.small != 0:
                self.small -= 1
                return True
            else :
                return False

obj = ParkingSystem(1, 1, 0) #Input
param_1 = obj.addCar(1) #Input
param_2 = obj.addCar(2) #Input
param_3 = obj.addCar(3) #Input
param_4 = obj.addCar(1) #Input
print(param_1,param_2,param_3,param_4) #Output

# Other fast solution
#     def __init__(self, big, medium, small):
#         self.A = [big, medium, small]
#     def addCar(self, carType):
#         self.A[carType - 1] -= 1
#         return self.A[carType - 1] >= 0

# class ParkingSystem:
#     def __init__(self, big: int, medium: int, small: int):
#         self.big = big
#         self.medium = medium
#         self.small = small
#         self.check_big = True
#         self.check_medium = True
#         self.check_small = True
#     def addCar(self, carType: int) -> bool:
#         if carType == 1:
#             if self.big != 0:
#                 self.big -= 1
#                 return 1
#             else :
#                 return 0
#         elif carType == 2:
#             if self.medium != 0:
#                 self.medium -= 1
#                 return 1
#             else :
#                 return 0
#         else :
#             if self.small != 0:
#                 self.small -= 1
#                 return 1
#             else :
#                 return 0           