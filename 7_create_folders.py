import os
import time

def create_multi_dirs():
    path = "C:\\legalzoom"
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created folder: {path}")

    print(f"Exporting results to folder: {path}")
    time.sleep(5)

    my_dirs = ["dir1"]

    for dirs in my_dirs:
       
        if not os.path.exists(dirs):
            os.mkdir(dirs)
            print("Directory created!")
        else:
            print(f"{dirs} already exists, skipping.")
    print("Directory created!")

create_multi_dirs();