class animal:
    def __init__(self,name,species,age):
        self.name=name
        self.species=species
        self.age=age
    
class dog(animal):
    def __init__(self,name,species,age,breed):
        super().__init__(name,species,age)
        self.breed=breed

    def __str__(self):
        return f"Is a {self.name} and its breed is {self.breed}"
    
d=dog("Tutu","canis",1,"German")
print(d)
        