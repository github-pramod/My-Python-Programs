contents = ""

with open("songs.txt", 'r') as song_file:  # songs.txt will have the list of songs by Lil Uzi Vert
    for content in song_file:
        contents += content

dictionary = {"hungry": "Would you like to have a sandwich?",
              "Cricket": "You must watch 100 100's of Sachin Tendulkar",
              "Lil Uzi Vert": contents}

while True:
    entry = input("Enter something!! ")  # takes input from the user
    for key in dictionary.keys():  # searching if any of the keys is present in the entry or not.
        if key in entry:  # if key us present in the entry
            output = dictionary[key]  # the value of the key will be displayed.
            print(output)
    if entry == "quit":  # in case the user wants to quit the game
        break
