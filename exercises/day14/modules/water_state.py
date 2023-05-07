solid = 30
gas = 212

def current_state(temp):
    state = ""
    if temp < solid:
        state = "Solid"
    elif temp > gas:
        state = "Gas"
    else:
        state = "Liquid"
    return state