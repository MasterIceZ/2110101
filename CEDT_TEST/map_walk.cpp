#include <bits/stdc++.h>

using namespace std;

const int MxN = 15;
const char di[] = {0, 1, -1};
const char dj[] = {1, 0, 0};

int n, m;
char a[MxN][MxN], answer[MxN * MxN];
bitset<MxN> visited[MxN];

void rec(int i, int j, int cur_len) {
  if(i == n && j == m) {
    cout << answer << "\n";
    return ;
  }
  for(int k=0; k<3; ++k) {
    int ii = di[k] + i, jj = dj[k] + j;
    if(ii < 1 || jj < 1 || ii > n || jj > m) {
      continue;
    }
    if(a[ii][jj] == '1' || visited[ii][jj]) {
      continue;
    }
    visited[ii][jj] = true;
    answer[cur_len] = 'A' + k;
    rec(ii, jj, cur_len + 1);
    answer[cur_len] = '\0';
    visited[ii][jj] = false;
  }
}

int main() {
  cin.tie(nullptr)->ios::sync_with_stdio(false);
  cin >> n >> m;
  for(int i=1; i<=n; ++i) {
    for(int j=1; j<=m; ++j) {
      cin >> a[i][j];
    }
  }
  visited[1][1] = true;
  rec(1, 1, 0);
  cout << "DONE\n";
  return 0;
}