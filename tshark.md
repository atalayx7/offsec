# tshark

```bash
tshark -n -r traffic.pcapng -Y 'dns' > dns.txt

tshark -r data.pcap -T fields -e usb.capdata | grep -v '00:00:00:00:00:00:00:00' | cut -d ':' -f 3

tshark -r data.pcap -T fields -e http.host -e http.request.uri http | sort | uniq -c | sort -nr | more

tshark -r data.pcap -T fields -e http.host -e http.request.uri http | grep -vE "google\. | apple\." | sort | uniq -c | more

tshark -r data.pcap -w $filename.pcap ip.addr==$ip

tshark -r /tmp/testCap.pcap -T fields -e ip -f "port 80 or port 443 or port 53"

tshark -i $interface

tshark -i $interface -w /tmp/traffic.pcap

tshark -i $interface -f "port 80 or port 443 or port 53" -b filesize:5 -a files:3 -w /tmp/update.pcap

tshark -i $interface -T fields -e ip -f "port 80 or port 443" | cut -d "," -f 2,3

tshark -i $interface -T fields -e ip -f "port 80 or port 443" | UNIQ
```
