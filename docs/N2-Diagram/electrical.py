import openmdao.api as om

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
