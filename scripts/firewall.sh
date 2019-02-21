#!/bin/bash
# Run this with root privileges
iptables -N UDP
iptables -A UDP -p udp -m udp --dport 123 -j ACCEPT
iptables-save > /etc/iptables/iptables.rules

# Run
# systemctl start iptables.serviec

