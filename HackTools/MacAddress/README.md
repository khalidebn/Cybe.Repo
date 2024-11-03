# **Change MAC Address Script**

This Python script allows users to change the MAC address of a specified network interface on a Linux system. It is useful for privacy, security testing, or troubleshooting network-related issues.

## **Features**

- Simple and Easy to Use: Quickly change the MAC address using a single command.
- Argument Parsing: Uses argparse to handle command-line arguments effectively.
- Network Management: Temporarily disables and then re-enables the network interface to apply the changes.

## **Requirements**

- Operating System: Linux
- Python Version: Python 3.x
- Dependencies:
  - subprocess: Built-in Python module (no installation required).
  - argparse: Built-in Python module (no installation required).

**Network** Tools: The script uses ifconfig, which is part of the net-tools package. If ifconfig is not installed, you can install it using:
'''
sudo apt-get install net-tools

'''
