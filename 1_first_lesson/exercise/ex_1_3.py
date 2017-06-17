"""
--> sentence, <-- reverse sentence
order the words in a sentence in reverse
"""
reversed_sentence = ''

sentence = str(input('please type in a sentence\n'))

sentence_list = sentence.split(' ')

# using a loop
for word in reversed(sentence_list):
    reversed_sentence += word + ' '

# using the join method
print(' '.join(reversed(sentence_list)))

print(reversed_sentence)