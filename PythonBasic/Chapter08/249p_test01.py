file = open("D:/Pywork/DataScience/PythonBasic/Chapter08/data/ftest.txt", mode='r')

lines = file.readlines()
docs = []
words = []

for line in lines:
    docs.append(line.strip()) #문장추출

    for word in line.split():
        words.append(word)

print(docs)
print('문단 길이 : ', len(docs))
print(words)
print('단어 길이 : ',len(words))