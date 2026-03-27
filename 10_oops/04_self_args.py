class ChaiCup:
    size = 150
    
    def describe(self):
        return f"a {self.size} ML Chai Cup"

cup = ChaiCup()
print(cup.describe())

ChaiCup.describe(cup)# output: a 150 ML Chai Cup

cup2 = ChaiCup()
cup2.size = 100
print(cup.describe())# output: a 150 ML Chai Cup
print(cup2.describe())# output: a 100 ML Chai Cup