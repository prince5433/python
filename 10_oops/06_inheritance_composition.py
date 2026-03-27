class BaseChai:

    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"preparing {self.type} chai....")

class MasalaChai(BaseChai):

    def add_spices(self):
        print("adding cardamom, ginger and cloves")

class ChaiShop:
    chai_cls = BaseChai
    def __init__(self):
        #yaha pe hamne object k reference ko chai_cls se banaya hai, jiska matlab hai ki agar ham chai_cls ko change karte hain to chai object bhi change ho jayega
        self.chai = self.chai_cls("regular")

    def serve(self):
        print(f"serving {self.chai.type} chai")
        self.chai.prepare()

class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai


shop=ChaiShop()
fancy=FancyChaiShop()
shop.serve()
fancy.serve()
fancy.chai.add_spices()