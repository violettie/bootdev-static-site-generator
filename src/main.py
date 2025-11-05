from textnode import TextNode
from textnode import TextType

print("hello world")

def main():
    text_node = TextNode("Sample Text", TextType.BOLD, None)
    print(text_node.__repr__())

if __name__ == "__main__":
    main()