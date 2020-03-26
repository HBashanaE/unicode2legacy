
unicode = []
legacy = []

def unicodeToLegacy(text):
    outputText = text
    for i in range(len(unicode)):
        outputText = outputText.replace(unicode[i],legacy[i])
    return outputText

file = open('test.txt', 'r', encoding = 'utf-8')
test = file.readlines()
file.close()
with open('legacy.txt', 'r', encoding = 'utf-8') as legacyTxt: 
    legacyData = legacyTxt.read()
with open('unicode.txt', 'r', encoding = 'utf-8') as unicodeTxt: 
    unicodeData = unicodeTxt.read()


legacy = legacyData.strip().split()
unicode = unicodeData.strip().split()

for line in test:
    outputText = unicodeToLegacy(line)
    print(outputText)
    