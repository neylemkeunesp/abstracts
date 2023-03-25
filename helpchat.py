#!/opt/homebrew/bin/python3.11 







# Description: This script is a chatbot that uses 
# GPT-3 to answer questions about linux commands

# Import the OpenAI library
import openai
import subprocess
import re

# Set up the OpenAI API client :
openai.api_key = "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"

# Set up the model (more models, visit https://beta.openai.com/playground)
model_engine = "gpt-3.5-turbo"
#? document the function

def txtcomp(rawtxt):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a chatbot"},
            {"role": "user", "content": rawtxt},
        ]
            )
    result = ''
    for choice in response.choices:
        result += choice.message.content
    return result

def find_quoted_substring(s):
  # find all the quoted substrings in s
  quoted_substrings = re.findall(r'"[^"]*"|\`\`\`[^\`]*\`\`\`|"[^"]*"|\'[^\']*\'|\`[^\`]*\`', s)
  if len(quoted_substrings)>0:
    quoted_substrings2=[remove_quotes(s) for s in quoted_substrings]
  return quoted_substrings2 if quoted_substrings2 else None
def remove_quotes(s):
  s1=s.replace("```bash","```")
  # retorna uma string sem aspas simples, duplas ou triplas no início ou no final
  return s1.strip("'\"\`\n")
if __name__ == '__main__':
    task = input("Describe a linux task: ") 
    rawtxt = "Return just the bash command that: " + task
    output=txtcomp(rawtxt)
    print(output)
    command_lis=find_quoted_substring(output)
    count=0
    for command in command_lis:
        print(str(count)+") The command is: " + command) 
        count+=1
    command_choice=int(input("Select the command to be executed (-1 to none):  "))
    print("Executing: " + command_lis[command_choice])
    if command_choice>-1: 
        print("The output is:\n")
        output = subprocess.run(command_lis[command_choice], capture_output=True, shell=True)
        print(output.stdout.decode())
    else:
        print("No command executed")