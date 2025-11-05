import unittest

from leafnode import LeafNode
from parentnode import ParentNode

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
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_no_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()
        
    def test_to_html_no_children(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    def test_to_html_empty_children(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")

    def test_to_html_multiple_children(self):
        child1 = LeafNode("p", "First paragraph.")
        child2 = LeafNode("p", "Second paragraph.")
        parent_node = ParentNode("div", [child1, child2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><p>First paragraph.</p><p>Second paragraph.</p></div>",
        )

    def test_to_html_nested_structure(self):
        grandchild1 = LeafNode("i", "italic text")
        grandchild2 = LeafNode("b", "bold text")
        child = ParentNode("p", [grandchild1, grandchild2])
        parent_node = ParentNode("div", [child])
        self.assertEqual(
            parent_node.to_html(),
            "<div><p><i>italic text</i><b>bold text</b></p></div>",
        )

    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], props=[("class", "container")])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_deeply_nested(self):
        level3 = LeafNode("em", "deep text")
        level2 = ParentNode("span", [level3])
        level1 = ParentNode("p", [level2])
        root = ParentNode("div", [level1])
        self.assertEqual(
            root.to_html(),
            "<div><p><span><em>deep text</em></span></p></div>",
        )