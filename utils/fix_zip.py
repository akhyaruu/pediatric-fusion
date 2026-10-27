# Used for kaggel dataset import

# Removing spaces: File names such as 101.1 App_M.bmp will be changed to 101.1_App_M.bmp (spaces are replaced by underscores).
# Removing strange symbols: Characters such as ä, ü, or quotation marks, which often cause confusion for Python libraries will be removed.
# Removing the leading folder name: If the ZIP file contains a folder such as US_Pictures/ or US_Pictures_kaggle_ready/, this code will strip that folder name.

# Run through "python fix_zip.py"

import zipfile
import re

INPUT_ZIP = "US_Pictures.zip"
OUTPUT_ZIP = "US_Pictures_kaggle_ready.zip"

def clean_filename(filename):
    filename = filename.strip()
    filename = filename.replace(" ", "_")
    filename = re.sub(r"[^a-zA-Z0-9_\-\./]", "", filename)

    if filename.startswith("US_Pictures/"):
        filename = filename.replace("US_Pictures/", "", 1)
    elif filename.startswith("US_Pictures_kaggle_ready/"):
        filename = filename.replace("US_Pictures_kaggle_ready/", "", 1)

    return filename

print("Processing zip...")
with zipfile.ZipFile(INPUT_ZIP, "r") as zin:
    with zipfile.ZipFile(OUTPUT_ZIP, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            if item.is_dir():
                continue

            new_name = clean_filename(item.filename)

            if new_name.startswith("__MACOSX") or new_name.endswith(".DS_Store"):
                continue

            with zin.open(item) as f:
                zout.writestr(new_name, f.read())

print(f"Done! The clean file is saved as: {OUTPUT_ZIP}")
