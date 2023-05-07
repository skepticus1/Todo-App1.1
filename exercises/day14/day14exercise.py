# feet to meter

from modules.parse14 import parse
import modules.convert14


feet_inches = "6 6"
size = parse(feet_inches)
meters = modules.convert14.convert(size["foot"], size["inch"])
print(meters)



# 1
# state of water depending on temp

import modules.water_state

temp = (float(input("enter water temperature: ")))
print(modules.water_state.current_state(temp))

# bug 1
import modules.functions14

print(modules.functions14.count("Trees are good. Grass is green."))

