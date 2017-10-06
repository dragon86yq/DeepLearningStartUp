from collections import Counter
words = []
content = []
with open('happiness_seg.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if len(line) > 0:
            words = words + line.split(' ')

# punctuation = [u'。', u'，', u'“', u'”', u'…', u'？', u'！', u'、', u'；', u'（', 
#                         u'）',u'?',u'：', u'― ―']
# stopwords  = [u'的', u'地', u'得', u'而', u'了', u'在', u'是', u'我', u'和', u'们', u'被', u'对', u'来说', u'它',
#                         u'就',  u'不',  u'都',  u'上', u'也', u'很', u'到', u'他', u'要', u'更', u'有', u'一个', u'― ―'
#                         u'去', u'你',  u'会', u'着', u'看', u'好', u'这', u'时', u'中', u'并', u'下', u'使']

# 当前后两个list元素长度为2时，将其存入新建的list
for i in range(len(words) - 1):
    # if (words[i] not in punctuation and words[i] not in stopwords)  and (words[i+1] not in punctuation and words[i+1] not in stopwords):
    if (len(words[i]) > 1  and len(words[i+1]) > 1):
            content.append(words[i] + ' ' + words[i+1])

counter = Counter(content)
b = counter.most_common(10)
for a in counter.most_common(10):
    print(a[0] + '\t' + str(a[1]))