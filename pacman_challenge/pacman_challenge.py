a_list = []
lives_count = 3
points = 5000
ghost_count = 0
ghost_points = 200
extra = 10000

points_dict = {
        'dot': 10,
        'cherry': 100,
        'strawberry': 300,
        'orange': 500,
        'apple': 700,
        'melon': 1000,
        'galaxian': 2000,
        'bell': 3000,
        'key': 5000,
}

def start():
    read = open('game.txt', 'r+')
    instructions = read.read().split(",")

    for word in instructions:
        low = word.lower()
        a_list.append(low)

        game()
        extra_life()

def game():
    for word in a_list:
        if word in points_dict:
            value = points_dict.get(word)
            global points
            points += value
            global lives_count
            if lives_count == 0:
                game_over()
        elif word == 'invincibleghost':
            lives_count -= 1
        elif word == 'vulnerableghost':
            global ghost_count
            if ghost_count == 0:
                global ghost_points
                points += ghost_points
                ghost_points *= 2
                ghost_count += 1
            elif ghost_count > 0:
                points += ghost_points
                ghost_points *= 2
        extra_life()

def extra_life():
    global extra
    if points >= extra:
        global lives_count
        lives_count += 1
        extra += 10000
        pass

def game_over():
    while True:
        if lives_count == 0:
            extra_life()
            print('Game Over')
            print(points)
            print(lives_count)
            exit()
        else:
            pass


start()
print('Game Over')
print(f'You had {points} points')
print(f'Your lives: {lives_count}')