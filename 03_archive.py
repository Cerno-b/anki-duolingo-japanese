from datetime import datetime
import shutil
import os

inpath = "duolingo.txt"
outpath = "duolingo_import.txt"
archive_dir = "archive"

today = datetime.today().strftime('%Y%m%d')

# move input file to archive
inpath_archive = os.path.join(archive_dir, f"{today}_{inpath}")
shutil.move(inpath, inpath_archive)

# move output file to archive
outpath_archive = os.path.join(archive_dir, f"{today}_{outpath}")
shutil.move(outpath, outpath_archive)

# create an empty file as a convenience for future entries
with open(inpath, "w", encoding="utf-8") as f:
    pass