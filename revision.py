import matplotlib.pyplot as plt
from copy import deepcopy

class Channel:
	def __init__(self, equilibrium):
		self.equilibrium = equilibrium  # E_c the voltage when the current is 0
		self.maximum_conductance = 1  # g_bar_c the maximum conductance of the channel fixme
		self.fraction_open = 0  # g_c the fraction of the channels current from 0 to 1 at time t
		self.conductance = 0

	def getConductance(self):
		self.conductance = self.fraction_open * self.maximum_conductance
		return self.conductance

	def getCurrent(self, membrane_potential):
		return self.getConductance() * (self.equilibrium - membrane_potential)  # g_c * g_bar_c * (v_m - E_c)

class Neuron:
	def __init__(self):
		self.inhibitory = Channel(-70)  # chloride Cl- GABA
		self.excitatory = Channel(+55)  # sodium Na+ glutamate
		self.leak = Channel(-70)  # potassium K+
		self.leak.fraction_open = 0.1
		# self.calcium = Channel(0)  # calcium Ca++ todo
		self.threshold = +55

		self.act = 0
		self.default_membrane_potential = self.getEquilibriumMembranePotential()
		self.membrane_potential = self.default_membrane_potential
		self.I_net = self.getNetCurrent()

	def getEquilibriumMembranePotential(self):
		i = self.inhibitory.getConductance() * self.inhibitory.equilibrium
		e = self.excitatory.getConductance() * self.excitatory.equilibrium
		l = self.leak.getConductance() * self.leak.equilibrium
		denominator = self.inhibitory.getConductance() + self.excitatory.getConductance() + self.leak.getConductance()
		if denominator == 0:
			return 0
		else:
			return (i + e + l) / denominator

	def getNetCurrent(self):
		return self.inhibitory.getCurrent(self.membrane_potential) + self.excitatory.getCurrent(self.membrane_potential) + self.leak.getCurrent(self.membrane_potential)

	def step(self, dtvm):
		self.act = 0
		if self.membrane_potential >= self.threshold:
			self.act = 1
			self.membrane_potential = self.default_membrane_potential
		self.I_net = self.getNetCurrent()
		self.membrane_potential = self.membrane_potential + dtvm * self.I_net

def plotGraph(graph):
	keys = []

	fig, ax1 = plt.subplots()
	ax1.plot(range(cycles), [slice.membrane_potential for slice in graph], color='c')

	# gain = 0.5
	# rate_coading = []
	# total = 0
	# for slice in graph:
	# 	total += slice.act
	# 	rate_coading += [gain * total]
	# ax1.plot(range(cycles), rate_coading, linestyle=":", color='b')

	ax1.set_xlabel("cycle")
	ax1.set_ylabel("voltage", color='c')
	keys += ["voltage"]

	ax2 = ax1.twinx()
	ax2.plot(range(cycles), [slice.inhibitory.conductance for slice in graph], linestyle="--", color='r')
	ax2.plot(range(cycles), [slice.excitatory.conductance for slice in graph], linestyle="--", color='g')
	ax2.plot(range(cycles), [slice.leak.conductance for slice in graph], linestyle="--", color='b')
	ax2.set_ylabel("conductance")
	keys += ["excitatory", "inhibitory", "leak"]

	ax3 = ax1.twinx()
	ax3.plot(range(cycles), [slice.I_net for slice in graph], color='m')
	ax3.set_ylabel("net current")
	keys += ["net current"]

	# ax4 = ax1.twinx()
	# ax4.plot(range(cycles), [slice.act for slice in graph], color='y')
	# ax4.set_ylabel("act")
	# keys += ["act"]

	fig.legend(keys)
	fig.tight_layout()
	plt.show()


if __name__ == "__main__":
	neuron = Neuron()
	graph = []
	dtvm = 0.05
	cycles = 400

	for i in range(cycles):
		if i == 50:
			neuron.excitatory.fraction_open = 1
		if i == 100:
			neuron.inhibitory.fraction_open = 0.75
		if i == 150:
			neuron.excitatory.fraction_open = 0
		if i == 200:
			neuron.inhibitory.fraction_open = 0
		neuron.step(dtvm)
		graph += [deepcopy(neuron)]

	plotGraph(graph)



