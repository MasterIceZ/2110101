#include <iostream>
#include <vector>
#include <stack>

using namespace std;

vector<int> l;

int main() {
  cin.tie(nullptr)->ios::sync_with_stdio(false);
  int n, k, v;
  cin >> n >> k >> v;
  for(int i=1, x; i<=n; ++i) {
    cin >> x;
    l.emplace_back(x);
    if(i == k) {
      l.emplace_back(v);
    }
  }
  int max_left = k, min_right = k + 1;
  int pop_value = v;
  while(true) {
    int cnt_pop = 0;
    int cur_left = max_left;
    while(cur_left >= 0 && l[cur_left] == pop_value) {
      cur_left -= 1;
      cnt_pop += 1;
    }
    int cur_right = min_right;
    while(cur_right <= n && l[cur_right] == pop_value) {
      cur_right += 1;
      cnt_pop += 1;
    }
    if(cnt_pop >= 3) {
      max_left = cur_left;
      min_right = cur_right;
      if(l[max_left] != l[min_right]) {
        break;
      }
      pop_value = l[max_left];
    }
    else {
      break;
    }
  }
  for(int i=0; i<=max_left; ++i) {
    cout << l[i] << " ";
  }
  for(int i=min_right; i<=n; ++i) {
    cout << l[i] << " ";
  }
  cout << "\n";
  return 0;
}