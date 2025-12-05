price = int(input("Enter Price : "))

if price < 100000:
    discount_rate = 0
elif price < 500000:
    discount_rate = 0.10
else:
    discount_rate = 0.20

discount = price * discount_rate
final_price = price - discount

print(f"discount : {int(discount)} T")
print(f" final price : {int(final_price)} T")
