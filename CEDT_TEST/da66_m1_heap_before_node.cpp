#include <bits/stdc++.h>

using namespace std;

set<int> s;
int n, m;

void dfs(int u) {
  s.erase(u);
  if(u * 2 + 1 < n) {
    dfs(u * 2 + 1);
  }
  if(u * 2 + 2 < n) {
    dfs(u * 2 + 2);
  }
}

int main() {
  cin.tie(nullptr)->ios::sync_with_stdio(false);
  cin >> n >> m;
  for(int i=0; i<n; ++i) {
    s.emplace(i);
  }
  dfs(m);
  cout << s.size() << "\n";
  for(auto x: s) {
    cout << x << " ";
  }
  cout << "\n";
  return 0;
}