import array

class Plant:
    def __init__(self, genus, species):
        self.genus = genus
        self.species = species
        

    def plantname(self):
        print("The plant is: " + self.genus + " " + self.species)

    def plantGarden(cls, *plants):
        garden = []
        for plant in plants:
            plant_name = plant.genus + " " + plant.species
            if plant_name not in garden:
                garden.append(plant_name)
        print("Here is your garden: ", garden)
    
    def waterPlants(cls, *plants):
        watered = []
        dry = list(plants)
        for plant in plants:
            plant_name = plant.genus + " " + plant.species
            if plant not in watered:
                dry.remove(plant)
                watered.append(plant)
                print(plant_name, "is moist\n")
            else:
                print("You already watered", plant_name, "!\n")

        

class Grass(Plant): 
    pass

asparagus = Plant("asparagus", "officinalis")
asparagus.plantname()

waterLettuce = Plant("pistia", "stratiotes")
aloe = Plant("aloe", "vera")
angelTrumpet = Plant("brugmansia", "suaveolens")
bamboo = Plant("bamboosa", "ardinarifolia")
carrot = Plant("daucus", "carota")

Plant.plantGarden(waterLettuce, aloe, angelTrumpet, bamboo, bamboo, carrot, aloe, asparagus)
Plant.waterPlants(waterLettuce, aloe, angelTrumpet, bamboo, bamboo, carrot, aloe, asparagus)