# tcpdump

```bash
tcpdump -i eth0 host $ip and port $port

tcpdump -i eth0 src host $ip and dst port 514 or src port 517

tcpdump -i eth0 src host $ip and '(port 514 or 517)'

tcpdump -i eth0 -s 0 -w redis.pcap

tcpdump -i eth0 tcp

tcpdump -i eth0 not udp

tcpdump -i eth0 udp or tcp or icmp

tcpdump -i any port 53

tcpdump -i any port 53 -w capturedfile.cap

tcpdump -i eth0 net 192.168.1.0/24 and portrange 135-139

tcpdump -i eth0 host $ip and port 514 -c 2

```
