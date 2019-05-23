import matplotlib.pyplot as plt
from copy import deepcopy

class Channel:
	def __init__(self, equilibrium, maximum_conductance):
		self.equilibrium = equilibrium  # E_c the voltage when the current is 0
		self.maximum_conductance = maximum_conductance  # g_bar_c the maximum conductance of the channel fixme
		self.fraction_open = 0  # g_c the fraction of the channels current from 0 to 1 at time t

	def getConductance(self):
		return self.fraction_open * self.maximum_conductance

	def getCurrent(self, membrane_potential):
		return self.getConductance() * (membrane_potential - self.equilibrium)  # g_c * g_bar_c * (v_m - E_c)

class Neuron:
	def __init__(self):
		# chloride Cl- GABA
		self.inhibitory = Channel(
			equilibrium = -70,
			maximum_conductance=1
		)
		# sodium Na+ glutamate
		self.excitatory = Channel(
			equilibrium = +55,
			maximum_conductance=1
		)
		# potassium K+
		self.leak = Channel(
			equilibrium = -70,
			maximum_conductance=1
		)
		self.leak.fraction_open = 0.5
		# calcium Ca++ todo

		self.membrane_potential = self.getEquilibriumMembranePotential()

	def getEquilibriumMembranePotential(self):
		i = self.inhibitory.getConductance() * self.inhibitory.equilibrium
		e = self.excitatory.getConductance() * self.excitatory.equilibrium
		l = self.leak.getConductance() * self.leak.equilibrium
		return (i + e + l) / (self.inhibitory.getConductance() + self.excitatory.getConductance() + self.leak.getConductance())

	def getNetCurrent(self):
		return self.inhibitory.getCurrent(self.membrane_potential) + self.excitatory.getCurrent(self.membrane_potential) + self.leak.getCurrent(self.membrane_potential)

	def step(self, dtvm):
		self.membrane_potential = self.membrane_potential - dtvm * self.getNetCurrent()

if __name__ == "__main__":
	neuron = Neuron()
	graph = []
	dtvm = 0.05
	cycles = 400

	for i in range(cycles):
		if i == 50:
			neuron.excitatory.fraction_open = 1
		if i == 150:
			neuron.excitatory.fraction_open = 0
		neuron.step(dtvm)
		graph += [deepcopy(neuron)]

	fig, ax1 = plt.subplots()
	ax2 = ax1.twinx()

	# keys = []
	ax1.plot(range(cycles), [slice.membrane_potential for slice in graph], color='g')
	ax2.plot(range(cycles), [slice.excitatory.fraction_open for slice in graph], color='r')
	# keys += ["moo"]

	ax1.set_xlabel("cycle")
	ax1.set_ylabel("voltage memebrane potential", color='g')
	ax2.set_ylabel("neuron.excitatory.fraction_open", color='r')
	# plt.title("A graph showing the total number of cells with antibodies of each type")
	# plt.legend(keys)
	plt.show()




