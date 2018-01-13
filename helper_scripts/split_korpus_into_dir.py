import os
from pathlib import Path

file_path = 'data/pap-all.txt'
contents = Path(file_path).read_text()

os.makedirs('data/pap-all', exist_ok=True)

for id, article in enumerate(contents.split("###")):
    f = open('data/pap-all/' + str(id) + '.txt','w')
    f.write(article)
    f.close()
