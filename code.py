print("Welcome to the ultimate converter :D")
print("1. Metric system converter")
print("2. Imperial system converter")
print("3. Time converter")
slct = int(input("Input the number of the area you want to go: "))
metric_compriment_onm = {
    "mm" : 0.001,
    "cm" : 0.01,
    "dm" : 0.1,
    "m"  : 1.0,
    "dam": 10.0,
    "hm" : 100.0,
    "km" : 1000.0,
}
imperial_compriment_onyard = {
    "inch"   : 0.027778,
    "foot"   : 0.333333,
    "yard"   : 1.0,
    "chain"  : 22.0,
    "furlong": 220.0,
    "mile"   : 1760.0,
    "league" : 5280,
}
time_units_ons = {
    "nano"    : 0.000000001,
    "micro"   : 0.000001,      
    "milli"   : 0.001,
    "s"       : 1.0,
    "min"     : 60.0,
    "hour(s)" : 3600.0,
    "day(s)"  : 86400.0,
    "month(s)": 2629746.0,
    "year(s)" : 31557600.0,
}

if slct == 1:
    unit_slct = input("Type the unit you want to convert: ")
    unit = metric_compriment_onm.get(unit_slct)
    unit_value = int(input("Type the unit value: "))
    unit_slct2 = input("Type the unit of destiny: ")
    unit_dest = metric_compriment_onm.get(unit_slct2)
    unit_in_standard = unit_value*unit
    unit_real = unit_in_standard/unit_dest