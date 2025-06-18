from itertools import groupby

s = input()

compressed = [(len(list(group)),key) for key, group in groupby(s)]
print(' '.join(str(item) for item in compressed))
