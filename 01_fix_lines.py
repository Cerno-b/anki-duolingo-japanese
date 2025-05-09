import re

inoutpath = "duolingo.txt"

with open(inoutpath, encoding="utf-8") as f:
    text = f.read().strip()
    
text = re.sub(r"([^\r?\n]+)\r?\n\r?\n([^\r?\n]+)", r"\1;\2", text)

with open(inoutpath, "w", encoding="utf-8") as f:
    f.write(text)