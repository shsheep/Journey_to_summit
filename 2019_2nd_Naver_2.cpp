#include <iostream>
#include <queue>
#include <utility>

using namespace std;
typedef long long ll;

ll solution(ll n) {
	n--;

	priority_queue< pair<ll, ll> > pq;
	for (ll i = 1; i <= n ; i++)
		pq.push(make_pair(-i*(i+1), i+1));
		//pq.push(make_pair(i*(i+1), i+1));

	ll bf = 0;
	while (n--) {
		cout << "This turn is " << n << " ->  ";
		int size = pq.size();
		priority_queue< pair<ll, ll> > tmp;
		for (int i = 0 ; i < size; i++) {
			pair<ll, ll> p = pq.top();
			pq.pop();
			cout << p.first << "," << p.second << " ";
			tmp.push(p);
		}
		cout << "bf is " << bf;
		cout << "\n";
		pq = tmp;
		pair<ll, ll> tp = pq.top(); pq.pop();
		cout << "tp is " << tp.first << "," << tp.second << "  END\n";
		pq.push(make_pair(tp.first * (tp.second+1), tp.second+1));
		if ( bf == tp.first)
			n++;
		bf = tp.first;
	}
	
	while (pq.top().first == bf)
		pq.pop();
	
	return pq.top().first;
}

int main() {
	ll n;
	cin >> n;
	cout << solution(n);
	return 0;
}

