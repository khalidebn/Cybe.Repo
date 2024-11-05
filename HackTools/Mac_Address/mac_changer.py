#!/usr/bin/env python

import subprocess
import argparse


def change_mac(interface, new_mac):
    print(f"[+] Changing MAC address for {interface} to {new_mac}")

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def is_valid_mac(mac):
    # Check if MAC address is in the correct format
    if len(mac) == 17 and all(char in "0123456789ABCDEFabcdef:" for char in mac):
        return True
    return False


def is_valid_interface(interface):
    return interface in ["eth0", "wlan0", "eth1", "wlan1"]


parser = argparse.ArgumentParser(
    description="Change MAC address of a network interface")
parser.add_argument("-i", "--interface", dest="interface",
                    required=True, help="Interface to change its MAC address")
parser.add_argument("-m", "--mac", dest="new_mac",
                    required=True, help="New MAC address")

args = parser.parse_args()


if not is_valid_interface(args.interface):
    print("[-] Invalid interface. Please specify a valid network interface.")
elif not is_valid_mac(args.new_mac):
    print("[-] Invalid MAC address format. Please specify a valid MAC address (e.g., 00:11:22:33:44:55).")
else:
    change_mac(args.interface, args.new_mac)
