def is_invalid(test_id):
    id_len = len(str(test_id))
    if id_len % 2 != 0:  # Only IDs with even number of digits can be invalid
        return False
    return str(test_id)[: id_len // 2] == str(test_id)[id_len // 2 :]


def main_1(input_file):
    with open(input_file, "r") as f:
        data = f.read()
        data = [tuple(map(int, i.split("-"))) for i in data.split(",")]
    invalids = list()
    for entry in data:
        for test_num in range(entry[0], entry[1] + 1):
            if is_invalid(test_num):
                invalids.append(test_num)
    return sum(invalids)


if __name__ == "__main__":
    print(main_1("02-input.txt"))
