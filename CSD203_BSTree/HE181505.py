class Bird:
    def __init__(self, xType, xRate, xWing):
        self.type = xType
        self.rate = xRate
        self.wing = xWing

class BSTree:
    def __init__(self):
        self.root = None

    def f0(self):
        return "He181505"

    def insert(self, xType, xRate, xWing):
        if xType[0] == 'B' or xRate > 10:
            return
        new_bird = Bird(xType, xRate, xWing)
        if self.root is None:
            self.root = new_bird
        else:
            self._insert_helper(self.root, new_bird)

    def _insert_helper(self, current, new_bird):
        if new_bird.rate < current.rate:
            if current.left is None:
                current.left = new_bird
            else:
                self._insert_helper(current.left, new_bird)
        else:
            if current.right is None:
                current.right = new_bird
            else:
                self._insert_helper(current.right, new_bird)

    def f1(self):
        self.insert("A", 5, 9)
        self.insert("E", 2, 5)
        self.insert("D", 8, 6)
        self.insert("F", -6, 7)
        self.insert("X", 4, 5)
        self.insert("Y", 6, -7)
        self.in_order(self.root)

    def f2(self):
        self.pre_order_with_wing_range(self.root, 4, 10)

    def f3(self):
        self.breadth_first_odd_nodes(self.root)

    def f4(self):
        self.post_order_wing_rate(self.root, 4, 6)

    def f5(self):
        self.in_order_with_type(self.root, 'A', 'C')

    def f6(self):
        pass

    def f7(self):
        pass

    def f8(self):
        pass

    def f9(self):
        pass

    def f10(self):
        pass

    def f11(self):
        pass

    def pre_order_with_wing_range(self, node, min_wing, max_wing):
        if node is not None:
            if min_wing <= node.wing <= max_wing:
                print(f"({node.type},{node.rate},{node.wing})", end=" ")
            self.pre_order_with_wing_range(node.left, min_wing, max_wing)
            self.pre_order_with_wing_range(node.right, min_wing, max_wing)

    def breadth_first_odd_nodes(self, root):
        if root is None:
            return
        queue = [root]
        odd_position = True
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.pop(0)
                if odd_position:
                    print(f"({node.type},{node.rate},{node.wing})", end=" ")
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            odd_position = not odd_position

    def post_order_wing_rate(self, node, max_wing, min_rate):
        if node is not None:
            self.post_order_wing_rate(node.left, max_wing, min_rate)
            self.post_order_wing_rate(node.right, max_wing, min_rate)
            if node.wing <= max_wing and node.rate > min_rate:
                print(f"({node.type},{node.rate},{node.wing})", end=" ")

    def in_order_with_type(self, node, start_char, end_char):
        if node is not None:
            self.in_order_with_type(node.left, start_char, end_char)
            if node.type[0] == start_char or node.type[0] == end_char:
                print(f"({node.type},{node.rate},{node.wing})", end=" ")
            self.in_order_with_type(node.right, start_char, end_char)
