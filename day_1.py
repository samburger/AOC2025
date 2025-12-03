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
    return zeroes


def main_2(input_file):
    with open(input_file, "r") as f:
        rotations = f.readlines()
    pos = 50
    zeroes = 0
    for rot in rotations:
        dir = -1 if rot.startswith("L") else 1
        rot = int(rot[1:]) * dir
        zeroes += abs(rot) // 100
        new_pos = (pos + (rot % 100)) % 100
        if (new_pos < pos) and rot > 0 and pos != 0:
            zeroes += 1
        elif (new_pos > pos) and rot < 0 and pos != 0:
            zeroes += 1
        elif new_pos == 0 and pos != 0:
            zeroes += 1
        pos = new_pos
    return zeroes


if __name__ == "__main__":
    print("Part 1: ", main_1("01-input.txt"))
    print("Part 2: ", main_2("01-input.txt"))
