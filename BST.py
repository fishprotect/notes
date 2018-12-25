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
        node = Node(v=int(val))     # 每次插入一个节点，必须新建一个对象，在c/c++中，则必须申请一个struct
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
# delete有三种情况
'''
    case1:要删除的node没有子元素，该node是一个leaf
    case2:套删除的node有一个叶子，则直接用他的子元素代替他
    case3:要删除的node有两个叶子，用一个子元素代替他（一般我们用left leaf代替）
'''
def bst_delete(node,value):

    # 定义一个函数，含有case1，case2，case3
    def delete_node(node):
        # case1
        if node.left == None and node.right == None:
            node = None
        # case2
        elif node.left == None and node.rigth != None:
            node = node.right
        elif node.left != None and node.right != None:
            node = node.left
        # case3
        else:
            new_node = node.right
            node = node.left
            node.right = new_node
    # 在tree中查找含有该值的node
    if node.val == value:
        delete_node(node)
        print('delete the value %s' % value)
    elif value > node.val:
        if node.right != None:
            bst_delete(node.right,value)
        else:
            print('#')
    elif value < node.val:
        if node.left != None:
            bst_delete(node.left,value)
        else:
            print('#')
    


if __name__ == "__main__":
    node = None
    root = create(node,'root') #创建一个树
    # bst_search = bst_search(root,18)
    # 查找6的pred
    bst_pred = bst_pred(root,6)
    # 插入值1，插入值100，13
    bst_insert(root,1)
    bst_insert(root,100)
    bst_insert(root,13)
    # 查找最小值和最大值
    min_node = bst_min(root)
    max_node = bst_max(root)
    # 搜索13
    bst_search13 = bst_search(root,13)
    # print结果
    print('min:',min_node)
    print('max:',max_node)
    print('search:',bst_search13)
    print('bst_pred:',bst_pred)
    bst_delete(root,13)
    bst_searchn13 = bst_search(root,13)
    print(bst_searchn13)
