#include<iostream>
#include<unordered_map>
#include<vector>
#include<iomanip>

#define INT_MAX 2147483647
#define INT_MIN -2147483648

using namespace std;


// int max = 2**31-1
// 2147483647 / 10 = 214748364
// 214748364 * 10 = 2147483640

class Solution {
public:
    unordered_map<int,int> m;
    
    Solution()
    {
        m = {{'0', 0},{'1', 1},{'2', 2},{'3', 3},{'4', 4},{'5', 5},{'6', 6},{'7', 7},{'8', 8},{'9', 9}};
    }

    int isDigit(const char c) {
        return c >= 48 && c <= 57;
    }

    int isSign(const char c) {
        return c=='-' || c=='+';
    }

    int positive_acc(int j, string s) {
        int i, x;
        for (i=0; j < s.size() && isDigit(s[j]); j++) {
            x = m.at(s[j]);
            
            if (i >= INT_MAX/10 && x + i - INT_MAX/10 > 7) return INT_MAX;
            
            i = i*10 + x;
        }
        
        return i;
    }

    int negative_acc(int j, string s) {
        int i, x;
        for (i=0 ; j < s.size() && isDigit(s[j]); j++) {
            x = -m.at(s[j]);
            
            if (i <= INT_MIN/10 && i - INT_MIN/10 + x < -8) return INT_MIN;

            i = i*10 + x;
        }
        
        return i;
    }

    int idxOfFirstNonSpaceChar(string& s) {
        int j=0;

        // remove all leading spaces
        while (j<s.size() && s[j]==' ') j++;

        return j;
    }

    int myAtoi(string s) {
        const int j = idxOfFirstNonSpaceChar(s);
        
        // j can grow at least one step and it is a digit
        if ((j < s.size() && isDigit(s[j]))) {
            return positive_acc(j, s);
        }
        
        // j can grow at leat two steps and it is a sign
        if ((j < s.size()-1 && isSign(s[j]) && isDigit(s[j+1]))) {
            if (s[j]=='+') {
                return positive_acc(j+1, s);
            }
            
            return negative_acc(j+1, s);
        }

        return 0;
    }
};

int main(int argc, char const *argv[])
{
    //cout << INT_MIN-1 << endl;
    Solution sol;
    vector<string> strings={
        "42", "  -42", "4193 with words", "+-12", "+1", "-91283472332", "words and 987", "91283472332", "1"
    };
    cout.fill(' ');
    for (string string: strings) {
        cout << setw(15) << string << " -> " << sol.myAtoi(string) << endl; 
    }
    return 0;
}
