from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = None
    BOLD = "b"
    ITALIC = "i"
    CODE = "code"
    LINK = "a"
    IMAGE = "img"


class TextNode():
    def __init__(self, text, text_type: TextType, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, value):
        if (self.text == value.text) and (self.text_type == value.text_type) and (self.url == value.url):
            return True
        else:
            return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    

def text_node_to_html_node(text_node: TextNode):
    tag = text_node.text_type.value
    if tag == "a":
        return LeafNode(tag, text_node.text, {"href": text_node.url})
    if tag == "img":
        return LeafNode(tag, '', props= {"src": text_node.url, "alt": text_node.text})
    return LeafNode(tag, text_node.text)
