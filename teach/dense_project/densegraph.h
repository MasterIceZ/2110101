#ifndef __DENSE_GRAPH_H__
#define __DENSE_GRAPH_H__

// Your code here
#include <vector>
using namespace std;
class DenseGraph{
public:
    DenseGraph():
      DenseGraph(3) {}

    DenseGraph(int n_in) {
        // Your code here
        n = n_in;
        edges = vector<vector<bool>> (n, vector<bool> (n, false));
    }

    DenseGraph(const DenseGraph& G) {
        // Your code here
        edges = G.edges;
    }

    void AddEdge(int a, int b) {
        // Your code here
        edges[a][b] = true;
    }

    void RemoveEdge(int a, int b) {
        // Your code here
        edges[a][b] = false;
    }

    bool DoesEdgeExist(int a, int b) const {
        // Your code here
        return edges[a][b];
    }

    DenseGraph Transpose() const {
        // Your code here
        DenseGraph transpose(n);
        for(int i=0; i<=n-1; ++i) {
          for(int j=0; j<=n-1; ++j) {
            transpose.edges[j][i] = edges[i][j];
          }
        }
        return transpose;
    }

protected:
    int n;
    // Your code here
    vector<vector<bool>> edges;
};
#endif // __DENSE_GRAPH_H__
