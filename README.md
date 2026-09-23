# StoreLine — Multi-Store Ordering System

Flask backend na kagaya ng structure ng GTBI system: Dockerfile, requirements.txt,
PostgreSQL sa production, at role-based na login (Admin / Store User).

## Mga pages

**Admin (HQ)**
Dashboard, Master Inventory Items, Manage Stores, View Orders, P.O HQ,
Month End Inventory, Spoilage, Trans-In, Generate Report, Logout

**Store User**
Dashboard, New Orders, View Orders, Spoilage, Logout

## Paano patakbuhin sa local machine

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

# optional: gamitin ang sarili mong .env
cp .env.example .env
# i-edit ang .env at ilagay ang DATABASE_URL / SECRET_KEY mo

python run.py
```

Kung walang DATABASE_URL na nakalagay, gagamit ito ng local SQLite file
(`storeline.db`) — okay lang para sa testing.

Bubukas ito sa **http://localhost:5000**. Sa unang pagpapatakbo, awtomatikong
gagawa ito ng starter data:

| Username | Password | Role |
|---|---|---|
| `admin` | `admin123` | HQ Admin |
| `angonobranch` | `store123` | Store — Angono Branch |
| `taytaybranch` | `store123` | Store — Taytay Branch |
| `caintabranch` | `store123` | Store — Cainta Branch |

**Palitan agad ang mga password na ito bago i-deploy sa production.**

## Pag-deploy sa Render

1. I-push ang project na ito sa isang GitHub repo.
2. Sa Render dashboard: **New → Web Service**, i-connect ang repo mo.
   Awtomatiko itong madi-detect bilang Docker environment dahil may Dockerfile.
3. Gumawa ng **PostgreSQL database** sa Render (New → PostgreSQL).
4. Sa Web Service settings mo, idagdag ang environment variables:
   - `DATABASE_URL` — kunin mo sa "Internal Database URL" ng Postgres mo
   - `SECRET_KEY` — kahit anong random na string
5. Deploy. Awtomatikong gagawa ang app ng tables at starter data sa unang boot
   (`db.create_all()` + seed script).

May kasamang `render.yaml` din kung gusto mong gamitin ang "Blueprint" na
one-click deploy feature ng Render.

## Structure

```
run.py                  entry point (gunicorn run:app)
app/
  __init__.py            Flask app factory
  extensions.py          db = SQLAlchemy()
  models.py               Store, User, InventoryItem, Order, Spoilage,
                           PurchaseOrder, TransIn, MonthEndCount
  auth.py                 login / logout routes
  admin_routes.py         lahat ng Admin (HQ) pages
  store_routes.py         lahat ng Store User pages
  seed.py                 unang-boot na starter data
templates/                Jinja templates (base, login, admin/, store/)
static/css/style.css      shared stylesheet
Dockerfile
requirements.txt
render.yaml
.env.example
```
