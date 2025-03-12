import random as rm

class Isekai:
    def __init__(self, name):
        self.name = name
        self.level = 0
        self.monster = ["Slime", "Goblin", "Orc", "Troll", "Stempede of monster", "Dragon"]
        self.position = ["Traveller","Villager","Village hero","Noble","King","SSS rank adventurer"]
        self.weapon = ["Wooden sword","Iron sword","Steel sword","Mithril sword","Excalibur"]
        
    def hit(self):
        print(f"{self.name} have killed the {self.monster[self.level]}!")
        self.level += 1
        print(f"{self.name} have leveled up!")

    
player1 = Isekai(input("1. Create a character : "))
while player1:
    print(f"Welcome to isekai! You are a {player1.name} with level {player1.level}.")
    print(f"{player1.name} is a {player1.position[player1.level]} with a {player1.weapon[player1.level]}.")
   
    while True:
        if player1.level == 5:
            print(f"{player1.name} have defeated the final boss and saved the world!")
            break
        else:
            print(f"Attention! {player1.monster[player1.level]} is infront of you!")
            print("What do you want to do?")
            print("0. Check Status")
            print("1. Hit")
            print("2. Run")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "0":
                print(f" \
                        Name : {player1.name}\n \
                        Occupation : {player1.position[player1.level]}\n \
                        Sword rank : {player1.weapon[player1.level]}\n \
                        Level : {player1.level}\n ")
            elif choice == "1":
                count = 1
                while True:
                    monster_attack = rm.randint(0,2**player1.level)
                    try_attack = int(input(f"Enter your attack number to correctly hit him in between 0 and {2**player1.level}: "))
                                 
                    if try_attack == monster_attack:
                        player1.hit()
                        break
                    else:
                        print("You missed!")
                        
            elif choice == "2":
                print(f"{player1.name} ran away.")
                break

            elif choice == "3":
                print(f"{player1.name} exited the game.")
                break
    
    


    
