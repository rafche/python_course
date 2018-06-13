# reading files, use
# use with, it close the file automatically after reading

        print(type(text))
def read_file(file):
    with open(file, 'r') as f:
        text = f.read()
        print(text)


read_file('sometext.txt')