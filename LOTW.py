from pyfiglet import Figlet
from termcolor import colored
import socket
import sys
import requests

preview = Figlet(font='slant')
preview_rendertext = preview.renderText('Look_Out_The\nWindow')
print(colored(preview_rendertext , 'red'), '⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺')


def output_info(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        
        output = {
            '[IP]' : response.get('query'),
            '[Int_Prov]' : response.get('isp'),
            '[Org]' : response.get('org'),
            '[Country]' : response.get('country'),
            '[Region Name]' : response.get('regionName'),
            '[City]' : response.get('city'),
            '[ZIP]' : response.get('zip'),
            '[Lat]' : response.get('lat'),
            '[Lon]' : response.get('lon'),
        }
        
        for k, v in output.items():
            print(f'{k} : {v}')
            
    
    except requests.exceptions.ConnectionError:
        print(colored('\n[!!!] Check your connection!', 'red', attrs=['underline']))


try:
    def main():
        print('[*] Please select a server type:\n\n    [01] Static ip| Choose this type of server only if you have a static ip address.\n    [02] ngrok| '+colored('Not done yet, but you can still use the script along with ngrok manually.', 'red', attrs=['underline']))
        server_type = input('\n[*] Select a server type: ')
        if server_type == '01' or '1':
            print(colored('\n[!!!] MAKE SURE YOU HAVE THE RIGHT PORT OPEN!!!\n', 'red', attrs=['underline']))
            your_static_add = input('[*] Type your static address '+colored('[example: 91.x.x.x]', 'red')+': ')
            your_address = input(f'\n[*] Type your local address '+colored('[example: 192.168.1.10]', 'red')+': ')
            your_port = input('\n[*] Type your open port '+colored('[example: 5555]', 'red') + ': ')

            bind_ADDRESS = your_address, int(your_port)

            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind((bind_ADDRESS))
            colored_link_ip = colored(your_static_add, 'red')
            bruh = ':'
            colored_link_port = colored(your_port, 'red')
            print(f'\n[*] Send this link to the target: http://{colored_link_ip + bruh + colored_link_port} | You can use the url shorter to make the link more secure in appearance.')
            print(f'[*] Listening {bind_ADDRESS}...')    
            server.listen(1)
            client, client_addr = server.accept()

            print(colored('[*] Accepted connection!\n', 'blue'))
            ip = client_addr[0]
            output_info(ip=ip)

            input(colored('\n[*] Press ENTER to exit...\n', 'green', attrs=['underline']))

            client.close()
            server.close()
            
            sys.exit()

    if __name__ == '__main__':
        main()
    
except KeyboardInterrupt:
    sys.exit()