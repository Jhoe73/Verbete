import os
filePath = '../word/migrations/words.txt'

if os.path.exists(filePath):
    os.remove(filePath)

f = open("br-sem-acentos.txt", "r")
nf = open("../word/migrations/words.txt", "a")

for w in f:
    if len(w) == 6 and w.islower():
        nf.write(w)

f.close()
nf.close()


