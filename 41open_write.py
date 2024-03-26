file = "frnd.txt"

fo = open(file, 'r')
old = fo.read()
fo.close()

f1 = open(file, 'a')
new = old.replace('sreeni', 'vasan')
f1.write(new)
f1.close()