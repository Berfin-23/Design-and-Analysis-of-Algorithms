class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight  # Calculate the ratio of value per unit weight


def knapsack_max_value(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse=True)  # Sort items by ratio in descending order
    max_profit = 0
    queue = []

    # Create a dummy node and enqueue it
    dummy = Node(0, 0, 0)
    queue.append(dummy)

    while queue:
        # Extract an item from the queue
        node = queue.pop(0)

        if node.level < len(items):  # Check if level is within bounds
            # Compute profit of next level node
            profit_next = node.profit + items[node.level].value
            weight_next = node.weight + items[node.level].weight

            # If adding the next item doesn't exceed capacity and could potentially lead to greater profit
            if weight_next <= capacity and profit_next > max_profit:
                max_profit = profit_next  # Update max profit

            # Compute bound of next level node
            bound_next = bound(profit_next, capacity, items, node.level + 1)

            # If bound is greater than maxProfit, add next level node to queue
            if bound_next > max_profit:
                next_node = Node(node.level + 1, profit_next, weight_next)
                queue.append(next_node)

            # Consider the case when next level node is not included in the solution
            without_next_node = Node(node.level + 1, node.profit, node.weight)
            bound_without_next = bound(without_next_node.profit, capacity, items, node.level + 1)

            # If bound is greater than maxProfit, add the node to queue
            if bound_without_next > max_profit:
                queue.append(without_next_node)

    return max_profit


def bound(profit, capacity, items, level):
    bound = profit
    total_weight = 0

    # Calculate the bound until the knapsack's capacity is reached or all items are considered
    while level < len(items) and total_weight + items[level].weight <= capacity:
        total_weight += items[level].weight
        bound += items[level].value
        level += 1

    # If there are still items left, include a fractional amount of the next item
    if level < len(items):
        bound += (capacity - total_weight) * items[level].ratio

    return bound


class Node:
    def __init__(self, level, profit, weight):
        self.level = level
        self.profit = profit
        self.weight = weight


# Example usage:
items = [Item(60, 10), Item(100, 20), Item(120, 30)]  # Example items with value and weight
capacity = 50  # Example capacity of the knapsack

print("Maximum value:", knapsack_max_value(items, capacity))