# flat a list of lists, which contains multiple stacked lists
#
# expected input:
# [a, b, c, [1, 2, 3, [9, 3, 5,6 ]], e, ]
#
# output should look like:
# [a, b, c, 1, 2, 3, 9, 3, 5, 6, e]


def flat_listoflists(input_list, final_list=None):
    '''
    :param input_list: 
    :param final_list: 
    :return: flatet 
    '''
    if final_list is None:
        final_list = []

    for element in input_list:
        if not isinstance(element, list):
            final_list.append(element)
        else:
            flat_listoflists(element, final_list)
    return final_list


input_listoflists = ['a', 'b', 'c', [1, 2, 3, [9, 3, 5, 6]], 'e']
input_listoflists_II = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 3, 4, 5, 6, 7, 8, 9],
                        [3, 4, 5, 6, 7, 8, 9], [4, 5, 6, 7, 8, 9], [5, 6, 7, 8, 9], [6, 7, 8, 9], [7, 8, 9], [8, 9],
                        [9]]
input_listoflists_III = [
    ['dog', 'cat', 'bird', ['apple', 'google', ['Austria', 'Germany', 'Swiss', 'France'], [1, 2, 3, ]], 'Nobody ']]

print(flat_listoflists(input_listoflists))
print(flat_listoflists(input_listoflists_II))
print(flat_listoflists(input_listoflists_III))
