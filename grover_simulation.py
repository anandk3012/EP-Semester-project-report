from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

# Grover's Algorithm: Single-item search in a two-qubit database
def grover_algorithm():
    qc = QuantumCircuit(2)  # 2 qubits
    
    # Apply Hadamard gates to create superposition
    qc.h([0, 1])
    
    # Oracle: Flip the amplitude of the marked state (|11>)
    qc.cz(0, 1)
    
    # Diffuser
    qc.h([0, 1])
    qc.x([0, 1])
    qc.cz(0, 1)
    qc.x([0, 1])
    qc.h([0, 1])
    
    # Measurement
    qc.measure_all()
    return qc

qc = grover_algorithm()
qc.draw('mpl')

# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, simulator, shots=1024).result()
counts = result.get_counts()
print("Counts:", counts)
plot_histogram(counts)
