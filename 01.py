def main_1(input_file):
    with open(input_file, "r") as f:
        rotations = f.readlines()
    pos = 50
    zeroes = 0
    for rot in rotations:
        dir = -1 if rot.startswith("L") else 1
        rot = int(rot[1:]) * dir
        pos = (pos + rot) % 100
        if pos == 0:
            zeroes += 1
    print(zeroes)


def main_2(input_file):
    with open(input_file, "r") as f:
        rotations = f.readlines()
    pos = 50
    zeroes = 0
    for rot in rotations:
        dir = -1 if rot.startswith("L") else 1
        rot = int(rot[1:]) * dir
        pos = (pos + rot) % 100
        if 

if __name__ == "__main__":
    print("Part 1: ", main_1("01-input.txt"))
    print("Part 2: ", main_2("01-input.txt"))
