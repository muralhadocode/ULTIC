i = True
while i == True:
    print("Welcome to the ultimate converter :D")
    print("1. Metric compriment system converter")  # make this and below this one thing
    print("2. Imperial compriment system converter")
    print("3. Time converter")
    print("4. Metric velocity system converter")  # make this and below this one thing
    print("5. Imperial velocity system converter")
    print("6. Metric mass system converter")  # make this and below this one thing
    print("7. Imperial mass system converter")
    print("8. Metric volume system converter")  # make this and below this one thing
    print("9. Imperial volume system converter")
    print("10. Metric area system converter")  # make this and below this one thing
    print("11. Imperial area system converter")

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
    metric_velocity_onms = {
        "mm/s": 0.001,
        "cm/s": 0.01,
        "m/s": 1.0,
        "km/h": 0.277778,
        "km/s": 1000.0,
    }
    imperial_velocity_onmph = {
        "ft/s": 0.681818,
        "mph": 1.0,
        "knot": 1.15078,
        "mach": 767.269,
    }
    metric_mass_ong = {
        "mcg": 0.000001,
        "mg": 0.001,
        "cg": 0.01,
        "dg": 0.1,
        "g": 1.0,
        "dag": 10.0,
        "hg": 100.0,
        "kg": 1000.0,
        "tonne": 1000000.0,
    }
    imperial_mass_onpound = {
        "grain": 0.000142857,
        "dram": 0.0027344,
        "ounce": 0.0625,
        "pound": 1.0,
        "stone": 14.0,
        "quarter": 28.0,
        "hundredweight": 112.0,
        "cwt": 112.0,
        "ton": 2240.0,
        "imperial ton": 2240.0,
    }
    metric_volume_onl = {
        "ml": 0.001,
        "cl": 0.01,
        "dl": 0.1,
        "l": 1.0,
        "m³": 1000.0,
        "m3": 1000.0,
    }
    imperial_volume_ongallon = {
        "fl oz": 0.0078125,
        "fluid ounce": 0.0078125,
        "cup": 0.0625,
        "pint": 0.125,
        "quart": 1.0,
    }
    metric_area_onm2 = {
        "mm²": 0.000001,
        "mm2": 0.000001,
        "cm²": 0.0001,
        "cm2": 0.0001,
        "dm²": 0.01,
        "dm2": 0.01,
        "m²": 1.0,
        "m2": 1.0,
        "are": 100.0,
        "hectare": 10000.0,
        "km²": 1000000.0,
        "km2": 1000000.0,
    }
    imperial_area_onacre = {
        "sq inch": 0.000000159,
        "inch2": 0.000000159,
        "inch²": 0.000000159,
        "sq foot": 0.0000229568,
        "foot2": 0.0000229568,
        "foot²": 0.0000229568,
        "sq yard": 0.000206612,
        "yard2": 0.000206612,
        "yard²": 0.000206612,
        "acre": 1.0,
        "sq mile": 640.0,
        "mile2": 640.0,
        "mile²": 640,
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
        unit = metric_velocity_onms.get(unit_slct)
        unit_value = float(input("Type the unit value: "))
        unit_slct2 = input("Type the unit of destiny: ")
        unit_dest = metric_velocity_onms.get(unit_slct2)
        unit_in_standard = unit_value * unit
        unit_real = unit_in_standard / unit_dest
        print(f"{unit_value}{unit_slct} = {unit_real}{unit_slct2}")
    elif slct == 5:
        unit_slct = input("Type the unit you want to convert: ")
        unit = imperial_velocity_onmph.get(unit_slct)
        unit_value = float(input("Type the unit value: "))
        unit_slct2 = input("Type the unit of destiny: ")
        unit_dest = imperial_velocity_onmph.get(unit_slct2)
        unit_in_standard = unit_value * unit
        unit_real = unit_in_standard / unit_dest
        print(f"{unit_value}{unit_slct} = {unit_real}{unit_slct2}")
    elif slct == 6:
        unit_slct = input("Type the unit you want to convert: ")
        unit = metric_mass_ong.get(unit_slct)
        unit_value = float(input("Type the unit value: "))
        unit_slct2 = input("Type the unit of destiny: ")
        unit_dest = metric_mass_ong.get(unit_slct2)
        unit_in_standard = unit_value * unit
        unit_real = unit_in_standard / unit_dest
        print(f"{unit_value}{unit_slct} = {unit_real}{unit_slct2}")
    elif slct == 7:
        unit_slct = input("Type the unit you want to convert: ")
        unit = imperial_mass_onpound.get(unit_slct)
        unit_value = float(input("Type the unit value: "))
        unit_slct2 = input("Type the unit of destiny: ")
        unit_dest = imperial_mass_onpound.get(unit_slct2)
        unit_in_standard = unit_value * unit
        unit_real = unit_in_standard / unit_dest
        print(f"{unit_value}{unit_slct} = {unit_real}{unit_slct2}")
    elif slct == 8:
        unit_slct = input("Type the unit you want to convert: ")
        unit = metric_volume_onl.get(unit_slct)
        unit_value = float(input("Type the unit value: "))
        unit_slct2 = input("Type the unit of destiny: ")
        unit_dest = metric_volume_onl.get(unit_slct2)
        unit_in_standard = unit_value * unit
        unit_real = unit_in_standard / unit_dest
        print(f"{unit_value}{unit_slct} = {unit_real}{unit_slct2}")
    elif slct == 9:
        unit_slct = input("Type the unit you want to convert: ")
        unit = imperial_volume_ongallon.get(unit_slct)
        unit_value = float(input("Type the unit value: "))
        unit_slct2 = input("Type the unit of destiny: ")
        unit_dest = imperial_volume_ongallon.get(unit_slct2)
        unit_in_standard = unit_value * unit
        unit_real = unit_in_standard / unit_dest
        print(f"{unit_value}{unit_slct} = {unit_real}{unit_slct2}")
    elif slct == 10:
        unit_slct = input("Type the unit you want to convert: ")
        unit = metric_area_onm2.get(unit_slct)
        unit_value = float(input("Type the unit value: "))
        unit_slct2 = input("Type the unit of destiny: ")
        unit_dest = metric_area_onm2.get(unit_slct2)
        unit_in_standard = unit_value * unit
        unit_real = unit_in_standard / unit_dest
        print(f"{unit_value}{unit_slct} = {unit_real}{unit_slct2}")
    elif slct == 11:
        unit_slct = input("Type the unit you want to convert: ")
        unit = imperial_area_onacre.get(unit_slct)
        unit_value = float(input("Type the unit value: "))
        unit_slct2 = input("Type the unit of destiny: ")
        unit_dest = imperial_area_onacre.get(unit_slct2)
        unit_in_standard = unit_value * unit
        unit_real = unit_in_standard / unit_dest
        print(f"{unit_value}{unit_slct} = {unit_real}{unit_slct2}")
    elif slct == 20:
        i = False
