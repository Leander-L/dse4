# Durch GPT 5.5 generiert

"""Sort a list with the merge sort algorithm and plot the result.

The merge sort implementation modifies the input list in place. This keeps the
behavior of the original script: the same list object is sorted instead of
creating and returning a new sorted list.
"""

import matplotlib.pyplot as plt


def merge_sort(values):
    """Sort a list in ascending order using merge sort.

    Parameters
    ----------
    values : list
        List that should be sorted in place.

    Returns
    -------
    None
        The input list is modified directly.
    """
    if len(values) <= 1:
        return

    middle_index = len(values) // 2
    left_values = values[:middle_index]
    right_values = values[middle_index:]

    merge_sort(left_values)
    merge_sort(right_values)

    merge_sorted_halves(values, left_values, right_values)


def merge_sorted_halves(values, left_values, right_values):
    """Merge two sorted lists into the original target list."""
    left_index = 0
    right_index = 0
    target_index = 0

    while left_index < len(left_values) and right_index < len(right_values):
        if left_values[left_index] <= right_values[right_index]:
            values[target_index] = left_values[left_index]
            left_index += 1
        else:
            values[target_index] = right_values[right_index]
            right_index += 1

        target_index += 1

    while left_index < len(left_values):
        values[target_index] = left_values[left_index]
        left_index += 1
        target_index += 1

    while right_index < len(right_values):
        values[target_index] = right_values[right_index]
        right_index += 1
        target_index += 1


def plot_values(values):
    """Plot the values in their current order."""
    x_values = range(len(values))
    plt.plot(x_values, values)
    plt.show()


def main():
    """Run the original before-and-after merge sort example."""
    values = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    plot_values(values)
    merge_sort(values)
    plot_values(values)


if __name__ == "__main__":
    main()