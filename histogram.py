from qiskit import QuantumCircuit 
from qiskit_aer import AerSimulator 
from qiskit.visualization import plot_histogram 
import matplotlib.pyplot as plt 
simulator = AerSimulator() 
qc = QuantumCircuit(1,1) 
qc.h(0) 
qc.measure(0,0) 
job=simulator.run(qc, shots=10)
result10 = job.result() 
counts10 = result10.get_counts() 
job=simulator.run(qc, shots=100)
result100 = job.result() 
counts100 = result100.get_counts()
plot_histogram([counts10, counts100], legend=['10 shots', '100 shots']) 
plt.show() 
