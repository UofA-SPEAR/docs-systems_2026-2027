__docformat__ = 'epytext'

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
import csv
import os

from mechanical import Mechanical
from science import Science
from electrical import Electrical
from software import Software

MAX_WEIGHT = 50             # kg

def build_problem():
    """
    Builds the rover model by adding every subsystem and budgets.
 
    @return: the rover model, not set up yet
    @rtype: om.Problem
    @note: order matters, things that produce numbers should come before
    things that use them, so budgets are added last
    @see: add_budgets
    """
    p = om.Problem()
    model = p.model

    model.add_subsystem('mechanical', Mechanical())
    model.add_subsystem('science', Science())
    model.add_subsystem('electrical', Electrical())
    model.add_subsystem('software', Software())

    # add budget last as dependent on subsystem outputs
    add_budgets(model)

    return p

def add_budgets(model):
    """
    Adds the mass, power, storage, compute and network budgets and
    connects the subsystems to them. Each budget gets a total and what's
    left (limit - total).
 
    @param model: top level group (p.model)
    @note: scaling_factors: 1 adds, -1 subtracts
    @note: unconnected inputs default to 1.0, so connect it or set it in
    specs.csv
    @note: openmdao has no byte units, so storage and network have the
    unit in the name. Mbps is bits not bytes (1 MB/s = 8 Mbps)
    @see: load_specs
    """
    # mass
    mass_budget = om.AddSubtractComp()
    mass_budget.add_equation('total_mass', input_names=['m_mech', 'm_sci', 'm_elec', 'm_sw'], units='kg')
    mass_budget.add_equation(
        'mass_left',
        input_names=['max_mass', 'm_mech', 'm_sci', 'm_elec', 'm_sw'],
        scaling_factors=[1, -1, -1, -1, -1],
        units='kg')
    model.add_subsystem('mass_budget', mass_budget)
 
    model.connect('mechanical.total.mass', 'mass_budget.m_mech')
    model.connect('science.total.mass', 'mass_budget.m_sci')
    model.connect('electrical.total.mass', 'mass_budget.m_elec')
    model.connect('software.total.mass', 'mass_budget.m_sw')

    # power
    power_budget = om.AddSubtractComp()
    power_budget.add_equation('total_power', input_names=['p_mech', 'p_sci', 'p_elec', 'p_sw'], units='W')
    power_budget.add_equation(
        'power_left',
        input_names=['max_power', 'p_mech', 'p_sci', 'p_elec', 'p_sw'],
        scaling_factors=[1, -1, -1, -1, -1],
        units='W')
    model.add_subsystem('power_budget', power_budget)
 
    model.connect('mechanical.total.elec_power', 'power_budget.p_mech')
    model.connect('science.total.elec_power', 'power_budget.p_sci')
    model.connect('electrical.total.elec_power', 'power_budget.p_elec')
    model.connect('software.total.elec_power', 'power_budget.p_sw')
    
    model.connect('electrical.total.max_power', 'power_budget.max_power')
    
    # storage
    # since openmdao has no byte units using unit in the name
    storage_budget = om.AddSubtractComp()
    storage_budget.add_equation('total_MBps', input_names=['s_mech', 's_sci', 's_elec', 's_sw'])
    model.add_subsystem('storage_budget', storage_budget)
 
    model.connect('mechanical.total.data_MBps', 'storage_budget.s_mech')
    model.connect('science.total.data_MBps', 'storage_budget.s_sci')
    model.connect('electrical.total.data_MBps', 'storage_budget.s_elec')
    model.connect('software.total.data_MBps', 'storage_budget.s_sw')

    # compute
    compute_budget = om.AddSubtractComp()
    compute_budget.add_equation('gpu_total', input_names=['gpu_mech', 'gpu_sci', 'gpu_elec', 'gpu_sw'])
    compute_budget.add_equation(
        'gpu_left',
        input_names=['gpu_limit', 'gpu_mech', 'gpu_sci', 'gpu_elec', 'gpu_sw'],
        scaling_factors=[1, -1, -1, -1, -1])
    compute_budget.add_equation('cpu_total', input_names=['cpu_mech', 'cpu_sci', 'cpu_elec', 'cpu_sw'])
    compute_budget.add_equation(
        'cpu_left',
        input_names=['cpu_limit', 'cpu_mech', 'cpu_sci', 'cpu_elec', 'cpu_sw'],
        scaling_factors=[1, -1, -1, -1, -1])
    compute_budget.add_equation('ram_total', input_names=['ram_mech', 'ram_sci', 'ram_elec', 'ram_sw'])
    compute_budget.add_equation(
        'ram_left',
        input_names=['ram_limit', 'ram_mech', 'ram_sci', 'ram_elec', 'ram_sw'],
        scaling_factors=[1, -1, -1, -1, -1])
    model.add_subsystem('compute_budget', compute_budget)
 
    model.connect('mechanical.total.gpu_pct', 'compute_budget.gpu_mech')
    model.connect('science.total.gpu_pct', 'compute_budget.gpu_sci')
    model.connect('electrical.total.gpu_pct', 'compute_budget.gpu_elec')
    model.connect('software.total.gpu_pct', 'compute_budget.gpu_sw')
 
    model.connect('mechanical.total.cpu_pct', 'compute_budget.cpu_mech')
    model.connect('science.total.cpu_pct', 'compute_budget.cpu_sci')
    model.connect('electrical.total.cpu_pct', 'compute_budget.cpu_elec')
    model.connect('software.total.cpu_pct', 'compute_budget.cpu_sw')
 
    model.connect('mechanical.total.ram_GB', 'compute_budget.ram_mech')
    model.connect('science.total.ram_GB', 'compute_budget.ram_sci')
    model.connect('electrical.total.ram_GB', 'compute_budget.ram_elec')
    model.connect('software.total.ram_GB', 'compute_budget.ram_sw')

    # network
    network_budget = om.AddSubtractComp()
    network_budget.add_equation('total_Mbps', input_names=['n_mech', 'n_sci', 'n_elec', 'n_sw'])
    network_budget.add_equation(
        'bw_left',
        input_names=['link_Mbps', 'n_mech', 'n_sci', 'n_elec', 'n_sw'],
        scaling_factors=[1, -1, -1, -1, -1])
    model.add_subsystem('network_budget', network_budget)
 
    model.connect('mechanical.total.net_Mbps', 'network_budget.n_mech')
    model.connect('science.total.net_Mbps', 'network_budget.n_sci')
    model.connect('electrical.total.net_Mbps', 'network_budget.n_elec')
    model.connect('software.total.net_Mbps', 'network_budget.n_sw')

def load_specs(p, filename=os.path.join(os.path.dirname(__file__), 'specs.csv')):
    """
    Loads every value from specs.csv (path, value, units) into the model,
    including the limits. Blank units are read as None (counts, %).
 
    @param p: the rover model
    @param filename: csv with path, value, units
    @raise FileNotFoundError: csv not found
    @raise KeyError: path isn't in the model
    @raise ValueError: value isn't a number
    """
    with open(filename, newline='') as f:
        for row in csv.DictReader(f):
            p.set_val(row['path'], float(row['value']), units=row['units'] or None)

    p.set_val('mass_budget.max_mass', MAX_WEIGHT, units='kg')


def display_summary(p):
    """
    Prints the total and what's left for each budget.
 
    @param p: the rover model
    @note: call after p.run_model()
    """
    print('Total mass:   ', p.get_val('mass_budget.total_mass'), 'kg')
    print('Mass left:    ', p.get_val('mass_budget.mass_left'), 'kg')

    print('Total power:  ', p.get_val('power_budget.total_power'), 'W')
    print('Power left:   ', p.get_val('power_budget.power_left'), 'W')

    print('Total storage:', p.get_val('storage_budget.total_MBps'), 'MB/s')

    print('GPU left:     ', p.get_val('compute_budget.gpu_left'), '%')
    print('CPU left:     ', p.get_val('compute_budget.cpu_left'), '%')
    print('RAM left:     ', p.get_val('compute_budget.ram_left'), 'GB')

    print('Total network:', p.get_val('network_budget.total_Mbps'), 'Mbps')
    print('Network left: ', p.get_val('network_budget.bw_left'), 'Mbps')

# ========================================================================
# Running Model
#
# ========================================================================
def main():
    """
    Builds the model, loads specs.csv, runs it, prints the budgets and
    opens the N2.
 
    @see: build_problem, load_specs, display_summary
    """
    p = build_problem()
    
    p.setup()
    load_specs(p)
    p.final_setup()

    p.run_model()

    display_summary(p)

    om.n2(p, outfile='n2_diagram.html', show_browser=True)

if __name__ == '__main__':
    main()
