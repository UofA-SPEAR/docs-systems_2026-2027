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
            battery_mass={'units': 'kg'},
            battery_Wh={'units': 'W*h'},
            battery_max_W={'units': 'W'},
            mass={'units': 'kg'},
            capacity={'units': 'W*h'},
            max_power={'units': 'W'}
        ))
