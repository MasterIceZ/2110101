#include <bits/stdc++.h>

using namespace std;

using ll = long long;

inline bool isPrime(ll v){
  if(v <= 1ll) {
    return false;
  }
  if(v <= 3ll) {
    return true;
  }
  if(v % 2ll == 0ll || v % 3ll == 0ll) {
    return false;
  }
  for(ll i=5; i*i<=v; i+=6ll) {
    if(v % i == 0ll || v % (i + 2ll) == 0ll) {
      return false;
    }
  }
  return true;
}

int main() {
  int q;
  cin >> q;
  while(q--) {
    int a, b, n, m;
    cin >> a >> n >> b >> m;
    cout << (isPrime(stoll(string(n, a + '0') + string(m, b + '0'))) ? "YES" : "NO") << "\n";
  }
  return 0;
}