#include <iostream>
#include <vector>
#include <string>

using namespace std;

class LinkedListNode
{
public:
    const int k;
    LinkedListNode *next;

    LinkedListNode(int k) : k(k), next(nullptr) {}
    LinkedListNode(int k, LinkedListNode *next) : k(k), next(next) {}
    LinkedListNode(vector<int> &vals, int i) : k(vals[i])
    {
        next = i < vals.size() ? new LinkedListNode(vals, i + 1) : nullptr;
    }
};

class LinkedList
{
public:
    LinkedListNode *root;
    LinkedListNode *last;
    int size;

    LinkedList() : root(nullptr), size(0) {}
    LinkedList(int k) : root(new LinkedListNode(k)), size(1) {}
    LinkedList(vector<int> &vals) : size(vals.size())
    {
        root = new LinkedListNode(vals, 0);
        last = getLastAddr();
    }

    string toString()
    {
        string s = "[";
        auto cur = root;

        while (cur != nullptr)
        {
            s += to_string(cur->k) + " -> ";
            cur = cur->next;
        }

        s += "nil]";
        return s;
    }

    LinkedListNode *getLastAddr()
    {
        auto cur = root;
        while (cur->next != nullptr)
            cur = cur->next;
        return cur;
    }

    void push_back(int n)
    {
        if (root == nullptr)
        {
            root = new LinkedListNode(n);
            last = root;
        }
        else
        {
            last->next = new LinkedListNode(n);
            last = last->next;
        }
        size++;
        return;
    }

    void push_front(int n)
    {
        if (root == nullptr)
        {
            root = new LinkedListNode(n);
            last = root;
        }
        else
        {
            auto newRoot = new LinkedListNode(n, root);
            root = newRoot;
        }
        size++;
        return;
    }

    int pop_back()
    {
        if (root == nullptr) {
            throw "Empty list";
        }

        int k = last->k;

        // case size == 1
        if (root == last)
        {
            delete root;
            root = nullptr;
            last = nullptr;
        }
        else
        {
            auto newLast = root;

            while (newLast->next != last)
            {
                newLast = newLast->next;
            }

            delete last;
            newLast->next = nullptr;
            last = newLast;
        }

        size--;
        return k;
    }

    int pop_front()
    {
        if (root == nullptr) {
            throw "Empty list";
        }

        int k = root->k;

        // case size == 1
        if (root == last)
        {
            delete root;
            root = nullptr;
            last = nullptr;
        }
        else
        {
            auto newRoot = root->next;
            delete root;
            root = newRoot;
        }
        size--;
        return k;
    }
};

int main()
{
    vector<int> arr{2, 3, 5, 1, 2, 4, 6, 8};
    auto listFromArr = LinkedList(arr);

    cout << listFromArr.toString() << endl;

    listFromArr.push_back(10);
    listFromArr.push_front(7);

    cout << listFromArr.toString() << endl;

    auto list = LinkedList();

    for (int i : {5, 2, 3})
    {
        list.push_back(i);
    }

    for (int i : {4, 9, 1})
    {
        list.push_front(i);
    }

    cout << list.toString() << endl;

    while (list.size != 0)
    {
        cout << list.pop_back() << " ";
    }
    cout << endl;

    for (int i : {5, 2, 3})
    {
        list.push_front(i);
    }

    for (int i : {4, 9, 1})
    {
        list.push_back(i);
    }

    cout << list.toString() << endl;

    while (list.size != 0)
    {
        cout << list.pop_front() << " ";
    }
    cout << endl;

    return 0;
}