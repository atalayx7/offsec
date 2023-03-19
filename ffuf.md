# ffuf

```bash

ffuf -u http://URL/FUZZ -w /opt/SecLists/Discovery/Web-Content/common.txt -X POST -fc 405

ffuf -u http://URL/FUZZ -w /usr/share/wordlists/dirb/common.txt -mc 200,204,301,302,307,401 -o results.txt

ffuf -u $URL/FUZZ/ -w $wordlist

ffuf -u $URL/FUZZ -w $wordlist -recursion

ffuf -u $URL/FUZZ -w $wordlist -recursion -e .bak  

ffuf -u $URL/W1 -w $wordlist:W1 -e .bak  

ffuf -u $URL/FUZZ -w $wordlist -s   #silent

ffuf -u $URL/FUZZ -w $wordlist -s | tee ./outfile.txt

ffuf -u $URL/FUZZ -w $wordlist -of html -o ./outputfile.txt

ffuf -u $URL/FUZZ -w $wordlist -of html -o ./outputfile.txt -b "NAME1=VALUE1; NAME2=VALUE2" #cookie

ffuf -u $URL/FUZZ -w $wordlist -of html -o ./outputfile.txt -b -H "NAME1=VALUE1; NAME2=VALUE2" #header
 
ffuf -u https://W2.io/W1 -w ./wordlist:W1 -w ./domains:W2

ffuf -request /tmp/request -w ./wordlist 

ffuf -u $URL -w vhostnames.txt -H “Host: FUZZ. target” -acc “www”

ffuf -u $URL/FUZZ -w $wordlist --replay-proxy http://127.0.0.1:8080

ssh -R 8888:localhost:8080 ffuf     #ffuf proxy
ffuf -u $URL/FUZZ -w ./wordlist -replay-proxy http://127.0.0.1:8888

ffuf -request search.req -request-proto http -w special-chars.txt -mc all  #fuzzing
```
