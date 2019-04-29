
class Channel():
    def __init__(self, equilibrium_potential):
        self.equilibrium_potential = equilibrium_potential  # E_c the voltage when the current is 0
        self.max_conductance = 0  # g_bar_c the maximum conductance of the channel fixme

    def update(self, v_m, time):
        self.actual_conductance_fraction = 0  # g_c the fraction of the channels current from 0 to 1 at time t fixme

        self.conductance = self.actual_conductance_fraction * self.max_conductance
        self.net_potential = v_m - self.equilibrium_potential
        self.current = self.conductance * self.net_potential  # g_c * g_bar_c * (v_m - E_c)


class Neuron():
    def __init__(self):
        self.excitatory = Channel(55)  # sodium Na+ glutamate
        self.inhibitory = Channel(-70)  # chloride Cl- GABA
        self.leak = Channel(-70)  # potasium K+
        # calcium Ca++

        self.net_current = 0

        self.voltage_membrane = 0  # begin at the net equilibruim potential fixme
        self.time = 0

    def step(self, dt_vm):
        self.excitatory.update(self.voltage_membrane, self.time)
        self.inhibitory.update(self.voltage_membrane, self.time)
        self.leak.update(self.voltage_membrane, self.time)

        self.net_current = self.excitatory.current + self.inhibitory.current + self.leak.current

        self.voltage_membrane += dt_vm * self.net_current  # the neurons membrain potential at time t
        self.time += 1


if __name__ == "__name__":
    neuron = Neuron()
    graph = []
    dt_vm = 0.1

    for t in range(100):
        neuron.step(dt_vm)
        graph += [neuron.voltage_membrane]

