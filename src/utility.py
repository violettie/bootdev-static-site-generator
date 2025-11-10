import re

from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if type(old_node) != TextNode:
            new_nodes.append(old_node)
        else:
            if old_node.text.count(delimiter) % 2 != 0:
                raise ValueError("Not enough delimiters in text node to split.")
            
            while delimiter in old_node.text:
                first_index = old_node.text.find(delimiter)
                if first_index > 0:
                    new_nodes.append(TextNode(old_node.text[:first_index], TextType.PLAIN))
                
                second_index = old_node.text.find(delimiter, first_index + len(delimiter))
                new_nodes.append(TextNode(old_node.text[first_index + len(delimiter):second_index], text_type))
                
                old_node.text = old_node.text[second_index + len(delimiter):]

            if old_node.text:
                new_nodes.append(old_node)
    
    return new_nodes

def extract_markdown_images(text):
    results = []
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    results = re.findall(pattern, text)
    return results

def extract_markdown_links(text):
    results = []
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    results = re.findall(pattern, text)
    return results