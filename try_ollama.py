# Install Ollama from https://ollama.com/download
# Install a Model from https://ollama.com/models
# Install the Ollama Python client
# Start the Ollama server if not already running

import ollama

# print(ollama.list())
# print(ollama.show('qwen2.5-coder:0.5b'))

# Initialize the Ollama client
client = ollama.Client()

# Define the model and the input prompt
model = "qwen2.5-coder:0.5b"  # Replace with your model name
prompt = "Write a Python function to calculate the factorial of a number. Include a main function to test the factorial function with a command line argument. The name of the function should be gen_code()."

# Send the query to the model
response = client.generate(model=model, prompt=prompt)

# Print the response from the model
# print("Response from Ollama:")
# print(response.response)
# print("Response from Ollama (raw):")
# print(response)

# Extract the string inbetween the triple backticks
import re
code_response = re.search(r'```python(.*?)```', response.response, re.DOTALL)
# print(code_response.group(1)  else "No code found in the response.")

if code_response:
    code = code_response.group(1).strip()
    # Save the code to a file
    with open("gen_code.py", "w") as f:
        f.write(code)
else:
    print("No code found in the response.")

# Execute gen_code.py from the current directory

inputs = "10"

import subprocess
cmd = 'python gen_code.py ' + inputs

p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
out, err = p.communicate() 
result = out.decode("utf-8").split('\\n')
for line in result:
    print(line)