from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprListener import ExprListener
from antlr4.tree.Trees import Trees
import graphviz

def create_parse_tree_dot(tree, parser):
    dot_tree = Trees.toStringTree(tree, None, parser)
    graph = graphviz.Digraph()
    labels = {}
    
    def add_node(node):
        nonlocal labels
        node_id = str(len(labels))
        labels[node_id] = str(node)
        graph.node(node_id, label=node.getText())
        return node_id
    
    def add_edges(parent_id, child):
        if child.getChildCount() == 0:
            child_id = add_node(child)
            graph.edge(parent_id, child_id)
        else:
            for i in range(child.getChildCount()):
                child_id = add_node(child.getChild(i))
                graph.edge(parent_id, child_id)
                add_edges(child_id, child.getChild(i))
    
    root_id = add_node(tree)
    add_edges(root_id, tree)
    
    return dot_tree, graph, labels

def main():
    input_stream = FileStream("input.txt")
    lexer = ExprLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ExprParser(token_stream)
    tree = parser.program()  # Replace `your_start_rule` with the actual start rule of your grammar
    
    # Generate parse tree visualization
    # dot_tree, graph, labels = create_parse_tree_dot(tree, parser)
    
    # Save the parse tree visualization as PNG
    # graph.render("parse_tree", format="png", cleanup=True)
    # print("Parse tree visualization saved as parse_tree.png")

    # print(Trees.toStringTree(tree, None, parser))
    listener = ExprListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)


if __name__ == '__main__':
    main()
