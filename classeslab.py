import array

class Plant:
    def __init__(self, genus, species):
        self.genus = genus
        self.species = species
        self.garden = []
        

    def plantname(self):
        print("The plant is: " + self.genus + " " + self.species)

    def plantGarden(self, *plants):
        for plant in plants:
            if plant not in self.garden:
                self.garden.append(plant.genus + " " + plant.species)
        print("Here is your garden: ", self.garden)
        

class Grass(Plant): 
    pass

asparagus = Plant("asparagus", "officinalis")
asparagus.plantname()

waterLettuce = Plant("pistia", "stratiotes")
aloe = Plant("aloe", "vera")
angelTrumpet = Plant("brugmansia", "suaveolens")
bamboo = Plant("bamboosa", "ardinarifolia")
carrot = Plant("daucus", "carota")

Plant.plantGarden(waterLettuce, aloe, angelTrumpet, bamboo, bamboo, carrot)