class Character:
    #variables/attributes:
    #health (integer)
    #name (string)
    #traits (list)

    def __init__(self): #default constructor
        self.health = 0
        self.name = "default"
        self.traits = ['none']
    def __init__(self, health, name, traits): #overloaded constructor
        self.health = health
        self.name = name
        self.traits = traits

    #methods    
    def take_damage(self): #subtracts 5 points of health from character
        self.health -= 5

    def heal(self): #adds 5 points of health to character
        self.health += 10

    def get_health(self): #returns health value for printing
        return self.health
        
    def get_name(self): #returns name of Character
        return self.name

    def add_trait(self, t):
        self.traits.append(t)

    def print_traits(self):
        print('traits: ' , self.traits)

    def print_all(self):
        print('name: ' , self.get_name())
        print('health: ', self.get_health())
        self.print_traits()

def main():
    myCharacter = Character(100, 'My Name', ['annoying', 'stubborn'])
    myCharacter.add_trait('stupid')
    myCharacter.print_all()

    myCharacter_2 = Character(100, 'Your Name', ['sooo dumb', 'soooo annoying'])
    myCharacter_2.take_damage()
    myCharacter_2.print_all()

    user_input = int(input('\nif you wanna create a character of your own enter 1\nEnter Here:'))

    if user_input == 1:
        name = input('\nEnter Name Here: ')
        health = input('Enter Health Here: ')
        traits = input('Enter Traits Here (Separated by spaces)\n')

        traits = traits.split()

        yourCharacter = Character(health, name, traits)
        print("Your Character Info:\n")
        yourCharacter.print_all()

    print('\nThank You For Using My Program')

main()