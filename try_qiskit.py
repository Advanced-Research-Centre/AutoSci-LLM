# For Ollama basics, see try_ollama.py
import ollama
import re
import subprocess

client = ollama.Client()
model = "qwen2.5-coder:0.5b"  # Replace with your model name
prompt = "Write a Qiskit function to create a quantum circuit that generates an equal superposition on n qubits. Do not include measurements. The name of the function should be gen_qode(). Include a main function to test the function with a command line argument of n and print the quantum circuit generated. Import required libraries only."
response = client.generate(model=model, prompt=prompt)

def extract_and_save(full_response, fname = "gen_qode"):
    code_response = re.search(r'```python(.*?)```', full_response.response, re.DOTALL)
    if code_response:
        code = code_response.group(1).strip()
        with open(fname+".py", "w") as f:
            f.write(code)
    else:
        print("No code found in the response.")

# Execute gen_code.py from the current directory

def exec_qode(inputs, fname = "gen_qode"):
    cmd = 'python '+ fname + ".py " + inputs
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    out, err = p.communicate() 
    result = out.decode("utf-8").split('\\n')
    for line in result:
        print(line)

extract_and_save(response, "gen_qode")
inputs = "10"
exec_qode(inputs, "gen_qode")