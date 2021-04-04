
def add_sale(num):
    num = str(num[1]) + '\n'
    with open('sales.txt', 'a', encoding='utf-8') as sale_file:
        sale_file.write(num)    # из списка в строку


if __name__ == '__main__':
    add_sale()
