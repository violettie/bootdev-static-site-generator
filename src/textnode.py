from enum import Enum
from leafnode import LeafNode

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.PLAIN:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("strong", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, [("href", text_node.url)])
        case TextType.IMAGE:
            return LeafNode("img", None, [("src", text_node.url), ("alt", text_node.text)])
        case _:
            raise ValueError("Unknown TextType")

class TextType(Enum):
    PLAIN = 1
    BOLD = 2
    ITALIC = 3
    CODE = 4
    LINK = 5
    IMAGE = 6

class TextNode():
    def __init__(self, text, text_type, url=None):        
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(text_node1, text_node2):
        return (text_node1.text == text_node2.text and
                text_node1.text_type == text_node2.text_type and
                text_node1.url == text_node2.url)
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
