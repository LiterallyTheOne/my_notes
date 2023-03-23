#include <vector>
#include <algorithm>

std::vector<int> arg_sort(std::vector<int> a)
{
    std::vector<int> a_index;
    for (int i = 0; i < a.size(); i++)
    {
        a_index.push_back(i);
    }

    std::sort(a_index.begin(), a_index.end(),
              [&a](size_t i1, size_t i2)
              { return a[i1] < a[i2]; });

    return a_index;
}