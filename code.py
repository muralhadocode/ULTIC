i = True
while i == True:
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
    digital_data_onbit = {
        "bit": 1.0,
        "byte": 8.0,
        "kilobit": 1000.0,
        "kb": 1000.0,
        "kilobyte": 8000.0,
        "KB": 8000.0,
        "megabit": 1000000.0,
        "Mb": 1000000.0,
        "megabyte": 8000000.0,
        "MB": 8000000.0,
        "gigabit": 1000000000.0,
        "Gb": 1000000000.0,
        "gigabyte": 8000000000.0,
        "GB": 8000000000.0,
        "terabyte": 8000000000000.0,
        "TB": 8000000000000.0,
        "kibibyte": 8192.0,
        "KiB": 8192.0,
        "mebibyte": 8388608.0,
        "MiB": 8388608.0,
        "gibibyte": 8589934592.0,
        "GiB": 8589934592,
    }
    angle_ondegree = {
        "degree": 1.0,
        "°": 1.0,
        "radian": 57.2958,
        "gradian": 0.9,
        "grad": 0.9,
        "gon": 0.9,
        "arcminute": 0.0166667,
        "'": 0.0166667,
        "arcsecond": 0.000277778,
        '"': 0.000277778,
        "turn": 360.0,
        "full revolution": 360.0,
    }
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
        "qt": 0.25,
        "quart": 0.25,
        "gallon": 1.0,
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
        "a": 100.0,
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
    metric_pressure_onpascal = {
        "pascal": 1.0,
        "Pa": 1.0,
        "hectopascal": 100.0,
        "hPa": 100.0,
        "kilopascal": 1000.0,
        "kPa": 1000.0,
        "bar": 100000.0,
        "atmosphere": 101325.0,
        "atm": 101325.0,
    }
    imperial_pressure_onpsi = {
        "psi": 1.0,
        "ksi": 1000.0,
        "inHg": 0.491154,
        "mmHg": 0.0193368,
    }
    metric_energy_onjoule = {
        "joule": 1.0,
        "J": 1.0,
        "kilojoule": 1000.0,
        "kJ": 1000.0,
        "calorie": 4.184,
        "cal": 4.184,
        "kilocalorie": 4184.0,
        "kcal": 4184.0,
        "watt-hour": 3600.0,
        "Wh": 3600.0,
        "kilowatt-hour": 3600000.0,
        "kWh": 3600000.0,
    }
    imperial_energy_onbtu = {
        "BTU": 1.0,
        "foot-pound": 0.000778169,
        "ft-lb": 0.000778169,
        "therm": 100000.0,
        "thm": 100000.0,
    }
    metric_power_onwatt = {
        "watt": 1.0,
        "W": 1.0,
        "kilowatt": 1000.0,
        "kW": 1000.0,
        "megawatt": 1000000.0,
        "MW": 1000000.0,
        "milliwatt": 0.001,
        "mW": 0.001,
    }
    imperial_power_onhp = {
        "horsepower": 1.0,
        "hp": 1.0,
        "BTU per hour": 0.0003930,
        "BTU/h": 0.0003930,
        "foot-pound per second": 0.00181818,
        "ft-lb/s": 0.00181818,
    }
    metric_force_onnewton = {
        "newton": 1.0,
        "N": 1.0,
        "kilonewton": 1000.0,
        "kN": 1000.0,
        "dyne": 0.00001,
        "dyn": 0.00001,
        "kilogram-force": 9.80665,
        "kgf": 9.80665,
    }
    imperial_force_onlbf = {
        "pound-force": 1.0,
        "lbf": 1.0,
        "ounce-force": 0.0625,
        "poundal": 0.0310810,
    }
    print("Welcome to the ultimate converter :D")
    print("!!PLEASE READ THE README.md SO YOU DONT MAKE WRONG MOVES!!")
    print("1. Metric system conversion")
    print("2. Imperial system conversion")
    print("3. Other conversions")
    slct_prim = int(input("Type the number of the converter you want to go: "))
    if slct_prim == 1:
        print("1. Metric compriment system converter")
        print("2. Metric velocity system converter")
        print("3. Metric mass system converter")
        print("4. Metric volume system converter")
        print("5. Metric area system converter")
        print("6. Metric pressure system converter")
        print("7. Metric energy system converter")
        print("8. Metric power system converter")
        print("9. Metric force system converter")
        print("10. Go back")
        slct_sec = int(input("Input the number of the area you want to go: "))
        if slct_sec == 1:
            unit_slct = input("Type the unit you want to convert: ")
            unit = metric_compriment_onm.get(unit_slct)
            unit_value = float(input("Type the unit value: "))
            unit_slct2 = input("Type the unit of destiny: ")
            unit_dest = metric_compriment_onm.get(unit_slct2)
            unit_in_standard = unit_value * unit
            unit_real = unit_in_standard / unit_dest
            print(f"{unit_value}{unit_slct} = {unit_real}{unit_slct2}")
        elif slct_sec == 2:
            unit_slct = input("Type the unit you want to convert: ")
            unit = metric_velocity_onms.get(unit_slct)
            unit_value = float(input("Type the unit value: "))
            unit_slct2 = input("Type the unit of destiny: ")
            unit_dest = metric_velocity_onms.get(unit_slct2)
            unit_in_standard = unit_value * unit
            unit_real = unit_in_standard / unit_dest
            print(f"{unit_value}{unit_slct} = {unit_real}{unit_slct2}")
        elif slct_sec == 3:
            unit_slct = input("Type the unit you want to convert: ")
            unit = metric_mass_ong.get(unit_slct)
            unit_value = float(input("Type the unit value: "))
            unit_slct2 = input("Type the unit of destiny: ")
            unit_dest = metric_mass_ong.get(unit_slct2)
            unit_in_standard = unit_value * unit
            unit_real = unit_in_standard / unit_dest
            print(f"{unit_value}{unit_slct} = {unit_real}{unit_slct2}")
        elif slct_sec == 4:
            unit_slct = input("Type the unit you want to convert: ")
            unit = metric_volume_onl.get(unit_slct)
            unit_value = float(input("Type the unit value: "))
            unit_slct2 = input("Type the unit of destiny: ")
            unit_dest = metric_volume_onl.get(unit_slct2)
            unit_in_standard = unit_value * unit
            unit_real = unit_in_standard / unit_dest
            print(f"{unit_value}{unit_slct} = {unit_real}{unit_slct2}")
        elif slct_sec == 5:
            unit_slct = input("Type the unit you want to convert: ")
            unit = metric_area_onm2.get(unit_slct)
            unit_value = float(input("Type the unit value: "))
            unit_slct2 = input("Type the unit of destiny: ")
            unit_dest = metric_area_onm2.get(unit_slct2)
            unit_in_standard = unit_value * unit
            unit_real = unit_in_standard / unit_dest
            print(f"{unit_value}{unit_slct} = {unit_real}{unit_slct2}")
        elif slct_sec == 6:
            unit_slct = input("Type the unit you want to convert: ")
            unit = metric_pressure_onpascal.get(unit_slct)
            unit_value = float(input("Type the unit value: "))
            unit_slct2 = input("Type the unit of destiny: ")
            unit_dest = metric_pressure_onpascal.get(unit_slct2)
            unit_in_standard = unit_value * unit
            unit_real = unit_in_standard / unit_dest
            print(f"{unit_value}{unit_slct} = {unit_real}{unit_slct2}")
        elif slct_sec == 7:
            unit_slct = input("Type the unit you want to convert: ")
            unit = metric_energy_onjoule.get(unit_slct)
            unit_value = float(input("Type the unit value: "))
            unit_slct2 = input("Type the unit of destiny: ")
            unit_dest = metric_energy_onjoule.get(unit_slct2)
            unit_in_standard = unit_value * unit
            unit_real = unit_in_standard / unit_dest
            print(f"{unit_value}{unit_slct} = {unit_real}{unit_slct2}")
        elif slct_sec == 8:
            unit_slct = input("Type the unit you want to convert: ")
            unit = metric_power_onwatt.get(unit_slct)
            unit_value = float(input("Type the unit value: "))
            unit_slct2 = input("Type the unit of destiny: ")
            unit_dest = metric_power_onwatt.get(unit_slct2)
            unit_in_standard = unit_value * unit
            unit_real = unit_in_standard / unit_dest
            print(f"{unit_value}{unit_slct} = {unit_real}{unit_slct2}")
        elif slct_sec == 9:
            unit_slct = input("Type the unit you want to convert: ")
            unit = metric_force_onnewton.get(unit_slct)
            unit_value = float(input("Type the unit value: "))
            unit_slct2 = input("Type the unit of destiny: ")
            unit_dest = metric_force_onnewton.get(unit_slct2)
            unit_in_standard = unit_value * unit
            unit_real = unit_in_standard / unit_dest
            print(f"{unit_value}{unit_slct} = {unit_real}{unit_slct2}")
        elif slct_sec == 10:
            continue
        else:
            print("ERROR: No option encountered for this number")
    elif slct_prim == 2:
        print("1. Imperial compriment system converter")
        print("2. Imperial velocity system converter")
        print("3. Imperial mass system converter")
        print("4. Imperial volume system converter")
        print("5. Imperial area system converter")
        print("6. Imperial pressure system converter")
        print("7. Imperial energy system converter")
        print("8. Imperial power system converter")
        print("9. Imperial force system converter")
        print("10. Go back")
        slct_sec = int(input("Input the number of the area you want to go: "))
        if slct_sec == 1:
            unit_slct = input("Type the unit you want to convert: ")
            unit = imperial_compriment_onyard.get(unit_slct)
            unit_value = float(input("Type the unit value: "))
            unit_slct2 = input("Type the unit of destiny: ")
            unit_dest = imperial_compriment_onyard.get(unit_slct2)
            unit_in_standard = unit_value * unit
            unit_real = unit_in_standard / unit_dest
            print(f"{unit_value}{unit_slct} = {unit_real}{unit_slct2}")
        elif slct_sec == 2:
            unit_slct = input("Type the unit you want to convert: ")
            unit = imperial_velocity_onmph.get(unit_slct)
            unit_value = float(input("Type the unit value: "))
            unit_slct2 = input("Type the unit of destiny: ")
            unit_dest = imperial_velocity_onmph.get(unit_slct2)
            unit_in_standard = unit_value * unit
            unit_real = unit_in_standard / unit_dest
            print(f"{unit_value}{unit_slct} = {unit_real}{unit_slct2}")
        elif slct_sec == 3:
            unit_slct = input("Type the unit you want to convert: ")
            unit = imperial_mass_onpound.get(unit_slct)
            unit_value = float(input("Type the unit value: "))
            unit_slct2 = input("Type the unit of destiny: ")
            unit_dest = imperial_mass_onpound.get(unit_slct2)
            unit_in_standard = unit_value * unit
            unit_real = unit_in_standard / unit_dest
            print(f"{unit_value}{unit_slct} = {unit_real}{unit_slct2}")
        elif slct_sec == 4:
            unit_slct = input("Type the unit you want to convert: ")
            unit = imperial_volume_ongallon.get(unit_slct)
            unit_value = float(input("Type the unit value: "))
            unit_slct2 = input("Type the unit of destiny: ")
            unit_dest = imperial_volume_ongallon.get(unit_slct2)
            unit_in_standard = unit_value * unit
            unit_real = unit_in_standard / unit_dest
            print(f"{unit_value}{unit_slct} = {unit_real}{unit_slct2}")
        elif slct_sec == 5:
            unit_slct = input("Type the unit you want to convert: ")
            unit = imperial_area_onacre.get(unit_slct)
            unit_value = float(input("Type the unit value: "))
            unit_slct2 = input("Type the unit of destiny: ")
            unit_dest = imperial_area_onacre.get(unit_slct2)
            unit_in_standard = unit_value * unit
            unit_real = unit_in_standard / unit_dest
            print(f"{unit_value}{unit_slct} = {unit_real}{unit_slct2}")
        elif slct_sec == 6:
            unit_slct = input("Type the unit you want to convert: ")
            unit = imperial_pressure_onpsi.get(unit_slct)
            unit_value = float(input("Type the unit value: "))
            unit_slct2 = input("Type the unit of destiny: ")
            unit_dest = imperial_pressure_onpsi.get(unit_slct2)
            unit_in_standard = unit_value * unit
            unit_real = unit_in_standard / unit_dest
            print(f"{unit_value}{unit_slct} = {unit_real}{unit_slct2}")
        elif slct_sec == 7:
            unit_slct = input("Type the unit you want to convert: ")
            unit = imperial_energy_onbtu.get(unit_slct)
            unit_value = float(input("Type the unit value: "))
            unit_slct2 = input("Type the unit of destiny: ")
            unit_dest = imperial_energy_onbtu.get(unit_slct2)
            unit_in_standard = unit_value * unit
            unit_real = unit_in_standard / unit_dest
            print(f"{unit_value}{unit_slct} = {unit_real}{unit_slct2}")
        elif slct_sec == 8:
            unit_slct = input("Type the unit you want to convert: ")
            unit = imperial_power_onhp.get(unit_slct)
            unit_value = float(input("Type the unit value: "))
            unit_slct2 = input("Type the unit of destiny: ")
            unit_dest = imperial_power_onhp.get(unit_slct2)
            unit_in_standard = unit_value * unit
            unit_real = unit_in_standard / unit_dest
            print(f"{unit_value}{unit_slct} = {unit_real}{unit_slct2}")
        elif slct_sec == 9:
            unit_slct = input("Type the unit you want to convert: ")
            unit = imperial_force_onlbf.get(unit_slct)
            unit_value = float(input("Type the unit value: "))
            unit_slct2 = input("Type the unit of destiny: ")
            unit_dest = imperial_force_onlbf.get(unit_slct2)
            unit_in_standard = unit_value * unit
            unit_real = unit_in_standard / unit_dest
            print(f"{unit_value}{unit_slct} = {unit_real}{unit_slct2}")
        elif slct_sec == 10:
            continue
        else:
            print("ERROR: No option encountered for this number ")
    elif slct_prim == 3:
        print("1. Time units converter")
        print("2. Digital data units converter")
        print("3. Temperature units converter")
        print("4. Angle units converter")
        print("5. Go back")
        slct_sec = int(input("Input the number of the area you want to go: "))
        if slct_sec == 1:
            unit_slct = input("Type the unit you want to convert: ")
            unit = time_units_ons.get(unit_slct)
            unit_value = float(input("Type the unit value: "))
            unit_slct2 = input("Type the unit of destiny: ")
            unit_dest = time_units_ons.get(unit_slct2)
            unit_in_standard = unit_value * unit
            unit_real = unit_in_standard / unit_dest
            print(f"{unit_value}{unit_slct} = {unit_real}{unit_slct2}")
        elif slct_sec == 2:
            unit_slct = input("Type the unit you want to convert: ")
            unit = digital_data_onbit.get(unit_slct)
            unit_value = float(input("Type the unit value: "))
            unit_slct2 = input("Type the unit of destiny: ")
            unit_dest = digital_data_onbit.get(unit_slct2)
            unit_in_standard = unit_value * unit
            unit_real = unit_in_standard / unit_dest
            print(f"{unit_value}{unit_slct} = {unit_real}{unit_slct2}")
        elif slct_sec == 3:
            unit_orig = input("Type the unit you want to convert: ")
            unit_value = float(input("Type the value of the unit: "))
            unit_dest = input("Type the unit of destiny: ")
            if unit_orig == "celsius" or unit_orig == "C°" or unit_orig == "C":
                if unit_dest == "fahrenheit" or unit_dest == "F°" or unit_dest == "F":
                    F = unit_value * 9 / 5 + 32
                    print(f"{unit_value}C° = {F}F°")
                elif unit_dest == "kelvin" or unit_dest == "K":
                    K = unit_value + 273.15
                    print(f"{unit_value}C° = {K}K")
            if unit_orig == "fahrenheit" or unit_orig == "F°" or unit_orig == "F":
                if unit_dest == "celsius" or unit_dest == "C°" or unit_dest == "C":
                    C = (unit_value - 32) * 5 / 9
                    print(f"{unit_value}F° = {C}C°")
                elif unit_dest == "kelvin" or unit_dest == "K":
                    C = (unit_value - 32) * 5 / 9
                    K = C + 273.15
                    print(f"{unit_value}F° = {K}K")
            if unit_orig == "kelvin" or unit_orig == "K":
                if unit_dest == "celsius" or unit_dest == "C°" or unit_dest == "C":
                    C = unit_value - 273.15
                    print(f"{unit_value}K = {C}C°")
                elif unit_dest == "fahrenheit" or unit_dest == "F°" or unit_dest == "F":
                    C = unit_value - 273.15
                    F = C * 9 / 5 + 32
                    print(f"{unit_value}K = {F}F°")
        elif slct_sec == 4:
            unit_slct = input("Type the unit you want to convert: ")
            unit = angle_ondegree.get(unit_slct)
            unit_value = float(input("Type the unit value: "))
            unit_slct2 = input("Type the unit of destiny: ")
            unit_dest = angle_ondegree.get(unit_slct2)
            unit_in_standard = unit_value * unit
            unit_real = unit_in_standard / unit_dest
            print(f"{unit_value}{unit_slct} = {unit_real}{unit_slct2}")
        elif slct_sec == 5:
            continue
        else:
            print("ERROR: No option encounterd for this number")
    elif slct_prim == 4:
        i = False
    else:
        print("ERROR: No option encounterd for this number")
