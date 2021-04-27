from pathlib import Path
import shutil, pathlib
import re

def add_files_to_order(p):
    """
    создание папок
    """
    Path.mkdir(Path('/Users/Noname/Downloads/music'))
    Path.mkdir(Path('/Users/Noname/Downloads/photo'))
    Path.mkdir(Path('/Users/Noname/Downloads/films')) 
    Path.mkdir(Path('/Users/Noname/Downloads/docs')) 
    Path.mkdir(Path('/Users/Noname/Downloads/archive')) 
    Path.mkdir(Path('/Users/Noname/Downloads/unidentified')) 
   
    for l in p.iterdir():
        i= (l.name)
        #print(i)
        if l.suffix == '.mp3' or l.suffix == '.ogg' or l.suffix == '.wav' or l.suffix == '.amr':
            
            Path(f'{p}/{i}').rename(f'{p}/music/{normalize(i)}')
            
        elif l.suffix == '.jpeg' or l.suffix == '.png' or l.suffix == '.jpg' or l.suffix == '.svg':
            
            Path(f'{p}/{i}').rename(f'{p}/photo/{normalize(i)}')
        
        elif l.suffix == '.avi' or l.suffix == '.mp4' or l.suffix == '.mov' or l.suffix == '.mkv':
            
            Path(f'{p}/{i}').rename(f'{p}/films/{normalize(i)}')
        elif l.suffix == '.docx' or l.suffix == '.txt' or l.suffix == '.pdf' or l.suffix == '.xlsx' or l.suffix == '.pptx':
            
            Path(f'{p}/{i}').rename(f'{p}/docs/{normalize(i)}')
        
        elif l.suffix == '.zip' or l.suffix == '.gz' or l.suffix == '.tar':
            Path(f'{p}/{i}').rename(f'{p}/archive/{i}') 
            new_folder = re.findall('\w+[^\.]+', i)         #создала папку для распаковки архива
            Path.mkdir(Path(f'{p}/archive/{new_folder[0]}'))  #создала папку для распаковки архива
            print(l.name)
            print(new_folder[0])
            shutil.unpack_archive(i, new_folder[0])  # распаковка архива-не удалась            
        elif l.name != 'music' and l.name != 'photo' and l.name != 'docs' and l.name != 'archive' and l.name != 'films' and l.name != 'unidentified' and l.name != '.DS_Store':    
            try:
                path = pathlib.Path(f'{p}/{l.name}') #удвление пустых
                path.rmdir()  
            except OSError:     
                continue
        else:
            if l.name != 'music' and l.name != 'photo' and l.name != 'docs' and l.name != 'archive' and l.name != 'films' and l.name != 'unidentified' and l.name != '.DS_Store':
                
                Path(f'{p}/{i}').rename(f'{p}/unidentified/{i}')
               
            
            

def normalize(line):
    letters = "qwertyuiopasdfghjklzxcvbnm"
    LETTERS = "QWERTYUIOPASDFGHJKLZXCVBNM"
    numbers = "0123456789."
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
        elif (l in letters) or (l in LETTERS) or (l in numbers) :
            translated += l
        else:
            translated += "_"   
    return translated


print(add_files_to_order(Path('/Users/Noname/Downloads')))


       