class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
class Tree:
    def __init__(self):
        self.bt=None
    def insertNode(self,ele):
        newNode=Node(ele);
        if(self.bt==None):
            bt=newNode
        else:
            temp=self.bt
            while(temp)
