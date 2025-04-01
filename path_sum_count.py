from collections import defaultdict

def path_sum(root: TreeNode, targetSum: int) -> int:
    def dfs(node, current_sum):
        if not node:
            return 0

        # Calculate current prefix sum
        current_sum += node.val

        # Count paths with sum equal to targetSum
        path_count = prefix_sums[current_sum - targetSum]

        # Update prefix sums with the current sum
        prefix_sums[current_sum] += 1

        # Recurse into left and right subtrees
        path_count += dfs(node.left, current_sum)
        path_count += dfs(node.right, current_sum)

        # Backtrack: remove the current sum from the prefix sums
        prefix_sums[current_sum] -= 1

        return path_count

    # Hash map to store prefix sums and their frequencies
    prefix_sums = defaultdict(int)
    prefix_sums[0] = 1  # Base case: a path with sum 0 exists

    return dfs(root, 0)
