#the isecure code
import os
def get_secret_key():
    # Hardcoded secret key (not recommended)
    secret_key = "12345"
    return secret_key

def execute_command(user_input):
    
    os.system(f"echo {user_input}")

if __name__ == "__main__":
    key = get_secret_key()
    print(f"Secret Key: {key}")
    execute_command("Hello, World!")

