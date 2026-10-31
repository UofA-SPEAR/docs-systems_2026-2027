'''
A N2 Diagram is used for representing the logical data flow for a system.
It holds the relationship for how each component affects each other such 
that if additional changes were to be made, we can simulate the changes
to get a rough estimate before looking more into the idea.

Last Modified: Oct 30
'''

import openmdao.api as om
# to track budget for total power, data, and mass on the overall system
MAX_WEIGHT = 50             # kg


class Mechanical(om.Group):

    def setup(self):
        self.add_subsystem('chassis', om.ExecComp(
            # ensure it is a formula, no change
            'mass = 1.0 * chassis_mass',
            chassis_mass={'val':-0.0, 'units': 'kg'},
            mass={'units': 'kg'}
        ))
        self.add_subsystem('rocker_bogie', om.ExecComp(
            'mass = 2 * (rocker_mass + bogie_mass)',
            rocker_mass={'val':-0.0, 'units': 'kg'},
            bogie_mass={'val':-0.0, 'units': 'kg'},
            mass={'units': 'kg'}
        ))
        self.add_subsystem('wheels', om.ExecComp(
            'mass = n_wheels * wheel_mass',
            wheel_mass={'val':-0.0, 'units': 'kg'},
            mass={'units': 'kg'}
        ))
        self.add_subsystem('drive_motors',)

    self.connect("")

class Science(om.Group):

    def setup(self):
        self.add_subsystem()

class Electrical(om.Group):
    
    def setup(self):
        self.add_subsystem()

class Software(om.Group):
    
    def setup(self):
        self.add_subsystem('jetson_orin_agx', om.ExecComp(

        ))
        self.add_subsystem('heltec radio')
        self.add_subsystem('ZED')

p = om.Problem()
model = p.model

model.set_input_defaults()
model.add_subsystem()

p.setup()
p.final_setup()

p.run_model()