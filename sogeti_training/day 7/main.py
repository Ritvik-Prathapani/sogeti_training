import module1_customers as m1
import module2_orders as m2
import module3_orderitems as m3

customer_1 = m1.Customer(
    first_name="Sai",
    last_name="Kumar",
    phone="1234567890",
    email="temp@gmail.com",
    street="ABC Street",
    city="Hyderabad",
    state="Telangana",
    zip_code="500032"
)

order_1 = m2.Orders(
    customer=customer_1, 
    order_status="Processing",
    order_date="2024-01-29",
    required_date="2024-02-05",
    shipped_date="2024-02-02",
    store_id="S123",
    staff_id="ST456"
)

order_item_1 = m3.OrderItems(
    order=order_1,  
    product_id="P001",
    quantity=2,
    list_price=500.00,
    discount=10.00
)

customer_1.display_details()
order_1.display_order_details()
order_item_1.display_order_item_details()

total_price = order_item_1.calculate_total()
print(f"Final Amount Payable (After Discount): ₹{total_price}")
