# Import the subprocess module to run bash commands
import subprocess

# Define a function to send a message to chatgpt and get a response
def chatgpt(message):
  # Use the chatgpt command-line tool with your API token
  # Set the engine to gpt-3.5-turbo and the mode to bash
  # Use the --json flag to get the response as a JSON object
  command = f"chatgpt --token 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 --engine gpt-3.5-turbo --mode bash --json {message}"
  # Run the command and capture the output
  output = subprocess.run(command, capture_output=True, shell=True)
  # Decode the output and parse the JSON object
  response = output.stdout.decode().strip()
  response = json.loads(response)
  # Return the text of the response
  return response["text"]

# Prompt the user to describe a linux task
task = input("Describe a linux task: ")

# Use chatgpt to generate a bash command for the task
command = chatgpt(task)

# Print the command
print(f"The command for {task} is: {command}")

# Execute the command and print the output
output = subprocess.run(command, capture_output=True, shell=True)
print(output.stdout.decode())