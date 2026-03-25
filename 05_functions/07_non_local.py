def update_order():
    chai_type = "Elaichi"

    def kitchen():
        nonlocal chai_type
        # nonlocal keyword is used to modify the variable defined in the nearest enclosing scope
        chai_type = "Kesar"

    kitchen()
    print("after kitchen update", chai_type)

update_order()