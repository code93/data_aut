import os

int_field="names"

if os.path.isdir(str("./")+str(int_field)+"/") is False:
    os.mkdir(str("./")+str(int_field)+"/")

with open('block-list names.txt') as f:
    words1 = f.readlines()
with open("allow-list.txt") as g:
    words2 = g.readlines()

removeword = set(words2).intersection(set(words1))
remaining_words = set(words2)-removeword
text1 = "".join(w.lower() for w in removeword if w !="")
text2 = "".join(w.lower() for w in remaining_words if w !="")

with open(str("./")+str(int_field)+"/"+'words_removed.txt', 'w') as f:
    f.write(text1)

with open(str("./")+str(int_field)+"/"+'allow-list.txt', 'w') as f:
    f.write(text2)