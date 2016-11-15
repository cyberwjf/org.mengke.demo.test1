# Algorithms & Data Structure

##求二叉树节点个数
```c++
int GetNodeNum(BinaryTreeNode * pRoot)  
{  
    if(pRoot == NULL)
    {
        return 0;  
    }
    else
    {
        return GetNodeNum(pRoot->m_pLeft) + GetNodeNum(pRoot->m_pRight) + 1; 
    }
} 
```
##求二叉树的深度
```c++
int GetDepth(BinaryTreeNode * pRoot)  
{  
    if(pRoot == NULL) // 递归出口  
        return 0;  
    int depthLeft = GetDepth(pRoot->m_pLeft);  
    int depthRight = GetDepth(pRoot->m_pRight);  
    return depthLeft > depthRight ? (depthLeft + 1) : (depthRight + 1);   
}  
```
##前序遍历二叉树
```c++
void PreOrderTraverse(BinaryTreeNode * pRoot)  
{  
    if(pRoot == NULL)  
        return;  
    Visit(pRoot); // 访问根节点  
    PreOrderTraverse(pRoot->m_pLeft); // 前序遍历左子树  
    PreOrderTraverse(pRoot->m_pRight); // 前序遍历右子树  
} 
```

##中序遍历二叉树
```c++
void InOrderTraverse(BinaryTreeNode * pRoot)  
{  
    if(pRoot == NULL)  
        return;  
    InOrderTraverse(pRoot->m_pLeft); // 中序遍历左子树  
    Visit(pRoot); // 访问根节点  
    InOrderTraverse(pRoot->m_pRight); // 中序遍历右子树  
} 
```

##后序遍历二叉树
```c++
void PostOrderTraverse(BinaryTreeNode * pRoot)  
{  
    if(pRoot == NULL)  
        return;  
    PostOrderTraverse(pRoot->m_pLeft); // 中序遍历左子树  
    Visit(pRoot); // 访问根节点  
    PostOrderTraverse(pRoot->m_pRight); // 中序遍历右子树  
} 
```
##求二叉树中叶子节点的个数
```c++
int GetLeafNodeNum(BinaryTreeNode * pRoot)  
{  
    if(pRoot == NULL)  
        return 0;  
    if(pRoot->m_pLeft == NULL && pRoot->m_pRight == NULL)  
        return 1;  
    int numLeft = GetLeafNodeNum(pRoot->m_pLeft); // 左子树中叶节点的个数  
    int numRight = GetLeafNodeNum(pRoot->m_pRight); // 右子树中叶节点的个数  
    return (numLeft + numRight);  
}  
```
##判断两棵二叉树是否结构相同
```c++
bool StructureCmp(BinaryTreeNode * pRoot1, BinaryTreeNode * pRoot2)  
{  
    if(pRoot1 == NULL && pRoot2 == NULL) // 都为空，返回真  
        return true;  
    else if(pRoot1 == NULL || pRoot2 == NULL) // 有一个为空，一个不为空，返回假  
        return false;  
    bool resultLeft = StructureCmp(pRoot1->m_pLeft, pRoot2->m_pLeft); // 比较对应左子树   
    bool resultRight = StructureCmp(pRoot1->m_pRight, pRoot2->m_pRight); // 比较对应右子树  
    return (resultLeft && resultRight);  
}
```
##判断二叉树是不是平衡二叉树
```c++
bool IsAVL(BinaryTreeNode * pRoot, int & height)  
{  
    if(pRoot == NULL) // 空树，返回真  
    {  
        height = 0;  
        return true;  
    }  
    int heightLeft;  
    bool resultLeft = IsAVL(pRoot->m_pLeft, heightLeft);  
    int heightRight;  
    bool resultRight = IsAVL(pRoot->m_pRight, heightRight);  
    if(resultLeft && resultRight && abs(heightLeft - heightRight) <= 1) // 左子树和右子树都是AVL，并且高度相差不大于1，返回真  
    {  
        height = max(heightLeft, heightRight) + 1;  
        return true;  
    }  
    else  
    {  
        height = max(heightLeft, heightRight) + 1;  
        return false;  
    }  
} 
```

##求二叉树的镜像

```c++
BinaryTreeNode * Mirror(BinaryTreeNode * pRoot)  
{  
    if(pRoot == NULL)
        return NULL;  
    BinaryTreeNode * pLeft = Mirror(pRoot->m_pLeft);
    BinaryTreeNode * pRight = Mirror(pRoot->m_pRight);
 
    pRoot->m_pLeft = pRight;  
    pRoot->m_pRight = pLeft;  
    return pRoot;  
}  
```

##求二叉树中两个节点的最低公共祖先节点
```c++
BinaryTreeNode * RebuildBinaryTree(int* pPreOrder, int* pInOrder, int nodeNum)  
{  
    if(pPreOrder == NULL || pInOrder == NULL || nodeNum <= 0)  
        return NULL;  
    BinaryTreeNode * pRoot = new BinaryTreeNode;  
    // 前序遍历的第一个数据就是根节点数据  
    pRoot->m_nValue = pPreOrder[0];  
    pRoot->m_pLeft = NULL;  
    pRoot->m_pRight = NULL;  
    // 查找根节点在中序遍历中的位置，中序遍历中，根节点左边为左子树，右边为右子树  
    int rootPositionInOrder = -1;  
    for(int i = 0; i < nodeNum; i++)  
        if(pInOrder[i] == pRoot->m_nValue)  
        {  
            rootPositionInOrder = i;  
            break;  
        }  
    if(rootPositionInOrder == -1)  
    {  
        throw std::exception("Invalid input.");  
    }  
    // 重建左子树  
    int nodeNumLeft = rootPositionInOrder;  
    int * pPreOrderLeft = pPreOrder + 1;  
    int * pInOrderLeft = pInOrder;  
    pRoot->m_pLeft = RebuildBinaryTree(pPreOrderLeft, pInOrderLeft, nodeNumLeft);  
    // 重建右子树  
    int nodeNumRight = nodeNum - nodeNumLeft - 1;  
    int * pPreOrderRight = pPreOrder + 1 + nodeNumLeft;  
    int * pInOrderRight = pInOrder + nodeNumLeft + 1;  
    pRoot->m_pRight = RebuildBinaryTree(pPreOrderRight, pInOrderRight, nodeNumRight);  
    return pRoot;  
}  
```
