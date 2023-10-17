Creating a binary and linear search algorithm in Python without using Python is a bit challenging, but I can provide you with a pseudo-code representation of both algorithms in a language-agnostic manner. You would need to adapt these algorithms to the programming language of your choice.

Here's a pseudo-code for a linear search:

```plaintext
function linear_search(arr, target):
    for i from 0 to length(arr) - 1:
        if arr[i] == target:
            return i
    return -1
```

And here's a pseudo-code for a binary search:

```plaintext
function binary_search(arr, target):
    left = 0
    right = length(arr) - 1

    while left <= right:
        mid = (left + right) / 2
        if arr[mid] == target:
            return mid
        else if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

You can translate these pseudo-codes into your language of choice to create functional binary and linear search algorithms.
