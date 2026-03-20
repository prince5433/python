def make_chai():
    if not kettle_has_water():6
        fill_kettle()
    plug_in_kettle()
    boil_water()
    if not is_cup_clean():
        wash_cup()
    add_to_cup("sugar")
    add_to_cup("tea leaves")
    pour("boiled water")
    stir("cup")
    serve("chai")

make_chai()//
