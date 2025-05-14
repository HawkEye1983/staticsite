import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_noteq(self):
        node = TextNode("This tests not equal", TextType.BOLD)
        node2 = TextNode("This tests not equal", TextType.NORMAL)
        self.assertNotEqual(node, node2)
    
    def test_ne2(self):
        node = TextNode("Equal", TextType.NORMAL)
        node2 = TextNode("Not equal", TextType.ITALIC)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()