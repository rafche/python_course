# reading files
# use with, it close the file automatically after reading


def read_file(file):
    with open(file, 'r') as f:
        text = f.read()
        print(text)
        print(type(text))


read_file('sometext.txt')