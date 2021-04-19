
def normalize(line):
    letters = "qwertyuiopasdfghjklzxcvbnm"
    LETTERS = "QWERTYUIOPASDFGHJKLZXCVBNM"
    numbers = "0123456789"
    translated = ""
    map = {ord('а'): 'a', ord('б'): 'b',ord('в'): 'v', ord('г'): 'g',ord('д'): 'd', ord('е'): 'e',ord('ё'): 'e', 
    ord('ж'): 'zh',ord('з'): 'z', ord('и'): 'i',ord('й'): 'i', ord('к'): 'k',ord('л'): 'l', ord('м'): 'm',
    ord('н'): 'n', ord('о'): 'o',ord('п'): 'p', ord('р'): 'r',ord('с'): 's', ord('т'): 't',ord('у'): 'u', 
    ord('ф'): 'f',ord('х'): 'kh', ord('ц'): 'tc',ord('ч'): 'ch', ord('ш'): 'sh', ord('щ'): 'shch',ord('ъ'): '', 
    ord('ы'): 'y',ord('ь'): '', ord('э'): 'e',ord('ю'): 'iu', ord('я'): 'ia',
    ord('А'): 'A', ord('Б'): 'B',ord('В'): 'V', ord('Г'): 'G',ord('Д'): 'D', ord('Е'): 'E',ord('Ё'): 'E', 
    ord('Ж'): 'ZH',ord('З'): 'Z', ord('И'): 'I',ord('Й'): 'I', ord('К'): 'K',ord('Л'): 'L', ord('М'): 'M',
    ord('Н'): 'N', ord('О'): 'O',ord('П'): 'P', ord('Р'): 'R',ord('С'): 'S', ord('Т'): 'T',ord('У'): 'U', 
    ord('Ф'): 'F',ord('Х'): 'KH', ord('Ц'): 'TC',ord('Ч'): 'CH', ord('Ш'): 'SH', ord('Щ'): 'SHCH',ord('Ъ'): '', 
    ord('Ы'): 'Y',ord('Ь'): '', ord('Э'): 'E',ord('Ю'): 'IU', ord('Я'): 'IA'}
    
    
    for l in line:
        if ord(l) in map:
           # print(l)
            translated += l.translate(map)
        elif (l in letters) or (l in LETTERS) or (l in numbers):
            translated += l
        else:
            translated += "_"    
    print(translated)


n = str(input('введите строку для транслитерации кириллических символов на латиницу: '))
normalize(n)    