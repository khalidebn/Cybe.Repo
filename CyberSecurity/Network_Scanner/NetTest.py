# Note

# scapy.ls >> List all the fields that have been set
# scapy.ls(scapy.ARP())

# .summary() >> This method give you a result or summary of what you created above.

# .show() >> Show us more details about the content of the packests

# -----------------------------------------------------------------------------------------------

### Send and receive packets (sr) ####
# .sr() >> function is for sending packets and receiving answers
# .sr1() >> is a variant that only returns one packet that answered the packet (or the packet set) sent.
# The packets must be layer 3 packets (IP, ARP, etc.).
# srp() do the same for layer 2 packets (Ethernet, 802.3, etc.).

# ------------------------------------------------------------------------------------------
# Some function have been used:
# Summary
# print(answered_list.summary())
# print(unanswered.summary())
# print(arp_broadcast.summary())


#!/usr/bin/env python
import scapy.all as scapy
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target",
                      help="Target IP / IP range.")
    options, arguments = parser.parse_args()
    return options


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast,
                              timeout=1, verbose=False)[0]
    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list


def print_result(results_list):
    print("IP\t\t\tMAC Address\n-------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])


options = get_arguments()
scan_result = scan(options.target)
print_result(scan_result)
