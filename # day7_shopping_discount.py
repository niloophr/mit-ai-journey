p1 = int(input("Price 1: "))
p2 = int(input("Price 2: "))
p3 = int(input("Price 3: "))
total = p1 + p2 + p3

if total > 10000:
    final = total * 0.9
    print(f"Final price with 10% discount: {final}")
else:
    print(f"Final price: {total}")
