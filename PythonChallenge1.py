alpha = dict()
x = 0
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z']
for letra in abc:
    if x == 24:
        alpha[abc[x]] = abc[0]
    elif x == 25:
        alpha[abc[x]] = abc[1]
    else:
        alpha[abc[x]] = abc[x + 2]
    x += 1
alpha[" "] = " "
alpha["."] = "."
alpha["'"] = "'"
alpha["("] = "("
alpha[")"] = ")"
alpha["/"] = "/"
alpha[":"] = ":"


def decoder(code):
    """
    :param code: string to be translated
    :return: string translated
    """
    decripted = ""
    for letra in code:
        decripted += alpha[letra]
    print(decripted)


if __name__ == '__main__':
    c = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb " \
        "rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
    decoder("map")

# Resposta: ocr
