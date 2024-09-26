# CyberSecurity
Few Projects worked on in my training program

The Caesar Cipher encryption and decryption program
How it works:
Encrypt Function: It shifts each letter of the message by the specified shift value. The modulo operation ensures the letters wrap around after 'Z' or 'z'.
Decrypt Function: It reverses the encryption by shifting the letters back by the given shift value.
Main Program: The user can choose between encryption and decryption, input the message and shift value, and the program will output the result accordingly.

Simple Image Encryption Tool usin Pixel Manipulation
Steps:
Encrypt the Image: Modify each pixel by applying a mathematical operation (e.g., adding a constant).
Decrypt the Image: Reverse the operation (e.g., subtract the same constant)
How it works:
Pillow (PIL) Library: Used to handle image processing (load, save, manipulate).
Encrypting: Adds a constant (key) to each pixel value (RGB values) and wraps around using modulo 256 (since pixel values range from 0 to 255).
Decrypting: Subtracts the same constant (key) from each pixel value, reversing the encryption.
User Input: The user selects whether to encrypt or decrypt, inputs the file paths and the key.

Password Strength Assessment Tool
This tool will evaluate passwords based on the following criteria:

Length: Password should be at least 8 characters.
Uppercase Letters: Checks for the presence of uppercase letters.
Lowercase Letters: Checks for lowercase letters.
Digits: Checks for the presence of numbers.
Special Characters: Checks for characters like !@#$%^&*().
How It Works:
Regex: The code uses regular expressions (re) to search for uppercase letters, lowercase letters, digits, and special characters.
Criteria: The password is evaluated against the five criteria (length, upper/lowercase letters, digits, and special characters).
Scoring: Based on how many criteria are met, the password strength is classified as Weak, Moderate, or Strong.
Feedback: The tool provides feedback and gives improvement suggestions if the password does not meet all criteria

Simple Keylogger
Ethical Reminder:
Always obtain consent from the user before running keyloggers on their device.
Use this tool only in educational or controlled environments with permission (e.g., on your own devices for cybersecurity testing).
Key Considerations:
Key Formatting: The program cleans up keypress data (e.g., removing quotes around characters and formatting special keys like Enter or Shift).
Stopping the Listener: The listener keeps running until it is manually stopped. You can modify this by adding a key to stop logging (like pressing ESC)
Security and Ethics:
Permissions: Ensure that you have explicit consent before running this keylogger on someone else’s system. Running a keylogger without permission is illegal and unethical.
Testing on Personal Devices: It's a useful tool for cybersecurity testing on your own devices to understand potential vulnerabilities.

Python Packet Sniffer:
We can build a simple packet sniffer using the scapy library, which is a powerful packet manipulation tool in Python. It allows us to capture, decode, and analyze network packets.
Ethical Reminder:
Only use this tool on networks you own or have permission to monitor.
Unauthorized packet sniffing is illegal and a violation of privacy.
How It Works:
scapy Library: scapy is a powerful Python library used for network traffic sniffing and packet manipulation. It captures packets at a low level (including IP, TCP, UDP, ICMP layers).

This function analyzes packets captured by scapy and extracts relevant information like Source IP, Destination IP, Protocol, Ports, and Payload Data.
It checks if the packet is an IP packet and further inspects if it's a TCP, UDP, or ICMP packet.
It prints the captured packet details to the console.
start_sniffer Function:

This function uses scapy’s sniff() method to capture network traffic. It listens on the specified network interface and calls the analyze_packet() function for each packet captured.
Interface: The user is prompted to input the network interface (e.g., eth0, wlan0, etc.) to start sniffing. This can vary based on your system setup.
Features:
Source/Destination IP: Displays the source and destination IP addresses for each packet.
Protocol Information: Shows whether the packet is using TCP, UDP, or ICMP.
Port Information: Displays the source and destination ports (for TCP/UDP packets).
Payload Data: Displays the payload data if available (as raw bytes).
