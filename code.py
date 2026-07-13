i = True
while i == True:
    print("Welcome to the ultimate converter :D")
    print("1. Metric system converter")
    print("2. Imperial system converter")
    print("3. Time converter")
    print("4. Velocity converter")
    slct = int(input("Input the number of the area you want to go: "))
    metric_compriment_onm = {
        "mm": 0.001,
        "cm": 0.01,
        "dm": 0.1,
        "m": 1.0,
        "dam": 10.0,
        "hm": 100.0,
        "km": 1000.0,
    }
    imperial_compriment_onyard = {
        "inch": 0.027778,
        "foot": 0.333333,
        "yard": 1.0,
        "chain": 22.0,
        "furlong": 220.0,
        "mile": 1760.0,
        "league": 5280.0,
    }
    time_units_ons = {
        "nano": 0.000000001,
        "micro": 0.000001,
        "milli": 0.001,
        "s": 1.0,
        "min": 60.0,
        "hour(s)": 3600.0,
        "day(s)": 86400.0,
        "month(s)": 2629746.0,
        "year(s)": 31557600.0,
    }
    velocity_units_onms = {
        "m/s": 1.0,
        "km/h": 0.277778,
        "mph": 0.44704,
        "knot": 0.514444,
        "ft/s": 0.3048,
        "mach": 343.0,
    }

    if slct == 1:
        unit_slct = input("Type the unit you want to convert: ")
        unit = metric_compriment_onm.get(unit_slct)
        unit_value = float(input("Type the unit value: "))
        unit_slct2 = input("Type the unit of destiny: ")
        unit_dest = metric_compriment_onm.get(unit_slct2)
        unit_in_standard = unit_value * unit
        unit_real = unit_in_standard / unit_dest
        print(f"{unit_value}{unit_slct} = {unit_real}{unit_slct2}")
    elif slct == 2:
        unit_slct = input("Type the unit you want to convert: ")
        unit = imperial_compriment_onyard.get(unit_slct)
        unit_value = float(input("Type the unit value: "))
        unit_slct2 = input("Type the unit of destiny: ")
        unit_dest = imperial_compriment_onyard.get(unit_slct2)
        unit_in_standard = unit_value * unit
        unit_real = unit_in_standard / unit_dest
        print(f"{unit_value}{unit_slct} = {unit_real}{unit_slct2}")
    elif slct == 3:
        unit_slct = input("Type the unit you want to convert: ")
        unit = time_units_ons.get(unit_slct)
        unit_value = float(input("Type the unit value: "))
        unit_slct2 = input("Type the unit of destiny: ")
        unit_dest = time_units_ons.get(unit_slct2)
        unit_in_standard = unit_value * unit
        unit_real = unit_in_standard / unit_dest
        print(f"{unit_value}{unit_slct} = {unit_real}{unit_slct2}")
    elif slct == 4:
        unit_slct = input("Type the unit you want to convert: ")
        unit = velocity_units_onms.get(unit_slct)
        unit_value = float(input("Type the unit value: "))
        unit_slct2 = input("Type the unit of destiny: ")
        unit_dest = velocity_units_onms.get(unit_slct2)
        unit_in_standard = unit_value * unit
        unit_real = unit_in_standard / unit_dest
        print(f"{unit_value}{unit_slct} = {unit_real}{unit_slct2}")
    elif slct == 5:
        i = False
