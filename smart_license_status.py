#!/usr/bin/env python 

from scrapli.driver.core import IOSXEDriver
import json
import csv
import getpass

'''
Displays the format that must be followed so the Testbeds can ge generated.
'''
def get_inventory():
    print('Your CSV file must be in the following format:')
    print('''
    hostname  IP Address    Port
    R1        192.168.1.1   22
    R2        192.168.1.2   22
    R3        192.168.1.3   22
    R4        192.168.1.4   22
    R4        192.168.1.4   22
    R3        192.168.1.3   22
    
   
    '''
    )
    csv_file = input('Enter the name of your CSV Inventory file:')
    username = input('Enter your username:')
    password = input('Enter your password:')
    return csv_file, username, password

'''
Connects to devices in CSV, executes commands and then grabs output
'''
def get_status():
    csv_file, username, password = get_inventory()
    device = {}
    with open ("Smart_License_Status.csv", "w") as output_file:
        data_writer = csv.writer(output_file, delimiter=',', quotechar='"')
        data_writer.writerow(['Hostname', 'IP', 'Status'])
        with open(csv_file, "r") as csv_input:
            next(csv_input)
            for line in csv_input:
                # save the csv as a dictionary
                host, ip, port = line.replace(' ', '').strip().split(',')
                device = {'host': ip, 'auth_username' : username, 'auth_password': password, 'auth_secondary': password, 'port': int(port), 'auth_strict_key': False}
                print("Connecting to " + host + " on IP: " + ip + "...")
                try:
                    cli = IOSXEDriver(**device)
                    cli.open()
                    sh_ver = cli.send_command("show version | in Smart Licensing Status")
                    status = sh_ver.result.partition("Smart Licensing Status: ")[2]
                    status = "N/A" if status == "" else status
                    data_writer.writerow([host,ip,status])
                except:
                    print(host + " " + "Unauthorized/Unavailable")
                    data_writer.writerow([host, ip, 'Unauthorized/Unreachable'])



if __name__ == "__main__":
    get_status()