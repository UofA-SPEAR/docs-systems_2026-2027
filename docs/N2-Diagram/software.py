
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
