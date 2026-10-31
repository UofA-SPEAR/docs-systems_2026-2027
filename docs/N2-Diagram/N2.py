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

MAX_WEIGHT = 50             # kg

# ========================================================================
#
# ========================================================================
class Science(om.Group):

    def setup(self):
        self.add_subsystem()

# ========================================================================
#
# ========================================================================
class Electrical(om.Group):
    
    def setup(self):
        self.add_subsystem('battery', om.ExecComp(
            ['mass = 1.0 * battery_mass',
            'capacity = 1.0 * battery_Wh',
            'max_power = 1.0 * battery_max_W'],
            battery_mass={'val':-0.0, 'units': 'kg'},
            battery_Wh={'val':-0.0, 'units': 'W*h'},
            battery_max_W={'val':-0.0, 'units': 'W'},

            mass={'units': 'kg'},
            capacity={'units': 'W*h'},
            max_power={'units': 'W'}
        ))

# ========================================================================
# Software
#
# Groups:
#   - Radios
#   - Cameras
#   
# ========================================================================
class Software(om.Group):
    
    def setup(self):
        self.add_subsystem('jetson_orin_agx', om.ExecComp(
            ['mass = 1.0 * jetson_mass',
            'elec_power = 1.0 * jetson_power',
            'storage_GB = ',
            'ram_limit_GB = 1.0 * ram_GB'],
            jetson_mass={'val':-0.0, 'units': 'kg'},
            jetson_power={'val':-0.0, 'units': 'W'},

            mass={'units': 'kg'},
            elec_power={'units': 'W'}

        ))
        
        self.add_subsystem('radios', Radios())
        self.add_subsystem('cameras', Cameras())

        total = om.AddSubtractComp()
        total.add_equation('mass', input_names=['m_jetson', 'm_box', 'm_mounts'], units= 'kg')

        self.connect('','total.m_jetson')

# ========================================================================
#
# ========================================================================
class Radios(om.Group):
    def setup(self):
        self.add_subsystem('heltec_radio', om.ExecComp(
            []
        ))

# ========================================================================
#
# ========================================================================
class Cameras(om.Group):
    def setup(self):
        self.set_input_defaults('num_ZED_X_One_GS', 6)

        self.add_subsystem('ZED_X_One_GS', om.ExecComp(
            [],

        ))

        self.add_subsystem('ZED_X_Stereo', om.ExecComp(

        ))

        self.add_subsystem('ZED_X_Mini_Stereo', om.ExecComp(

        ))

        self.add_subsystem('infrared', om.ExecComp(

        ))

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