n = input()
english = set(map(int, input().split()))
a = input()
french = set(map(int, input().split()))
print(len(english.union(french)))