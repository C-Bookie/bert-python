import PyOpenWorm as POW
from PyOpenWorm.worm import Worm
from PyOpenWorm.neuron import Neuron
from PyOpenWorm.network import Network
import OpenWormData as OWD

if __name__ == "__main__":
	with POW.connect('default.conf') as conn:
		ctx = POW.Context(ident=OWD.BIO_ENT_NS['worm0'], conf=conn.conf).stored

		print("Neurons:")
		print(", ".join(sorted(Neuron().name.get())))

		with ctx.stored(Worm, Neuron, Network) as cctx:
			w = cctx.Worm()
			net = cctx.Network()
			neur = cctx.Neuron()

			print(net.count())
