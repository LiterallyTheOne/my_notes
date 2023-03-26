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