class car:
    brand = "hyundai"

    def __init__(self,color,vechicalNo):
        self.color = color
        self.vehicalNo = vechicalNo

    def show(self):
        print(f"Brand: {self.brand}")
        print(f"Color: {self.color}")
        print(f"Vechical No: {self.vehicalNo}")

    def getColor(self):
        return self.color

C1 = car("red","mh12")

# print(C1.color)     # red
# print(C1.vehicalNo)
# print(car.brand)

C1.show()   # Brand: hyundai Color: red Vechical No: mh12
print(C1.getColor())






# class student:
#     id = 0
#     name = "tvk"


# s1 = student()      # s1 is object of class student
# print(s1)          # <__main__.student object at 0x00000287B173BFD0>
# print(s1.id)       # 0
# print(s1.name)     # tvk

