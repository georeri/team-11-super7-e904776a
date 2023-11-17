MIN_ALLOWED = 0
MAX_ALLOWED = 9
map = []

def make_map():
    positions = []
    for x in range(MIN_ALLOWED, MAX_ALLOWED + 1):
        positions.append(["x" for y in range(MIN_ALLOWED, MAX_ALLOWED + 1)])
    return positions

def print_map(map_array):
    for rows in map_array:
        for item in rows:
            print(item + " ", end="")
        print()

def update_map(map_array, x, y, player):
    positions = map_array
    positions[x][y] = player
    print("\n")
    print_map(positions)
    

map = make_map()
print_map(map)
pass