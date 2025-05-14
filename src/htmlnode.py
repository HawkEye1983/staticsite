from textnode import TextNode, TextType

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
    
    def to_html(self):
        raise NotImplementedError("This should be implemented by subclasses.")

    def props_to_html(self):
        return ''.join(f' {key}="{value}"' for key, value in self.props.items())
    
    def __repr__(self):
        props_str = '{' + ', '.join(f'"{key}": "{value}"' for key, value in self.props.items()) + '}'
        return f"HTMLNode(Tag: {self.tag}, Value: {self.value}, Children: {self.children}, Props: {props_str})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode must have a value")
        super().__init__(tag=tag, value=value, children=None, props=props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if self.tag is None:
            return self.value
        else:
            props_str = self.props_to_html()
            if self.tag == "img":
                return f"<{self.tag}{props_str} />"
            return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"