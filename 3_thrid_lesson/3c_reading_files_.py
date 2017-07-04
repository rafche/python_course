def readfile(filename):
    with open(filename, 'r') as f:
        text = f.read()
    return text


def wrangling_data(data):
    '''
    :param data: raw data
    :return: data in blocks (\n\n)
    '''
    return data.split('\n\n')


def validate_block(block: list):
    '''
    :param block: block
    :return: only valid blocks
    '''
    if len(block.split(':')) > 1:
        return block


if __name__ == '__main__':
    data_in_blocks = wrangling_data(readfile('sometext.txt'))
    valid_blocks = [validate_block(x) for x in data_in_blocks if validate_block(x) is not None]

    for part in valid_blocks:
        print('{:~^50}'.format(part.split(':')[0].rstrip().lstrip()))
        print('{:^50}'.format(part.split(':')[-1].rstrip().lstrip()))
        print('{:^50}'.format('-'))
        print('')
