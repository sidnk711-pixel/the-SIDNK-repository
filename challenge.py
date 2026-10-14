def price_calculation(p, d, t):
    discount = p*(d/100)
    price = p-discount
    tax = price*(t/100)
    price_after_tax = price+tax
    return price_after_tax
final_price = price_calculation(100, 10, 5)
print(final_price)