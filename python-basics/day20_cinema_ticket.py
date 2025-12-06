age = int(input("Enter your Age : "))
film_type = input("Enter Film type you Want (normal Or 3D) : ")
time = int(input("Choose the time you want (14 Or 19 Or 22) : "))

base_price = 50000
final_price = base_price
price_increase_count = 0

# Calculate price increases
if film_type == "3D":
    final_price = final_price * 1.20  # 20% increase
    price_increase_count += 20

if 18 <= time <= 22:
    final_price = final_price * 1.10  # 10% increase
    price_increase_count += 10

# Calculate age discount
discount = 0
if age < 12:
    discount = 50
elif 18 <= age <= 25:
    discount = 30
elif age > 60:
    discount = 40

# Apply discount
discount_amount = final_price * (discount / 100)
final_price_with_discount = final_price - discount_amount

# Display results
print(f"\n=== Ticket Invoice ===")
print(f"Base Price: {base_price:,} Tomans")
print(f"Price Increase Percentage: {price_increase_count}%")

if price_increase_count > 0:
    increased_price = base_price * (1 + price_increase_count/100)
    print(f"Price After Increase: {increased_price:,.0f} Tomans")

print(f"Age Discount Percentage: {discount}%")

if discount > 0:
    print(f"Discount Amount: {discount_amount:,.0f} Tomans")

print(f"Final Price: {final_price_with_discount:,.0f} Tomans")
