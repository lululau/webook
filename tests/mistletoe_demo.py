from mistletoe import Document
from mistletoe.token import Token
from mistletoe.span_token import Link

def get_links(token: Token) -> list[Link]:
    if isinstance(token, Link):
        return [token]
    if "children" in vars(token):
        links = []
        for child in token.children:
            links.extend(get_links(child))
        return links
    return []


with open('links.md', 'r') as f:
    md = Document(f)
    for link in get_links(md):
        print(f"{link.target} -> {link.children[0].content}")