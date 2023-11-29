class Pokemon:

    def __init__(self, id, name, type_one):
        self.id = id
        self.name = name
        self.type_one = type_one
        self.type_two = ""


    def set_second_type(self, second_type):
        """Set Pokémon who has second type"""
        self.type_two = second_type

# Calling pokemon objects
pokemon_1 = Pokemon("001", "Bulbasaur", "grass")
pokemon_1.set_second_type("poison")

pokemon_2 = Pokemon("002", "Ivysaur", "grass")
pokemon_2.set_second_type("poison")

pokemon_3 = Pokemon("003", "Venusaur", "grass")
pokemon_3.set_second_type("poison")

# Calling pokemon
bulbasaur = pokemon_1.id, pokemon_1.name, pokemon_1.type_one, pokemon_1.type_two
ivysaur = pokemon_2.id, pokemon_2.name, pokemon_2.type_one, pokemon_2.type_two
venusaur = pokemon_3.id, pokemon_3.name, pokemon_3.type_one, pokemon_3.type_two


# Add pokemon in national pokedex
pokedex = f"{bulbasaur}\n{ivysaur}\n{venusaur}\n"

print(pokedex)
