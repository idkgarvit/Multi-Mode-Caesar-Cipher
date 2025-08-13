# Multi-Mode Caesar Cipher with Brute Force & Word-to-Number Key Support

## 📜 Overview
This project is a **Python-based Caesar Cipher tool** designed for encryption, decryption, and brute force attacks.  
It was originally created as part of a cryptography lab assignment but has been enhanced with extra features for flexibility and usability.

## ✨ Features
- **Encryption & Decryption** for both lowercase and uppercase alphabets.
- **Brute Force Mode** to crack unknown keys by testing all possible shifts.
- **Word-to-Number Key Conversion** — Enter keys as either numbers (`3`) or number words (`three`).
- **Multi-Mode Execution** — Choose to:
  - Encrypt only
  - Decrypt only
  - Encrypt & Decrypt in one go
  - Run a brute force attack

## 📂 Project Structure
```
main.py        # Main program file
requirements.txt # Dependencies list
```

## 🚀 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/caesar-cipher.git
   cd caesar-cipher
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python main.py
   ```

## ⚙️ Modes
When prompted:
- `E` → Encrypt text
- `D` → Decrypt text
- `B` → Encrypt & Decrypt in one go
- `BF` → Brute force attack

## 📌 Example
```
Do you want to (E)ncrypt, (D)ecrypt, (B)oth, or (BF) brute force? e
Enter the text: Hello World
Enter the key value : three
Encrypted: Ebiil Tloia
```

## 🔮 Future Improvements
- Support for **multiple languages**, including non-Latin scripts like Hindi and Japanese.
- Option to handle punctuation shifts.
- GUI interface for better user experience.

## 📦 Dependencies
- `word2number` — For converting number words to integers.

Install with:
```bash
pip install word2number
```

## 📜 License
This project is released under the MIT License.
