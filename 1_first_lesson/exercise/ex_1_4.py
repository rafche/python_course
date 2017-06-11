"""
--> string, <-- longest sequence
"""

input_string = 'abckhaklilaabcdefgh'
longest_seq = ''
temp_seq = ''

for letter in input_string:
    # first run compare_char will be empty
    if (temp_seq == ''):
        temp_seq = letter
    # compare the last character of string
    elif (temp_seq[-1] < letter):
        temp_seq += letter
    elif (temp_seq[-1] > letter):
        if (len(longest_seq) < len(temp_seq)):
            longest_seq = temp_seq
            temp_seq = letter
        else:
            temp_seq = letter
if (len(temp_seq) > len(longest_seq)):
    longest_seq = temp_seq
print(longest_seq)
