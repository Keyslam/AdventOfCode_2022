def parse():
    return open("input.txt", "r").readline()


def index_of_unique_series(message: str, length: int):
    for i in range(length, len(message)):
        to_check = message[i-length:i]
        duplicates = len(set(to_check)) != length
        if not duplicates:
            return i


def one():
    print(index_of_unique_series(parse(), 4))


def two():
    print(index_of_unique_series(parse(), 14))


if __name__ == '__main__':
    one()
    two()
