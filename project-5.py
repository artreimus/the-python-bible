films = {
    "Finding Dory": [3,5],
    "Bourne": [18,5],
    "Tarzan": [15,5],
    "Ghost Busters": [12,5]
}


while True: 
    choice = input('What film do you want to watch?')
    if choice in films:
        age = int(input("How old are you?: ").strip())
        num_seats = films[choice][1]
        if age >= num_seats:
            if films[choice][1] > 0:
                print("Enjoy the film")
                films[choice][1] = num_seats - 1
            else: 
                print("Sorry, we are sold out")
        else:
            print("You are too young to watch that film")
    else:
        print("Sorry, we don't have that film")