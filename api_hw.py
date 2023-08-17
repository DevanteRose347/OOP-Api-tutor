# Create a Move_Tutor Class that in herits from the Pokemon parent class.

# This class should have a list attribute (move_list) that holds pokemon moves 
# which should be populated with an api call to the PokeApi moves section  
# (just like we did with abilities and types in the Pokemon class example).
# Finally create a class method that teaches your pokemon up to 4 moves. 
# This method should take in a user input to what move they would like to teach and do a membership inside the move_list. 
# If the move exists inside the move_list the pokemon can learn that move and append to the final taught_moves list. 

class Pokemon():
    
    def __init__(self, name):
        self.id = None
        self.name = name
        self.types = []
        self.abilities = []
        self.weight = None 
        self.height = None
        self.image = None
        self.poke_api_call()
        
    def poke_api_call(self):
#         print('In the poke api call')
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.name.lower()}")
#         print(response)

        if response.status_code == 200: #200 is a successful request & response
            data = response.json() #jsonifying the data to be a usable dictionary/object 
        else:
            return "Not a valid pokemon name. Please try again", response.status_code        

#         print(data)
        self.id = data['id'] #im trying to grab the key of id 
        self.name = data['name']
        self.weight  = data['weight']
        self.height = data['height']
        self.abilities = [ability['ability']['name'] for ability in data['abilities']]
        self.types = [type_['type']['name'] for type_ in data['types']]
        self.image = data['sprites']['front_shiny']
        print(self.image)
        
        print(f"{self.name}'s data has been updated")
    
    def throw_random_ability(self):
        return choice(self.abilities)
    
    def display_image(self):
        
        display(Image(url = self.image))
    
    def __repr__(self):
        return f"You caught a {self.name}! Congrats!"




class Move_Tutor(Pokemon):
    def __init__(self):
        self.move = 
        self.move_list = []
        self.taught_moves = []


    def move_api_call(self):
#         print('In the poke api call')
        response = requests.get(f"https://pokeapi.co/api/v2/move/{self.name.lower()}")
#         print(response)

        if response.status_code == 200: #200 is a successful request & response
            data = response.json() #jsonifying the data to be a usable dictionary/object 
        else:
            return "Not a valid pokemon name. Please try again", response.status_code       
        
    def teach_move(self):
    
    pikachu.teach_move()

    pikachu.show_moves()