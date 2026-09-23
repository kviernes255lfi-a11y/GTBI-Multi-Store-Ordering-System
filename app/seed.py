from .extensions import db
from .models import User, Store, InventoryItem


def seed_if_empty():
    """Populate first-run demo data: HQ admin, 3 stores, a store login per
    store, and a starter inventory catalog. Safe to call every boot —
    it only runs once, when the users table is empty."""
    if User.query.first():
        return

    stores = [
        Store(name="Angono Branch", location="Angono, Rizal", manager="J. Cruz"),
        Store(name="Taytay Branch", location="Taytay, Rizal", manager="R. Dela Pena"),
        Store(name="Cainta Branch", location="Cainta, Rizal", manager="L. Ramos"),
    ]
    db.session.add_all(stores)
    db.session.flush()

    items = [
        InventoryItem(name="Rice 25kg", category="Grocery", unit="sack", stock=120),
        InventoryItem(name="Cooking Oil 1L", category="Grocery", unit="bottle", stock=340),
        InventoryItem(name="Canned Sardines", category="Canned Goods", unit="can", stock=900),
        InventoryItem(name="Bottled Water 500ml", category="Beverage", unit="bottle", stock=600),
    ]
    db.session.add_all(items)

    admin = User(username="admin", role="admin")
    admin.set_password("admin123")
    db.session.add(admin)

    for s in stores:
        username = s.name.lower().replace(" ", "")
        u = User(username=username, role="store", store=s)
        u.set_password("store123")
        db.session.add(u)

    db.session.commit()
