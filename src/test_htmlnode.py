import unittest

from htmlnode import HTMLNode

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

if __name__ == "__main__":
    unittest.main()