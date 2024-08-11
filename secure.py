
# how to secure the code after the review and the error messages 
import os
# Dangerous use of os.system (could lead to command injection)
import subprocess

def get_secret_key():
    # Use an environment variable for the secret key
    secret_key = os.getenv('SECRET_KEY', 'default_key')
    return secret_key

def execute_command(user_input):
    # Use subprocess.run for safer command execution
    subprocess.run(['echo', user_input], check=True)

if __name__ == "__main__":
    key = get_secret_key()
    print(f"Secret Key: {key}")
    execute_command("Hello, World!")

