import qiskit as q

def gen_qode(n):
    # Create a quantum register with n qubits
    qc = q.QuantumCircuit(n)
    
    # Generate the superposition of all possible states for each qubit
    for i in range(n):
        qc.h(i)  # Apply Hadamard gate to the ith qubit
    
    return qc

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Generate an equal superposition on n qubits.")
    parser.add_argument("n", type=int, help="The number of qubits for which to generate the superposition.")
    
    args = parser.parse_args()
    
    # Generate the quantum circuit
    qc = gen_qode(args.n)
    
    # Print the quantum circuit
    print(qc)

if __name__ == "__main__":
    main()