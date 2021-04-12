from pathlib import Path

p = Path('/Users/Noname/Downloads')
for i in p.iterdir():
    if i in p.glob('*.mp3') or i in p.glob('*.ogg') or i in p.glob('*.waw') or i in p.glob('*.amr'):
        music = i
    elif i in p.glob('*.jpeg') or i in p.glob('*.png') or i in p.glob('*.jpn') or i in p.glob('*.svg'):
        photo = i
    elif i in p.glob('*.avi') or i in p.glob('*.mp4') or i in p.glob('*.mov') or i in p.glob('*.mkv'):
        films = i 
    elif i in p.glob('*.docx') or i in p.glob('*.txt') or i in p.glob('*.pdf') or i in p.glob('*.xlsx'):
        films = i            
      #DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX
    #if p.glob('*.mp3'):  
     #   print(txt_file)        
       