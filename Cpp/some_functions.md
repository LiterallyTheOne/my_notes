# Some functions

Here, I take note of some not implemented functions
in c++ which I found useful.

[some functions code](codes/src/some_functions.cpp)

## arg sort

Gives you the arguments of a vector in sorted order.

```cpp

#include <vector>
#include <algorithm>

/**
 * @brief Takes a vector and retuns a vector contains argmunt sort
 *
 * @param a vector that needs to be sorted
 *
 * @return a vector of sorted arguments
*/
std::vector<int> arg_sort(std::vector<int> a)
{
    // make indexes
    std::vector<int> a_index;
    for (int i = 0; i < a.size(); i++)
    {
        a_index.push_back(i);
    }

    // use sort function and a lambda to sort indexes
    std::sort(a_index.begin(), a_index.end(),
              [&a](size_t i1, size_t i2)
              { return a[i1] < a[i2]; });

    return a_index;
}

```
