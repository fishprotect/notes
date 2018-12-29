class Node():
    def __init__(self,v=None,l=None,r=None,h=0):
        self.val    = v
        self.right  = r
        self.left   = l
        self.height = h
# 判断平衡因子
def get_avl_fc(node):
    if node.left == None and node.right == None:
        return 0
    elif node.left != None and node.right != None:
        return node.left.height - node.right.height
    elif node.left == None:
        return -node.right.height
    else:
        return node.left.height
# 前序遍历 返回节点值，节点高度，平衡因子
def pedprint(node):
    if node == None:
        return 
    else:
        print('val: %s;height: %s;AVL_fc: %s'%(node.val,node.height,get_avl_fc(node)))
        pedprint(node.left)
        pedprint(node.right)

# 得到某一节点的高度
def get_height(node):
    if node.left == None and node.right == None:
        return 1
    elif node.right != None and node.left != None:
        return node.left.height+1 if node.left.height > node.right.height else node.right.height+1
    elif node.left == None and node.right != None:
        return node.right.height+1
    else:
        return node.left.height+1
# 新建一棵树
def create(name):
    value = input('please input %s value:' % name)
    if value == '#':
        node = None
    else:
        node = Node(v=int(value))
        node.left = create(str(value)+' left')
        node.right = create(str(value)+' right')
        node.height = get_height(node)
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

if __name__ == "__main__":
    root = create('root')
    pedprint(root)
