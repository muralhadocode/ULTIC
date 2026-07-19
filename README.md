# ULTIC

ULTIC stands for ultimate (ULTI) converter (C), basically it's a VERY large converter and it can convert most of the units of the imperial and metric system, currently there is no conversion beetween them, but its a very complete converter, it has other converters too like digital data, temperatures, angle, etc.

# Why did i build this?

So, i was at home just makin another project and i thought about the units, and i thought about creating a code in python wich can convert both systems, so after i finished a part of the other project, i started making this one, the first premise was that it would only convert the lenght units like from meters to inches or smth like that, but it would be too simple and plain, soooo... i i started thinking that the name should make sense witht the project so like metric and imperial lenght converter = not an ultimate converter, and, all units converter = ultimate converter, so i started making it, it only has the metric system converter, imperial system converter and the other converters, i plan to make the converters convert betweeen the systems so like rn you cant go from metric to imperial ;-;

# How it works!

You use numbers to guide you trough the menus, and when you choose the system you want to convert, you put the unit, then the value of the unit, and them you put the unit you want to convert it to, basically btc (behind the code) it gets that unit and the value of it, it transforms the unit to a standard like meters and it converts from meters to the unit that you want to be the destination so like:

Unit in standard = Unit value \* Unit<br>
Unit transformed = Unit in standard / Unit destination

And to select the units you need to see this dictionary so you can see the available units to convert and how to type them:

# Metric system units dictionary:

(You can just use whats behind the -, so like the one that work is mm, cm, dm, m, etc.)

- Compriment:<br>
  mm - Millimeters<br>
  cm - Centimeters<br>
  dm - Decimeters<br>
  m - Meters<br>
  dam - Decameter<br>
  hm - Hectometer<br>
  km - Kilometer<br>

- Velocity:<br>
  mm/s - Millimeters per second<br>
  cm/s - Centimeters per second<br>
  m/s - Meters per second<br>
  km/h - Kilometers per hour<br>
  km/s - Kilometers per second<br>

- Mass:<br>
  mcg - Microgram<br>
  mg - Milligram<br>
  cg - Centigram<br>
  dg - Decigram<br>
  g - Gram<br>
  dag - Decagram<br>
  hg - Hectogram<br>
  kg - Kilogram<br>
  tonne - Ton<br>

- Volume:<br>
  ml - Milliliters<br>
  cl - Centiliters<br>
  dl - Deciliters<br>
  l - Liters<br>
  m³ or m3 - Cubic meters<br>

- Area:<br>
  mm² or mm2 - Square millimeters<br>
  cm² or cm2 - Square centimeters<br>
  dm² or dm2 - Square decimeters<br>
  m² or m2 - Square meters<br>
  a or are - Are<br>
  hectare - Hectare<br>
  km² or km2 - Square kilometers<br>

- Pressure:<br>
  pascal or Pa - Pascal<br>
  hectopascal or hPA - Hectopascal <br>
  kilopascal or kPa - Kilopascal<br>
  bar - Bar<br>
  atmosphere or atm - Atmosphere<br>

- Energy:<br>
  joule or J - Joule<br>
  kilojoule or kJ - Kilojoule<br>
  calorie or cal - Calorie <br>
  kilocalorie or kcal - Kilocalorie<br>
  watt-hour or Wh - Watts per hour<br>
  kilowatt-hour or kWh - Kilowatt<br>

- Power:<br>
  watt or W - Watt<br>
  kilowatt or kW - Kilowatt<br>
  megawatt or MW - Megawatt<br>
  milliwatt or mW - Milliwatt<br>

- Force:<br>
  newton or N - Newtons<br>
  kilonewton or kN - Kilonewtons<br>
  dyne or dyn - Dyne<br>
  kilogram-force or kgf - Kilogram per force<br>

<br>

# Imperial system units dictionary:

- Compriment:<br>
  inch - Inches<br>
  foot - Foot<br>
  yard - Yards<br>
  chain - Chains<br>
  furlong - Furlong<br>
  mile - Miles<br>
  league - League<br>

- Velocity:<br>
  ft/s - Feet per second<br>
  mph - Miles per hour<br>
  know - Knots<br>
  mach - Mach<br>

- Mass:<br>
  grain - Grains<br>
  dram - Drachma<br>
  ounce - Ounces<br>
  pound - Pounds<br>
  stone - Stones<br>
  quarter - Quarters<br>
  hundredweight or cwt - Hundredweight<br>
  ton or imperial ton - Imperial ton<br>

- Volume:<br>
  fl oz or fluid ounce - Fluid ounce<br>
  cup - Cup<br>
  pint - Pints<br>
  quart or qt - Quarts<br>
  gallon - Gallons<br>

- Area:<br>
  sq inch, inch2 or inch² - Square inches<br>
  sq foot, foot2 or foot² - Square foot<br>
  sq yard, yard2 or yard² - Square yards<br>
  acre - Acre<br>
  sq mile, mile2 or mile² - Square miles<br>

- Pressure:<br>
  psi - Pounds per square inch<br>
  ksi - Kilopound-force per square inch<br>
  inHg - Inch of mercury<br>
  mmHg - Millimeters of mercury<br>

- Energy:<br>
  BTU - British thermal units<br>
  ft-lb or foot-pound - Foot-pound<br>
  thm or therm - Therm<br>

- Power:<br>
  horsepower or hp - Horsepower<br>
  BTU per hour or BTU/h - British thermal units per hour<br>
  foot-pound per second or ft-lb/s - Foot-pounds per second<br>

- Force:<br>
  pound-force or lbf - Pound-force<br>
  ounce-force or ozf - Ounce-force<br>
  poundal or pdl - Poundal<br>

<br>

# Other converters dictionaries:

- Time:<br>
  nano - Nanoseconds<br>
  micro - Microseconds<br>
  milli - Milliseconds<br>
  s - Seconds<br>
  min - Minutes<br>
  hour(s) - Hours<br>
  day(s) - Days<br>
  month(s) - Months<br>
  year(s) - Years<br>

- Digital data:<br>
  bit - Bits<br>
  byte - Byte<br>
  kilobit or kb - Kilobits<br>
  kilobyte or KB - Kilobyte<br>
  megabit or Mb - Megabit<br>
  megabyte or MB - Megabyte<br>
  gigabit or Gb - Gigabit<br>
  gigabyte or GB - Gigabyte<br>
  terabyte or TB - Terabyte<br>
  kikibyte or KiB - Kikibyte<br>
  mebibyte or MiB - Mebibyte<br>
  gibibyte or GiB - Gibibyte<br>

- Angle:<br>
  degree or ° - Degree<br>
  radian - Radian<br>
  gradian, grad or gon - Gradian<br>
  arcminute or ' - Arcminute<br>
  arcsecond or " - Arcsecond<br>
  turn or full revolution - Full revolution<br>

- Temperaute:<br>
  C, C° or celsius - Celsius<br>
  F, F° or fahrenheit - Fahrenheit<br>
  K or kelvin - Kelvin<br>

- Fuel consumption:<br>
  mpg or miles per gallon - Miles per gallon<br>
  km/l or kilometers per liter - Kiloemeters per liter<br>
  l/100km or liters per 100km - Liters per 100km<br>
