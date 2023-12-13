#include <bits/stdc++.h>

using namespace std;
using ll = long long;

const int MxN = 1010;
const ll MOD = 32717ll;

ll a[MxN], c[MxN], r[MxN << 1];

int main() {
  cin.tie(nullptr)->ios::sync_with_stdio(false);
  int k, n;
  cin >> k >> n;
  for(int i=1; i<=k; ++i) {
    cin >> c[i];
  }
  for(int i=0; i<=k-1; ++i) {
    cin >> a[i];
    r[i] = a[i];
  }
  for(int i=k; i<=n; ++i) {
    for(int j=1; j<=i; ++j) {
      ll cur = (r[i - j] * c[j]) % MOD;
      r[i] = (r[i] + cur) % MOD;
    }
  }
  cout << r[n] << "\n";
  return 0;
}