for i in range(25):
    print(f"nb{i+1} = random.randint(2,20)")

l = []
for i in range(20):
    l.append(f"nb{i+1}")
print(','.join(l))

ll = [ '|',' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|' ]
for i in range(20):
    print(*ll, sep=' ')