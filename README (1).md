# Caesar Cipher with ASCII (Python)

This project implements a Caesar Cipher encryption and decryption tool
in Python, using **ASCII values** instead of manually checking against
alphabet strings.

## Features

-   **Encryption**: Shift characters forward or backward based on a key.
-   **Decryption**: Retrieve the original message from the cipher text.
-   **Brute Force**: Try all possible 26 key shifts to crack the cipher.
-   **Word to Number Conversion**: Accepts both numeric keys (e.g., `3`)
    and number words (e.g., `three`) via `word2number`.

## Requirements

-   Python 3.x

-   Install dependency:

    ``` bash
    pip install word2number
    ```

## Usage

Run the script:

``` bash
python caesar_cipher.py
```

Choose a mode: - `E` → Encrypt - `D` → Decrypt - `B` → Both (Encrypt +
Decrypt) - `BF` → Brute Force

Example:

    Do you want to (E)ncrypt, (D)ecrypt, (B)oth, or (BF) brute force? e
    Enter the text: Hello World
    Enter the key value: 3
    Encrypted: Ebiil Tloia

## Notes

-   Works with both uppercase and lowercase letters.
-   Non-alphabet characters (numbers, spaces, punctuation) are preserved
    as-is.
-   Uses ASCII values via `ord()` and `chr()` for character shifting.

------------------------------------------------------------------------

Author: Your Name
