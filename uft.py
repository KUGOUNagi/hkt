import codecs
import sys

fin = codecs.open("untitled.txt", "r", "shift_jis")
fout_utf = codecs.open("utf-8.txt", "w", "uft-8")
for row in fin:
    fout_utf.write(row)
fin.close()
fout_utf.close()