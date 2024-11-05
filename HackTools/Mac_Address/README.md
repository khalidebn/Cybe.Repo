# **Change MAC Address Script**

A simple Python script to change the MAC address of a network interface on Unix-based operating systems. This script can be useful for network security testing, bypassing certain network restrictions, or preserving privacy by masking your device's actual hardware MAC address

## **Features**

- **Change MAC Address:** Easily change the MAC address of aspecified network interface.
- **Validation:** This script includes input validation for both interface names and MAC address format.
- **Error Handling:** Provides clear error messages if invalid input is given.

## **Requirements**

- **Operating System**: Linux
- **Python Version:** Python 3.x
- **Permissions:** You need superuser (root) permissions to change network settings.
- Dependencies:

  - subprocess: Built-in Python module (no installation required).
  - argparse: Built-in Python module (no installation required).

- **Network-Tools:** The script uses ifconfig, which is part of the net-tools package. If ifconfig is not installed, you can install it using:

```
    sudo apt-get install net-tools
```

## Installation
