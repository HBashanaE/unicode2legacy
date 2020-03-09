# unicodeCharList=['අ','ආ','ඇ','ඈ','ඉ',
#                  'ඊ','උ','ඌ','එ','ඒ',
#                  'ඓ','ඔ','ඕ','ඖ','ක',
#                  'ඛ','ග','ඝ','ඟ','ච',
#                  'ඡ','ජ','ඦ','ඣ','ඤ',
#                  'ඥ','ට','ඨ','ඩ','ඪ',
#                  'ණ','ත','ථ','ද','ධ',
#                  'ඳ','න','ප','ඵ','බ',
#                  'භ','ඹ','ම','ය','ර',
#                  'ල','ව','ශ','ෂ','ස',
#                  'හ','ළ','ෆ',
#                  '්','ා','ැ','ෑ','ි','ී','ෘ','ෲ']
# unicodeSpecialList1 = ['ෙ','ෛ']
# unicodeSpecialList2 = ['ේ','ො','ෝ','ෞ']
# unicodeSpecialList3 = ['ු','ූ']
# unicodeSpecialChars = [' ','.',',','\'','"',';',':','/','?','<','>','[',']','{','}','(',')','!','@','#','$','%','^','&','*','-','+','=','_','`','~']
# legacyCharList= ['w','wd','we','wE','b',
#                  'B','W','W!','t','ta',
#                  'st','T','´','t!','l',
#                  'L','.','>','Õ','p',
#                  'P','c','','CO','[',
#                  '{','g','G','v','V',
#                  'K',';',':','o','O',
#                  '','k','m','M','n',
#                  'N','U','u','h','r',
#                  ',','j','Y','I','i',
#                  'y','<','*',
#                  'a','d','e','E','s','S','D','DD']
# legacySpecialList1 = ['f','ff']
# legacySpecialList2 = [['f','a'],['f','d'],['f','da'],['f','!']]
# legacySpecialList3 = [['q','=','ÿ','÷','Cÿ','','¿','re'],['Q','+','¥','ª','C¥','','¿E','rE']]
# legacySpecialChars = [' ','\'','"',')','Ù','Õ','_','^','$','<','>','[',']','{','}','*','(','Ø','@','#','^',']','^','&','*','+','±','','','','','','','','','']

unicodeChar = ['අ','ආ','ඇ','ඈ','ඉ',
                 'ඊ','උ','ඌ','එ','ඒ',
                 'ඓ','ඔ','ඕ','ඖ','ක',
                 'ඛ','ග','ඝ','ඟ','ච',
                 'ඡ','ජ','ඦ','ඣ','ඤ',
                 'ඥ','ට','ඨ','ඩ','ඪ',
                 'ණ','ත','ථ','ද','ධ',
                 'ඳ','න','ප','ඵ','බ',
                 'භ','ඹ','ම','ය','ර',
                 'ල','ව','ශ','ෂ','ස',
                 'හ','ළ','ෆ',
                 'ා','ෘ','ෲ','ෙ','ෛ','ො','ෝ','ෞ','්','ි','ී','ේ','ැ','ෑ','ු','ූ']
unicodeEasySuffix1 = ['ා','ෘ','ෲ']
unicodeEasySuffix2 = ['ෙ','ෛ']
unicodeNotSoEasySuffix1 = ['ො','ෝ','ෞ']
unicodeNotSoEasySuffix2 = ['්','ි','ී','ේ']
unicodeNotSoEasySuffix3 = ['ැ','ෑ']
unicodeNotSoEasySuffix4 = ['ු','ූ']

legacyChar = ['w','wd','we','wE','b',
                 'B','W','W!','t','ta',
                 'st','T','´','t!','l',
                 'L','.','>','Õ','p',
                 'P','c','','CO','[',
                 '{','g','G','v','V',
                 'K',';',':','o','O',
                 '','k','m','M','n',
                 'N','U','u','h','r',
                 ',','j','Y','I','i',
                 'y','<','*',
                 'd','D','DD', 'f','ff',]
legacyEasySuffix1 = ['d','D','DD']
legacyEasySuffix2 = ['f','ff']
legacyNotSoEasySuffix1 = ['d','ds','!']
legacyNotSoEasySuffix2 = ['','','','f']
legacyNotSoEasySuffix3 = ['e','E']
legacyNotSoEasySuffix4 = ['','']

def unicodeToLegacy(text):
    outputText = ''
    listOfChars = list(text)
    print(listOfChars)
    for chari in range(1, len(listOfChars)):
        prevChar = listOfChars[chari-1]
        char = listOfChars[chari]
        j = unicodeChar.index(prevChar)
        if char in unicodeEasySuffix1:
            i = unicodeEasySuffix1.index(char)
            outputText += legacyChar[j] + legacyEasySuffix1[i]
        if char in unicodeEasySuffix2:
            i = unicodeEasySuffix2.index(char)
            outputText += legacyEasySuffix1[i] + legacyChar[j]
        elif char in unicodeNotSoEasySuffix1:
            outputText += ''
        elif char in unicodeNotSoEasySuffix2:
            outputText += ''
        elif char in unicodeNotSoEasySuffix3:
            outputText += ''
        elif char in unicodeNotSoEasySuffix4:
            outputText += ''
        else:
            outputText += legacyChar[j]
        
    return outputText

while True:
    inputText = input("Please enter your text")
    outputText = unicodeToLegacy(inputText)
    print(outputText)
    