from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# Create a quantum circuit with 3 qubits and 3 classical bits
quantumCircuit = QuantumCircuit(3, 3)

# Initialize q1 to |+> state (superposition)
quantumCircuit.initialize([1/2**0.5, 1/2**0.5], 0)  # q1 in |+>, q2 and q3 remain |0⟩

# Apply Hadamard gate to q2
quantumCircuit.h(1)

# Apply CNOT gate to q3 controlled by q2
quantumCircuit.cx(1, 2)

# Apply CNOT gate to q2 controlled by q1
quantumCircuit.cx(0, 1)

# Apply Hadamard gate to q1
quantumCircuit.h(0)

# Measure all qubits
quantumCircuit.measure([0, 1, 2], [0, 1, 2])

print("Quantum Circuit:")
print(quantumCircuit)

# Remove final measurements to get the statevector
quantumCircuit.remove_final_measurements()

# Get the statevector of the circuit
# Statevector: This is the final quantum state of the system 
# after all the gates have been applied, but before any 
# measurements. The statevector is a complex vector that 
# represents the amplitudes of the quantum states. 
# It provides a complete description of the quantum system's state.

statevector = Statevector.from_instruction(quantumCircuit)
print(statevector)
