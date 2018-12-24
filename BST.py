# BST:binary search tree
'''
    BST中复杂度最高的是：delete
'''
# min,max,predecessor,insert,delete
# 树节点用class表示
class Node():
    def __init__(self,v=None,l=None,r=None):
        self.val = v
        self.left = l
        self.right = r

# 新建一棵树
def create(node,name):
    val = input("input the %s value:"%name)
    if val == '#':
        node = None
    else:
        node = Node(v=int(val))
        node.left = create(node,val+' left')
        node.right = create(node,val+' right')
    return node
# 查找BST中的最小值
def bst_min(root):
    print(root.val)
    if root.left == None:
        return root.val
    else:
        return bst_min(root.left)
# 查找BST中的最大值
def bst_max(node):
    if node.right == None:
        return node.val
    else:
        return bst_max(node.right)
# 在BST中查找某一特定值，如果找不到则返回‘#’
def bst_search(node,value):
    if int(node.val) == value:
        return str(node.val)+'bst_search'
    elif node.val > value:
        if node.left != None:
            return bst_search(node.left,value)
        else:
            return '#'
    else:
        if node.right != None:
            return bst_search(node.right,value)
        else:
            return '#'

# 在BST中查找一个比给定值稍小的值，比如，给定值时7，则查找比7稍小的值（在BST中）
def bst_pred(node,value):
    if value >= node.val:
        if node.right == None:
            return node.val
        elif node.right.val >= value:
            return node.val
        else:
            return bst_pred(node.right,value)
    else:
        if node.left == None:
            return node.val
        else:
            return bst_pred(node.left,value)
# 在BST中插入一个值，
def bst_insert(node,value):
    if value > node.val:
        if node.right == None:
            insert_node = Node(v=value)
            node.right = insert_node
        else:
            bst_insert(node.right,value)
    else:
        if node.left == None:
            insert_node = Node(v=value)
            node.left = insert_node
        else:
            bst_insert(node.left,value)

def bst_delete(node,value):


if __name__ == "__main__":
    node = None
    root = create(node,'root') #创建一个树
    max_node = bst_max(root)
    # bst_search = bst_search(root,18)
    bst_pred = bst_pred(root,6)
    bst_insert(root,1)
    bst_insert(root,100)
    bst_insert(root,13)
    min_node = bst_min(root)
    max_node = bst_max(root)
    bst_search = bst_search(root,13)
    print('min:',min_node)
    print('max:',max_node)
    print('search:',bst_search)
    print('bst_pred:',bst_pred)
