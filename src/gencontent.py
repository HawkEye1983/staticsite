import os
from markdown_utils import markdown_to_html_node
from pathlib import Path

def generate_pages(dir_path_content, template_path, destination_dir_path, base):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        destination_path = os.path.join(destination_dir_path, filename)
        if os.path.isfile(from_path):
            destination_path = Path(destination_path).with_suffix(".html")
            generate_page(from_path, template_path, destination_path, base)
        else:
            generate_pages(from_path, template_path, destination_path, base)

def generate_page(from_path, template_path, destination_path, base):
    print(f" * {from_path} {template_path} -> {destination_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()
    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()
    node = markdown_to_html_node(markdown_content)
    html = node.to_html()
    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    template = template.replace('href="/', 'href="' + base)
    template = template.replace('src="/', 'src="', + base)
    destination_dir_path = os.path.dirname(destination_path)
    if destination_dir_path != "":
        os.makedirs(destination_dir_path, exist_ok=True)
    to_file = open(destination_path, "w")
    to_file.write(template)

def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No title found.")