import sys

if __name__ == '__main__':
    sale = list(map(int, sys.argv[1:]))
    with open("bakery.csv") as f:
        text = f.readlines()
        if len(sale) == 2:
            for line in text[sale[0] - 1:sale[1]]:
                print(line.strip())
        elif len(sale) == 1:
            for line in text[sale[0] - 1:]:
                print(line.strip())
        else:
            for line in text:
                print(line.strip())
    exit()