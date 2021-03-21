import sys


def show_sales(i):
    z = 0

    if len(i) == 1:
        with open('sales.txt', 'r', encoding='utf-8') as read_f:
            for line in read_f:
                print(line)

    elif len(i) == 2:
        x = int(i[1])
        with open('sales.txt', 'r', encoding='utf-8') as read_f:
            for line in read_f:
                z += 1
                if x <= z:
                    print(line)

    elif len(i) == 3:
        x = int(i[1])
        y = int(i[2])
        with open('sales.txt', 'r', encoding='utf-8') as read_f:
            for line in read_f:
                z += 1
                if x <= z <= y:
                    print(line)

    else:
        print('максимум два аргумента!')
        exit(0)

show_sales(sys.argv)

if __name__ == '__main__':
    show_sales(sys.argv)