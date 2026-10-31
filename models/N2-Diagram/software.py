import openmdao.api as om
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
            'ram_limit_GB = 1.0 * ram_GB'],
            jetson_mass={'units': 'kg'},
            jetson_power={'units': 'W'},
            mass={'units': 'kg'},
            elec_power={'units': 'W'}

        ))
        
        self.add_subsystem('radios', Radios())
        self.add_subsystem('cameras', Cameras())

        total = om.AddSubtractComp()
        total.add_equation('mass', input_names=['m_jetson', 'm_radios', 'm_cameras'], units='kg')
        total.add_equation('elec_power', input_names=['p_jetson', 'p_radios', 'p_cameras'], units='W')
        total.add_equation('data_MBps', input_names=['d_cameras', 'd_logs'])
        total.add_equation('net_Mbps', input_names=['n_cameras', 'n_telem'])
        total.add_equation('gpu_pct', input_names=['gpu_jetson', 'gpu_radios', 'gpu_cameras'])
        total.add_equation('cpu_pct', input_names=['cpu_jetson', 'cpu_radios', 'cpu_cameras'])
        total.add_equation('ram_GB', input_names=['ram_jetson', 'ram_radios', 'ram_cameras'])
        self.add_subsystem('total', total)

        self.connect('jetson_orin_agx.mass', 'total.m_jetson')
        self.connect('radios.heltec_radio.mass', 'total.m_radios')
        self.connect('cameras.total.mass', 'total.m_cameras')
        self.connect('jetson_orin_agx.elec_power', 'total.p_jetson')
        self.connect('radios.heltec_radio.elec_power', 'total.p_radios')
        self.connect('cameras.total.elec_power', 'total.p_cameras')

# ========================================================================
# Radios
#
# Component:
#   - Heltec radio
# ========================================================================
class Radios(om.Group):
    def setup(self):
        self.add_subsystem('heltec_radio', om.ExecComp(
            ['mass = 1.0 * radio_mass',
            'elec_power = 1.0 * radio_power',
            'link_Mbps = 1.0 * lora_Mbps'],            # bandwidth limit
            radio_mass={'units': 'kg'},
            radio_power={'units': 'W'},
            mass={'units': 'kg'},
            elec_power={'units': 'W'}
        ))

# ========================================================================
# Cameras
#
# Component:
#   - ZED X One GS (x num_ZED_X_One_GS)
#   - ZED X Stereo
#   - ZED X Mini Stereo
#   - Infrared
# ========================================================================

class Cameras(om.Group):
    def setup(self):
        self.set_input_defaults('num_ZED_X_One_GS', 6)

        self.add_subsystem('ZED_X_One_GS', om.ExecComp(
            ['mass = num_ZED_X_One_GS * cam_mass',
            'elec_power = num_ZED_X_One_GS * cam_power',
            'data_MBps = num_ZED_X_One_GS * record_MBps',
            'video_Mbps = num_ZED_X_One_GS * stream_Mbps'],
            cam_mass={'units': 'kg'},
            cam_power={'units': 'W'},
            mass={'units': 'kg'},
            elec_power={'units': 'W'}
        ), promotes_inputs=['num_ZED_X_One_GS'])

        self.add_subsystem('ZED_X_Stereo', om.ExecComp(
            ['mass = 1.0 * cam_mass',
            'elec_power = 1.0 * cam_power',
            'data_MBps = 1.0 * record_MBps',
            'video_Mbps = 1.0 * stream_Mbps'],
            cam_mass={'units': 'kg'},
            cam_power={'units': 'W'},
            mass={'units': 'kg'},
            elec_power={'units': 'W'}
        ))

        self.add_subsystem('ZED_X_Mini_Stereo', om.ExecComp(
            ['mass = 1.0 * cam_mass',
            'elec_power = 1.0 * cam_power',
            'data_MBps = 1.0 * record_MBps',
            'video_Mbps = 1.0 * stream_Mbps'],
            cam_mass={'units': 'kg'},
            cam_power={'units': 'W'},
            mass={'units': 'kg'},
            elec_power={'units': 'W'}
        ))

        self.add_subsystem('infrared', om.ExecComp(
            ['mass = 1.0 * cam_mass',
            'elec_power = 1.0 * cam_power',
            'data_MBps = 1.0 * record_MBps',
            'video_Mbps = 1.0 * stream_Mbps'],
            cam_mass={'units': 'kg'},
            cam_power={'units': 'W'},
            mass={'units': 'kg'},
            elec_power={'units': 'W'}
        ))

        total = om.AddSubtractComp()
        total.add_equation('mass', input_names=['m_one_gs', 'm_stereo', 'm_mini', 'm_ir'], units='kg')
        total.add_equation('elec_power', input_names=['p_one_gs', 'p_stereo', 'p_mini', 'p_ir'], units='W')
        total.add_equation('data_MBps', input_names=['d_one_gs', 'd_stereo', 'd_mini', 'd_ir'])
        total.add_equation('video_Mbps', input_names=['v_one_gs', 'v_stereo', 'v_mini', 'v_ir'])
        self.add_subsystem('total', total)
 
        self.connect('ZED_X_One_GS.mass', 'total.m_one_gs')
        self.connect('ZED_X_Stereo.mass', 'total.m_stereo')
        self.connect('ZED_X_Mini_Stereo.mass', 'total.m_mini')
        self.connect('infrared.mass', 'total.m_ir')
 
        self.connect('ZED_X_One_GS.elec_power', 'total.p_one_gs')
        self.connect('ZED_X_Stereo.elec_power', 'total.p_stereo')
        self.connect('ZED_X_Mini_Stereo.elec_power', 'total.p_mini')
        self.connect('infrared.elec_power', 'total.p_ir')
 
        self.connect('ZED_X_One_GS.data_MBps', 'total.d_one_gs')
        self.connect('ZED_X_Stereo.data_MBps', 'total.d_stereo')
        self.connect('ZED_X_Mini_Stereo.data_MBps', 'total.d_mini')
        self.connect('infrared.data_MBps', 'total.d_ir')
 
        self.connect('ZED_X_One_GS.video_Mbps', 'total.v_one_gs')
        self.connect('ZED_X_Stereo.video_Mbps', 'total.v_stereo')
        self.connect('ZED_X_Mini_Stereo.video_Mbps', 'total.v_mini')
        self.connect('infrared.video_Mbps', 'total.v_ir')