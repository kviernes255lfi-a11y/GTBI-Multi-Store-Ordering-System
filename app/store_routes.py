from collections import defaultdict

@store_bp.route("/orders/new", methods=["GET", "POST"])
def new_order():
    if request.method == "POST":
        # Note: Kung maramihang items ang ise-save mo mula sa bagong UI, 
        # dito mo ipoproseso ang loop ng mga input quantities galing sa form.
        db.session.commit()
        return redirect(url_for("store.new_order"))
        
    # Kunin lahat ng inventory items at i-group sila ayon sa category
    all_items = InventoryItem.query.all()
    categories_dict = defaultdict(list)
    
    for item in all_items:
        # Siguraduhing may attribute o column kang 'category' at 'name' sa iyong InventoryItem model
        cat_name = getattr(item, 'category', 'MISCELLANEOUS')
        categories_dict[cat_name].append(item)
        
    my_orders = Order.query.filter_by(store_id=current_user.store_id).order_by(Order.id.desc()).all()
    
    return render_template(
        "store/new_order.html", 
        categories_dict=dict(categories_dict), 
        orders=my_orders
    )
