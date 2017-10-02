from collections import Counter
words = []
content = []
with open('happiness_seg.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if len(line) > 0:
            words = words + line.split(' ')

# 当前后两个list元素长度为2时，将其存入新建的list
for i in range(len(words)):
    if len(words[i]) == 2 and len(words[i+1]) == 2:
        content.append(words[i] + ' ' + words[i+1])

counter = Counter(content)
counter.most_common(10)
for a in counter.most_common(10):
    print(a[0] + '\t' + str(a[1]))