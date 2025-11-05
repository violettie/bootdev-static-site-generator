import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_creation(self):
        node = HTMLNode(tag="div", value="Hello", children=[], props=[("class", "container")])
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, [("class", "container")])

    def test_props_to_html_with_props(self):
        node = HTMLNode(props=[("id", "main"), ("class", "container")])
        expected_html = 'id="main" class="container"'
        self.assertEqual(node.props_to_html(), expected_html)

    def test_props_to_html_no_props(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")
    
    def test_repr(self):
        node = HTMLNode(tag="p", value="Paragraph", children=None, props=None)
        expected_repr = "HTMLNode(tag=p, value=Paragraph, children=None, props=None)"
        self.assertEqual(repr(node), expected_repr)
    