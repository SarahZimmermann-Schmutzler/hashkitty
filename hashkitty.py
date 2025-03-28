"""
HASHKITTY - A programm to crack hashed passwords.
"""

import argparse
import hashlib
import itertools
import string
from typing import Callable, Optional, Any


def get_hash_function(hash_mode: int) -> Callable[[bytes], Any]:
   """
    Returns the appropriate hash function based on the given hash mode.

    Args:
        hash_mode (int): Hash mode identifier (0 for MD5, 1 for SHA-1, 2 for SHA-256, 3 for SHA-512).

    Returns:
        Callable[[bytes], Any]: The hash function corresponding to the hash mode.

    Raises:
        ValueError: If an invalid hash mode is provided.
    """
   if hash_mode == 0:
       return hashlib.md5
   elif hash_mode == 1:
       return hashlib.sha1
   elif hash_mode == 2:
       return hashlib.sha256
   elif hash_mode == 3:
       return hashlib.sha512
   else:
        raise ValueError('Invalid Hash Mode. Supported are MD5 (0), SHA-1 (1), SHA-256 (2), SHA-512 (3).')
   

def read_hash(args: argparse.Namespace) -> Optional[str]:
    """
    Reads the hash value from the command-line given Hash or a file.

    Args:
        args (argparse.Namespace): Parsed command-line arguments.

    Returns:
        Optional[str]: The hash value as a string, or None if the file is not found or no hash is provided.
    """
    if args.hash:
        return args.hash
    elif args.hashfile:
        try:
            with open(args.hashfile, 'r') as f:
                return f.read().strip()
        except FileNotFoundError:
            print(f'Error: File {args.hashfile} was not found.')
            return None

    
def dictionary_attack(hash_value: str, hash_function: Callable[[bytes], Any], wordlist_file: str) -> Optional[str]:
    """
    Attempts to crack the hash using a Dictionary Attack.

    Args:
        hash_value (str): The hash value to crack.
        hash_function (Callable[[bytes], Any]): The hash function to use.
        wordlist_file (str): Path to the wordlist file.

    Returns:
        Optional[str]: The cracked password if found, otherwise None.
    """
    try:
        with open(wordlist_file, 'r') as file:
            for word in file:
                word = word.strip()
                word_hash = hash_function(word.encode()).hexdigest()
                if word_hash == hash_value:
                    print(f"Password found: {word}")
                    return word
    except FileNotFoundError:
        print(f'Error: File {wordlist_file} was not found.')
        return None
    print('Password not found.')
    return None
        

def brute_force_attack(hash_value: str, hash_function: Callable[[bytes], Any]) -> Optional[str]:
    """
    Attempts to crack the hash using a Brute-Force Attack.

    Args:
        hash_value (str): The hash value to crack.
        hash_function (Callable[[bytes], Any]): The hash function to use.

    Returns:
        Optional[str]: The cracked password if found, otherwise None.
    """
    charset = string.ascii_lowercase + string.digits
    for length in range(1,8): # length of tried passwords
        for guess_tuple in itertools.product(charset, repeat=length):
            guess = ''.join(guess_tuple)
            guess_hash = hash_function(guess.encode()).hexdigest()
            if guess_hash == hash_value:
                print(f"Password found: {guess}")
                return guess
    else:
        print('Password not found.')
        return None


def main() -> None:
    """
    Main function for the password cracker script.

    This function serves as the entry point of the program and performs the following steps:

    1. **Argument Parsing**:
        - Configures and processes command-line arguments using argparse.
        - Supported arguments see below in the code

    2. **Hash Function Selection**:
        - Determines the hash function to use (MD5, SHA-1, SHA-256, SHA-512) based on the user-provided hash mode using `get_hash_function`.

    3. **Hash Reading**:
        - Reads the hash value either directly from the command-line argument or from a file using `read_hash`.
        - If no valid hash value can be retrieved, the program exits.

    4. **Attack Execution**:
        - Executes the attack mode specified by the user:
            - **Brute-Force Attack** (`-a 0`): Attempts to find the password by iterating through all possible combinations of characters up to a fixed length.
            - **Dictionary Attack** (`-a 1`): Attempts to find the password by hashing each word in a provided wordlist file and comparing it to the target hash.
        - If the dictionary attack is selected but no wordlist file is provided, an error message is displayed.

    5. **Output**:
        - If the password is found, it is printed to the console.
        - If the password cannot be found, a message is displayed indicating failure.

    Usage Examples:
        - Brute-force attack with SHA-256:
            `python script.py -m 2 -a 0 -h 5e884898da28047151d0e56f8dc6292773603d0d6aabbddf8bc1d84a0b4e7f08`
        - Dictionary attack with MD5 and a wordlist:
            `python script.py -m 0 -a 1 -w wordlist.txt -H hashfile.txt`

    Returns:
        None
    """
    # create parser; turn off help because -h should stand for "Hash"
    parser = argparse.ArgumentParser(description='Hashed Password Cracker', add_help=False)

    # add arguments
        # Defined help argument bec. -h stands for "hash" in this prgram
    parser.add_argument('--help', action='help', help='Customized help argument')
        # Hash Modes: MD5 (0), SHA-1 (1), SHA-256 (2), SHA-512 (3)
    parser.add_argument('-m', required=True, type=int, choices=[0, 1, 2, 3], help='Hash Mode: MD5 (0), SHA-1 (1), SHA-256 (2), SHA-512 (3)')
        # Attack Modes: Brute-Force (0) or Dictionary Attack (1)
    parser.add_argument('-a', required=True, type=int, choices=[0, 1], help='Attack Mode: Brute-Force-Attack (0), Dictionary Attack (1)')
        # Wordlist for Dictionary Attack (required for this type of attack)
    parser.add_argument('-w', '--wordlist', type=str, help='Path to wordlist for Dictionary Attack')
        # Hash as direct parameter or in a file; mutually exclusive group ensures that either `-h` or `-H` is provided
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-h', '--hash', type=str, help='Hash as string')
    group.add_argument('-H', '--hashfile', type=str, help='Path to hashfile')
    
    # parse arguments
    args = parser.parse_args()
    
    # getting right Hash Function via Hash Mode
    hash_function = get_hash_function(args.m)

    # reading the Hash
    hash_value = read_hash(args)
    
    if not hash_value:
        return # exit if hash could not be read

    # handling Attack Mode
        # Brute-Force-Attack
    if args.a == 0:
        brute_force_attack(hash_value, hash_function)
        # Dictionary Attack
    elif args.a == 1:
        if not args.wordlist:
            print('Error. For this attack you need a wordlist.')
        else:
            dictionary_attack(hash_value, hash_function, args.wordlist)

if __name__ == "__main__":
    main()