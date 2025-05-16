import os
import shutil
import sys
from utility.copy_static_dir import copy_contents
from gencontent import generate_pages

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"
default_basepath = "/"

def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    if not os.path.exists(dir_path_static):
        raise Exception(f"Source {dir_path_static} does not exist.")
    if os.path.exists(dir_path_public):
        print(f"Destination {dir_path_public} already exists. Removing...")
        shutil.rmtree(dir_path_public)
    copy_contents(dir_path_static, dir_path_public)
    print("Generating content.")
    generate_pages(dir_path_content, template_path, dir_path_public, basepath)

if __name__ == "__main__":
    main()