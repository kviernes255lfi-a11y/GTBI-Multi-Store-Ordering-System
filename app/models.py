from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from .extensions import db


class Store(db.Model):
    __tablename__ = "stores"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    location = db.Column(db.String(160), default="—")
    manager = db.Column(db.String(120), default="—")


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # "admin" or "store"
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), nullable=True)
    store = db.relationship("Store", backref="users")

    def set_password(self, raw):
        self.password_hash = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self.password_hash, raw)


class InventoryItem(db.Model):
    __tablename__ = "inventory_items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(160), nullable=False)
    category = db.Column(db.String(80), default="General")
    unit = db.Column(db.String(40), default="unit")
    stock = db.Column(db.Integer, default=0)


class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), nullable=False)
    store = db.relationship("Store")
    item_name = db.Column(db.String(160), nullable=False)
    qty = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), default="Pending")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Spoilage(db.Model):
    __tablename__ = "spoilage"
    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), nullable=False)
    store = db.relationship("Store")
    item_name = db.Column(db.String(160), nullable=False)
    qty = db.Column(db.Integer, nullable=False)
    reason = db.Column(db.String(200), default="Unspecified")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class PurchaseOrder(db.Model):
    __tablename__ = "purchase_orders"
    id = db.Column(db.Integer, primary_key=True)
    vendor = db.Column(db.String(160), nullable=False)
    item_name = db.Column(db.String(160), nullable=False)
    qty = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), default="Pending")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class TransIn(db.Model):
    __tablename__ = "trans_in"
    id = db.Column(db.Integer, primary_key=True)
    from_store = db.Column(db.String(120), nullable=False)
    to_store = db.Column(db.String(120), nullable=False)
    item_name = db.Column(db.String(160), nullable=False)
    qty = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class MonthEndCount(db.Model):
    __tablename__ = "month_end_counts"
    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), nullable=False)
    store = db.relationship("Store")
    item_name = db.Column(db.String(160), nullable=False)
    system_qty = db.Column(db.Integer, default=0)
    counted_qty = db.Column(db.Integer, default=0)
    variance = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
