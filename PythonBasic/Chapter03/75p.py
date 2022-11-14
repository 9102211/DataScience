string = """나는 홍길동 입니다.
주소는 서울시 입니다.
나이는 30세 입니다."""

sents = []  # 문장 저장
words = []  # 단어 저장

#out for
for sen in string.split(sep="\n"):
    sents.append(sen)

    #inner for
    for word in sen.split():
        words.append(word)

print('문장 :', sents)
print('문장수 :', len(sents))
print('단어 :', words)
print('단어수 :', len(words))
