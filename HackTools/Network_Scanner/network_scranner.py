#!/usr/bin/env python

import scapy.all as scapy


def scan(ip):

    # This var requesting the ARP & Broadcast(Ether) packets.
    arp_request = scapy.ARP(pdst=ip)
    broadcast_request = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast = broadcast_request/arp_request

    print("-------------------------------------------------------------")
    # This give me two list the answerd list & unanswered list and I use [0] > to show me just the first list (answered_list)
    answered_list = scapy.srp(arp_broadcast, timeout=1, verbose=True)[0]

    print("\n IP \t\t\t Mac Address")
    print("-------------------------------------------------------------")

    for element in answered_list:
        print(element[1].psrc + "\t\t" + element[1].hwsrc)


scan(input("\n[+] Please Type Your IP Address Or The IP Range >> "))
