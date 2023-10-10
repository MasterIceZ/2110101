#include <bits/stdc++.h>
using namespace std;

const int MxN = 100010;

struct node_t {
	int sum = 0, maxx = 0;
} none;

// segment tree
struct segment_tree {
	node_t tree[MxN << 2];
	node_t merge_node(node_t l, node_t r) {
		node_t res;
		res.sum = l.sum + r.sum;
		res.maxx = max(l.maxx, r.maxx);
		return res;
	}
	void update(int l, int r, int id, int v, int idx) {
		if(l > r || l > idx || r < idx) {
			return ;
		}
		if(l == r) {
			tree[idx].sum += v;
			tree[idx].maxx = tree[idx].sum;
			return ;
		}
		int mid = (l + r) >> 1;
		update(l, mid, id, v, idx << 1);
		update(mid + 1, r, id, v, idx << 1 | 1);
		tree[idx] = merge_node(tree[idx << 1], tree[idx << 1 | 1]);
	}
	node_t query(int l, int r, int wl, int wr, int idx) {
		if(l > r || l > wr || r < wl) {
			return none;
		}
		if(wl <= l && r <= wr) {
			return tree[idx];
		}
		int mid = (l + r) >> 1;
		return merge_node(query(l, mid, wl, wr, idx << 1), query(mid + 1, r, wl, wr, idx << 1 | 1));
	}
} seg;

int main() {
	cin.tie(nullptr)->ios::sync_with_stdio(false);
	int n, m, p, answer = 0;
	cin >> n >> m >> p;
	for(int i=1; i<=m; ++i) {
		int _, l, r, v;
		cin >> _ >> l >> r >> v;
		l++, r++;
		int read_value = seg.query(1, n, l, r-1, 1).maxx;
		cerr << "D: " << read_value << "\n";
		if(read_value + v >= p) {
			answer += i;
			continue;
		}
		seg.update(1, n, l, v, 1);
		seg.update(1, n, r, -v, 1);
		cout << "++++++\n";
		for(int j=1; j<=4*n; ++j) {
			cout << seg.tree[j].maxx << " " << seg.tree[j].sum << "\n";
		}
		cout << "\n";
	}
	cout << answer;
	return 0;
}
