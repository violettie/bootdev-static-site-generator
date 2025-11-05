import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("Example", TextType.ITALIC, "http://example.com")
        expected_repr = "TextNode(Example, 3, http://example.com)"
        self.assertEqual(repr(node), expected_repr)

    def test_url_none(self):
        node = TextNode("No URL", TextType.PLAIN)
        expected_repr = "TextNode(No URL, 1, None)"
        self.assertEqual(repr(node), expected_repr)

    def test_different_nodes(self):
        node1 = TextNode("Text 1", TextType.CODE)
        node2 = TextNode("Text 2", TextType.CODE)
        self.assertNotEqual(node1, node2)

    def test_text_node_to_html_node_plain(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_text_node_to_html_node_bold(self):
        node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "strong")
        self.assertEqual(html_node.value, "Bold text")

    def test_text_node_to_html_node_link(self):
        node = TextNode("Link text", TextType.LINK, "http://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Link text")
        self.assertIn(("href", "http://example.com"), html_node.props)

    def test_text_node_to_html_node_image(self):
        node = TextNode("Image alt text", TextType.IMAGE, "http://example.com/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertIsNone(html_node.value)
        self.assertIn(("src", "http://example.com/image.png"), html_node.props)
        self.assertIn(("alt", "Image alt text"), html_node.props)
    
    def test_text_node_to_html_node_unknown(self):
        node = TextNode("Unknown", None)
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)
    
    def test_text_node_to_html_node_italic(self):
        node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic text")

    def test_text_node_to_html_node_code(self):
        node = TextNode("Code text", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "Code text")

    def test_text_node_to_html_node_image_no_alt(self):
        node = TextNode("", TextType.IMAGE, "http://example.com/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertIsNone(html_node.value)
        self.assertIn(("src", "http://example.com/image.png"), html_node.props)
        self.assertIn(("alt", ""), html_node.props)

    def test_text_node_to_html_node_link_no_url(self):
        node = TextNode("Link text", TextType.LINK)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Link text")
        self.assertIn(("href", None), html_node.props)
    
    def test_text_node_to_html_node_empty_text(self):
        node = TextNode("", TextType.PLAIN)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "")

    def test_text_node_to_html_node_special_characters(self):
        node = TextNode("<>&\"", TextType.PLAIN)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "<>&\"")


if __name__ == "__main__":
    unittest.main()