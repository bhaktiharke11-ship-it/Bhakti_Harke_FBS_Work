## 

class Vechicles:
    def __init__(self , wheelers , num_people):
        self.wheelers = wheelers
        self.num_people = num_people

    
    def total_calculator(self):
        if self.wheelers == 2:
            basic_toll = 20
            allow_person = 2
            extra_charge = 10

        elif self.wheelers == 3:
            basic_toll = 30
            allow_person = 3
            extra_charge = 20

        elif self.wheelers== 4:
            basic_toll = 40
            allow_person = 4
            extra_charge = 30

        else:
            basic_toll = 60
            allow_person = 10
            extra_charge = 100

    def displayData(self):
        pass

wheelers = int(input("Enter wheelers:"))
people = int(input("Enter people :"))













        