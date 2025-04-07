import qiskit as q

def gen_qode(n):
    """Generate an equal superposition on n qubits."""
    
    # Create a quantum circuit with 'n' qubits and initialize them to zero
    qc = q.QuantumCircuit(n)
    
    # Perform a controlled Hadamard gate on each qubit, effectively creating a superposition
    for i in range(n):
        qc.h(i)
    
    return qc

def main():
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python gen_qode.py <n>")
        sys.exit(1)
    
    n = int(sys.argv[1])
    
    # Generate the quantum circuit
    qc = gen_qode(n)
    
    # Print the quantum circuit in a readable format
    print(f"Quantum Circuit with {n} qubits:\n{qc}")

if __name__ == "__main__":
    main()