import codecs

fin = codecs.open("untitled.txt", "r", "uft-8")
fout_utf = codecs.open("utf-8.txt", "w", "shift_jis")
for row in fin:
    fout_utf.write(row)
fin.close()
fout_utf.close()