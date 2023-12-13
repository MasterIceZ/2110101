#include <bits/stdc++.h>

using namespace std;

const int MxN = 5050;
const int di[] = {-1, 0, 0, 1};
const int dj[] = {0, -1, 1, 0};

char a[MxN][MxN];
int dist[MxN][MxN];
queue<pair<int, int>> q;

int main() {
  cin.tie(nullptr)->ios::sync_with_stdio(false);
  int n, m;
  cin >> n >> m;
  memset(dist, -1, sizeof dist);
  for(int i=1; i<=n; ++i) {
    for(int j=1; j<=m; ++j) {
      cin >> a[i][j]; 
      if(a[i][j] == '1') {
        dist[i][j] = 1;
        q.emplace(i, j);
      }
    }
  }
  while(!q.empty()) {
    pair<int, int> now = q.front(); q.pop();
    for(int k=0; k<4; ++k) {
      int ii = di[k] + now.first, jj = dj[k] + now.second;
      if(ii < 1 || jj < 1 || ii > n || jj > m) {
        continue;
      }
      if(dist[ii][jj] != -1 || a[ii][jj] == '3') {
        continue;
      }
      dist[ii][jj] = dist[now.first][now.second] + 1;
      q.emplace(ii, jj);
    }
  }
  int answer = 1e9 + 100;
  for(int i=1; i<=n; ++i) {
    for(int j=1; j<=m; ++j) {
      if(a[i][j] != '2') {
        continue;
      }
      answer = min(answer, (dist[i][j] != -1 ? dist[i][j]: (int) (1e9 + 100)));
    }
  }
  cout << answer << "\n";
  return 0;
}