import urllib.request

response = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/equality.html')
html = response.read()
text = str(html)
soup = text.split()
code = str(soup[-1])
x = 1
for letra in code:
    if x < len(code):
        if not code[x - 1].isupper():
            if code[x].isupper():
                if code[x + 1].isupper():
                    if code[x + 2].isupper():
                        if code[x + 3].islower():
                            if code[x + 4].isupper():
                                if code[x + 5].isupper():
                                    if code[x + 6].isupper():
                                        if not code[x + 7].isupper():
                                            print(code[x], code[x + 1], code[x + 2], code[x + 3], code[x + 4], code[x + 5],
                                                  code[x + 6])
    x += 1

#Resposta: linkedlist