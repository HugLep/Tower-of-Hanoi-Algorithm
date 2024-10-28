BASES_NB = 3

def tower_print():
    
    global base_1, base_2, base_3, BASES_NB

    max_height = len(base_1) + len(base_2) + len(base_3)

    for i in range(max_height - 1, -1, -1):

        # BASE 1
        if len(base_1) < i + 1:
            print("   ", end="")
        else:
            for space in range(max_height - base_1[i]):
                print(" ", end="")
            for ring in range(base_1[i]):
                print("o", end="")

        print("  ", end="") #SPACE
        
        # BASE 2
        if len(base_2) < i + 1:
            print("   ", end="")
        else:
            for space in range(max_height - base_2[i]):
                print(" ", end="")
            for ring in range(base_2[i]):
                print("o", end="")

        print("  ", end="") #SPACE
        
        # BASE 3
        if len(base_3) < i + 1:
            print("   ", end="")
        else:
            for space in range(max_height - base_3[i]):
                print(" ", end="")
            for ring in range(base_3[i]):
                print("o", end="")

        print("")


    for i in range(BASES_NB):
        for base in range(max_height):
            print("#", end="")
        print("  ", end="")
    print("")

def ring_move_r2b(ring_a, base_b_index):
    global base_1, base_2, base_3

    match base_b_index:
        case 1:
            base_b = base_1
        case 2:
            base_b = base_2
        case 3:
            base_b = base_3

    index_base_a = 1
    ring_a_valid = False
    for base in [base_1, base_2, base_3]:
        if len(base) > 0:
            last_ring_index = len(base) - 1
            if base[last_ring_index] == ring_a:
                ring_a_valid = True
                break
        index_base_a += 1
    
    if ring_a_valid != True:
        return 1
    if len(base_b) > 0:
        if ring_a > base_b[len(base_b) - 1]:
            return 2

    match index_base_a:
        case 1:
            base_1.pop(len(base_1) - 1)
        case 2:
            base_2.pop(len(base_2) - 1)
        case 3:
            base_3.pop(len(base_3) - 1)
    base_b.append(ring_a)
    print(ring_a, " --> base_" + str(base_b_index))

def tower_initialization(h):
    global base_1, base_2, base_3
    base_1 = []
    base_2 = []
    base_3 = []

    while h > 0:
        base_1.append(h)
        h -= 1


height = int(input("height : "))
tower_initialization(height)
tower_print()

input_ring_a = int(input("Ring to move       : "))
input_base_b = int(input("Towards which base : "))
while input_ring_a != -1 and (input_base_b >= 1 and input_base_b <= BASES_NB) and (input_ring_a >= 1 and input_ring_a <= height):
    ring_move_r2b(input_ring_a, input_base_b)
    tower_print()

    input_ring_a = int(input("Ring to move       : "))
    input_base_b = int(input("Towards which base : "))