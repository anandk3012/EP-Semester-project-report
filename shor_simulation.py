from qiskit.algorithms import Shor
from qiskit import Aer

# Simulating Shor's Algorithm for factoring 15
def shor_algorithm():
    backend = Aer.get_backend('aer_simulator')  # Quantum simulator backend
    shor = Shor(backend=backend)
    
    # Factorize 15
    result = shor.factor(15)
    return result

result = shor_algorithm()
print("Factors of 15:", result.factors)
