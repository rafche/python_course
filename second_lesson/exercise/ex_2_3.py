"""
--> input order details and price, <-- restaurant bill
"""


def inputs():
    '''
    --> nothing, <-- user input
    endless loop which collects the user input
    :return: nothing
    '''
    order_items = []
    temp_order_items = []
    while (1):
        temp_order_items.clear()
        command = input('please [a]dd a item or leave input loop [x]\n')

        if command == 'x' or command == 'X':
            break
        elif command == 'a' or command == 'A':

            temp_article = str(input('please type in the article\n'))
            temp_price = float(input('please type in the price/unit\n'))
            temp_order_items.append(temp_article)
            temp_order_items.append(temp_price)
            order_items.append(temp_order_items.copy())

    print(order_items)
    return order_items


def prn_header(order_details):
    '''
    :param order_details: full order list
    :return:
    '''
    total = 0
    tax = 0
    print('{0:-^32}'.format(' hard python cafe '))

    for order_item in order_details:
        print('{item:<15} {price:>14.2f} €'.format(item=order_item[0], price=order_item[1]))
        total += order_item[1]
    print('{0:-^32}'.format(''))
    tax = total/100*20
    print('Mwst 20%{tax:>22.2f} €'.format(tax=tax))
    print('Grand Total{sum:>19.2f} €'.format(sum=total+tax))

if __name__ == '__main__':
    # order_items = inputs()
    # prn_header(order_items)


    # for debugging
    prn_header([['Cola', 2],
                ['Fanta', 2],
                ['Almdudler', 2],
                ['Espresso', 2.1],
                ['Frucade', 2.499],
                ['Red Bull', 2.499],
                ])



