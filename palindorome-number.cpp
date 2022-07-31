#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int cntDigits(int x) {
        int cnt = 0;
        while (x /= 10) cnt++;
        return cnt+1;
    }
    
    bool isPalindrome(int x) {
        int start = pow(10,cntDigits(x)-1);

        if (x < 0) return false;

        while (x && start >= 10) {
            cout << x << endl;
            cout << x / start << " - " << x % 10 << endl;
            if (x / start != x % 10) return false;
            x %= start;
            x /= 10;
            start /= 100;
        }

        return true;
    }

    bool isPalindrome2(int x) {
        if (x < 0) return false;
        if (x == 0) return true;

        int acc = 0;
        
        while (x) {
            acc = acc * 10 + x % 10;

            // If the last digit was zero, it can't be palindrome
            if (acc == 0) return false;

            cout << x << " <--> " << acc << endl;

            // In this case we're in middle of number and it's legth is even            
            if (acc == x) {
                return true;
            // In this case it's length is odd so we trashout the last digit of acc
            } else if (acc > x) {
                return (acc / 10) == x;
            }

            x /= 10;
        }

        return false;
    }

    bool isPalindrome3(int x) {
        if (x < 0 || !(x%10)) return false;
        if (x == 0) return true;

        int acc = 0;

        while ((acc = acc*10 + x%10) < x) x /= 10;

        return acc == x || acc / 10 == x;
    }

};

int main(int argc, char** argv) {
    int x = atoi(argv[1]);
    Solution sol;

    cout << (sol.isPalindrome3(x) ? "it is" : "it is not") << endl;
}
