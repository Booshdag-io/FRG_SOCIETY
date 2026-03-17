\# 💀 FRG\_SOCIETY | Project DPRK (Educational PoC)



This repository contains a \*\*Cybersecurity Proof of Concept (PoC)\*\* developed as a project for the Computer Science career. It simulates a complete ransomware lifecycle: \*\*Encryption\*\*, \*\*User Notification\*\*, and \*\*System Restoration\*\*.



\## ⚠️ LEGAL DISCLAIMER

\*\*This software is for educational and research purposes only.\*\* The author is NOT responsible for any misuse of this tool. Unauthorized use of this script on systems you do not own is illegal. This project was created to demonstrate how symmetric encryption works and how to develop recovery tools.



\---



\## 🛠️ Technical Stack

\* \*\*Language:\*\* Python 3.10+

\* \*\*Encryption Standard:\*\* AES-128 (via Fernet Symmetric Encryption)

\* \*\*Libraries:\*\* `cryptography`, `pygame`, `rich`

\* \*\*Target OS:\*\* Windows (Requires Administrator Privileges)



\## 📂 Project Structure

1\. \*\*`fuck\_rg.py`\*\*: The main execution engine. It performs a recursive scan of the `C:\\` drive, excluding critical system folders to avoid OS instability, and encrypts files.

2\. \*\*`ui.py`\*\*: The visual impact module. Using Pygame, it launches a full-screen warning with the FRG\_SOCIETY ASCII art.

3\. \*\*`frg\_recovery.py`\*\*: The "Antidote". It uses the master key generated during infection to restore all files to their original state and cleans up the ransom note.



\## 🚀 Execution Flow

1\. \*\*Encryption Phase:\*\* The script generates a unique `root\_audit.key` in the root of `C:\\`.

2\. \*\*Persistence:\*\* A ransom note (`hello.txt`) is dropped on the User's Desktop with instructions.

3\. \*\*Lockscreen:\*\* The `ui.py` module takes over the display to inform the user of the "breach".

4\. \*\*Decryption:\*\* The user runs the recovery tool, which restores the filesystem and removes the traces.



\---

\*Developed by a 3rd-year Computer Science Student.\*

\---

\## 👤 Author

\*\*David Telles\*\*

\*Computer Science Student\*

\*GitHub:\* \[Booshdag-io](https://github.com/Booshdag-io)

