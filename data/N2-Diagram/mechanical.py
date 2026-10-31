import openmdao.api as om

# ========================================================================
# Mechanical
#
# Groups:
#   - Chassis
#   - Drive
#   - Arm
# ========================================================================
class Mechanical(om.Group):
    
    def setup(self):
        self.add_subsystem('chassis', Chassis())
        self.add_subsystem('drive', Drive())
        self.add_subsystem('arm', Arm())

        total = om.AddSubtractComp()
        total.add_equation('mass', input_names=['m_chassis', 'm_drive', 'm_arm'], units='kg')
        total.add_equation('elec_power', input_names=['p_chassis', 'p_drive', 'p_arm'], units='W')
        total.add_equation('data_MBps', input_names=['d_chassis', 'd_drive', 'd_arm'])
        total.add_equation('net_Mbps', input_names=['n_chassis', 'n_drive', 'n_arm'])
        total.add_equation('gpu_pct', input_names=['gpu_chassis', 'gpu_drive', 'gpu_arm'])
        total.add_equation('cpu_pct', input_names=['cpu_chassis', 'cpu_drive', 'cpu_arm'])
        total.add_equation('ram_GB', input_names=['ram_chassis', 'ram_drive', 'ram_arm'])
        self.add_subsystem('total', total)

        self.connect('chassis.total.mass', 'total.m_chassis')
        self.connect('drive.total.mass', 'total.m_drive')
        self.connect('drive.drive_motors.elec_power', 'total.p_drive')

# ========================================================================
# Drive
#
# Component:
#   - Rocker Bogie
#   - Wheels
#   - Drive motors
#   
# ========================================================================
class Drive(om.Group):
    def setup(self):
        self.set_input_defaults('n_wheels', 6)

        
        self.add_subsystem('rocker_bogie', om.ExecComp(
            'mass = 2 * (rocker_mass + bogie_mass)',
            rocker_mass={'units': 'kg'},
            bogie_mass={'units': 'kg'},
            mass={'units': 'kg'}
        ))

        self.add_subsystem('wheels', om.ExecComp(
            'mass = n_wheels * wheel_mass',
            wheel_mass={'units': 'kg'},
            mass={'units': 'kg'}
        ), promotes_inputs=['n_wheels'])

        self.add_subsystem('drive_motors', om.ExecComp(
            ['mass = n_wheels * motor_mass',
            'elec_power = n_wheels * motor_power'],
            motor_mass={'units': 'kg'},
            motor_power={'units': 'W'},
            mass={'units': 'kg'},
            elec_power={'units': 'W'}
        ), promotes_inputs=['n_wheels'])

        total = om.AddSubtractComp()
        total.add_equation('mass', input_names=['m_rb', 'm_wheels', 'm_motors'], units= 'kg')
        self.add_subsystem('total', total)

        self.connect('rocker_bogie.mass', 'total.m_rb')
        self.connect('wheels.mass', 'total.m_wheels')
        self.connect('drive_motors.mass', 'total.m_motors')

# ========================================================================
# Chassis
#
# Component:
#   - Chassis
#   - Electrical Box
#   - Camera Mounts
# ========================================================================
class Chassis(om.Group):
    
    def setup(self):
        self.add_subsystem('chassis', om.ExecComp(
            # ensure it is a formula, no change
            'mass = 1.0 * chassis_mass',
            chassis_mass={'units': 'kg'},
            mass={'units': 'kg'}
        ))

        self.add_subsystem('electrical_box', om.ExecComp(
            'mass = 1.0 * box_mass',
            box_mass={'units': 'kg'},
            mass={'units': 'kg'}
        ))

        self.add_subsystem('camera_mounts', om.ExecComp(
            'mass = 1.0 * mount_mass',
            mount_mass={'units': 'kg'},
            mass={'units': 'kg'}
        ))

        total = om.AddSubtractComp()
        total.add_equation('mass', input_names=['m_chassis', 'm_box', 'm_mounts'], units= 'kg')
        self.add_subsystem('total', total)

        self.connect('chassis.mass', 'total.m_chassis')
        self.connect('electrical_box.mass', 'total.m_box')
        self.connect('camera_mounts.mass', 'total.m_mounts')

# ========================================================================
# Arm
# 
# ========================================================================
class Arm(om.Group):
    pass
    # def setup(self):
    #     self.add_subsystem()
