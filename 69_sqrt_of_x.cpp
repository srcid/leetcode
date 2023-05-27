#include<iostream>
#include<cmath>
#include<unistd.h>

using namespace std;

class Solution {
public:
    int mySqrt(int x) {
        if (x<2) return x;
        
        int i=1, j=x, r;

        for (; i < j; i++) {
            r = (i+j)/2;

            if (r == x / r) {
                return r;
            } if (r > x / r) {
                j = r-1;
            } else {
                i = r+1;
            }
        }

        return j;
    }
    
    int mySqrtBruteForce(int x) {
        for (int i=2; i<=x; i++) {
            if (i > x / i) return i-1; 
        }
        
        return x;
    }

    /**
    sqrt(x) pertence à [1, ... , x/2+1]
    */
    double mySqrtDouble(int x) {
        if (x==0) return 0;

        double 
            i=1,     // bottom 
            j=x/2+1, // top
            r,       // middle
            d;       // difference

        do {
            r = (i+j)/2;
            d = r - x / r;

            // cout << "i: " << i <<
            //         " | j: " << j <<
            //         " | r: " << r << 
            //         " | d: " << d << endl;

            if ( d > 0 ) { /* r > x / r */
                j = r;
            }
            if ( d < 0 ) { /* r < x / r */
                i = r;
            }

            //sleep(1);

        } while (abs(d) > 0.01);
        
        //cout << "root: " <<  r << endl;

        return r;
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    for (int i=0; i<20; i++) {
        cout << "x=" << i << " " << s.mySqrt(i) << " " << sqrt(i) << endl;
        //cout << "x= " << i << endl;
        //auto myroot = s.mySqrt(i);
        //auto root = sqrt(i);
        //if (abs(myroot - root) > 0.003) cout << i << " -> " << myroot - root << " " << myroot << " " << root << endl;
    }
    return 0;
}
