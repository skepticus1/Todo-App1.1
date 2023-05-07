def parse(size):
    values = size.split(" ")
    feet = float(values[0])
    inches = float(values[1])
    return {"foot": feet, "inch": inches}