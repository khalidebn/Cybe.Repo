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

  - **subprocess**: Built-in Python module (no installation required).
  - **argparse**: Built-in Python module (no installation required).
  - **Network-Tools:** The script uses ifconfig, which is part of the net-tools package. If ifconfig is not installed, you can install it using:

```
    sudo apt-get install net-tools
```

## Installation

1. Clone the repository:

```
git clone https://github.com/khalidebn/change-mac-address.
```

2. Navigate to the directory:

```
cd change-mac-address
```

## Usage

To run the script, use the following command format:

```
python change_mac.py -i <interface> -m <new_mac_address>
```

## Arguments

- `-i, --interface`: The name of the network interface you want to change(e.g., `eth0`, `wlan0`).
- `-m, --mac`: The new MAC address to assign(in the format, `XX:XX:XX:XX:XX:XX`).

## Example

Change the MAC address of the `eth0` interface to `00:11:22:33:44:55`:

```
python change_mac.py -i eth0 -m 00:11:22:33:44:55
```

## Output

```
[+] Changing MAC address for eth0 to 00:11:22:33:44:55
```

## Check-out

To check the output of the `eth0` interface, type `ifconfig eth0`:

```
eth0      Link encap:Ethernet  HWaddr 00:11:22:33:44:55
          inet addr:192.168.1.2  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fe80::21a:2bff:fe3c:4d5e/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:123456 errors:0 dropped:0 overruns:0 frame:0
          TX packets:654321 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:98765432 (98.7 MB)  TX bytes:123456789 (123.4 MB)
          Interrupt:20 Memory:df200000-df220000
```

## Safety and Disclaimer

- **Root Access:** Root rights are needed for this script. When running scripts as a superuser, use caution and make sure you always know what the script is doing.
- **Network Impact:** Your network connection may be momentarily interrupted if you change your MAC address. Use it sensibly and only in settings where you are authorized to do so.
- **Legal Compliance:** Make sure that any changes to your MAC address are in accordance with local laws and regulations.
