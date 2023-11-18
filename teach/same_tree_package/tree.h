#ifndef TREE_H_INCLUDED
#define TREE_H_INCLUDED

class Tree{
    class Node{
        public:
            friend class Tree;
            Node() {data = -1; left = NULL; right = NULL;}
            Node(const int x, Node* left, Node* right) : data(x), left(left), right(right) {}

        protected:
            int data;
            Node* left;
            Node* right;
    };
public:

    Tree() {
        mRoot = NULL;
        mSize = 0;
    }

    ~Tree() {
        clear(mRoot);
    }

    void clear(Node*& r) {
        if (!r) return;
        clear(r->left);
        clear(r->right);
        delete r;
    }

    void insert(int x) {
        insertAt(mRoot, x);
    }
    bool isSameBinaryTree(Tree& t) {
        // Insert your code here
        return isSameBinaryTree(mRoot, t.mRoot);
    }
    // You can also put your code here

protected:
    bool isSameBinaryTree(Node *a, Node *b) {
      if(a == NULL && b == NULL) {
        return true;
      }
      if(a == NULL || b == NULL) {
        return false;
      }
      bool is_same = true;
      is_same &= (a->data == b->data);
      is_same &= isSameBinaryTree(a->left, b->left);
      is_same &= isSameBinaryTree(a->right, b->right);
      return is_same;
    } 
    void insertAt(Node*& r, int x) {
        if (!r) {
           r = new Node(x, NULL, NULL);
           mSize++;
           return;
        }
        if (r->data == x) return; // Do nothing
        if (x < r->data) insertAt(r->left, x); else
        insertAt(r->right, x);
    }
    Node* mRoot;
    int mSize;

};

#endif // TREE_H_INCLUDED
