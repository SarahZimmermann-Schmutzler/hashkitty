# HASHKITTY

A programm to **crack hashed passwords via Brute-Force or Dictionary Attack**.  
This is a lightweight version of the known [hashcat](https://hashcat.net/hashcat/) - tool.  

The program was created as part of my training at the Developer Academy and is used exclusively for teaching purposes.  

## Table of Contents

1. [Technologies](#technologies)
1. [Getting Started](#getting-started)
1. [Usage](#usage)
   * [Program Options](#program-options)
   * [Program Flow](#program-flow)
   * [Example Run](#example-run)  

## Technologies

* **Python** 3.12.2
  * **argparse, hashlib, itertools, string, typing**

## Getting Started

0) [Fork](https://docs.github.com/de/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) the project to your namespace, if you want to make changes or open a [Pull Request](https://docs.github.com/de/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests).

1. [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) the project to your platform if you just want to use it:

    ```bash
    git clone git@github.com:SarahZimmermann-Schmutzler/hashkitty.git
    ```

1. There are **no dependencies** to install. All Python modules needed are part of the standard library.

## Usage

* For the further commands navigate to the directory you cloned **hashkitty** into.

### Program Options

* To see all available **program options** have a look in the `help-section`:

    ```bash
    python hashkitty.py --help
    ```

    | Option (Long) | Short | Choices | Description | Required? |
    | ------------- | ----- | ------- | ----------- | --------- |
    | --help |  |  | Get a list of the **available options** | no |
    | --hash | -h |  | Hash as **string** | yes, if no -H |
    | --hashfile | -H |  | Path to **hashfile** | yes, if no -h |
    |  | -m | 0 (MD5) <br> 1 (SHA-1) <br> 2 (SHA-256) <br> 3 (SHA-512) | **Hash Mode** | yes |
    |  | -a | 0 (Brute-Force Attack) <br> 1 (Dictionary Attack) | **Attack Mode** | yes |
    | --wordlist | -w |  | Path to wordlist for **Dictionary Attack** | yes |

### Program Flow

* **Hashes** are one-way encryptions that convert a password into a cryptographic fingerprint. Since hashes are difficult to decrypt directly, Hashkitty attempts to find the original password by hashing different possible passwords and comparing them with the given hash until it finds a match.
  * The **Hash** can be specified in a **file or directly inline**.
  * This programm supports the **Hash Modes: MD5, SHA-1, SHA-256 and SHA-512**.

* **Attack Modes**:
  * **Brute-Force-Attack**: Based on the Hash value and function the program systematically tries all possible combinations of characters to guess a password or access. It is a time-consuming “trial and error” method in which every possible password is tried until the right one is found.
    * If the password is found, it is printed to the console.

  * **Dictionary Attack**: A dictionary attack involves trying out a pre-prepared list of commonly used passwords. It's faster than a Brute-Force Attack, but won't work if the password isn't in the list.  
    * A **wordlist** is needed to run a Dictionary Attack, e.g. [rockyou.txt](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt).
    * If the password is found, it is printed to the console.

### Example Run

* To run a **Brute-Force Attack** with an inline SHA-256 hash use the following command:

    ```bash
    python hashkitty.py -a 0 -m 2 -h "6ca13d52ca70c883e0f0bb101e425a89e8624de51db2d2392593af6a84118090"
    ```

  * After a while it will yield the following **output**:

    ```bash
    Password found: abc123
    ```

* To run a **Dictionary Attack** with a SHA-512 hash storing in the [file](./hashkitty_file.txt) and a wordlist in the same directory you need this command:

    ```bash
    python hashkitty.py -a 1 -m 3 -H hashkitty_file.txt -w rockyou.txt
    ```

  * It will yield the following **output**:

    ```bash
    Password found: 0123456789
    ```
