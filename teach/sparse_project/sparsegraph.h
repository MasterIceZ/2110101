#ifndef __SPARSE_GRAPH_H__
#define __SPARSE_GRAPH_H__

// Your code here

#include <set>

using namespace std;

class SparseGraph{
public:
    SparseGraph() {}

    SparseGraph(int n_in) {}

    SparseGraph(const SparseGraph& G):
      edges(G.edges), is_transpose(G.is_transpose) {}

    void AddEdge(int a, int b) {
      edges.emplace(a, b);
    }

    void RemoveEdge(int a, int b) {
      edges.erase(make_edge(a, b));
    }

    bool DoesEdgeExist(int a, int b) const {
      return edges.find(make_edge(a, b)) != edges.end();
    }

    SparseGraph Transpose() const {
      SparseGraph transpose(*this);
      transpose.is_transpose = !is_transpose;
      return transpose;
    }

protected:
    // Your code here
    pair<int, int> make_edge(int u, int v) const {
      if(is_transpose) {
        return make_pair(v, u);
      }
      return make_pair(u, v);
    }

    set<pair<int, int>> edges;
    bool is_transpose = false;
};
#endif // __SPARSE_GRAPH_H__

