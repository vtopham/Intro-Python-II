from room import Room
from player import Player
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

    
#core loop of the game
def game_loop():
    print(f"Location: {victoria.current_room.name}\n{victoria.current_room.description}\n\nWhere do you go next? [n] [e] [s] [w] [q for quit]")
    user_input = input()
    if user_input == "q":
        print("Thanks for playing and have a nice day!")
    elif user_input == "n" or user_input == "e" or user_input == "s" or user_input == "w":
        move_player(user_input)
    else:
        print("Please enter a valid direction, or q to quit the game!")






game_loop()