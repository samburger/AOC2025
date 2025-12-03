def is_invalid_1(test_id: int):
    id_len = len(str(test_id))
    if id_len % 2 != 0:  # Only IDs with even number of digits can be invalid
        return False
    return str(test_id)[: id_len // 2] == str(test_id)[id_len // 2 :]


def is_invalid_2(test_id: int):
    """Now an ID is invalid if it is made of only repeats, of any number."""
    id_len = len(str(test_id))
    # For an ID to be made of repeats, the max length of a repeat is id_len//2.
    # So we can start by checking id_len//2, and decrease from there.
    # But we only need to check repeat lengths that evenly divide id_len.
    for repeat_len in range(id_len // 2, 0, -1):
        if id_len % repeat_len != 0:
            continue
        # Split the ID into equal substrings of repeat_len length
        sub_ids = str(test_id).split(str(test_id)[:repeat_len])
        # Now sub_ids will be a list of empty strings if the test_id contained only repeats.
        # Check if they are all equivalent
        if all(not bool(i) for i in sub_ids):
            return True


def main_1(input_file):
    with open(input_file, "r") as f:
        data = f.read()
        data = [tuple(map(int, i.split("-"))) for i in data.split(",")]
    invalids = list()
    for entry in data:
        for test_num in range(entry[0], entry[1] + 1):
            if is_invalid_1(test_num):
                invalids.append(test_num)
    return sum(invalids)


def main_2(input_file):
    with open(input_file, "r") as f:
        data = f.read()
        data = [tuple(map(int, i.split("-"))) for i in data.split(",")]
    invalids = list()
    for entry in data:
        for test_num in range(entry[0], entry[1] + 1):
            if is_invalid_2(test_num):
                invalids.append(test_num)
    return sum(invalids)


if __name__ == "__main__":
    print(main_1("02-input.txt"))
    print(main_2("02-input.txt"))
