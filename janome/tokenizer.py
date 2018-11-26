import codecs

def Tokenizer():
    f = codecs.open('sanshiro.txt', "r", "sjis")
    text = f.read()
    f.close()
    import re
    text = re.split('\-{5,}',text)[2]
    text = re.split('底本：',text)[0]
    text = text.replace('|', '')
    text = re.sub('《.+?》', '', text)
    text = re.sub('［＃.+?］', '',text)
    text = re.sub('\n\n', '\n', text) 
    text = re.sub('\r', '', text)

    print(text[:100])
    print()
    print()
    print(text[-100:])
    return text
