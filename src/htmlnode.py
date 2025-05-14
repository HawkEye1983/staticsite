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