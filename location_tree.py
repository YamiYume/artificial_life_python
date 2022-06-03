from organism import Organism


class Node:
    def __init__(self, organism: Organism, kind: int) -> None:
        self.kind = kind
        self.key = organism.coordinates[kind]
        self.value = [organism]
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1

    def append(self, organism):
        self.value.append(organism)


class RBtree():
    def __init__(self, kind):
        self.kind = kind
        self.root = None

    def insert_organism(self, organism):
        if self.root is None:
            self.root = Node(organism, self.kind)
            self.root.color = 0
            return

        try:
            self.search_key(organism.coordinates[self.kind], self.root). \
                append(organism)

        except KeyError:
            new_node = Node(organism, self.kind)

            x = self.root
            y = None
            while x is not None:
                if new_node.key > x.key:
                    y = x
                    x = x.right
                else:
                    y = x
                    x = x.left

            new_node.parent = y
            if new_node.key > y.key:
                y.right = new_node
            else:
                y.left = new_node

            if new_node.parent is None:
                return

            if new_node.parent.parent is None:
                return

            try:
                self.fixInsert(new_node)
            except AttributeError:
                pass

    def LR(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def RR(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def fixInsert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.RR(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.LR(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.LR(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.RR(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    def search_key(self, key, subtree):
        if self.root is None:
            raise KeyError

        if subtree is None:
            raise KeyError

        if key == subtree.key:
            return subtree
        elif key < subtree.key:
            return self.search_key(key, subtree.left)
        else:
            return self.search_key(key, subtree.right)

        raise KeyError
