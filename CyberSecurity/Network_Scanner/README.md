# Network Scanner

This project is a Python-based network scanner that identifies devices connected to a specified IP range in a local network. By leveraging ARP requests (Address Resolution Protocol), it can discover active devices and show their IP and MAC addresses, helping users see what devices are on their network.

## Project Overview

Network scanning is commonly used for identifying devices within a local network. This tool can be particularly useful for network administrators or IT professionals to monitor networked devices, troubleshoot connectivity issues, or identify unauthorized devices.

## Features

- Scans a specified IP address or IP range.
- Lists IP and MAC addresses of devices found on the network.
- Uses ARP requests and Ethernet broadcast frames for device detection.

## Requirements

- This script requires Python 3
- The Scapy library.

## Installation

1. **Clone the Repository**:

```
git clone https://github.com/khalidebn/network-scanner.git
cd network-scanner

```

2. **Install Scapy**: Scapy can be installed via pip:

```
pip install scapy

```

## Usage

1. **Run the Script**:

```
python network_scanner.py

```

2. **Provide the IP Range**: Enter a single IP or an IP range (e.g., 192.168.1.1/24).
3. **Example Output:**

```
-------------------------------------------------------------

 IP                     MAC Address
-------------------------------------------------------------
192.168.1.2             aa:bb:cc:dd:ee:ff
192.168.1.3             gg:hh:ii:jj:kk:ll

```

## Code Explanation

The core part of the script involves:

- ARP Request: Creates an ARP packet to request the MAC address of each IP.
- Broadcast Request: Encapsulates the ARP packet in an Ethernet frame with a broadcast destination.
- Response Handling: Displays IP and MAC addresses of responsive devices.

## Disclaimer

Use this script only on networks you own or have permission to scan. Unauthorized network scanning is illegal and may lead to consequences.

## License

```
MIT License

Copyright (c) [2024] [Khalid Ebn Elwaleed Mohamed]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
