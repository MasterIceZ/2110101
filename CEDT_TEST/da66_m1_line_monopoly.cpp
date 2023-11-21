#include <bits/stdc++.h>

using namespace std;

int main() {
  cin.tie(nullptr)->ios::sync_with_stdio(false);
  int n;
  cin >> n;
  set<pair<int, int>> st;
  for(int i=1, opr, l, r; i<=n; ++i) {
    cin >> opr;
    if(opr == 2) {
      cout << st.size() << "\n";
      continue;
    }
    cin >> l >> r;
    st.emplace(l, r);
    auto this_position = st.find(make_pair(l, r));
    auto before_this_position = this_position;
    --before_this_position;
    if(this_position != st.begin() && this_position->first - 1 <= before_this_position->second) {
      l = before_this_position->first;
      r = max(before_this_position->second, this_position->second);
      st.erase(before_this_position);
      st.erase(this_position);
      st.emplace(l, r);
    }
    this_position = st.find(make_pair(l, r));
    auto after_this_position = this_position;
    ++after_this_position;
    while(after_this_position != st.end() && this_position->second >= after_this_position->first - 1) {
      l = this_position->first;
      r = max(this_position->second, after_this_position->second);
      st.erase(this_position);
      st.erase(after_this_position);
      st.emplace(l, r);
      this_position = st.find(make_pair(l, r));
      after_this_position = this_position;
      ++after_this_position;
    }
  }
  
}