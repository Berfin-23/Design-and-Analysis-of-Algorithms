def knapsack(item_weights, item_values, num_items, max_weight):
    # Initialize a table to store the maximum values
    dp_table = [[0] * (max_weight + 1) for _ in range(num_items + 1)]

    # Build DP table
    for item in range(1, num_items + 1):
        for weight in range(1, max_weight + 1):
            if item_weights[item - 1] <= weight:
                dp_table[item][weight] = max(item_values[item - 1] + dp_table[item - 1][weight - item_weights[item - 1]], dp_table[item - 1][weight])
            else:
                dp_table[item][weight] = dp_table[item - 1][weight]

    # Backtrack to find items included in the knapsack
    included_items = []
    item, weight = num_items, max_weight
    while item > 0 and weight > 0:
        if dp_table[item][weight] != dp_table[item - 1][weight]:
            included_items.append(item - 1)
            weight -= item_weights[item - 1]
        item -= 1

    return dp_table[num_items][max_weight], included_items[::-1]

# Example usage
item_values = [60, 100, 120]
item_weights = [10, 20, 30]
num_items = len(item_values)
max_weight = 50
max_value, items_included = knapsack(item_weights, item_values, num_items, max_weight)
print("Maximum value:", max_value)
print("Items included:", items_included)