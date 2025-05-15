import unittest

from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link

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

class TestSplitNodesImage(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.NORMAL),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.NORMAL),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_split_image(self):
        node = TextNode(
            "This is a text with one ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is a text with one ", TextType.NORMAL),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes
        )
    
    def test_split_image_no_image(self):
        node = TextNode("This is text with no images.", TextType.NORMAL)
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes, [node])

class TestSplitNodesLink(unittest.TestCase):
    def test_split_link(self):
        node = TextNode("This is text with a link to [boot.dev](https://boot.dev)", TextType.NORMAL)
        new_node = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link to ", TextType.NORMAL),
                TextNode("boot.dev", TextType.LINK, "https://boot.dev"),
            ],
            new_node
        )
    
    def test_split_links(self):
        node = TextNode("This is text with a link to [boot.dev](https://boot.dev) and [google.com](http://www.google.com)", TextType.NORMAL)
        new_node = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link to ", TextType.NORMAL),
                TextNode("boot.dev", TextType.LINK, "https://boot.dev"),
                TextNode(" and ", TextType.NORMAL),
                TextNode("google.com", TextType.LINK, "http://www.google.com"),
            ],
            new_node
        )