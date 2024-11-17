from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

# Quantum Teleportation Protocol
def teleportation():
    qc = QuantumCircuit(3)  # 3 qubits: Qubit 0 (Alice's), 1 (entanglement), 2 (Bob's)
    
    # Step 1: Create an entangled pair between Qubit 1 and Qubit 2
    qc.h(1)
    qc.cx(1, 2)
    
    # Step 2: Prepare Qubit 0 in an arbitrary state (|ψ> = α|0> + β|1>)
    qc.x(0)  # Example: Prepare |1> state (replace with general preparation if needed)
    
    # Step 3: Alice applies Bell measurement on Qubit 0 and Qubit 1
    qc.cx(0, 1)
    qc.h(0)
    
    # Step 4: Send classical results to Bob and correct his state
    qc.barrier()
    qc.cx(1, 2)
    qc.cz(0, 2)
    
    # Measurement
    qc.measure_all()
    return qc

qc = teleportation()
qc.draw('mpl')

# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, simulator, shots=1024).result()
counts = result.get_counts()
print("Counts:", counts)
plot_histogram(counts)
