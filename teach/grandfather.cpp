#include <bits/stdc++.h>

using namespace std;
using ll = long long;

map<ll, ll> p;

int main() {
  cin.tie(nullptr)->ios::sync_with_stdio(false);
  int n, m;
  ll u, v;
  cin >> n >> m;
  for(int i=1; i<=n; ++i) {
    cin >> u >> v;
    p[v] = u;
  }
  for(int i=1; i<=m; ++i) {
    cin >> u >> v;
    if(u == v || p[p[u]] == 0 || p[p[v]] == 0 || p[p[u]] != p[p[v]]) {
      cout << "NO";
    }
    else {
      cout << "YES";
    }
    cout << "\n";
  }
  return 0;
}