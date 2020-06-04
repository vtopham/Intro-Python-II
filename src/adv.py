from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#add some items to the rooms
room['outside'].items_list = {
    'nosehairs': Item('Nosehairs', 'Fresh plucked!')
}

room['foyer'].items_list = {
    'cat': Item('Cat', 'She loves ya till she bites ya'),
    'dog': Item('Dog', 'All dogs are boys and all cats are girls')
}

room['overlook'].items_list = {
    'shiny': Item('Shiny', "I think it's a piece of foil")
}

room['narrow'].items_list = {
    'sword': Item('Sword', "Too bad it's about an inch long")
}

room['treasure'].items_list = {
    'recipes': Item('Recipes', "From gran's kitchen")
}



#
# Main
#

# Make a new player object that is currently in the 'outside' room.

victoria = Player("victoria", room['outside']) 

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

    
#Takes validated input and moves the player, if possible
def move_player(user_input):
    next_room = getattr(victoria.current_room, f"{user_input}_to")
    if next_room == "invalid":
        print("=======That area is out of bounds=======")
    else: 
        victoria.current_room = next_room
    game_loop()

#Lets a user attempt to pick up an item
def take_item(item):
    is_in_room = 0
    #is the item in the room?
    for k, v in victoria.current_room.items_list.items():
        if v.name.lower() == item:
            victoria.inventory.append(v)
            v.on_take()
            is_in_room = 1
            key = k
    if is_in_room == 1:
        victoria.current_room.items_list.pop(key)
    else:
        print("That item isn't in this room!")
    game_loop()      

#Lets a user drop an item
def drop_item(item):
    is_in_inventory = 0
    #is the item in the room?
    is_in_inventory = 0
    for x in range(len(victoria.inventory)):
        
        if victoria.inventory[x].name.lower() == item:
            
            victoria.current_room.items_list[victoria.inventory[x].name] = victoria.inventory[x]
            
            victoria.inventory[x].on_drop()
            victoria.inventory.pop(x)
            is_in_inventory = 1
    if is_in_inventory == 0:
        print(f"You never had {item} to begin with!")
    game_loop()

        
    

#when a bad command is issued            
def valid_command_needed():
    print("Please enter a valid command, or q to quit the game!")
    game_loop()
#core loop of the game
def game_loop():
    
    #print location information
    print(f"\n==Location==\n{victoria.current_room.name}\n{victoria.current_room.description}\n")
    
    #print items information
    print("==Items==")
    if len(victoria.current_room.items_list) == 0:
        print("There are no items in this room!")
    else:
        for k, v in victoria.current_room.items_list.items():
            print(f"{v.name}: {v.description}")
    print("\n")

    #print player instructions
    print("Movement: [n] [e] [s] [w] [q for quit]\nPick up item: [take [item]]\nInventory: [i]")
    
    #get input and act
    user_input = input().lower().split(" ")
    
    
    if len(user_input) == 1:
        user_input = user_input[0]
        #if the user wants to quit
        if user_input == "q":
            print("Thanks for playing and have a nice day!")
        #if the user wants to see their inventory
        elif user_input == "i":
            if len(victoria.inventory) > 0:
                print("==Inventory==")
                for x in victoria.inventory:
                    print(x.name)
            else:
                print("Your pockets are empty")
            game_loop()
        #if the user wants to move around
        elif user_input == "n" or user_input == "e" or user_input == "s" or user_input == "w":
            move_player(user_input)
        else: 
            valid_command_needed()
    elif len(user_input) == 2:
        #if the user wants to pick something up
        if user_input[0] == "take" or user_input[0] == "get":
            take_item(user_input[1])
        if user_input[0] == "drop":
            drop_item(user_input[1])
        else:
            valid_command_needed()
    else:
        valid_command_needed()





game_loop()