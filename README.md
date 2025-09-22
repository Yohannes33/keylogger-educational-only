🔐 Keylogger Project
🌟 Overview
Welcome to the Keylogger Project, a sophisticated Python-based application designed to capture and log keyboard inputs, system information, and clipboard data, then securely transmit this information via email. This project showcases advanced programming skills in system monitoring, network communication, and secure data handling, making it a standout addition to any technical portfolio. 🚀

⚠️ Note: This project is intended for educational purposes only and should be used responsibly and ethically, with explicit permission from any system being monitored.

✅ Features

⌨️ Keystroke Logging: Captures every keypress with precision, storing it in a readable format for analysis.
💻 System Information Gathering: Collects detailed system and network information, including hostname, IP address, processor details, and operating system specifications.
📋 Clipboard Monitoring: Retrieves and logs clipboard contents, providing insights into copied data.
📧 Email Integration: Securely sends logged data to a specified email address using SMTP with TLS encryption.
🗑️ File Management: Automatically cleans up generated log files to maintain discretion and minimize storage usage.

🛠️ Technologies Used

🐍 Python: Core programming language for implementation.
📚 Libraries:
pynput: For capturing keyboard events.
smtplib & email: For secure email transmission of logs.
socket & platform: For gathering system and network information.
win32clipboard: For accessing clipboard data on Windows systems.
os: For file handling and cleanup.



⚙️ Installation

📥 Clone the Repository:
git clone https://github.com/Yohannes33/keylogger-updated.git
cd keylogger-updated


📦 Install Dependencies: Ensure Python 3.x is installed, then install the required libraries:

pip install pynput pywin32


🔧 Configure Email Settings:

Update the email_address, password, and toaddr variables in the script with your email credentials.
Ensure you have an app-specific password if using Gmail (required for 2FA-enabled accounts).


📂 Set File Path:

Modify the file_path variable to a valid directory on your system where logs will be temporarily stored.



🚀 Usage

Run the script:
python keylogger.py


The keylogger will:

Start capturing keystrokes and save them to key_log.txt. 🖱️
Collect system information and save it to systeminfo.txt. 🖥️
Capture clipboard contents and save them to clipboardinfo.txt. 📋
Send all logs to the specified email address. 📬
Delete the log files to clean up. 🧹


Press the Esc key to stop the keylogger. ⏹️


🧩 Code Structure

⌨️ Keystroke Logging: Uses pynput.keyboard.Listener to capture and log keystrokes in a human-readable format.
📧 Email Functionality: Utilizes smtplib and email.mime to construct and send emails with attachments securely.
💻 System Information: Gathers hardware and network details using socket and platform.
📋 Clipboard Access: Retrieves clipboard data via win32clipboard.
🗑️ File Cleanup: Removes temporary files using os.remove.

⚖️ Ethical Considerations
This project is designed for educational and demonstration purposes only. Unauthorized use of keyloggers violates privacy laws and ethical standards. Always obtain explicit consent from system owners before deployment. 🛡️

🔮 Future Enhancements

🌐 Add support for cross-platform clipboard access (e.g., Linux, macOS).
📡 Implement real-time logging to a remote server.
🔒 Enhance security with encrypted log files before transmission.

📜 License
This project is licensed under the MIT License. See the LICENSE file for details. 📄
