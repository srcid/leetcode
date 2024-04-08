#include<iostream>
#include<algorithm>

using namespace std;

class Solution {
public:
    /**
     * Convert a int to a string of its binary form
    */
    string itob(int n) {
        string s = "";

        while (n > 0) {
            s.push_back(n&1 ? '1' : '0');
            n = n >> 1;
        }

        if (s == "") {
            return "0";
        }

        reverse(s.begin(), s.end());
        
        return s; 
    }

    /**
     * convert a string that represents a binary number to int
    */
    int btoi(string& s) {
        int acc = 0;
        int p = 0;

        for (auto ri = s.rbegin(); ri < s.rend(); ri++) {
            acc += ((*ri == '1' ? 1 : 0) << p);
            p++;
        }

        return acc;
    }

    string addBinary(string a, string b) {
        const int ai = btoi(a), bi = btoi(b);

        return itob(ai+bi);
    }   
};

class Solution2 {
    public:

    /**
     * Return 1 if char is '1', 0 otherwise
    */
    int getBit(const char c) {
        return c == '1' ? 1 : 0;
    }

    string addBinary2(string a, string b) {
        string res = "";
        int carry = 0, p, q;
        auto i = a.rbegin(), j = b.rbegin();

        while (i < a.rend() && j < b.rend()) {
            p = getBit(*i);
            q = getBit(*j);

            switch (p+q+carry)
            {
            case 0:
                res.push_back('0');
                break;
            case 1:
                res.push_back('1');
                carry = 0;
                break;
            case 2:
                res.push_back('0');
                carry = 1;
                break;
            case 3:
                res.push_back('1');
                carry = 1;
                break;
            }

            i++;
            j++;
        }

        while (i < a.rend()) {
            p = getBit(*i);

            switch (p+carry)
            {
            case 0:
                res.push_back('0');
                break;
            case 1:
                res.push_back('1');
                carry = 0;
                break;
            case 2:
                res.push_back('0');
                carry = 1;
                break;
            }

            i++;
        }

        while (j < b.rend()) {
            q = getBit(*j);

            switch (q+carry)
            {
            case 0:
                res.push_back('0');
                break;
            case 1:
                res.push_back('1');
                carry = 0;
                break;
            case 2:
                res.push_back('0');
                carry = 1;
                break;
            }

            j++;
        }

        if (carry) {
            res.push_back('1');
        }

        reverse(res.begin(), res.end());

        return res;
    }
};

int main() {
    Solution s;
    cout << s.addBinary("11", "1") << endl;

    return 0;
}