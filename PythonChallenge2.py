import urllib.request
from collections import Counter

response = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html')
html = response.read()
text = str(html)
soup = text.split()
code = soup[-1]
code = code[6:]
r = Counter(code).most_common()
print(r[-10:])

# Resposta: equality
