

#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <algorithm>

using namespace std;
int main()
{
    int b, n, cb = 0;
    cin >> b >> n;
    vector<int> t;
    vector<int> cs = {b};

    for (int i = 0; i < n; i++)
    {
        string op;
        cin >> op;
        if (op == "read")
        {
            cout << cs[cb] << endl;
        }
        else if (op == "credit" || op == "debit")
        {
            int x;
            cin >> x;
            if (op == "credit")
                cs[cb] += x;
            else
                cs[cb] -= x;
            t.push_back(op == "credit" ? x : -x);
        }
        else if (op == "abort")
        {
            int x;
            cin >> x;
            if (x <= t.size())
                cs[cb] -= t[x - 1], t[x - 1] = 0;
        }
        else if (op == "rollback")
        {
            int x;
            cin >> x;
            cb = x - 1;
            cs.resize(cb + 1);
        }
        else if (op == "commit")
        {
            cs.push_back(cs[cb]);
            cb++;
        }
    }
    return 0;
}