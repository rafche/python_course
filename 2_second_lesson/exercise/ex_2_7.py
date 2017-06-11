"""
compare if input List contains colors of rainbow-flag
"""

def compare_colors(rainbow, colors):
    temp = []
    for element in rainbow:
        if element in colors:
            temp.append(element)
    return temp

if __name__ == '__main__':
    colors_rainbowflag = ['pink','red','orange', 'yellow',
                      'green', 'turquoise', 'indigo', 'violet']
    colors = ['red', 'blue', 'green', 'brown', 'purple', 'orange', 'pink', 'black']

    print(compare_colors(colors_rainbowflag,colors))