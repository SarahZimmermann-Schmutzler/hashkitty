# HASHKITTY

A programm to crack hashed passwords via Brute-Force or Dictionary Attack.  
This is a lightweight version of the known <a href="https://hashcat.net/hashcat/">**hashcat**</a> - tool.  

The program was created as part of my training at the Developer Academy and is used exclusively for teaching purposes.  

It was coded on **Windows 10** using **VSCode** as code editor.

## Table of Contents
1. <a href="#technologies">Technologies</a>  
2. <a href="#features">Features</a>  
3. <a href="#getting-started">Getting Started</a>  
4. <a href="#usage">Usage</a>  
5. <a href="#additional-notes">Additional Notes</a>  

## Technologies
* **Python** 3.12.2
    * **argparse, hashlib, itertools, string** (modules from standard library) 

## Features
The following table shows which functions **Hashkitty** supports:  

| Flag | Choices | Description | Required |
| ---- | ------- | ----------- | -------- |
| --help |  | Get a list of the available options | no
| -h <br> --hash |  | Hash as string | yes, if no -H |
| -H <br> --hashfile |  | Path to hashfile | yes, if no -h |
| -m | 0 (MD5) <br> 1 (SHA-1) <br> 2 (SHA-256) <br> 3 (SHA-512) | Hash Mode | yes |
| -a | 0 (Brute-Force Attack) <br> 1 (Dictionary Attack) | Attack Mode | yes |
| -w <br> --wordlist |  | Path to wordlist for Dictionary Attack | yes, if Dictionary Attack |

- **Hashes** are one-way encryptions that convert a password into a cryptographic fingerprint. Since hashes are difficult to decrypt directly, Hashkitty attempts to find the original password by hashing different possible passwords and comparing them with the given hash until it finds a match. 
    - The Hash can be specified in a file or directly inline.
    - This programm supports the Hash Modes: MD5, SHA-1, SHA-256 and SHA-512.

- **Brute-Force-Attack**: Based on the Hash value and function the program systematically tries all possible combinations of characters to guess a password or access. It is a time-consuming “trial and error” method in which every possible password is tried until the right one is found.
    - If the password is found, it is printed to the console.

- **Dictionary Attack**: A dictionary attack involves trying out a pre-prepared list of commonly used passwords. It's faster than a Brute-Force Attack, but won't work if the password isn't in the list.  
    - A wordlist is needed to run a Dictionary Attack.
    - If the password is found, it is printed to the console.

## Getting Started
0) <a href="https://docs.github.com/de/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo">Fork</a> the project to your namespace, if you want to make changes or open a <a href="https://docs.github.com/de/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests">Pull Request</a>.
1) <a href="https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository">Clone</a> the project to your platform if you just want to use the program.
2) There are no dependencies to install. All Python modules needed are part of the standard library. 

## Usage
- Make sure you are in the folder where you cloned **Hashkitty** into.  

- Help! What options does the program support!?    
    `python hashkitty.py --help`  

- To run a **Brute-Force Attack** use the following command in your terminal:  
    `python hashkitty.py -a 0 -m [Hash Mode] -h [Hash] or -H [path/to/hashfile]`  
    - <ins>Example</ins>: Crack the passwort with an inline hash (mode SHA-256):  
    `python hashkitty.py -a 0 -m 2 -h "6ca13d52ca70c883e0f0bb101e425a89e8624de51db2d2392593af6a84118090"`  
    >i: It takes a little time. Play the song "The Girl From Ipanema" and fetch a hot drink of your choice?
    - What you see, if the attack was successful:  
    ```
    Password found: abc123
    ```

- To run a **Dictionary Attack** you need this command:  
    `python hashkitty.py -a 1 -m [Hash Mode] -h [Hash] or -H [path/to/hashfile] -w [pathToWordlist]`  
    - <ins>Example</ins>: Crack the passwort with an a hash as a file (mode SHA-1) and a wordlist:  
    `python hashkitty.py -a 1 -m 3 -H "path/to/hashfile" -w "path/to/wordlist"`  
    - What you see, if the attack was successful:  
    ```
    Password found: [password]
    ```

## Additional Notes
**Hashlib** is a module in the Python standard library that provides functions for computing cryptographic hash values. It allows generating hashes for various algorithms such as MD5, SHA-1, SHA-256 and more..  
  
The **argparse** module is used to parse (read) command line arguments in Python programs. It allows to define arguments and options that can be passed to the program when starting it from the command line. These are then processed and are available in the program as variables.  
  
**Itertools** provides a collection of iterators for efficient loops in Python. It provides functions that enable common combinatorial operations such as infinitely iterating over elements.
  
The **string** module offers functions and constants that make working with character strings easier. It includes pre-built strings for letters, numbers, whitespace and other useful things, as well as string manipulation functions.  
  
**ChatGPT** was involved in the creation of the program (Debugging, Prompt Engineering etc.).  
  
I use **Google Translate** for translations from German into English.
