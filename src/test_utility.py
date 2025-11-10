import unittest

from textnode import TextNode, TextType
from utility import split_nodes_delimiter, extract_markdown_images, extract_markdown_links

class TestUtility(unittest.TestCase):
    def test_split_nodes_delimiter_bold(self):
        old_nodes = [
            "Some text ",
            TextNode("normal *bold* normal", TextType.PLAIN),
            " more text ",
        ]
        delimiter_bold = "*"

        expected_nodes = [
            "Some text ",
            TextNode("normal ", TextType.PLAIN),
            TextNode("bold", TextType.BOLD),
            TextNode(" normal", TextType.PLAIN),
            " more text ",
        ]

        result_nodes = split_nodes_delimiter(old_nodes, delimiter_bold, TextType.BOLD)

        self.assertEqual(result_nodes, expected_nodes)
        self.assertEqual(len(result_nodes), len(expected_nodes))

    def test_split_nodes_delimiter_italic(self):
        old_nodes = [
            TextNode("This is _italic_ text", TextType.PLAIN),
        ]
        delimiter = "_"

        expected_nodes = [
            TextNode("This is ", TextType.PLAIN),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.PLAIN),
        ]

        result_nodes = split_nodes_delimiter(old_nodes, delimiter, TextType.ITALIC)

        self.assertEqual(result_nodes, expected_nodes)
        self.assertEqual(len(result_nodes), len(expected_nodes))

    def test_split_nodes_delimiter_odd_delimiters(self):
        old_nodes = [
            TextNode("This is **bold text with one delimiter", TextType.PLAIN),
        ]
        delimiter = "**"

        with self.assertRaises(ValueError):
            split_nodes_delimiter(old_nodes, delimiter, TextType.BOLD)
        
    def test_split_nodes_delimiter_no_delimiters(self):
        old_nodes = [
            TextNode("This is normal text", TextType.PLAIN),
        ]
        delimiter = "**"

        expected_nodes = [
            TextNode("This is normal text", TextType.PLAIN),
        ]

        result_nodes = split_nodes_delimiter(old_nodes, delimiter, TextType.BOLD)

        self.assertEqual(result_nodes, expected_nodes)
        self.assertEqual(len(result_nodes), len(expected_nodes))

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://example.com)"
        )
        self.assertListEqual([("link", "https://example.com")], matches)