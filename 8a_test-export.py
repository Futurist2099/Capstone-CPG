import os
import shutil

dest_folder = r"c:/legalzoom"

source_file = "status_report.txt"


destination_path = os.path.join(dest_folder, os.path.basename(source_file))

shutil.copy2(source_file, destination_path)

print(f"\nDone! employee(s) list backed up to C:/legalzoom")


