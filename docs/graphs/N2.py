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

Last Modified: Oct 30
'''
import openmdao.api as om

MAX_WEIGHT = 50             # kg

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
        self.add_subsystem('total', total)

        self.connect('chassis.total.mass', 'total.m_chassis')
        self.connect('drive.total.mass', 'total.m_drive')
        self.connect('arm.total.mass', 'total.m_arm')

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
            rocker_mass={'val':-0.0, 'units': 'kg'},
            bogie_mass={'val':-0.0, 'units': 'kg'},
            mass={'units': 'kg'}
        ))

        self.add_subsystem('wheels', om.ExecComp(
            'mass = n_wheels * wheel_mass',
            wheel_mass={'val':-0.0, 'units': 'kg'},
            mass={'units': 'kg'}
        ), promotes_inputs=['n_wheels'])

        self.add_subsystem('drive_motors', om.ExecComp(
            ['mass = n_wheels * motor_mass',
            'power = n_wheels * motor_power'],
            motor_mass={'val':-0.0, 'units': 'kg'},
            motor_power={'val':-0.0, 'units': 'W'},
            mass={'units': 'kg'},
            power={'units': 'W'}
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
#   - Electrical Box
#   - Camera Mounts
# ========================================================================
class Chassis(om.Group):
    
    def setup(self):
        self.add_subsystem('chassis', om.ExecComp(
            # ensure it is a formula, no change
            'mass = 1.0 * chassis_mass',
            chassis_mass={'val':-0.0, 'units': 'kg'},
            mass={'units': 'kg'}
        ))

# ========================================================================
# Arm
# 
# ========================================================================
class Arm(om.Group):
    pass

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
        self.add_subsystem()

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

        ))
        self.add_subsystem('heltec radio')
        self.add_subsystem('ZED')

# ========================================================================
#
# ========================================================================
class Radios(om.Group):
    pass

# ========================================================================
#
# ========================================================================
class Cameras(om.Group):
    pass

# ========================================================================
# Build Model
#
# Note: oder matters, things that produce numbers should come before things
# that use them
# ========================================================================
p = om.Problem()
model = p.model

# set shared values
model.set_input_defaults('n_wheels', 6.0)
model.add_subsystem('mechanical', Mechanical())
model.add_subsystem('science', Science())

# ========================================================================
# Running Model
#
# ========================================================================
p.setup()
p.final_setup()

p.run_model()