class Plant:
    def __init__(self, genus, species):
        self.genus = genus
        self.species = species

    def plantname(self):
        print("The plant is: " + self.genus + " " + self.species)

class Grass(Plant): 
    pass

asparagus = Plant("asparagus", "officinalis")
asparagus.plantname()