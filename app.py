from flask import Flask, render_template, request, redirect, url_for, flash, session
import os
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-change-me")

# =========================
# FOOD MENU - 32 ITEMS
# =========================

MENU = [
    # MAIN DISHES
    {"id": "Chicken Rice Meal", "price": 85, "category": "Main Dishes", "description": "Tender chicken served with warm steamed rice.", "image": "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?w=600"},
    {"id": "Healthy Rice Bowl", "price": 90, "category": "Main Dishes", "description": "A satisfying rice bowl with fresh ingredients.", "image": "https://images.unsplash.com/photo-1512058564366-18510be2db19?w=600"},
    {"id": "Classic Burger", "price": 100, "category": "Main Dishes", "description": "A juicy burger with fresh toppings.", "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=600"},
    {"id": "Creamy Pasta", "price": 95, "category": "Main Dishes", "description": "Delicious pasta tossed in a creamy sauce.", "image": "https://images.unsplash.com/photo-1473093295043-cdd812d0e601?w=600"},
    {"id": "Chicken Adobo", "price": 110, "category": "Main Dishes", "description": "Filipino-style chicken simmered in a savory sauce.", "image": "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?w=600"},
    {"id": "Beef Steak", "price": 130, "category": "Main Dishes", "description": "Tender beef with a flavorful savory sauce.", "image": "https://images.unsplash.com/photo-1600891964092-4316c288032e?w=600"},
    {"id": "Crispy Fried Chicken", "price": 105, "category": "Main Dishes", "description": "Golden crispy chicken served fresh.", "image": "https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec?w=600"},
    {"id": "Pork BBQ Rice", "price": 100, "category": "Main Dishes", "description": "Grilled barbecue pork served with rice.", "image": "https://images.unsplash.com/photo-1544025162-d76694265947?w=600"},

    # SIDE DISHES
    {"id": "Fresh Garden Salad", "price": 75, "category": "Side Dishes", "description": "Fresh vegetables served with light dressing.", "image": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=600"},
    {"id": "French Fries", "price": 55, "category": "Side Dishes", "description": "Golden and crispy potato fries.", "image": "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?w=600"},
    {"id": "Onion Rings", "price": 60, "category": "Side Dishes", "description": "Crunchy onion rings with a golden coating.", "image": "https://images.unsplash.com/photo-1639024471283-03518883512d?w=600"},
    {"id": "Garlic Bread", "price": 45, "category": "Side Dishes", "description": "Toasted bread with buttery garlic flavor.", "image": "https://images.unsplash.com/photo-1619531040576-f9416740661b?w=600"},
    {"id": "Mashed Potato", "price": 50, "category": "Side Dishes", "description": "Creamy mashed potatoes with butter.", "image": "https://images.unsplash.com/photo-1633436375153-d7045cb93e38?w=600"},
    {"id": "Coleslaw", "price": 45, "category": "Side Dishes", "description": "A refreshing mix of cabbage and carrots.", "image": "https://images.unsplash.com/photo-1625938144755-652e08e359b7?w=600"},
    {"id": "Cheese Sticks", "price": 65, "category": "Side Dishes", "description": "Crispy snacks filled with melted cheese.", "image": "https://images.unsplash.com/photo-1531749668029-2db88e4276c7?w=600"},
    {"id": "Potato Wedges", "price": 60, "category": "Side Dishes", "description": "Seasoned potato wedges, crispy outside and soft inside.", "image": "https://images.unsplash.com/photo-1518013431117-eb1465fa5752?w=600"},

    # DESSERTS
    {"id": "Classic Tart", "price": 50, "category": "Desserts", "description": "A buttery tart with a smooth, sweet filling.", "image": "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=600"},
    {"id": "Chocolate Cake Slice", "price": 60, "category": "Desserts", "description": "Rich chocolate cake for chocolate lovers.", "image": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=600"},
    {"id": "Strawberry Cupcake", "price": 45, "category": "Desserts", "description": "A soft cupcake with sweet strawberry flavor.", "image": "https://images.unsplash.com/photo-1486427944299-d1955d23e34d?w=600"},
    {"id": "Cookies", "price": 35, "category": "Desserts", "description": "Freshly baked cookies with a delicious crunch.", "image": "https://images.unsplash.com/photo-1499636136210-6f4ee915583e?w=600"},
    {"id": "Chocolate Brownies", "price": 45, "category": "Desserts", "description": "Soft and fudgy chocolate brownies.", "image": "https://images.unsplash.com/photo-1606313564200-e75d5e30476c?w=600"},
    {"id": "Cheesecake", "price": 70, "category": "Desserts", "description": "Smooth and creamy cheesecake with a biscuit crust.", "image": "https://images.unsplash.com/photo-1533134242443-d4fd215305ad?w=600"},
    {"id": "Glazed Donuts", "price": 40, "category": "Desserts", "description": "Soft donuts covered with sweet glaze.", "image": "https://images.unsplash.com/photo-1551024506-0bccd828d307?w=600"},
    {"id": "Mango Float", "price": 55, "category": "Desserts", "description": "A chilled Filipino dessert with mango and cream.", "image": "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=600"},

    # BEVERAGES
    {"id": "Iced Coffee", "price": 65, "category": "Beverages", "description": "Refreshing iced coffee with a smooth flavor.", "image": "https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=600"},
    {"id": "Fresh Lemonade", "price": 45, "category": "Beverages", "description": "Cool lemonade made with a refreshing citrus taste.", "image": "https://images.unsplash.com/photo-1513558161293-cdaf765edfd4?w=600"},
    {"id": "Mango Juice", "price": 50, "category": "Beverages", "description": "Sweet and refreshing mango juice.", "image": "https://images.unsplash.com/photo-1622597467836-f3285f2131b8?w=600"},
    {"id": "Orange Juice", "price": 45, "category": "Beverages", "description": "Fresh-tasting orange juice.", "image": "https://images.unsplash.com/photo-1600271886742-f049cd451bba?w=600"},
    {"id": "Milk Tea", "price": 60, "category": "Beverages", "description": "Creamy milk tea with a sweet tea flavor.", "image": "https://images.unsplash.com/photo-1558857563-b371033873b8?w=600"},
    {"id": "Strawberry Milkshake", "price": 75, "category": "Beverages", "description": "A creamy milkshake with strawberry flavor.", "image": "https://images.unsplash.com/photo-1572490122747-3968b75cc699?w=600"},
    {"id": "Iced Tea", "price": 40, "category": "Beverages", "description": "A chilled tea drink for a refreshing break.", "image": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=600"},
    {"id": "Bottled Water", "price": 20, "category": "Beverages", "description": "Clean and refreshing bottled drinking water.", "image": "https://images.unsplash.com/photo-1548839140-29a749e1cf4d?w=600"}
]

# =========================
# ORDER STORAGE
# =========================

orders = []
next_order_id = 1001


# =========================
# HELPER: GET CART ITEMS
# =========================

def get_cart_items():
    cart_items = []
    total = 0

    cart = session.get("cart", {})

    for item_name, quantity in cart.items():
        item = next((x for x in MENU if x["id"] == item_name), None)

        if item and isinstance(quantity, int) and 1 <= quantity <= 50:
            subtotal = item["price"] * quantity

            cart_items.append({
                "id": item["id"],
                "item": item["id"],
                "price": item["price"],
                "quantity": quantity,
                "subtotal": subtotal,
                "image": item["image"]
            })

            total += subtotal

    return cart_items, total


# =========================
# HOME PAGE
# =========================

@app.route("/")
def home():
    return render_template("index.html")


# =========================
# MENU PAGE
# =========================

@app.route("/menu")
def menu():
    return render_template("menu.html", menu=MENU)


# =========================
# ADD TO CART
# =========================

@app.route("/add-to-cart", methods=["POST"])
def add_to_cart():
    item_name = request.form.get("item", "")

    try:
        quantity = int(request.form.get("quantity", 1))
    except ValueError:
        quantity = 0

    item = next((x for x in MENU if x["id"] == item_name), None)

    if not item or not 1 <= quantity <= 50:
        flash("Invalid item or quantity.")
        return redirect(url_for("menu"))

    cart = session.get("cart", {})
    new_quantity = cart.get(item_name, 0) + quantity

    if new_quantity > 50:
        flash("Maximum quantity for one item is 50.")
        return redirect(url_for("menu"))

    cart[item_name] = new_quantity
    session["cart"] = cart

    flash(item_name + " added to your cart!")
    return redirect(url_for("menu"))


# =========================
# SHOPPING CART
# =========================

@app.route("/cart")
def cart():
    cart_items, total = get_cart_items()

    return render_template(
        "cart.html",
        cart_items=cart_items,
        total=total
    )


# =========================
# UPDATE CART
# =========================

@app.route("/update-cart", methods=["POST"])
def update_cart():
    item_name = request.form.get("item", "")

    try:
        quantity = int(request.form.get("quantity", 0))
    except ValueError:
        quantity = 0

    cart = session.get("cart", {})

    if item_name in cart:
        if 1 <= quantity <= 50:
            cart[item_name] = quantity
        else:
            cart.pop(item_name, None)

    session["cart"] = cart
    flash("Cart updated.")

    return redirect(url_for("cart"))


# =========================
# REMOVE ITEM
# =========================

@app.route("/remove-item", methods=["POST"])
def remove_item():
    item_name = request.form.get("item", "")

    cart = session.get("cart", {})
    cart.pop(item_name, None)

    session["cart"] = cart
    flash("Item removed from cart.")

    return redirect(url_for("cart"))


# =========================
# CHECKOUT
# =========================

@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    global next_order_id

    cart_items, total = get_cart_items()

    if not cart_items:
        flash("Your cart is empty!")
        return redirect(url_for("menu"))

    if request.method == "POST":
        customer = request.form.get("customer", "").strip()
        address = request.form.get("address", "").strip()

        if not customer or not address:
            flash("Please complete all customer information.")
            return redirect(url_for("checkout"))

        new_order = {
            "id": next_order_id,
            "customer": customer,
            "address": address,
            "items": cart_items,
            "total": total,
            "status": "Order received",
            "delivery_minutes": None,
        }

        orders.append(new_order)
        next_order_id += 1

        session.pop("cart", None)

        return render_template(
            "confirmation.html",
            order=new_order
        )

    return render_template(
        "checkout.html",
        cart_items=cart_items,
        total=total
    )


# =========================
# ORDER TRACKING
# =========================


# =========================
# ORDER TRACKING
# =========================

@app.route("/tracking", methods=["GET", "POST"])
def tracking():
    found_order = None

    if request.method == "POST":
        try:
            order_id = int(request.form.get("order_id", 0))
        except ValueError:
            order_id = 0

        found_order = next(
            (o for o in orders if o["id"] == order_id),
            None
        )

        if not found_order:
            flash("Order number not found.")

    return render_template("tracking.html", order=found_order)


# =========================
# SELLER DASHBOARD
# =========================

@app.route("/seller")
def seller():
    return render_template("seller.html", orders=orders)


# =========================
# SELLER UPDATE
# =========================

@app.route("/seller/update-order", methods=["POST"])
def seller_update_order():
    try:
        order_id = int(request.form.get("order_id", 0))
    except ValueError:
        order_id = 0

    status = request.form.get("status", "")
    minutes_text = request.form.get("delivery_minutes", "").strip()

    allowed = [
        "Order received",
        "Preparing",
        "Out for delivery",
        "Delivered"
    ]

    order = next(
        (o for o in orders if o["id"] == order_id),
        None
    )

    if order and status in allowed:
        order["status"] = status

        if minutes_text:
            try:
                minutes = int(minutes_text)
                if 1 <= minutes <= 240:
                    order["delivery_minutes"] = minutes
                else:
                    flash("Enter 1 to 240 minutes.")
                    return redirect(url_for("seller"))
            except ValueError:
                flash("Invalid delivery time.")
                return redirect(url_for("seller"))
        else:
            order["delivery_minutes"] = None

        flash("Order successfully updated!")
    else:
        flash("Unable to update order.")

    return redirect(url_for("seller"))

# =========================
# SELLER: UPDATE ORDER STATUS
# =========================

@app.route("/update-status", methods=["POST"])
def update_status():
    try:
        order_id = int(request.form.get("order_id", 0))
    except ValueError:
        order_id = 0

    status = request.form.get("status", "")

    allowed = [
        "Order received",
        "Preparing",
        "Out for delivery",
        "Delivered"
    ]

    order = next(
        (o for o in orders if o["id"] == order_id),
        None
    )

    if order and status in allowed:
        order["status"] = status
        flash("Order status updated.")
    else:
        flash("Unable to update order.")

    return redirect(url_for("tracking"))


# =========================
# RUN WEBSITE
# =========================

if __name__ == "__main__":
    app.run(debug=True)