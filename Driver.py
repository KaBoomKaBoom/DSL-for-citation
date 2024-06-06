from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprListener import ExprListener
from antlr4.tree.Trees import Trees
import graphviz

def to_dot(tree, parser):
    """
    Converts the parse tree to DOT format.
    """
    def escape(label):
        return label.replace('"', '\\"')

    def node_name(node):
        return f"node{node.getRuleIndex()}_{node.getText()}"

    def walk_tree(node, dot, parent=None):
        node_label = escape(Trees.getNodeText(node, parser.ruleNames))
        node_id = id(node)

        if parent:
            dot.edge(str(id(parent)), str(node_id))

        dot.node(str(node_id), node_label)

        for child in range(node.getChildCount()):
            walk_tree(node.getChild(child), dot, node)

    dot = graphviz.Digraph()
    walk_tree(tree, dot)
    return dot

def main():
    input_stream = FileStream("input.txt")
    lexer = ExprLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ExprParser(token_stream)
    tree = parser.program()  # Replace `program` with the actual start rule of your grammar

    # Print the parse tree in LISP-style notation
    print(Trees.toStringTree(tree, None, parser))

    # Generate and render the DOT file
    dot = to_dot(tree, parser)
    dot.render("parse_tree", format="png", view=True)  # This will create and open the parse tree image

    # Optionally walk the tree with a listener
    listener = ExprListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == '__main__':
    main()
