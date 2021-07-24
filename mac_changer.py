import subprocess
from optparse import OptionParser
from termcolor import colored
import re
def get_arguments():
    parser = OptionParser()
    parser.add_option("-i", "--interface", dest = "interface", help = "Interface to change its MAC adress")
    parser.add_option("-m", "--mac", dest = "mac_adress", help = "New MAC adress") 
    (options,arguments) = parser.parse_args()
    if not options.interface and not options.mac_adress:
        parser.error(colored("[-] Please specify an interface and mac_adress, use --help for more info",'red'))
    if not options.interface:
        parser.error(colored("[-] Please specify an interface, use --help for more info",'red'))
    if not options.mac_adress: 
        parser.error(colored("[-] Please specify an mac_adress, use --help for more info",'red'))   
    return options
    
def change_mac(interface,mac_adress):
    ifconfig_result = subprocess.check_output(["ifconfig",options.interface])
    if re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_result.decode()):
        ether = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_result.decode())
        print(colored(f"[+] Changing MAC adress for {interface} to {mac_adress}",'green'))
        subprocess.call(["sudo", "ifconfig", interface, "down"])
        subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", mac_adress])
        subprocess.call(["sudo", "ifconfig", interface, "up"])
        ifconfig_result_2  = subprocess.check_output(["ifconfig",options.interface])
        ether_2 = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_result_2.decode())
        if ether != ether_2:
            print(colored("[+] Succsessful",'green'))
        elif ether == ether_2:
            print(colored("[-] The MAC address remains the same",'red'))
    else:
        print(colored("[-]The selected interface does not have a MAC address",'red'))
options = get_arguments()
change_mac(options.interface,options.mac_adress)