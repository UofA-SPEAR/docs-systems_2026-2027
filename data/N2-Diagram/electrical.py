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

        self.add_subsystem('total', om.ExecComp(
            ['mass = 1.0 * m_battery',
            'elec_power = 1.0 * p_elec',
            'data_MBps = 1.0 * elec_MBps',
            'net_Mbps = 1.0 * elec_Mbps',
            'gpu_pct = 1.0 * elec_gpu',
            'cpu_pct = 1.0 * elec_cpu',
            'ram_GB = 1.0 * elec_ram',
            'max_power = 1.0 * battery_max'],
            m_battery={'units': 'kg'},
            p_elec={'units': 'W'},
            battery_max={'units': 'W'},
            mass={'units': 'kg'},
            elec_power={'units': 'W'},
            max_power={'units': 'W'}
        ))

        self.connect('battery.mass', 'total.m_battery')
        self.connect('battery.max_power', 'total.battery_max')