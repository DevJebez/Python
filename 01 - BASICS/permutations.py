from itertools import permutations

def split_into_groups(characters, group_size):
    # Generate all permutations of the characters
    all_permutations = permutations(characters)
    for i in all_permutations:
        print(i)

    # Convert each permutation to a list and group them into sets of three
    grouped_permutations = [list(perm) for perm in all_permutations if len(perm) % group_size == 0]

    # Remove duplicates by converting each group to a set and then back to a tuple
    unique_groups = list(set(tuple(sorted(group)) for group in grouped_permutations))

    # Convert each tuple back to a list
    unique_groups = [list(group) for group in unique_groups]

    return unique_groups

# Example usage
characters_set = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'}
result = split_into_groups(characters_set, 3)

# Print the result
print(result)
