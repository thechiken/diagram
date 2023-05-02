import re
import string

frequency = {}
document_text = open('ЛИТЕРАТУРА.txt', 'r')
text_string = document_text.read().lower()

for i in range (len(data)-1):
    #data[i+1]=data[i+1].split('.,')[:-1]
    #string.data[i+1]find('.')+1.]
    data[i+1] = '.,'.join(data[i+1].split('.,')[:-1])
    print(data[i+1])

match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
for word in match_pattern:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

frequency_list = frequency.keys()
for words in frequency_list:
    print (words, frequency[words])