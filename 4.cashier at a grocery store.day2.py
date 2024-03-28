item_prices = [2.5, 1.75, 3.0, 4.25] 
quantities = [3, 2, 4, 1] 
discount_rate = 10
tax_rate = 8
subtotal = sum(item_price * quantity for item_price, quantity in zip(item_prices, quantities))
discount_amount = (discount_rate / 100) * subtotal
discounted_subtotal = subtotal - discount_amount
tax_amount = (tax_rate / 100) * discounted_subtotal
total_cost = discounted_subtotal + tax_amount
print("Subtotal: $", subtotal)
print("Discounted Subtotal (after", discount_rate, "% discount): $", discounted_subtotal)
print("Tax Amount (at", tax_rate, "% tax rate): $", tax_amount)
print("Total Cost: $", total_cost)
