#text에 들어있는 단어 갯수 세기
#딕셔너리 응용 프로젝트

text = "My heart leaps up when I behold A rainbow in the sky: " \
"So was it when my life began;" \
"So is it now I am a man;" \
"So be it when I shall grow old,"\
"Or let me die!"\
"The Child is father of the Man;"\
"And I could wish my days to be"\
"Bound each to each by natural piety."


print(text)
text_list = text.split() #스트링을 리스트로 변환
print(text_list)

wordcount = dict()

for word in text_list:
   if word in wordcount:
      # wordcount[word] = wordcount[word] + 1
      wordcount[word] += 1
   else:
      wordcount[word] = 1
   print(word)

print(wordcount)

for key, value in wordcount.items():
   print(f'{key} {value}')

# 2번째 버젼 : defaltdict
from collections import defaultdict
wordcount = defaultdict(lambda:0)
for word in text_list:
   wordcount[word] += 1

print(wordcount)