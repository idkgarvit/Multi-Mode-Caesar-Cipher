# 🔐 Caesar Cipher with ASCII (Python)

A Python implementation of the **Caesar Cipher** algorithm using **ASCII values** (`ord()` / `chr()`) for encryption and decryption.  
This project demonstrates the basics of **cryptography, brute force attacks, and word-to-number conversion** in Python.

---

## 🚀 Features
- ✅ **Encrypt Text** → Shift characters using a key  
- ✅ **Decrypt Text** → Retrieve original message using the key  
- ✅ **Brute Force Attack** → Try all 26 possible shifts to crack unknown keys  
- ✅ **Word-to-Number Support** → Key can be given as number (`3`) or word (`three`)  
- ✅ **Preserves Non-Alphabet Characters** → Numbers, spaces, punctuation remain unchanged  

---

## 📂 Project Structure

📁 Caesar-Cipher-ASCII
│── caesar_cipher.py        # Main script
│── README.md               # Documentation (this file)
│── requirements.txt        # Python dependencies

---

## 🛠️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/Caesar-Cipher-ASCII.git
   cd Caesar-Cipher-ASCII
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 📌 Usage

Run the program:

```bash
python caesar_cipher.py
```

Choose a mode:
- `E` → Encrypt
- `D` → Decrypt
- `B` → Both (Encrypt + Decrypt)
- `BF` → Brute Force (try all keys)

### 🔑 Example (Encryption)

```
Do you want to (E)ncrypt, (D)ecrypt, (B)oth, or (BF) brute force? e
Enter the text: Hello World
Enter the key value: 3
Encrypted: Ebiil Tloia
```

### 🔓 Example (Decryption)

```
Do you want to (E)ncrypt, (D)ecrypt, (B)oth, or (BF) brute force? d
Enter the text: Ebiil Tloia
Enter the key value: 3
Decrypted: Hello World
```

### 🕵️ Example (Brute Force Attack)

```
Do you want to (E)ncrypt, (D)ecrypt, (B)oth, or (BF) brute force? bf
Enter the cipher text to brute force: Ebiil Tloia

...... Brute force results ......
Key 0: Ebiil Tloia
Key 1: Fcjjm Umpjb
Key 2: Gdkkn Vnqkc
...
Key 23: Hello World   ✅
Key 24: Ifmmp Xpsme
Key 25: Jgnnq Yqtnf
```

---

## 📦 Requirements
- Python 3.x
- Dependencies:
  ```txt
  word2number
  ```

Or install manually:
```bash
pip install word2number
```

---

## 📖 How it Works
1. Each character is converted to its **ASCII value** using `ord()`.  
2. A shift (positive or negative) is applied modulo 26.  
3. The result is converted back to a character with `chr()`.  
4. Non-alphabet characters (numbers, punctuation, spaces) remain unchanged.  
5. Decryption simply reverses the process.  

---

## 🎯 Learning Goals
- Understand **classical cryptography (Caesar cipher)**  
- Implement **encryption & decryption algorithms** in Python  
- Learn about **brute force attacks** and why weak ciphers fail  
- Practice working with **ASCII values** and string manipulation  

---

## 📌 Future Improvements
- Add support for custom alphabets  
- Implement **ROT13 mode** (common variant of Caesar Cipher)  
- Add **GUI version** (Tkinter/Flask app)  
- Extend project to **other ciphers** (Vigenère, Substitution)  

---

## 🤝 Contributing
Pull requests are welcome! If you’d like to improve the project, fork it and submit a PR.  

---

## 📜 License
This project is licensed under the MIT License.  

---

## 👨‍💻 Author
**Your Name**  
- 🌐 [GitHub](https://github.com/idkgarvit)  
- 💼 [LinkedIn](https://www.linkedin.com/in/garvit-kanojia-399701277/)  

---
