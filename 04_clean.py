from datetime import datetime
import shutil
import os

inpath = "duolingo.txt"
outpath = "duolingo_import.txt"

# create an empty file as a convenience for future entries
with open(inpath, "w", encoding="utf-8") as f:
    pass
    
os.remove(outpath)