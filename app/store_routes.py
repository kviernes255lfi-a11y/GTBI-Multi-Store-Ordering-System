from collections import defaultdict
from flask import Blueprint, render_template, request, redirect, url_for, abort
from flask_login import current_user

from .extensions import db
from .models import InventoryItem, Order, Spoilage

store_bp = Blueprint("store", __name__, url_prefix="/store")


@store_bp.before_request
def restrict_to_store():
    if not current_user.is_authenticated:
        return redirect(url_for("auth.login"))
    if current_user.role != "store":
        abort(403)


@store_bp.route("/dashboard")
def dashboard():
    my_orders = Order.query.filter_by(store_id=current_user.store_id).order_by(Order.id.desc()).all()
    stats = {
        "orders": len(my_orders),
        "pending": len([o for o in my_orders if o.status == "Pending"]),
        "spoilage": Spoilage.query.filter_by(store_id=current_user.store_id).count(),
        "items": InventoryItem.query.count(),
    }
    return render_template("store/dashboard.html", stats=stats, recent_orders=my_orders[:5])


@store_bp.route("/orders/new", methods=["GET", "POST"])
def new_order():
    if request.method == "POST":
        # Saluhin ang lahat ng quantity na isinumite mula sa dynamic inputs
        for key, value in request.form.items():
            if key.startswith("item_"):
                item_id = key.split("_")[1]
                qty = int(value or 0)
                if qty > 0:
                    inv_item = InventoryItem.query.get(item_id)
                    if inv_item:
                        db.session.add(Order(
                            store_id=current_user.store_id,
                            item_name=inv_item.name,
                            qty=qty
                        ))
        db.session.commit()
        return redirect(url_for("store.new_order"))

    # Kunin lahat ng inventory items at i-group sila ayon sa category para sa UI
    all_items = InventoryItem.query.all()
    categories_dict = defaultdict(list)
    
    for item in all_items:
        cat_name = getattr(item, 'category', 'MISCELLANEOUS')
        categories_dict[cat_name].append(item)
        
    my_orders = Order.query.filter_by(store_id=current_user.store_id).order_by(Order.id.desc()).all()
    
    return render_template(
        "store/new_order.html", 
        categories_dict=dict(categories_dict), 
        orders=my_orders
    )


@store_bp.route("/orders")
def orders():
    my_orders = Order.query.filter_by(store_id=current_user.store_id).order_by(Order.id.desc()).all()
    return render_template("store/view_orders.html", orders=my_orders)


@store_bp.route("/spoilage", methods=["GET", "POST"])
def spoilage():
    if request.method == "POST":
        db.session.add(Spoilage(
            store_id=current_user.store_id,
            item_name=request.form["item_name"],
            qty=int(request.form.get("qty") or 1),
            reason=request.form.get("reason") or "Unspecified",
        ))
        db.session.commit()
        return redirect(url_for("store.spoilage"))
    items = InventoryItem.query.all()
    records = Spoilage.query.filter_by(store_id=current_user.store_id).order_by(Spoilage.id.desc()).all()
    return render_template("store/spoilage.html", items=items, records=records, is_admin=False)
