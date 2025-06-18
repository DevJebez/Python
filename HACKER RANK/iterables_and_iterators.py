from itertools import combinations


n = int(input())
letters = input().split()
k = int(input())

total_combinations = list(combinations(letters, k))
favorable = [combo for combo in total_combinations if 'a' in combo]

probability = len(favorable) / len(total_combinations)
print(f"{probability:.4f}")
