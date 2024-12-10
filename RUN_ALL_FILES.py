import subprocess
import sys

# Loop through the 31 Python files (from 1.py to 31.py)
for i in range(11, 32):
    file_name = f"{i}.py"

    try:
        # Run the Python file using subprocess
        result = subprocess.run([sys.executable, file_name], capture_output=True, text=True)

        # Check if the script ran successfully
        if result.returncode == 0:
            print(f"Successfully ran {file_name}")
        else:
            print(f"Error occurred while running {file_name}")
            print(f"Error Output: {result.stderr}")
    except Exception as e:
        print(f"An error occurred while trying to run {file_name}: {str(e)}")

print("Finished running all 31 files!")
