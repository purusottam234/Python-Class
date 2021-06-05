MENU = {'sandwich': 10, 'tea': 9, 'salad': 5}


def restaurant():
    total = 0
    while True:
        order = input("Order: ").strip()
        if not order:
            break

        if order in MENU:
            price = MENU[order]
            total += price
            print(f'{order} is {price}, total is {total}')
        else:
            print(f'We are fresh out of {order} today')
    print(f'Your total is {total}')


restaurant()
