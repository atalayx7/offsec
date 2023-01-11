import ftplib

def ftp_login_list()
    # List of IP addresses to check
    ip_addresses = ['10.0.0.1', '10.0.0.2', '10.0.0.3', '10.0.0.4', '10.0.0.5']

    # Iterate over the IP addresses
    for ip in ip_addresses:
        # Connect to the FTP server
        ftp = ftplib.FTP(ip)

        # Try to login as anonymous user
        try:
            ftp.login()
            print(f'Anonymous login is allowed on {ip}')
        except ftplib.error_perm:
            print(f'Anonymous login is not allowed on {ip}')

        # Close the connection
        ftp.close()
        
def ftp_login_subnet():
    for i in range(1, 255):
        try:
            ftp = ftplib.FTP('192.168.0.' + str(i))
        except ftplib.error_temp:
            print('Unable to reach FTP server at 192.168.0.' + str(i))
            continue
        try:
            ftp.login('anonymous', '')
            print('Anonymous login is enabled on 192.168.0.' + str(i))
        except ftplib.error_perm:
            print('Anonymous login is disabled on 192.168.0.' + str(i))
        ftp.quit()
