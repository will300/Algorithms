class binode:
    def __init__(self, data):
        self.node1 = None
        self.node2 = None
        self.data = data

class binode_object:

    def __init__(self, head_value, object_type="bst"):
        self.head = binode(head_value)
        self.type = object_type
        
    def __repr__(self):
        if self.type == "bst":

            next_layer_nodes = [self.head]
            print_str = ""
            while len(next_layer_nodes):
                layer_nodes = next_layer_nodes
                next_layer_nodes = []
                print_values = []
                for node in layer_nodes:
                    print_values.append(str(node.data))
                    if node.node1: next_layer_nodes.append(node.node1)
                    if node.node2: next_layer_nodes.append(node.node2)
                print_str += " ".join(print_values) + "\n"
            return print_str

        elif self.type == "llist":

            print_str = str(self.head.data)
            node = self.head
            while node.node2:
                node = node.node2
                print_str += " " + str(node.data)
            return print_str

        else:
            raise ValueError("Invalid object type")


    def bst2llist(self, node=None, tail=None):
        self.type = "llist"
        # ------------------------- #
        if not node:
            node = self.head
        # ------------------------- #

        if not node.node1 and not node.node2:
            if not tail:
                self.head = node
            else:
                tail.node2 = node
                node.node1 = tail 
            return node 

        if node.node1 and node.node2:
            tail = self.bst2llist(node.node1, tail)
            node.node1 = tail
            tail.node2 = node  
            return self.bst2llist(node.node2, node)       

        if node.node1:
            tail = self.bst2llist(node.node1, tail)
            node.node1 = tail
            tail.node2 = node
            return node

        if node.node2:
            if not tail:
                self.head = node
            else:
                node.node1 = tail
                tail.node2 = node              
            return self.bst2llist(node.node2, node)            
   
 
tree = binode_object(4, "bst")
tree.head.node1 = binode(2)
tree.head.node2 = binode(5)
node = tree.head.node1
node.node1 = binode(1)
node.node2 = binode(3)
node.node1.node1 = binode(0)
tree.head.node2.node2 = binode(6)

print(tree)

tree.bst2llist()

print(tree)








