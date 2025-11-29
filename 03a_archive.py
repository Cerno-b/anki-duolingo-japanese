from datetime import datetime
import shutil
import os

inpath = "duolingo.txt"
outpath = "duolingo_import.txt"
archive_dir = "archive"

today = datetime.today().strftime('%Y%m%d')

# copy input file to archive
inpath_archive = os.path.join(archive_dir, f"{today}_{inpath}")
shutil.copy(inpath, inpath_archive)

# move output file to archive
outpath_archive = os.path.join(archive_dir, f"{today}_{outpath}")
shutil.move(outpath, outpath_archive)
