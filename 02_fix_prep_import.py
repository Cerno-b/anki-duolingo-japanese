inpath = "duolingo.txt"
outpath = "duolingo_import.txt"

outtext = ""

with open(inpath, encoding="utf-8") as f:
    for idx, line in enumerate(f.readlines()):
        line = line.strip()
        if line:
            parts = line.split(";")
            if len(parts) == 2:
                front, back = parts
                outtext += f"{front};{back};front\n"
                outtext += f"{back};{front};back\n"
            elif len(parts) == 3:
                front, back, hiragana = parts
                outtext += f"{front};{back}<br>{hiragana};front\n"
                outtext += f"{back};{front}<br>{hiragana};back\n"
            else:
                print(f"Error in line {idx}: element count not 2 or 3")

with open(outpath, "w", encoding="utf-8") as f:
    f.write(outtext)