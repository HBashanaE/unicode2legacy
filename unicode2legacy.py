unicodeCharList=['අ','ආ','ඇ','ඈ','ඉ',
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
                 '්','ා','ැ','ෑ','ි','ී','ෘ','ෲ']
unicodeSpecialList1 = ['ෙ','ෛ']
unicodeSpecialList2 = ['ේ','ො','ෝ','ෞ']
unicodeSpecialList3 = ['ු','ූ']
unicodeSpecialChars = [' ','.',',','\'','"',';',':','/','?','<','>','[',']','{','}','(',')','!','@','#','$','%','^','&','*','-','+','=','_','`','~']
legacyCharList= ['w','wd','we','wE','b',
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
                 'a','d','e','E','s','S','D','DD']
legacySpecialList1 = ['f','ff']
legacySpecialList2 = [['f','a'],['f','d'],['f','da'],['f','!']]
legacySpecialList3 = [['q','=','ÿ','÷','Cÿ','','¿','re'],['Q','+','¥','ª','C¥','','¿E','rE']]
legacySpecialChars = [' ','\'','"',')','Ù','Õ','_','^','$','<','>','[',']','{','}','*','(','Ø','@','#','^',']','^','&','*','+','±','','','','','','','','','']

def unicodeToLegacy(text):
    outputText = ''
    listOfChars = list(text)
    for chari in range(len(listOfChars)):
        prevChar = listOfChars[chari-1]
        char = listOfChars[chari]
        #print(char +' = ' + str(unicodeCharList.index(char)))
        if(unicodeCharList.count(char)):
            if(char == 'ැ' and prevChar == 'ර'):
                outputText=outputText[:-2]+'/'
            if(char == 'ෑ' and prevChar == 'ර'):
                outputText=outputText[:-2]+'?'
            else:
                outputText+=legacyCharList[unicodeCharList.index(char)]    
            
        else:
            if(unicodeSpecialList1.count(char)):
                outputText=outputText[:-1]+legacySpecialList1[unicodeSpecialList1.index(char)]+outputText[-1]
            elif(unicodeSpecialList2.count(char)):
                outputText=outputText[:-1]+legacySpecialList2[unicodeSpecialList2.index(char)][0]+outputText[-1]+legacySpecialList2[unicodeSpecialList2.index(char)][1]
            elif(unicodeSpecialList3.count(char)):
                if('වටයපසෆහජලබනමඛඹඨඩඪඵඝඦචඡධෂඣණ'.count(prevChar)):
                    outputText+=legacySpecialList3[unicodeSpecialList3.index(char)][0]
                elif('කගඟතනභශ'.count(prevChar)):
                    outputText+=legacySpecialList3[unicodeSpecialList3.index(char)][1]
                elif('ද'.count(prevChar)):
                    outputText=outputText[:-1]+legacySpecialList3[unicodeSpecialList3.index(char)][2]
                elif('ඳ'.count(prevChar)):
                    outputText=outputText[:-1]+legacySpecialList3[unicodeSpecialList3.index(char)][3]
                elif('ඤ'.count(prevChar)):
                    outputText=outputText[:-1]+legacySpecialList3[unicodeSpecialList3.index(char)][4]
                elif('ඥ'.count(prevChar)):
                    outputText=outputText[:-1]+legacySpecialList3[unicodeSpecialList3.index(char)][5]
                elif('ළ'.count(prevChar)):
                    outputText=outputText[:-1]+legacySpecialList3[unicodeSpecialList3.index(char)][6]
                elif('ර'.count(prevChar)):
                    outputText=outputText[:-1]+legacySpecialList3[unicodeSpecialList3.index(char)][7]
            elif(unicodeSpecialChars.count(char)):
                outputText+=legacySpecialChars[unicodeSpecialChars.index(char)]    
                
            
            

    return outputText

while True:
    inputText = input("Please enter your text")
    outputText = unicodeToLegacy(inputText)
    print(outputText)
    
    
