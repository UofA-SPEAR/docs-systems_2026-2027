'''
A N2 Diagram is used for representing the logical data flow for a system.
It holds the relationship for how each component affects each other such 
that if additional changes were to be made, we can simulate the changes
to get a rough estimate before looking more into the idea.

Budget tracks:

    Type    |   Rate units  |   Total
    =====================================
    mass    |               |   kg
    power   |        W      |   Wh
    storage |      MB/s     |   GB
    compute |  GPU %, CPU%  |   RAM GB
    network |       Mbps    |


values that are -0.0 should be filled in with the correct values when found

Last Modified: Oct 31
'''
import openmdao.api as om
from mechanical import Mechanical
from science import Science
from electrical import Electrical
from software import Software

MAX_WEIGHT = 50             # kg

# ========================================================================
# Build Model
#
# Note: oder matters, things that produce numbers should come before things
# that use them
# ========================================================================
p = om.Problem()
model = p.model

model.add_subsystem('mechanical', Mechanical())
model.add_subsystem('science', Science())
model.add_subsystem('electrical', Electrical())
model.add_subsystem('software', Software())

# ========================================================================
# budget calc
#
# ========================================================================

# mass
mass_budget = om.AddSubtractComp()
mass_budget = add_equation('total_mass', input_names=[''])

# power
power_budget = om.AddSubtractComp()
power_budget.add_equation()

# storage

# compute


# network



# ========================================================================
# Running Model
#
# ========================================================================
p.setup()
p.final_setup()

p.run_model()

print('Total mass: ', p.get_val('mass_budget.total_mass'), 'kg')
print('Mass left:  ', p.get_val('mass_budget.mass_left'), 'kg')
print('Total power:', p.get_val('power_budget.total_power'), 'W')
print('Power left:', p.get_val('power_budget.power_left'), 'W')
print('Total storage:', p.get_val('power_budget.total_storage'), 'GB')
print('Storage left:', p.get_val('power_budget.storage_left'), 'GB')


om.n2(p, outfile='n2_diagram.html', show_browser=True)