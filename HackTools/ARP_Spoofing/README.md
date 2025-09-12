# ARP Spoofing Tool

This Python script implements ARP spoofing using [Scapy](https://scapy.readthedocs.io/en/latest/). It allows you to poison the ARP cache of a target and a gateway, redirecting traffic between them through your machine (Man-in-the-Middle attack).

## Features

- Sends crafted ARP packets to a target and gateway to spoof their ARP tables.
- Restores original ARP tables upon exit.
- Displays the number of packets sent in real time.

## Requirements

- **Python 3**
- **Scapy** library  
  Install with:  
  ```bash
  pip install scapy
  ```

- **Administrator/root privileges**  
  (ARP spoofing requires sending raw packets.)

## Usage

1. **Modify Target and Gateway IPs**

   Edit these lines in `arp_spoof.py`:
   ```python
   target_ip = "192.168.44.130"     # Victim IP address
   gateway_ip = "192.168.44.2"      # Gateway/Router IP address
   ```

2. **Run the script:**
   ```bash
   sudo python arp_spoof.py
   ```

3. **Stop the attack:**  
   Press `CTRL + C` to stop the program and automatically restore the ARP tables.

## How it works

- The script continuously sends forged ARP replies to the target and gateway, associating your MAC address with the IP address of the gateway and target respectively.
- This causes both devices to send their network traffic through your machine, enabling packet sniffing or modification.
- When interrupted, the script sends correct ARP replies to restore the network.

## Disclaimer

This tool is for **educational purposes only**. Unauthorized ARP spoofing is illegal and unethical. Only use it on networks you own or have permission to test.

## References

- [ARP Spoofing (Wikipedia)](https://en.wikipedia.org/wiki/ARP_spoofing)
- [Scapy Documentation](https://scapy.readthedocs.io/en/latest/)
