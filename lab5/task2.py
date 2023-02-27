import re
get = open('row.txt', encoding='utf-8')
text = str(get.read())

pattern = r'ab{2, 3}$'
match = re.search(pattern, text)

print(match.group())