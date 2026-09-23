from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for, abort
from flask_login import current_user

from .extensions import db
from .models import InventoryItem, Store, Order, PurchaseOrder, Spoilage, TransIn, MonthEndCount

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


@admin_bp.before_request
def restrict_to_admin():
    if not current_user.is_authenticated:
        return redirect(url_for("auth.login"))
    if current_user.role != "admin":
        abort(403)


@admin_bp.route("/dashboard")
def dashboard():
    stats = {
        "items": InventoryItem.query.count(),
        "stores": Store.query.count(),
        "pending_orders": Order.query.filter_by(status="Pending").count(),
        "spoilage": Spoilage.query.count(),
        "open_po": PurchaseOrder.query.filter_by(status="Pending").count(),
    }
    recent_orders = Order.query.order_by(Order.id.desc()).limit(5).all()
    return render_template("admin/dashboard.html", stats=stats, recent_orders=recent_orders)


@admin_bp.route("/inventory", methods=["GET", "POST"])
def inventory():
    if request.method == "POST":
        db.session.add(InventoryItem(
            name=request.form["name"].strip(),
            category=request.form.get("category") or "General",
            unit=request.form.get("unit") or "unit",
            stock=int(request.form.get("stock") or 0),
        ))
        db.session.commit()
        return redirect(url_for("admin.inventory"))
    items = InventoryItem.query.order_by(InventoryItem.id.desc()).all()
    return render_template("admin/master_inventory.html", items=items)


@admin_bp.route("/inventory/<int:item_id>/delete", methods=["POST"])
def delete_inventory(item_id):
    item = InventoryItem.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for("admin.inventory"))


@admin_bp.route("/stores", methods=["GET", "POST"])
def stores():
    if request.method == "POST":
        db.session.add(Store(
            name=request.form["name"].strip(),
            location=request.form.get("location") or "—",
            manager=request.form.get("manager") or "—",
        ))
        db.session.commit()
        return redirect(url_for("admin.stores"))
    all_stores = Store.query.order_by(Store.id.desc()).all()
    return render_template("admin/manage_stores.html", stores=all_stores)


@admin_bp.route("/stores/<int:store_id>/delete", methods=["POST"])
def delete_store(store_id):
    s = Store.query.get_or_404(store_id)
    db.session.delete(s)
    db.session.commit()
    return redirect(url_for("admin.stores"))


@admin_bp.route("/orders")
def orders():
    all_orders = Order.query.order_by(Order.id.desc()).all()
    return render_template("admin/view_orders.html", orders=all_orders)


@admin_bp.route("/orders/<int:order_id>/<status>", methods=["POST"])
def update_order(order_id, status):
    if status not in ("Approved", "Rejected"):
        abort(400)
    o = Order.query.get_or_404(order_id)
    o.status = status
    db.session.commit()
    return redirect(url_for("admin.orders"))


@admin_bp.route("/po", methods=["GET", "POST"])
def po_hq():
    if request.method == "POST":
        db.session.add(PurchaseOrder(
            vendor=request.form.get("vendor", "").strip() or "Unnamed vendor",
            item_name=request.form["item_name"],
            qty=int(request.form.get("qty") or 1),
        ))
        db.session.commit()
        return redirect(url_for("admin.po_hq"))
    items = InventoryItem.query.all()
    pos = PurchaseOrder.query.order_by(PurchaseOrder.id.desc()).all()
    return render_template("admin/po_hq.html", pos=pos, items=items)


@admin_bp.route("/po/<int:po_id>/receive", methods=["POST"])
def receive_po(po_id):
    p = PurchaseOrder.query.get_or_404(po_id)
    p.status = "Received"
    db.session.commit()
    return redirect(url_for("admin.po_hq"))


@admin_bp.route("/monthend", methods=["GET", "POST"])
def month_end():
    if request.method == "POST":
        item = InventoryItem.query.filter_by(name=request.form["item_name"]).first()
        system_qty = item.stock if item else 0
        counted = int(request.form.get("counted_qty") or 0)
        store = Store.query.get_or_404(int(request.form["store_id"]))
        db.session.add(MonthEndCount(
            store=store,
            item_name=request.form["item_name"],
            system_qty=system_qty,
            counted_qty=counted,
            variance=counted - system_qty,
        ))
        db.session.commit()
        return redirect(url_for("admin.month_end"))
    stores = Store.query.all()
    items = InventoryItem.query.all()
    records = MonthEndCount.query.order_by(MonthEndCount.id.desc()).all()
    return render_template("admin/month_end.html", stores=stores, items=items, records=records)


@admin_bp.route("/spoilage", methods=["GET", "POST"])
def spoilage():
    if request.method == "POST":
        store = Store.query.get_or_404(int(request.form["store_id"]))
        db.session.add(Spoilage(
            store=store,
            item_name=request.form["item_name"],
            qty=int(request.form.get("qty") or 1),
            reason=request.form.get("reason") or "Unspecified",
        ))
        db.session.commit()
        return redirect(url_for("admin.spoilage"))
    stores = Store.query.all()
    items = InventoryItem.query.all()
    records = Spoilage.query.order_by(Spoilage.id.desc()).all()
    return render_template("admin/spoilage.html", stores=stores, items=items, records=records, is_admin=True)


@admin_bp.route("/transin", methods=["GET", "POST"])
def trans_in():
    if request.method == "POST":
        db.session.add(TransIn(
            from_store=request.form["from_store"],
            to_store=request.form["to_store"],
            item_name=request.form["item_name"],
            qty=int(request.form.get("qty") or 1),
        ))
        db.session.commit()
        return redirect(url_for("admin.trans_in"))
    stores = Store.query.all()
    items = InventoryItem.query.all()
    records = TransIn.query.order_by(TransIn.id.desc()).all()
    return render_template("admin/trans_in.html", stores=stores, items=items, records=records)


@admin_bp.route("/report")
def report():
    stores = Store.query.all()
    lines = []
    for s in stores:
        o_count = Order.query.filter_by(store_id=s.id).count()
        sp_qty = sum(sp.qty for sp in Spoilage.query.filter_by(store_id=s.id).all())
        lines.append(f"  {s.name:<22} orders: {str(o_count):<4} spoilage units: {sp_qty}")

    ctx = dict(
        total_orders=Order.query.count(),
        pending=Order.query.filter_by(status="Pending").count(),
        approved=Order.query.filter_by(status="Approved").count(),
        items=InventoryItem.query.count(),
        spoil_units=sum(sp.qty for sp in Spoilage.query.all()),
        transfers=TransIn.query.count(),
        monthend=MonthEndCount.query.count(),
        po_total=PurchaseOrder.query.count(),
        po_open=PurchaseOrder.query.filter_by(status="Pending").count(),
        by_store="\n".join(lines) if lines else "  No stores on file.",
        generated=datetime.utcnow().strftime("%b %d, %Y"),
    )
    return render_template("admin/report.html", **ctx)
