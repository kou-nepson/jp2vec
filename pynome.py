from janome.tokenizer import Tokenizer

# Tokenneizerインスタンスの生成 
t = Tokenizer()

def extract_words(text):
    tokens = t.tokenize(text)
    return [token.base_form for token in tokens 
        if token.part_of_speech.split(',')[0] in['名詞', '動詞']]

ret = extract_words('三四郎は京都でちょっと用があって降りたついでに。')
for word in ret:
    print(word)

sentences = '。'
word_list = [extract_words(sentence) for sentence in sentences]

for word in word_list[0]:
    print(word)
