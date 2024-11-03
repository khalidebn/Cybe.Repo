#!/usr/bin/env python

import subprocess
import argparse


def change_mac(interface, new_mac):
    print(f"[+] Changing MAC address for {interface} to {new_mac}")

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


parser = argparse.ArgumentParser(
    description="Change MAC address of a network interface")
parser.add_argument("-i", "--interface", dest="interface",
                    required=True, help="Type interface to change its MAC address")
parser.add_argument("-m", "--mac", dest="new_mac",
                    required=True, help="Type new MAC address")

args = parser.parse_args()

change_mac(args.interface, args.new_mac)
