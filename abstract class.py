class Fruit:
    def taste(self):
        raise NotImplementedError()
    def rich_in(self):
        raise NotImplementedError()
    def colour(self):
        raise NotImplementedError()
class Mango(Fruit):
    def taste(self):
        return "Sweet"
    def rich_in(self):
        return "Vitamin A"
    def colour(self):
        return "yellow"
class Orange(Fruit):
    def taste(self):
        return "Sour"
    def rich_in(self):
        return " Vitamin C"
    def colour(self):
        return "Orange"
Alphanso = Mango()
print(Alphanso.taste(),Alphanso.rich_in(),Alphanso.colour())
Org = Orange()
print(Org.taste(),Org.rich_in(),Org.colour())

        
