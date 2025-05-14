import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node
from textnode import TextNode, TextType


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://boot.dev", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://boot.dev" target="_blank"')
    
    def test_empty_node(self):
        node = HTMLNode()
        self.assertEqual(repr(node), 'HTMLNode(Tag: None, Value: None, Children: [], Props: {})')

    def test_repr(self):
        node = HTMLNode(tag="Tag", value="Value", props={"href": "https://boot.dev"})
        self.assertEqual(repr(node), 'HTMLNode(Tag: Tag, Value: Value, Children: [], Props: {"href": "https://boot.dev"})')
    
class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_tag_prop(self):
        node = LeafNode("a", "Click here.", {"href": "https://boot.dev"})
        self.assertEqual(node.to_html(), '<a href="https://boot.dev">Click here.</a>')
    
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "No tag provided.")
        self.assertEqual(node.to_html(), "No tag provided.")
    
    def test_leaf_to_html_error(self):
        with self.assertRaises(ValueError):
            LeafNode("a", None)

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(), "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_value_error(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("i", "Italic text")])
    
    def test_to_html_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode("a", None)

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_normal(self):
        text_node = TextNode("This is normal", TextType.NORMAL)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "This is normal")
    
    def test_bold(self):
        text_node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<b>This is bold</b>")
    
    def test_italic(self):
        text_node = TextNode("This is italic", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<i>This is italic</i>")
    
    def test_code(self):
        text_node = TextNode("This is code", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<code>This is code</code>")
    
    def test_link(self):
        text_node = TextNode("This is a link", TextType.LINK, "https://boot.dev")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<a href="https://boot.dev">This is a link</a>')
    
    def test_img(self):
        text_node = TextNode("This is an image", TextType.IMAGE, "https://boot.dev/image.jpg")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<img src="https://boot.dev/image.jpg" alt="This is an image" />')

if __name__ == "__main__":
    unittest.main()