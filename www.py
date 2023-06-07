class BST:
    def init(self,Value=None):
        self.value=value
        selft.left=None
        self.right=None
    def search(self,root,data):
        if root is None or root.value==data:
            return root
        if root.value<data:
            return self.search(root,right,data)
            return self.search(root,left,data)
        bst=Bst(1)
        bst.right=Bst(4)
        bst.left=Bst(2)
        bst.right=Bst(9)
        bst.left=Bst(3)
        bst.right=Bst(13)
        bst.left=Bst(7)
        result=bst.search(bst,1)
            print('Found Bst')
        else:
            print('Bst not found')