import re

get = open('row.txt', encoding='utf-8')
text = str(get.read())


pattern = r'[a-z]+_*[a-z]+'
match = re.search(pattern, text)

print(match.group())