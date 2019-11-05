"""
# TIME SHOVELING CODES

def make_new(root: Node, dummy: Node):
    if not dummy:
        return
    if dummy.left:
        tmp_left = Node(dummy.left.y, dummy.left.x, dummy.left.val)
        push(tmp_left, root)
    if dummy.right:
        tmp_right = Node(dummy.right.y, dummy.right.x, dummy.right.val)
        push(tmp_right, root)

    make_new(root, dummy.left)
    make_new(root, dummy.right)



def push(nd: Node, root: Node):
    ry, rx = root.y, root.x
    ny, nx = nd.y, nd.x
    root_changed = False
    if ry == 100001:
        if ny > root.left.y or ny > root.right.y:
            # TODO : Rearrange
            make_new(nd, root)
            return nd
    if ry < ny:
        root_changed = True
        if rx < nx:
            nd.left = root
        else:
            nd.right = root
    elif ry > ny:
        if rx < nx:
            if not root.right:
                root.right = nd
            else:
                root.right = push(nd, root.right)
        else:
            if not root.left:
                root.left = nd
            else:
                root.left = push(nd, root.left)
    else:
        dummy = Node(100001, 100001, None)
        if nx < rx:
            dummy.left = nd
            dummy.right = root
        else:
            dummy.left = root
            dummy.right = nd
        return dummy

    if root_changed:
        return nd
    else:
        return root


def preorder(root: Node, ret: []):
    if not root:
        return
    ret.append(root.val)
    preorder(root.left, ret)
    preorder(root.right, ret)


def postorder(root: Node, ret: []):
    if not root:
        return
    postorder(root.left, ret)
    postorder(root.right, ret)
    ret.append(root.val)


def solution(nodeinfo):
    answer = []
    root = Node(nodeinfo[0][1], nodeinfo[0][0], 1)
    for i in range(1, len(nodeinfo)):
        nd = nodeinfo[i]
        node = Node(nd[1], nd[0], i+1)
        root = push(node, root)
    pre, post = [], []
    preorder(root, pre)
    postorder(root, post)
    answer.append(pre)
    answer.append(post)
    return answer
"""
import sys
sys.setrecursionlimit(10**6)


class Node:
    def __init__(self, y: int, x: int, val: int):
        self.y = y
        self.x = x
        self.val = val
        self.left = None
        self.right = None


def push(nd: Node, root: Node):
    ry, rx = root.y, root.x
    ny, nx = nd.y, nd.x
    if rx < nx:
        if not root.right:
            root.right = nd
        else:
            root.right = push(nd, root.right)
    else:
        if not root.left:
            root.left = nd
        else:
            root.left = push(nd, root.left)
    return root


def preorder(root: Node, ret: list):
    if not root:
        return
    ret.append(root.val)
    preorder(root.left, ret)
    preorder(root.right, ret)


def postorder(root: Node, ret: list):
    if not root:
        return
    postorder(root.left, ret)
    postorder(root.right, ret)
    ret.append(root.val)


def solution(nodeinfo):
    if len(nodeinfo) == 1:
        return [[1], [1]]
    nodeinfo = [li + [idx+1] for idx, li in enumerate(nodeinfo)]
    nodeinfo.sort(key=lambda li: li[1], reverse=True)
    depth = []
    layer = [nodeinfo[0]]
    for i in range(1, len(nodeinfo)):
        if nodeinfo[i][1] == layer[-1][1]:
            layer.append(nodeinfo[i])
        else:
            depth.append(layer)
            layer = [nodeinfo[i]]
    depth.append(layer)
    root = Node(depth[0][0][1], depth[0][0][0], depth[0][0][2])
    for dep in depth[1:]:
        for x, y, val in dep:
            tmp = Node(y, x, val)
            root = push(tmp, root)
    answer = []
    pre, post = [], []
    preorder(root, pre)
    postorder(root, post)
    answer.append(pre)
    answer.append(post)
    return answer


print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))
print(solution([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16]]))
print(solution([[1, 2], [3, 4], [5, 1], [4, 2]]))
