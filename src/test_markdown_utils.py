import unittest

from markdown_utils import extract_markdown_images, extract_markdown_links

class TestMarkdownUtils(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is text with a link to [boot.dev](https://boot.dev)")
        self.assertListEqual([("boot.dev", "https://boot.dev")], matches)
    
    def test_extract_markdown_images_without_image(self):
        matches = extract_markdown_images("This is text without an image")
        self.assertListEqual([], matches)
    
    def test_extract_markdown_links_without_links(self):
        matches = extract_markdown_links("This is text without a link")
        self.assertListEqual([], matches)