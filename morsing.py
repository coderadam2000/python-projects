translation = input("Morse - English/English - Morse?\n")

english = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','.',',',' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','.',',',' ']
morse = ['·-', '-···', '-·-·', '-··', '·', '··-·', '--·', '····', '··', '·---', '-·-', '·-··', '--', '-·', '---', '·--·', '--·-', '·-·', '···', '-', '··-', '···-', '·--', '-··-', '-·--', '--··', '-----', '·----', '··---', '···--', '····-', '·····', '-····', '--···', '---··', '----·', '·-·-·-', '--··--', '   ', '·-', '-···', '-·-·', '-··', '·', '··-·', '--·', '····', '··', '·---', '-·-', '·-··', '--', '-·', '---', '·--·', '--·-', '·-·', '···', '-', '··-', '···-', '·--', '-··-', '-·--', '--··', '-----', '·----', '··---', '···--', '····-', '·····', '-····', '--···', '---··', '----·', '·-·-·-', '--··--', '  ','·-', '-···', '-·-·', '-··', '·', '··-·', '--·', '····', '··', '·---', '-·-', '·-··', '--', '-·', '---', '·--·', '--·-', '·-·', '···', '-', '··-', '···-', '·--', '-··-', '-·--', '--··', '-----', '·----', '··---', '···--', '····-', '·····', '-····', '--···', '---··', '----·', '·-·-·-', '--··--', '  ']

if translation == 'morse to english':
    c = ''
    result = ''
    inp = input('\n')
    newinp = ''

    for i in range(int(len(str(inp)))):
        if inp[i] == '_':
            newinp = newinp + '-'
        elif inp[i] == '.':
            newinp = newinp + '·'
        else:
            newinp = newinp + inp[i]
    inp = str(newinp)

    for i in range(int(len(str(inp)))):
        c = inp[i]
        j = -1
        found = False
        place = 0
        
        while not found:
            j = j + 1
            if c == morse[j]:
                place = j
                found = True
        
        result = result + english[place] + ' '
elif translation == 'english to morse':
    c = ''
    result = ''
    inp = input('\n')
    for i in range(int(len(str(inp)))):
        c = inp[i]
        j = -1
        found = False
        place = 0
        
        while not found:
            j = j + 1
            if c == english[j]:
                place = j
                found = True
        
        result = result + morse[place] + ' '

print(result)
