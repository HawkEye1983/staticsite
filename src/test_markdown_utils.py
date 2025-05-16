import unittest

from textnode import BlockType
from markdown_utils import extract_markdown_images, extract_markdown_links, markdown_to_blocks, block_to_block_type, markdown_to_html_node

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

    def test_markdown_to_blocks(self):
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        result = markdown_to_blocks(markdown)
        self.assertListEqual(
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item",
            ],
            result
        )

    def test_block_to_block_type(self):
        block = "# Heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> Quote\n> Another quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- List\n- List"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        block = "1. List\n2. List"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        block = "Paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

class TestBlockMarkdown(unittest.TestCase):
    def test_paragraph(self):
        md = """
This is a **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is a <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that *should* remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that *should* remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )