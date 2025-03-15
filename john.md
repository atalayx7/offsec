# Hash Cracking Commands

| No. | Description | Command |
|-----|-------------|---------|
| 1   | SSH Password Crack | `ssh2john.py id_rsa > id_rsa.hash`<br>`john id_rsa.hash --wordlist=/usr/share/wordlists/rockyou.txt` |
| 2   | SSHNG Password Crack | `sshng2john.py id_rsa > brainfuck.hash`<br>`john brainfuck.hash --wordlist:/usr/share/wordlists/rockyou.txt` |
| 3   | KeepPass2 Password Hash Crack | `keepass2john ignite.kdb > crack.txt`<br>`john --wordlist=/usr/share/wordlists/rockyou.txt crack.txt` |
| 4   | KDBX File Crack | `python keepass2john.py CEH.kdbx > passkey`<br>`john --format=KeePass --wordlist=/usr/share/wordlists/rockyou.txt passkey` |
| 5   | General John Crack | `john <FILENAME> --wordlist=/usr/share/wordlists/rockyou.txt`<br>`john hash --wordlist=/usr/share/wordlists/rockyou.txt` |
| 6   | SSH Password Crack with File | `ssh2john id_rsa > ignite`<br>`john --wordlist:/usr/share/wordlists/rockyou.txt ignite`<br>`chmod 700 id_rsa`<br>`ssh -i id_rsa root@$ip` |
| 7   | John The Ripper RSA Hash Crack | `~/git/JohnTheRipper/run/john rsa.hash --wordlists=/usr/share/wordlists/rockyou.txt --format=sshng` |
| 8   | RAR File Crack | `rar2john rarname.rar > rarhash.txt`<br>`john rarhash.txt --wordlist=/usr/share/wordlists/rockyou.txt` |
| 9   | ZIP File Crack | `zip2john <FILENAME>.zip > <FILENAME>.hash`<br>`john --show <FILENAME>.hash --wordlist=/usr/share/wordlists/rockyou.txt` |
| 10  | SHA256 Crack | `john --rules --wordlist=/usr/share/wordlists/rockyou.txt --format=raw-sha256 hashes.txt`<br>`john --wordlist=/usr/share/wordlists/rockyou.txt --format=raw-sha256 crack.txt` |
| 11  | SHA1 Crack | `john --wordlist=/usr/share/wordlists/rockyou.txt --format=raw-sha1 hashes.txt` |
| 12  | 7z Archive Crack | `./7z2john.py archive.7z > hash.txt`<br>`john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt` |
| 13  | 7z Hash Crack with Perl | `./7z2john.pl loot.7z > 7zhash`<br>`john 7zhash --wordlist:/usr/share/wordlists/rockyou.txt` |
| 14  | 7z Hashcat Crack | `/usr/share/john/7z2john.pl <FILENAME>`<br>`./hashcat -m 11600 <FILENAME> /usr/share/wordlists/rockyou.txt` |
| 15  | John The Ripper 7z Hash Crack | `~/git/JohnTheRipper/run/john --format=7z --wordlists=/usr/share/wordlists/rockyou.txt <HASHFILE>` |
| 16  | Unshadow Crack | `unshadow /etc/passwd /etc/shadow > crack.db`<br>`john crack.db` |
| 17  | MD5 Crack | `john --wordlist=/usr/share/wordlists/rockyou.txt --format=raw-md5 rack.txt` |
| 18  | MD4 Crack | `john --wordlist=/usr/share/wordlists/rockyou.txt --format=raw-md4 crack.txt` |
| 19  | RIPEMD128 Crack | `john --wordlist=/usr/share/wordlists/rockyou.txt --format=ripemd-128 crack.txt` |
| 20  | Whirlpool Crack | `john --wordlist=/usr/share/wordlists/rockyou.txt --format=whirlpool crack.txt` |
| 21  | PDF File Crack | `python pdf2john.py file.pdf > crack.txt`<br>`john --wordlist=/usr/share/wordlists/rockyou.txt crack.txt` |
| 22  | PuTTY Private Key Crack | `putty2john file.ppk > crack.txt`<br>`john --w=/usr/share/wordlists/rockyou.txt crack.txt` |
| 23  | Password Safe Crack | `pwsafe2john ignite.psafe3 > crack.txt`<br>`john --w=/usr/share/wordlists/rockyou.txt crack.txt` |
