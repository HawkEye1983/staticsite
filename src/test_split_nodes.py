import unittest

from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_bold_delimiter(self):
        node = TextNode("This is **bold** text", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("This is ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.NORMAL),
        ])
    
    def test_split_italic_delimiter(self):
        node = TextNode("This is *italic* text", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(new_nodes, [
            TextNode("This is ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.NORMAL),
        ])
    
    def test_split_code_delimiter(self):
        node = TextNode("This is `code block` text", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" text", TextType.NORMAL),
        ])
    
    def test_no_delimiter_bold(self):
        node = TextNode("This is no delimiter", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [node])
    
    def test_no_delimiter_code(self):
        node = TextNode("This is no delimiter", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [node])