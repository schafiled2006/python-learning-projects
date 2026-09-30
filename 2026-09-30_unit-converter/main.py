"""Small unit converter (length units only for now)."""

TO_METERS = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1.0,
    "km": 1000.0,
}

def convert(value, unit_from, unit_to):
    meters = value * TO_METERS[unit_from]
    return meters / TO_METERS[unit_to]

def parse(text):
    value, _, unit = text.partition(" ")
    return float(value), unit

if __name__ == "__main__":
    value, unit = parse(input("from (e.g. 5 km): "))
    target = input("to (mm/cm/m/km): ").strip()
    result = convert(value, unit, target)
    print(f"{value} {unit} = {result:g} {target}")
