import zipfile
import re
import os

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


print("Memproses zip...")
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

print(f"Selesai! File bersih tersimpan sebagai: {OUTPUT_ZIP}")
