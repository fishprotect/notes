class Node():
    def __init__(self,v=None,l=None,r=None):
        self.val    = v
        self.right  = r
        self.left   = l
def create(name):
    value = input('please input %s value:' % name)
    if value == '#':
        node = None
    else:
        node = Node(v=int(value))
        node.left = create(str(value)+' left')
        node.right = create(str(value)+' right')
    return node

# 下面的函数是：找到一个节点值等于value的节点，将它和它的左子节点交换
def l_roation(node,value):
    if node.val == value:
        # 
        new_r = Node()
        new_r.val = node.val
        new_r.right = node.right
        new_r.left = node.left.right

        node.val = node.left.val
        node.left = node.left.left

        node.right = new_r

        del new_r
    elif node.val < value:
        l_roation(node.right,value)
    elif node.val > value:
        l_roation(node.left,value)
