import os
import shutil

def copy_contents(source, destination):
    os.mkdir(destination)
    source_contents = os.listdir(source)
    for item in source_contents:
        source_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)
        if os.path.isfile(source_path):
            shutil.copy(source_path, destination_path)
        else:
            copy_contents(source_path, destination_path)