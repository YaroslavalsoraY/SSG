from enum import Enum
from htmlnode import (
    HTMLNode, LeafNode, ParentNode
)
from text_to_textnodes import text_to_textnodes
from textnode import text_node_to_html_node

class BlockType(Enum):
    PARAGRAPH = "parag"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "blockquote"
    UNORDERED_LIST = "un_lst"
    ORDERED_LIST = "ord_lst"


def markdown_to_blocks(markdown):
    result_lst = markdown.split("\n\n")
    for i in range(len(result_lst)):
        result_lst[i] = result_lst[i].strip()
    for c in range(result_lst.count("")):
        result_lst.remove("")
    return result_lst


def block_to_block_type(markdown: str):
    if markdown.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if markdown.startswith("```") and markdown.endswith("```"):
        return BlockType.CODE
    if markdown.startswith(">"):
        return BlockType.QUOTE
    if markdown.startswith("*") or markdown.startswith("-"):
        return BlockType.UNORDERED_LIST
    if markdown.startswith("1."):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        html_nodes.append(html_node)
    return html_nodes


def paragraph_to_htmlnode(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def heading_to_htmlnode(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    return ParentNode(f"h{level}", text_to_children(block[level+1:].lstrip()))


def code_to_htmlnode(block):
    node = ParentNode("code", text_to_children(block[4:-3]))
    return ParentNode("pre", [node])


def olist_to_htmlnode(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def ulist_to_htmlnode(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def quote_to_htmlnode(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_htmlnode(block)
    if block_type == BlockType.HEADING:
        return heading_to_htmlnode(block)
    if block_type == BlockType.CODE:
        return code_to_htmlnode(block)
    if block_type == BlockType.QUOTE:
        return quote_to_htmlnode(block)
    if block_type == BlockType.ORDERED_LIST:
        return olist_to_htmlnode(block)
    if block_type == BlockType.UNORDERED_LIST:
        return ulist_to_htmlnode(block)
    raise ValueError("Invalid block type")


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children_lst = []
    for block in blocks:
        node = block_to_html_node(block)
        children_lst.append(node)
    return ParentNode("div", children_lst, None)
