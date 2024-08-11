import os
import sys
import subprocess

def run_bandit(path):
    """
    Run Bandit on a specified file or directory.
    """
    if os.path.exists(path):
        if os.path.isdir(path):
            command = ['bandit', '-r', path]
        else:
            command = ['bandit', path]
        subprocess.run(command)
    else:
        print(f"Error: {path} does not exist.")
        sys.exit(1)

def main():
    """
    Main function to check arguments and run Bandit.
    """
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} [directory_path_or_file_path]")
        sys.exit(1)
    else:
        run_bandit(sys.argv[1])

if __name__ == "__main__":
    main()

