from colorama import Fore
import argparse
import os
import time
import subprocess

def get_running_tasks():
    try:
        # Execute the 'tasklist' command to list processes
        result = subprocess.run(['tasklist'], capture_output=True, text=True, check=True)
        output_lines = result.stdout.split('\n')

        # Parse the output to extract process names
        tasks = []
        for line in output_lines[3:]:  # Skip the header lines
            if line.strip():  # Check if line is not empty
                parts = line.split()
                name = parts[0]
                tasks.append(name)
        return tasks
    except subprocess.CalledProcessError:
        print("Error: Unable to retrieve running tasks.")
        return []

pyFLLW = f"{Fore.GREEN}pyFLLW {Fore.CYAN}>>"
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('filename', nargs='?', help='Specify filename')
parser.add_argument('flags', nargs='*', help='Specify flags')
args = parser.parse_args()
filename = args.filename
flags = args.flags
if not filename.endswith(".spwn"):
    filename = filename + ".spwn"
try:
    initial_mod_time = os.path.getmtime(filename)
except:
    pass

print(f"{pyFLLW} Ready and waiting for changes to {filename}{Fore.WHITE}")
while True:
    try:
        current_mod_time = os.path.getmtime(filename)
        if current_mod_time != initial_mod_time:
            print(f"{pyFLLW} Detected changes in {filename}, running spwn...{Fore.WHITE}")

            try:
                if "GeometryDash.exe" in get_running_tasks():
                    os.system("taskkill /F /IM GeometryDash.exe > NUL 2>&1")
                    print(f"{pyFLLW} Closed Geometry Dash.{Fore.WHITE}")
                if flags != []:
                    os.system(f"spwn build {filename} {flags}")
                else:
                    os.system(f"spwn build {filename}")
                print(f"{pyFLLW} Finished building, running Geometry Dash...{Fore.WHITE}")
                os.system("start steam://rungameid/322170")
            except:
                print(f"{pyFLLW} Error while building, waiting for new changes...{Fore.WHITE}")

            initial_mod_time = current_mod_time
        time.sleep(0.1)
    except FileNotFoundError:
        print(f'{pyFLLW} Detected rename or delete of "{filename}", closing FLLW...{Fore.WHITE}')
        break