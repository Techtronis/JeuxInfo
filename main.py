#debute le jeu
def start():
    gameOn = True
    username = input("Salut, comment t'appelles-tu? ")
    pokemonSelect(int(input(f"Salut {username}! Quelle Pokémon veux-tu? (1) Pikachu | (2) Salameche | (3) Carapuce")))
    
def pokemonSelect(choice):
    print(choice)
    attacks = []
    attackDamage = []
    hp = 100
    pokemons = ["Pikachu", "Salameche", "Carapuce"]
    mainPokemon = pokemons[choice-1]
    
    if mainPokemon == "Pikachu":
        attacks.extend(["éclair", "Griffure", "Electrocution"])
        attackDamage.extend([20, 10, 15])
    elif mainPokemon == "Salameche":
        attacks.extend(["Flamme", "Griffure", "Brulure"])
        attackDamage.extend([20, 10, 15])
    elif mainPokemon == "Carapuce":
        attacks.extend(["Noyade", "Griffure", "Jet d'eau"])
        attackDamage.extend([20, 10, 15])
    '''
    x=len(attacks)
    print(x)
    print(mainPokemon)
    '''
def locationSelect():
    locations = ["Route", "Ville", "Hautes herbes"]
    locChoice = int(input("Where do you want to go? (1) Road | (2) Ville | (3) Hautes herbes"))
    
    
    
    
    
    
start()