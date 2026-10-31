import openmdao.api as om

# ========================================================================
#
# ========================================================================
class Science(om.Group):
    def setup(self):
        self.add_subsystem('total', om.ExecComp(
            ['mass = 1.0 * sci_mass',
            'elec_power = 1.0 * sci_power',
            'data_MBps = 1.0 * sci_MBps',
            'net_Mbps = 1.0 * sci_Mbps',
            'gpu_pct = 1.0 * sci_gpu',
            'cpu_pct = 1.0 * sci_cpu',
            'ram_GB = 1.0 * sci_ram'],
            sci_mass={'units': 'kg'},
            sci_power={'units': 'W'},
            mass={'units': 'kg'},
            elec_power={'units': 'W'}
        ))

