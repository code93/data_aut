import os
import shutil
import pandas as pd
import re
from decouple import config
import os
import time
# read file as pandas dataframe


file_path = "./"
words=[]
int_fields = ["State","County","StreetName","Building","LandmkName"]

for root, directories, files in os.walk(file_path):
   for name in files:
        file = os.path.join(root, name)
        if file.endswith("csv"):
            dataframe_cols = pd.read_csv(file,index_col=0, nrows=0).columns.tolist()
            for int_field in int_fields:
                if int_field in dataframe_cols and str(config(str(int_field)))=="true":
                    dataframe = pd.read_csv(file, usecols = [str(int_field)])
                    for word in dataframe[str(int_field)]:
                        sep_words= re.split(" ",str(word))
                        for w in sep_words:
                            words.append(str(w))
        # if file.endswith("csv") and str(config("names"))=="true":
        #     dataframe_cols = pd.read_csv(file,index_col=0, nrows=0).columns.tolist()
        #     if "name" in dataframe_cols:
        #         dataframe = pd.read_csv(file,usecols = ["name"])
        #         for word in dataframe["name"]:
        #                sep_words= re.split(" ",str(word))
        #                for w in sep_words:
        #                    words.append(str(w))

words = set(words)
text = "\n".join(w.lower()+" 1" for w in words if w !="")

if str(config("onlyone"))=="true":
    for int_field in int_fields:
        if str(config(str(int_field)))=="true":
            if os.path.isdir(str("./")+str(int_field)+"/") is False:
                os.mkdir(str("./")+str(int_field)+"/")

            with open(str("./")+str(int_field)+"/"+'block_words.txt', 'w') as f:
                f.write(text)
            with open(str("./")+str(int_field)+"/"+'block_words.txt') as f:
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

if str(config("onlyone"))=="false":
    t = time.time()
    int_field = "multiple"
    if os.path.isdir(str("./")+str(int_field)+"/") is False:
                os.mkdir(str("./")+str(int_field)+"/")

    with open(str("./")+str(int_field)+"/"+'block_words.txt', 'a') as f:
        f.write(text)
    with open(str("./")+str(int_field)+"/"+'block_words.txt') as f:
        words1 = f.readlines()
    with open("allow-list.txt") as g:
        words2 = g.readlines()
    
    removeword = set(words2).intersection(set(words1))
    remaining_words = set(words2)-removeword
    text1 = "".join(w.lower() for w in removeword if w !="")
    text2 = "".join(w.lower() for w in remaining_words if w !="")

    with open(str("./")+str(int_field)+"/"+'words_removed.txt', 'a') as f:
        f.write(text1)

    with open(str("./")+str(int_field)+"/"+'allow-list.txt', 'a') as f:
        f.write(text2)

if str(config("all"))=="true":
    t = time.time()
    int_field = "all"
    if os.path.isdir(str("./")+str(int_field)+"/") is False:
                os.mkdir(str("./")+str(int_field)+"/")
    with open(str("./")+str(int_field)+"/"+'block_words.txt', 'a') as f:
        f.write(text)
    with open(str("./")+str(int_field)+"/"+'block_words.txt') as f:
        words1 = f.readlines()
    with open("allow-list.txt") as g:
        words2 = g.readlines()
    
    removeword = set(words2).intersection(set(words1))
    remaining_words = set(words2)-removeword
    text1 = "".join(w.lower() for w in removeword if w !="")
    text2 = "".join(w.lower() for w in remaining_words if w !="")
    with open(str("./")+str(int_field)+"/"+'words_removed.txt', 'a') as f:
        f.write(text1)

    with open(str("./")+str(int_field)+"/"+'allow-list.txt', 'a') as f:
        f.write(text2)

# if str(config("names"))=="true":
#     int_field = "names"
#     if os.path.isdir(str("./")+str(int_field)+"/") is False:
#             os.mkdir(str("./")+str(int_field)+"/")

#     with open(str("./")+str(int_field)+"/"+'block_words.txt', 'w') as f:
#         f.write(text)
#     with open(str("./")+str(int_field)+"/"+'block_words.txt') as f:
#         words1 = f.readlines()
#     with open("allow-list.txt") as g:
#         words2 = g.readlines()
    
#     removeword = set(words2).intersection(set(words1))
#     remaining_words = set(words2)-removeword
#     text1 = "".join(w.lower() for w in removeword if w !="")
#     text2 = "".join(w.lower() for w in remaining_words if w !="")

#     with open(str("./")+str(int_field)+"/"+'words_removed.txt', 'w') as f:
#         f.write(text1)

#     with open(str("./")+str(int_field)+"/"+'allow-list.txt', 'w') as f:
#         f.write(text2)