

# PARENT CLASS
class Biome():
    climate = 'Unknown'
    vegetation = 'Unknown'
    soil = 'Unknown'
    wildlife = 'Unknown'
    location = 'Earth'

    #defines method for parent class
    def information(self):
        msg = '\nClimate: {}\nVegetation: {}\nSoil: {}\nWildlife: {}\nLocation: {}'.format(self.climate,self.vegetation,self.soil,self.wildlife,self.location)
        return msg
    

# CHILD CLASS INSTANCE
class Rainforest(Biome):
    climate = 'Warm and humid'
    vegetation = 'Dense canopies of plants, bushes, and trees'
    soil = 'Iron and aluminum oxide. Low natural fertility'
    wildlife = 'Large cats, multitude of bird, reptile, and amphibian species'
    temperature_range = '70-90 degrees F'
    rainfall = '60-200 inches per year'
    
    #defines method for child class
    def information(self):
        msg = '\nClimate: {}\nVegetation: {}\nSoil: {}\nWildlife: {}\nLocation: {}\nTemperature Range: {}\nRainfall: {}'.format(self.climate,self.vegetation,self.soil,self.wildlife,self.location,self.temperature_range,self.rainfall)
        return msg 


# CHILD CLASS INSTANCE
class Taiga(Biome):
    climate = 'Cold and moist'
    vegetation = 'Thick, coniferous forests'
    soil = 'Permafrost'
    wildlife = 'Multitude of mammals, including large cats, bears, moose, and wolves'
    temperature_range = '-65 - 30 degrees F'
    seasons = 'Cold and harsh winters, hot and short summers'

    #defines method for child class
    def information(self):
        msg = '\nClimate: {}\nVegetation: {}\nSoil: {}\nWildlife: {}\nLocation: {}\nTemperature Range: {}\nSeasons: {}'.format(self.climate,self.vegetation,self.soil,self.wildlife,self.location,self.temperature_range,self.seasons)
        return msg



# INSTANTIATIONS OF CLASSES
if __name__ == '__main__':
    biome = Biome()
    print(biome.information())

    rainforest = Rainforest()
    print(rainforest.information())

    taiga = Taiga()
    print(taiga.information())
    
    
