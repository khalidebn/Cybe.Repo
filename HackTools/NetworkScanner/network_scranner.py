#!/usr/bin/env python

import scapy.all as scapy


def scan(ip):

    # This var requesting the ARP & Broadcast(Ether) packets.
    arp_request = scapy.ARP(pdst=ip)
    broadcast_request = scapy.Ether(dst="xx:xx:xx:xx:xx:xx")
    arp_broadcast = arp_request/broadcast_request

    # Summary
    print(arp_broadcast.summary())
    arp_broadcast.show()


scan("192.168.44.0")
