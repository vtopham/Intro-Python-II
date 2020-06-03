# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
    
    def room_loop(self):
        print(f"Location: {self.current_room.name}")
        print(f"Location: {self.current_room.description}")
        print(f"Location: {self.current_room.description}")
        
    # def move(direction):
    #     if direction == "n":

    #     elseif direction == "e":

    #     elseif direction == "s":

    #     elseif direction == "w":

    #     else:
    #         print("Please enter a valid direction")