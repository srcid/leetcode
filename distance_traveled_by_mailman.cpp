#include<iostream>
#include<vector>
#include<map>

using namespace std;

/** WARNING: This code doesn't handle cases were 
 * houses and letters being empty lists
 * 
 * houses has zip numbers in consecutive order
 * letters has number of houses that must be visited in the given
 * order, this function return the distance traveled by mailman 
 * 
 * houses = [1,2,3,4,5], letters = [3,5,1]
 * distance = 8
 * 
 * houses = {2,10,25,30,35,45,50,63,77}, letters = {10,30,77,2}
 * distance = 16
*/
int dist(vector<int> houses, vector<int> letters) {
    int dist = 0;
    auto curHouse = houses.begin();

    for (const int letter : letters) {
        while (*curHouse < letter) {
            curHouse++;
            dist++;
        }
        while (*curHouse > letter) {
            curHouse--;
            dist++;
        }
    }

    return dist;
}

int dist2(vector<int> houses, vector<int> letters) {
    int dist = 0;
    map<int, int> houseMap; //map<house number, house index>

    for (int i=0; i < houses.size(); i++) {
        houseMap[houses[i]] = i;   
    }

    dist += houseMap[letters[0]];

    for (int i=0; i < letters.size()-1; i++) {
        dist += abs(houseMap[letters[i]] - houseMap[letters[i+1]]);
    }

    return dist;
}

int main(int argc, char const *argv[])
{
    cout <<  dist({1,2,3,4,5},{3,5,1}) << endl;
    cout << dist2({2,10,25,30,35,45,50,63,77},{10,30,77,2}) << endl;
    return 0;
}
