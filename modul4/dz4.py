from pathlib import Path

p = Path('/Users/Noname/Downloads')
music = list()
photo = list()
films = list() 
docs = list() 
archive = list() 
unidentified = list() 
for i in p.iterdir():
    if i in p.glob('*.mp3') or i in p.glob('*.ogg') or i in p.glob('*.waw') or i in p.glob('*.amr'):
        music.append(i)
        
    elif i in p.glob('*.jpeg') or i in p.glob('*.png') or i in p.glob('*.jpn') or i in p.glob('*.svg'):
        photo.append(i)
       
    elif i in p.glob('*.avi') or i in p.glob('*.mp4') or i in p.glob('*.mov') or i in p.glob('*.mkv'):
        films.append(i)
    elif i in p.glob('*.docx') or i in p.glob('*.txt') or i in p.glob('*.pdf') or i in p.glob('*.xlsx') or i in p.glob('*.pptx'):
        docs.append(i)
       
    elif i in p.glob('*.zip') or i in p.glob('*.gz') or i in p.glob('*.tar'):
        archive.append(i)
                
    else:
        unidentified.append(i)
        

print(music)
print(photo)
print(films)
print(docs)
print(archive)
print(unidentified)
       