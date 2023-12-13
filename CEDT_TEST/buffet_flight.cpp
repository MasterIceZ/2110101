#include <bits/stdc++.h>

using namespace std;

const int MxN = 2020;

struct state_t {
  int v, w;
  bool operator < (const state_t& o) const {
    return w > o.w;
  }
  state_t(int _v, int _w):
    v(_v), w(_w) {}
};

int in[MxN], out[MxN], dist[MxN];
vector<int> adj[MxN];
priority_queue<state_t> pq;

int main() {
  cin.tie(nullptr)->ios::sync_with_stdio(false);
  int n, m;
  cin >> n >> m;
  for(int i=1; i<=n; ++i) {
    cin >> in[i];
  }
  for(int i=1; i<=n; ++i) {
    cin >> out[i];
  }
  for(int i=1, u, v; i<=m; ++i) {
    cin >> u >> v;
    u++, v++;
    adj[u].emplace_back(v);
  }
  memset(dist, 0x3f, sizeof dist);
  pq.emplace(1, dist[1] = 0);
  while(!pq.empty()) {
    state_t now = pq.top(); pq.pop();
    for(auto x: adj[now.v]) {
      int nxt = now.w + out[now.v] + in[x];
      if(dist[x] > nxt) {
        pq.emplace(x, dist[x] = nxt);
      }
    }
  }
  for(int i=1; i<=n; ++i) {
    cout << (dist[i] >= 1e9 + 100 ? -1: dist[i]) << " "; 
  }
  cout << "\n";
  return 0;
}