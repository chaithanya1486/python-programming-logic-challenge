st = {int(x) for x in input().split()}
i = int(input())
r = int(input())

# Insert i in set
st.add(i)

# Printing the set
for x in sorted(st):
    print(x, end=' ')
print()

# Remove r from set
st.remove(r)

# Printing the set
for x in sorted(st):
    print(x, end=' ')
print()

# Sum of set elements
total = sum(st)

# Print sum
print(total)
