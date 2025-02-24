from generate_public import (
    generate_public_dir,
    generate_pages_recursive
)
import os
import shutil


dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"



def main():
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    generate_public_dir(dir_path_static, dir_path_public)
    generate_pages_recursive(dir_path_content,
                            template_path,
                            dir_path_public,
)


if __name__ == "__main__":
    main()