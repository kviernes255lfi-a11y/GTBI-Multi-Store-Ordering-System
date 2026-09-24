from .extensions import db
from .models import User, Store, InventoryItem


def seed_if_empty():
    """Populate first-run demo data: HQ admin, 3 stores, a store login per
    store, and a starter inventory catalog. Safe to call every boot —
    it only runs once, when the inventory items table is empty."""
    if InventoryItem.query.first():
        return

    stores = [
        Store(name="Angono Branch", location="Angono, Rizal", manager="J. Cruz"),
        Store(name="Taytay Branch", location="Taytay, Rizal", manager="R. Dela Pena"),
        Store(name="Cainta Branch", location="Cainta, Rizal", manager="L. Ramos"),
    ]
    db.session.add_all(stores)
    db.session.flush()

    items = [
        # WRAPPER
        InventoryItem(name="DONUT WRAPPER - PLASTIC", category="WRAPPER", unit="PCS"),
        InventoryItem(name="DONUT WRAPPER PAPER - 2024", category="WRAPPER", unit="PCS"),
        InventoryItem(name="BUNWICH PAPER -BACON", category="WRAPPER", unit="PCS"),
        InventoryItem(name="BUNWICH PAPER - HAM & CHEESE/TUNA", category="WRAPPER", unit="PCS"),
        InventoryItem(name="SAVE A WRAP", category="WRAPPER", unit="PCS"),
        InventoryItem(name="GREASE PROOF PAPER", category="WRAPPER", unit="PCS"),
        
        # BAGS
        InventoryItem(name="MINI BAG BIODEGRADABLE (2024)", category="BAGS", unit="PCS"),
        InventoryItem(name="DUNKIN MINI PAPER BAG", category="BAGS", unit="PCS"),
        InventoryItem(name="SMALL BAG BIODEGRADABLE (2024)", category="BAGS", unit="PCS"),
        InventoryItem(name="DUNKIN SMALL PAPER BAG", category="BAGS", unit="PCS"),
        InventoryItem(name="ECO BAG 20X24", category="BAGS", unit="PCS"),
        InventoryItem(name='DUNKIN SMALL GIFT PAPER BAG W/ HANDLE (12.24" X 6.1" (W) X 3.94"(L)', category="BAGS", unit="PCS"),
        
        # BOXES
        InventoryItem(name="2024 SUPREME BUNDLE BOX", category="BOXES", unit="PCS"),
        InventoryItem(name="2024 AWESOME BUNDLE BOX)", category="BOXES", unit="PCS"),
        InventoryItem(name="2024 DOZEN BOX TWINE W/ HANDLE - (PEFC LOGO)", category="BOXES", unit="PCS"),
        InventoryItem(name="2025 GENERIC DONUT BOX BY 8", category="BOXES", unit="PCS"),
        InventoryItem(name="D8 - DUNKIN ANNIVERSARY BOX", category="BOXES", unit="PCS"),
        InventoryItem(name="DUNKIN YAN BOX - 2024", category="BOXES", unit="PCS"),
        InventoryItem(name="DONUT BOX BY 3", category="BOXES", unit="PCS"),
        InventoryItem(name="2023 PREMIUM BOX 6 PCS (PEFC LOGO)", category="BOXES", unit="PCS"),
        InventoryItem(name="LITTLE BUNCH BOX 2022 (PEFC LOGO)", category="BOXES", unit="PCS"),
        InventoryItem(name="DD MUNCHKINS BUCKET 2025", category="BOXES", unit="PCS"),
        InventoryItem(name="MUNCHKINS BUNCH 32", category="BOXES", unit="PCS"),
        InventoryItem(name="CHOCOBANG BOX", category="BOXES", unit="PCS"),
        InventoryItem(name="2024 VALENTINE BOX", category="BOXES", unit="PCS"),
        InventoryItem(name="2023 SAVORY BOX (PEFC LOGO)", category="BOXES", unit="PCS"),
        InventoryItem(name="2025 DONUT CUP-MAGENTA", category="BOXES", unit="PCS"),
        InventoryItem(name="2025 DONUT CUP-ORANGE", category="BOXES", unit="PCS"),
        InventoryItem(name="2024 D16  THEMATIC BOX - HAPPY BIRTHDAY", category="BOXES", unit="PCS"),
        InventoryItem(name="2024 D16  THEMATIC BOX - THANK YOU", category="BOXES", unit="PCS"),
        InventoryItem(name="2024 143 (3 X 3)", category="BOXES", unit="PCS"),
        InventoryItem(name="2026 D8 ENHYPEN A/R BOX", category="BOXES", unit="PCS"),
        
        # PAPER CUPS/LIDS
        InventoryItem(name="2024 12OZ ORANGE COLD CUPS (ECOPURE LOGO) FOR COFFEE", category="PAPER CUPS/LIDS", unit="PCS"),
        InventoryItem(name="2024 12OZ MAGENTA COLD CUPS (ECOPURE LOGO) FOR COFFEE", category="PAPER CUPS/LIDS", unit="PCS"),
        InventoryItem(name="2024 12OZ MOCHA COLD CUPS (ECOPURE LOGO) FOR COFFEE", category="PAPER CUPS/LIDS", unit="PCS"),
        InventoryItem(name="12OZ COLD CUPS - AMBER TERRAIN COFFEE (2025)", category="PAPER CUPS/LIDS", unit="PCS"),
        InventoryItem(name="12OZ COLD CUPS - YELLOW NON COFFEE (2025)", category="PAPER CUPS/LIDS", unit="PCS"),
        InventoryItem(name="2024 16OZ ORANGE COLD CUPS (ECOPURE LOGO) FOR COFFEE", category="PAPER CUPS/LIDS", unit="PCS"),
        InventoryItem(name="2024 16OZ MAGENTA COLD CUPS (ECOPURE LOGO) FOR COFFEE", category="PAPER CUPS/LIDS", unit="PCS"),
        InventoryItem(name="2024 16OZ MOCHA COLD CUPS (ECOPURE LOGO) FOR COFFEE", category="PAPER CUPS/LIDS", unit="PCS"),
        InventoryItem(name="16OZ COLD CUPS - AMBER TERRAIN COFFEE (2025)", category="PAPER CUPS/LIDS", unit="PCS"),
        InventoryItem(name="16OZ COLD CUPS - YELLOW NON COFFEE (2025)", category="PAPER CUPS/LIDS", unit="PCS"),
        InventoryItem(name="2024 22OZ ORANGE COLD CUPS (ECOPURE LOGO) - FOR MON COFFEE", category="PAPER CUPS/LIDS", unit="PCS"),
        InventoryItem(name="2024 22OZ MAGENTA COLD CUPS (ECOPURE LOGO) - FOR MON COFFEE", category="PAPER CUPS/LIDS", unit="PCS"),
        InventoryItem(name="2024 22OZ MOCHA COLD CUPS (ECOPURE LOGO) - FOR MON COFFEE", category="PAPER CUPS/LIDS", unit="PCS"),
        InventoryItem(name="22OZ COLD CUPS - AMBER TERRAIN COFFEE (2025)", category="PAPER CUPS/LIDS", unit="PCS"),
        InventoryItem(name="22OZ COLD CUPS - YELLOW NON COFFEE (2025)", category="PAPER CUPS/LIDS", unit="PCS"),
        InventoryItem(name="32OZ MAGENTA COLD CUPS", category="PAPER CUPS/LIDS", unit="PCS"),
        InventoryItem(name="32OZ BEIGE COLD CUPS", category="PAPER CUPS/LIDS", unit="PCS"),
        InventoryItem(name="12/16/22 OZ COLD FLAT LIDS (ECOPURE)", category="PAPER CUPS/LIDS", unit="PCS"),
        InventoryItem(name="12/16/22 OZ COLD DOME LIDS", category="PAPER CUPS/LIDS", unit="PCS"),
        InventoryItem(name="32OZ COLD FLAT LIDS", category="PAPER CUPS/LIDS", unit="PCS"),
        InventoryItem(name="BAGASSE DOME LIDS", category="PAPER CUPS/LIDS", unit="PCS"),
        InventoryItem(name="STRAWLESS LID", category="PAPER CUPS/LIDS", unit="PCS"),
        
        # HOT CUPS/LIDS
        InventoryItem(name="2025 ORANGE HOT CUPS 8OZ W/LIDS (ECOPURE LOGO)", category="HOT CUPS/LIDS", unit="PCS"),
        InventoryItem(name="2025 ORANGE HOT CUPS 12OZ W/LIDS (ECOPURE LOGO)", category="HOT CUPS/LIDS", unit="PCS"),
        InventoryItem(name="2024 HOT CUPS 16OZ W/LIDS (ECOPURE LOGO)", category="HOT CUPS/LIDS", unit="PCS"),
        InventoryItem(name="D'COFFEE BOX (4 CUPS)", category="HOT CUPS/LIDS", unit="PCS"),
        
        # BOWL CUPS/LIDS
        InventoryItem(name="2022 SOUP BOWL CUP W/ PRINT", category="BOWL CUPS/LIDS", unit="PCS"),
        InventoryItem(name="SOUP BOWL LID", category="BOWL CUPS/LIDS", unit="PCS"),
        InventoryItem(name="SOUP REHEATING STICKER", category="BOWL CUPS/LIDS", unit="PCS"),
        InventoryItem(name="SPOON BIODEGRADABLE", category="BOWL CUPS/LIDS", unit="PCS"),
        InventoryItem(name="2023 KRAFT SOUP BOWL W/LID", category="BOWL CUPS/LIDS", unit="PCS"),
        
        # OTHERS
        InventoryItem(name="ORANGE STRAW 32OZ", category="OTHERS", unit="PCS"),
        InventoryItem(name="2024 IND WRAPPED PAPER STRAW - ORANGE", category="OTHERS", unit="PCS"),
        InventoryItem(name="IND WRAPPED PAPER JELLO STRAW-ORANGE", category="OTHERS", unit="PCS"),
        InventoryItem(name="2021 BROWN PAPER NAKIN 10,000PCS/CASE", category="OTHERS", unit="PCS"),
        InventoryItem(name="CF FILTER (12CUPS)", category="OTHERS", unit="PCS"),
        InventoryItem(name="WOODEN COFFEE STIRRER", category="OTHERS", unit="PCS"),
        InventoryItem(name="PLASTIC STIRRER", category="OTHERS", unit="PCS"),
        InventoryItem(name="DRINK CADDY BIODEGRADABLE (2024)", category="OTHERS", unit="PCS"),
        InventoryItem(name="DD CUP SLEEVES - 2023", category="OTHERS", unit="PCS"),
        InventoryItem(name="HIGH DENSITY POLYETHYLENE TRANSPARENT (13X16.5) - BIODEGRADABLE", category="OTHERS", unit="PCS"),
        InventoryItem(name="HIGH DENSITY POLYETHYLENE MAGENTA (13X16.5) - BIODEGRADABLE", category="OTHERS", unit="PCS"),
        InventoryItem(name="HIGH DENSITY POLYETHYLENE GREEN (13X16.5) - BIODEGRADABLE", category="OTHERS", unit="PCS"),
        InventoryItem(name="COLORED STICKER (ROUND) (50 PCS/SHEET)", category="OTHERS", unit="PCS"),
        InventoryItem(name="CORNED BEEF STICKER (15PCS/SHEET)", category="OTHERS", unit="PCS"),
        InventoryItem(name="DUNKIN CHEESY JALAPEÑO CHUNKY TUNA STICKER (15PCS/SHEET)", category="OTHERS", unit="PCS"),
        InventoryItem(name="CLAYCO STICKER (5" DIA)", category="OTHERS", unit="PCS"),
        InventoryItem(name="FLAVORED ICED COFFEE - PENTAGON COUNTER/TABLE DISPLAY", category="OTHERS", unit="PCS"),
        InventoryItem(name="SPILL PROOF LINER", category="OTHERS", unit="PCS"),
        InventoryItem(name="VARIETY LABELS (GDI) - SHOP", category="OTHERS", unit="PCS"),
        InventoryItem(name="BIO KNIFE", category="OTHERS", unit="PCS"),
        InventoryItem(name="BIO FORK", category="OTHERS", unit="PCS"),
        
        # BUNWICH FILLINGS
        InventoryItem(name="BACON STRIPS 4 SLICES/PACK", category="BUNWICH FILLINGS", unit="PCS"),
        InventoryItem(name="SQUARE HAM 4 SLICES/PACK", category="BUNWICH FILLINGS", unit="PCS"),
        InventoryItem(name="PRO (CHEESE) 24PK/BOX 10PCS/PCK", category="BUNWICH FILLINGS", unit="PCS"),
        InventoryItem(name="MAYONAISE 470ML", category="BUNWICH FILLINGS", unit="PCS"),
        InventoryItem(name="TUNA FLAKES/CHUNKS - 180GMS", category="BUNWICH FILLINGS", unit="PCS"),
        InventoryItem(name="CATSUP PACKET 10 g", category="BUNWICH FILLINGS", unit="PCS"),
        InventoryItem(name="CHEEZ WHIZ PIMIENTO (105GMS)", category="BUNWICH FILLINGS", unit="PCS"),
        InventoryItem(name="MUSHROOMPIECES & STEMS (198 GMS)", category="BUNWICH FILLINGS", unit="PCS"),
        InventoryItem(name="JALAPEÑO CHEESE 120g", category="BUNWICH FILLINGS", unit="PCS"),
        InventoryItem(name="YELLOWFIN TUNA CHUNKS - 185GMS", category="BUNWICH FILLINGS", unit="PCS"),
        InventoryItem(name="SWEET PICKLE RELISH 270g", category="BUNWICH FILLINGS", unit="PCS"),
        InventoryItem(name="CANNED CORNED BEEF 150g", category="BUNWICH FILLINGS", unit="PCS"),
        InventoryItem(name="NORI FLAKES/PARSLEY FLAKES 80g", category="BUNWICH FILLINGS", unit="PCS"),
        InventoryItem(name="CHEEZE GLAZED", category="BUNWICH FILLINGS", unit="PCS"),
        InventoryItem(name="SHIITAKE SLICED MUSHROOM 198g", category="BUNWICH FILLINGS", unit="PCS"),
        InventoryItem(name="MAPLE SYRUP", category="BUNWICH FILLINGS", unit="PCS"),
        InventoryItem(name="CRUNCHY GARLIC BITS 160g", category="BUNWICH FILLINGS", unit="PCS"),
        InventoryItem(name="FRESHLY MINCED GARLIC 213g", category="BUNWICH FILLINGS", unit="PCS"),
        InventoryItem(name="CREAM CHEESE (220 GMS)", category="BUNWICH FILLINGS", unit="PCS"),
        InventoryItem(name="GARLIC MINCED 44g", category="BUNWICH FILLINGS", unit="PCS"),
        InventoryItem(name="SLICED BLACK OLIVES 140g", category="BUNWICH FILLINGS", unit="PCS"),
        InventoryItem(name="SPANISH SARDINES IN OLIVE  OIL 240g", category="BUNWICH FILLINGS", unit="PCS"),
        InventoryItem(name="WAFFLE MIX 1 KG", category="BUNWICH FILLINGS", unit="PCS"),
        
        # COFFEE
        InventoryItem(name="368GMS COFFEE (PACK)", category="HOT CHOCOLATE", unit="PCS"),
        InventoryItem(name="HRA COFFEE BEANS 500 GM/PACK", category="HOT CHOCOLATE", unit="PCS"),
        InventoryItem(name="DRIP COFFEE IN BOX (8 SH/BOX)", category="HOT CHOCOLATE", unit="PCS"),
        InventoryItem(name="PACKET CREAMER - 5 GMS", category="HOT CHOCOLATE", unit="PCS"),
        InventoryItem(name="SUGAR STICK TYPE - 6 GMS", category="HOT CHOCOLATE", unit="PCS"),
        InventoryItem(name="BROWN SUGAR", category="HOT CHOCOLATE", unit="PCS"),
        InventoryItem(name="CASTER SUGAR", category="HOT CHOCOLATE", unit="PCS"),
        InventoryItem(name="FRESH MILK", category="HOT CHOCOLATE", unit="PCS"),
        InventoryItem(name="CONDENSE MILK (PC-ANGELS)", category="HOT CHOCOLATE", unit="PCS"),
        InventoryItem(name="SPLENDA SUGAR (1000/BOX)", category="HOT CHOCOLATE", unit="PCS"),
        InventoryItem(name="SUGAR FREE SYRUP (2.1g)", category="HOT CHOCOLATE", unit="PCS"),
        InventoryItem(name="GREAT TASTE COFFEE GRANULES 20GMS", category="HOT CHOCOLATE", unit="PCS"),

        # HOT CHOCOLATE
        InventoryItem(name="HOT CHOCO POWDER (38grms/pc)", category="OTHER BEVERAGES", unit="PCS"),
        InventoryItem(name="STRAWBERRY SYRUP 1L", category="OTHER BEVERAGES", unit="PCS"),
        InventoryItem(name="VIVO WHIPPING CREAM 1.1 LTR", category="OTHER BEVERAGES", unit="PCS"),
               
        # DUNKCREATION
        InventoryItem(name="MINERAL WATER 500ML", category="DUNKCREATION", unit="PCS"),
        
        # SOFTDRINKS
        InventoryItem(name="COKE 1.5", category="SOFTDRINKS", unit="PCS"),
        InventoryItem(name="SPRITE IN CAN", category="SOFTDRINKS", unit="PCS"),
        InventoryItem(name="PREMIUM MATCHA POWDER 1kg", category="SOFTDRINKS", unit="PCS"),
        InventoryItem(name="PT STRAWBERRY", category="SOFTDRINKS", unit="PCS"),
        InventoryItem(name="CAFÉ SYRUP 700ml", category="SOFTDRINKS", unit="PCS"),
        InventoryItem(name="NSA PREMIUM DARK CHOCOLATE 1KG", category="SOFTDRINKS", unit="PCS"),
        
        # OTHER BEVERAGES
        InventoryItem(name="ROASTED ALMOND FLAVORED SYRUP", category="OTHER BEVERAGES", unit="PCS"),
        InventoryItem(name="ICY CHOCO POWDER (51g/oc)", category="OTHER BEVERAGES", unit="PCS"),
        InventoryItem(name="JOLLY CREAM CORN 425G", category="OTHER BEVERAGES", unit="PCS"),
        InventoryItem(name="ICY ORANGE POWDER (7 GMS)", category="OTHER BEVERAGES", unit="PCS"),
        InventoryItem(name="RICOA LIQUID CHOCO - 600ml", category="OTHER BEVERAGES", unit="PCS"),
        InventoryItem(name="OATSIDE MILK 1LTR", category="OTHER BEVERAGES", unit="PCS"),
        InventoryItem(name="LYCHEE IN SYRUP 565g", category="OTHER BEVERAGES", unit="PCS"),
        InventoryItem(name="POPPING TEA TAPIOCA PEARL", category="OTHER BEVERAGES", unit="PCS"),
        InventoryItem(name="SALTED CARAMEL SAUCE 2L", category="OTHER BEVERAGES", unit="PCS"),
        InventoryItem(name="MATCHA POWDER", category="OTHER BEVERAGES", unit="PCS"),
        InventoryItem(name="PT NON-DAIRY CREAMER", category="OTHER BEVERAGES", unit="PCS"),
        InventoryItem(name="CHOCO POWDER -1 KG", category="OTHER BEVERAGES", unit="PCS"),
        InventoryItem(name="CORN FLAKES CEREAL 150GRMS", category="OTHER BEVERAGES", unit="PCS"),
        InventoryItem(name="BROWN BUTTER SYRUP 700ml", category="OTHER BEVERAGES", unit="PCS"),
        InventoryItem(name="SWEET CORN FREEZE MIX 1KG", category="OTHER BEVERAGES", unit="PCS"),
        InventoryItem(name="DALANDAN (READY TO DRINK)", category="OTHER BEVERAGES", unit="PCS"),
        InventoryItem(name="HAZELNUT FLAVORED SYRUP 750ML", category="OTHER BEVERAGES", unit="PCS"),
        InventoryItem(name="SHOTTS VANILLA SYRUP 750ml", category="OTHER BEVERAGES", unit="PCS"),
        InventoryItem(name="FRENCH VANILLA SYRUP 700ML", category="OTHER BEVERAGES", unit="PCS"),
        InventoryItem(name="MACADAMIA SYRUP 1L", category="OTHER BEVERAGES", unit="PCS"),
        InventoryItem(name="HALO HALO MIX 360g", category="OTHER BEVERAGES", unit="PCS"),
        InventoryItem(name="PT TARO POWDER", category="OTHER BEVERAGES", unit="PCS"),
        
        # MINERAL WATER
        InventoryItem(name="PURIFIED WATER", category="MINERAL WATER", unit="PCS"),
        
        # PROMO ITEM
        InventoryItem(name="MOCHI PILLOWS", category="PROMO ITEM", unit="PCS"),
        InventoryItem(name="BLINGKINS BAVARIAN MUNCHKIN", category="PROMO ITEM", unit="PCS"),
        InventoryItem(name="BAVARIAN FILLED DONUT PILLOW", category="PROMO ITEM", unit="PCS"),
        InventoryItem(name="3 FOLDS UMBRELLA", category="PROMO ITEM", unit="PCS"),
        InventoryItem(name="GOLF UMBRELLA", category="PROMO ITEM", unit="PCS"),
        InventoryItem(name="DUNKIN YAN PILLOW-STRAWBERRY", category="PROMO ITEM", unit="BOX"),
        InventoryItem(name="DUNKIN YAN PILLOW-CHOCOLATE", category="PROMO ITEM", unit="PCS"),
        InventoryItem(name="23" UMBRELLA WITH 12 PANELS (MAGENTA)", category="PROMO ITEM", unit="PCS"),
        InventoryItem(name="23" UMBRELLA WITH 12 PANELS (ORANGE)", category="PROMO ITEM", unit="PCS"),
        InventoryItem(name="2026 BWS POGI CARD 1", category="PROMO ITEM", unit="PCS"),
        InventoryItem(name="BIG BALLOONS 12" W/LOGO", category="PROMO ITEM", unit="PCS"),
        InventoryItem(name="SMALL BALLOONS 6"", category="PROMO ITEM", unit="PCS"),
        InventoryItem(name="2026 BWS POGI CARD 2", category="PROMO ITEM", unit="PCS"),
        InventoryItem(name="STICKS/CAPS", category="PROMO ITEM", unit="PCS"),
        InventoryItem(name="2026 MYSTERY LOCK CHARM", category="PROMO ITEM", unit="PCS"),
        InventoryItem(name="BEAR (VALENTINE)", category="PROMO ITEM", unit="PCS"),
        InventoryItem(name="BEAR (CHRISTMAS)", category="PROMO ITEM", unit="PCS"),
        InventoryItem(name="DUNKIN S/S FLASK WITH STRAW", category="PROMO ITEM", unit="BOX"),
        InventoryItem(name="BWS GLASS MUG", category="PROMO ITEM", unit="PCS"),
        InventoryItem(name="GLASS CUP W/O HANDLE 400ML", category="PROMO ITEM", unit="PCS"),
        InventoryItem(name="POP MATCH MEMORY GAME", category="PROMO ITEM", unit="PCS"),
        InventoryItem(name="DUNKIN' HEART CHOCO BUTTERNUT PILLOW", category="PROMO ITEM", unit="PCS"),
        InventoryItem(name="BLUE CHAPTER PILLOW - BAVARIAN", category="PROMO ITEM", unit="PCS"),
        InventoryItem(name="BLUE CHAPTER PILLOW - STRAWBERRY", category="PROMO ITEM", unit="PCS"),
            
        # CLEANING MATERIALS
        InventoryItem(name="KAY QSR MULTI PURPOSE SINK DETERGENT", category="CLEANING MATERIALS", unit="PCS"),
        InventoryItem(name="KAY HANDWASH (2019)", category="CLEANING MATERIALS", unit="PCS"),
        InventoryItem(name="KAY SINK SANITIZER TABLET", category="CLEANING MATERIALS", unit="PCS"),
        InventoryItem(name="KAY CHLORINE TEST STRIPS", category="CLEANING MATERIALS", unit="PCS"),
        InventoryItem(name="ZZ COOPERMATIC", category="CLEANING MATERIALS", unit="PCS"),
        InventoryItem(name="DISPOSABLE PLASTIC GLOVES", category="CLEANING MATERIALS", unit="PCS"),
        InventoryItem(name="DISPOSABLE PAPER TOWEL (175/PCK)", category="CLEANING MATERIALS", unit="PCS"),
        InventoryItem(name="PLASTIC TRASH BAG - BLACK", category="CLEANING MATERIALS", unit="PCS"),
        InventoryItem(name="PLASTIC TRASH BAG (CLEAR)", category="CLEANING MATERIALS", unit="PCS"),
        InventoryItem(name="RAGS", category="CLEANING MATERIALS", unit="PCS"),
        InventoryItem(name="MOPHEAD", category="CLEANING MATERIALS", unit="PCS"),
        InventoryItem(name="MOPHANDLE", category="CLEANING MATERIALS", unit="PCS"),
        InventoryItem(name="QSR RESTROOM CLEANER 1 LTR", category="CLEANING MATERIALS", unit="PCS"),
        InventoryItem(name="DELIMING", category="CLEANING MATERIALS", unit="PCS"),
        InventoryItem(name="RUBBERMAID BRUSH", category="CLEANING MATERIALS", unit="PCS"),
        InventoryItem(name="GLASS PANEL", category="CLEANING MATERIALS", unit="PCS"),
        InventoryItem(name="DONUT JACKET BROWN W/O LOG - BIG", category="CLEANING MATERIALS", unit="PCS"),
        InventoryItem(name="DR. COFFEE MILK SYSTEM CLEANING TABLET (120 TABLET/BOTTLE)", category="CLEANING MATERIALS", unit="PCS"),
        InventoryItem(name="FALCON UV FLYTRAP W/ GLUEBOARD", category="CLEANING MATERIALS", unit="PCS"),
        InventoryItem(name="GLUE TRAP BOARD ", category="CLEANING MATERIALS", unit="PCS"),
        InventoryItem(name=" KAY QSR HEAVY DUTY DEGREASER", category="CLEANING MATERIALS", unit="PCS"),
        InventoryItem(name=" KAY QSR QUARRY TILE FLOOR CLEANER", category="CLEANING MATERIALS", unit="PCS"),
        InventoryItem(name=" KAY GLASS & MULTISURFACE CLEANER", category="CLEANING MATERIALS", unit="PCS"),
        InventoryItem(name=" KAY DELIMER - 2oz", category="CLEANING MATERIALS", unit="PCS"),
        
        # OFFICE SUPPLIES
        InventoryItem(name="JOURNAL TAPE (76mm)", category="OFFICE SUPPLIES", unit="PCS"),
        InventoryItem(name="CRT - BIG", category="OFFICE SUPPLIES", unit="PCS"),
        InventoryItem(name="ERC-03 RIBBON REFILL ", category="OFFICE SUPPLIES", unit="PCS"),
        InventoryItem(name="THERMAL PAPER IBM 514 (80X70)", category="OFFICE SUPPLIES", unit="PCS"),
        InventoryItem(name="SCOTCH TAPE", category="OFFICE SUPPLIES", unit="PCS"),
        InventoryItem(name="SENIOR CITIZEN", category="OFFICE SUPPLIES", unit="PCS"),
        InventoryItem(name="TIMECARD", category="OFFICE SUPPLIES", unit="PCS"),
        InventoryItem(name="CALCULATOR", category="OFFICE SUPPLIES", unit="PCS"),
        InventoryItem(name="STAPLER", category="OFFICE SUPPLIES", unit="PCS"),
        InventoryItem(name="RUBBER STAMP", category="OFFICE SUPPLIES", unit="PCS"),
        InventoryItem(name="PLASTIC COIN", category="OFFICE SUPPLIES", unit="PCS"),
        InventoryItem(name="PRICE LABELLER TAPE", category="OFFICE SUPPLIES", unit="PCS"),

        # UTENSILS
        InventoryItem(name="PLASTIC TRAY - IVORY", category="UTENSILS", unit="PCS"),
        InventoryItem(name="PLASTIC PITCHER (1775 ML)", category="UTENSILS", unit="PCS"),
        InventoryItem(name="PLASTIC PITCHER FOR COLD BREW", category="UTENSILS", unit="PCS"),
        InventoryItem(name="STAINLESS PITCHER FOR DELONGHI MACHINE", category="UTENSILS", unit="PCS"),
        InventoryItem(name="TONG 12" (MEDIUM)", category="UTENSILS", unit="PCS"),
        InventoryItem(name="VOLLRATH TONG (RED/GREEN)", category="UTENSILS", unit="PCS"),
        InventoryItem(name="FOOD FAN (CAMBRO)", category="UTENSILS", unit="PCS"),
        InventoryItem(name="CAMBRO 60CWCH* CAMWEAR 1/6 COVER W/HANDLE,CLR- 1005224", category="UTENSILS", unit="PCS"),
        InventoryItem(name="MAYO SQUEEZER", category="UTENSILS", unit="PCS"),
        InventoryItem(name="BREAD KNIFE", category="UTENSILS", unit="PCS"),
        InventoryItem(name="FINISHERS SPATULA", category="UTENSILS", unit="PCS"),
        InventoryItem(name="ICED COFFEE POT 1.6LTRS", category="UTENSILS", unit="PCS"),
        InventoryItem(name="ICED COFFEE SHAKER", category="UTENSILS", unit="PCS"),
        InventoryItem(name="WHIRE WHISK", category="UTENSILS", unit="PCS"),
        InventoryItem(name="BUNN THERMOS CARAFE", category="UTENSILS", unit="PCS"),
        InventoryItem(name="COOPER DIGITAL POCKET THERMOMETER (MODEL: DFP 450W)", category="UTENSILS", unit="PCS"),
        InventoryItem(name="COFFEE TIMER CT-40", category="UTENSILS", unit="PCS"),
        InventoryItem(name="COFFEE FILTER CONTAINER", category="UTENSILS", unit="PCS"),
        InventoryItem(name="SQUEEZEE DISPENSER-24 OZ", category="UTENSILS", unit="PCS"),
        InventoryItem(name="BAR SPOON W/TWISTED HANDLE", category="UTENSILS", unit="PCS"),
        InventoryItem(name="JIGGER FOR ICED COFFEE 25X50GRAMS", category="UTENSILS", unit="PCS"),
        InventoryItem(name="ASTDA MEASURING CUP 250ml", category="UTENSILS", unit="PCS"),
        InventoryItem(name="PLASTIC BEAKER-4 QTZ CAP", category="UTENSILS", unit="PCS"),
        InventoryItem(name="FOOD FAN 1/9 X 2.5" I CODE:JD-P1906", category="UTENSILS", unit="PCS"),
        InventoryItem(name="FOOD FAN 1/6 X 4" I CODE:JD-P1610", category="UTENSILS", unit="PCS"),
        InventoryItem(name="FOOD FAN COVER 1/6 I CODE:JD-P1601", category="UTENSILS", unit="PCS"),
        InventoryItem(name="POPPING TEA JIGGER", category="UTENSILS", unit="PCS"),
        InventoryItem(name="FOOD FAN COVER 1/9 I CODE:JD-P1901", category="UTENSILS", unit="PCS"),
        InventoryItem(name="FOOD FAN COVER 1/9 X 4" I CODE:JD-P1910", category="UTENSILS", unit="PCS"),
        InventoryItem(name="SQUEEZEE DISPENSER 3 HEAD", category="UTENSILS", unit="PCS"),
        InventoryItem(name="SQUEEZEE DISPENSER-12 OZ", category="UTENSILS", unit="PCS"),
        InventoryItem(name="POPPING TEA PLASTIC COLANDER BIG", category="UTENSILS", unit="PCS"),
        InventoryItem(name="POPPING TEA POWDER MIX SCOOPER", category="UTENSILS", unit="PCS"),
        InventoryItem(name="POPPING TEA S/S DRIP PAN", category="UTENSILS", unit="PCS"),
        InventoryItem(name="POPPING TEA S/S TRAY", category="UTENSILS", unit="PCS"),
        InventoryItem(name="POPPING TEA SHAKER", category="UTENSILS", unit="PCS"),
        InventoryItem(name="VOLLRATH DISHER PORTION-SIZE 24 (RED)", category="UTENSILS", unit="PCS"),
        InventoryItem(name="POPPING TEA STRAINER", category="UTENSILS", unit="PCS"),
        InventoryItem(name="POPPING TEA FOOD CONTAINER", category="UTENSILS", unit="PCS"),
        InventoryItem(name="POPPING TEA FOOD CONTAINER COVER", category="UTENSILS", unit="PCS"),
        InventoryItem(name="SHOT GLASS", category="UTENSILS", unit="PCS"),
        InventoryItem(name="TONG CONTAINER" I CODE:JD-P1610", category="UTENSILS", unit="PCS"),
        InventoryItem(name="TONG HOLDER", category="UTENSILS", unit="PCS"),
        InventoryItem(name="DESCALER (FOR PRIMA DONNA ESPRESSO MACHINE)", category="UTENSILS", unit="PCS"),
        InventoryItem(name="ICE SCOOPER HOLDER", category="UTENSILS", unit="PCS"),
        InventoryItem(name="ICE SCOOPER STAINLESS", category="UTENSILS", unit="PCS"),
        InventoryItem(name="VOLLRATH DISHER PORTION-SIZE 40 (ORCHID)", category="UTENSILS", unit="PCS"),

        # MISCELLANEOUS
        InventoryItem(name="MEDICAL KIT", category="MISCELLANEOUS", unit="PCS"),
        InventoryItem(name="DONUT BASKET", category="MISCELLANEOUS", unit="PCS"),
        InventoryItem(name="MONEY DETECTOR", category="MISCELLANEOUS", unit="PCS"),
        InventoryItem(name="PURGE DISPENSER", category="MISCELLANEOUS", unit="PCS"),
        InventoryItem(name="STRAW DISPENSER", category="MISCELLANEOUS", unit="PCS"),
        InventoryItem(name="PAPER TOWEL DISPENSER", category="MISCELLANEOUS", unit="PCS"),
        InventoryItem(name="PRICE LABELLER", category="MISCELLANEOUS", unit="PCS"),
        InventoryItem(name="WET FLOOR SIGN", category="MISCELLANEOUS", unit="PCS"),
        InventoryItem(name="PUMP (BALLOONS)", category="MISCELLANEOUS", unit="PCS"),
        InventoryItem(name="S/S DISPLAY CHROME BASKET (1/4)", category="MISCELLANEOUS", unit="PCS"),
        InventoryItem(name="DISPLAY CHROME BASKET L:24" X W:8.5" X H:2" (1/2)", category="MISCELLANEOUS", unit="PCS"),
        InventoryItem(name="STRAINER FOR COCOA POWDER DISPENSER-SMALL", category="MISCELLANEOUS", unit="PCS"),
        InventoryItem(name="LOCK AND LOCK OVEN GLASS", category="MISCELLANEOUS", unit="PCS"),
        InventoryItem(name="S/S CUP DISPENSER", category="MISCELLANEOUS", unit="PCS"),
        InventoryItem(name="COCOA POWDER DISPENSER W/COVER", category="MISCELLANEOUS", unit="PCS"),
        InventoryItem(name="BAKING SPRAY 600ml", category="MISCELLANEOUS", unit="PCS"),
        InventoryItem(name="EKA HALOGEN BULB (40W-230W G9 300C)", category="MISCELLANEOUS", unit="PCS"),
        InventoryItem(name="BOSTON KREME STAINLESS LATTE ART STENCIL", category="MISCELLANEOUS", unit="PCS"),
        
    ]
    
    db.session.add_all(items)

    # Gawin lamang ito kung wala pang admin user
    if not User.query.filter_by(username="admin").first():
        admin = User(username="admin", role="admin")
        admin.set_password("admin123")
        db.session.add(admin)

    for s in stores:
        username = s.name.lower().replace(" ", "")
        if not User.query.filter_by(username=username).first():
            u = User(username=username, role="store", store=s)
            u.set_password("store123")
            db.session.add(u)

    db.session.commit()
