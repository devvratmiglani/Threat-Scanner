import os
from settings import API_KEY
from includes.single_ip import display_ip_info
from includes.single_file import file_scann


def main():
    
    while True:
        if API_KEY == 'Virus Total API KEY':
            print("### Please Add your Virus Total API Key to settings.py ###")
        print("\n----------------")
        print("1. ---- IP Address: All info of an IP ---- ")
        print("2. ---- Path to a file: Scanning a file ---- ")
        print("3. ---- Exit: Exit out the program ----")
        print("----------------\n")

        choice = input("Enter your choice: ")
        if choice == "1":
            ip = input("Enter IP address: ")
            display_ip_info(ip)
        elif choice == "2":
            path = input("Enter file path: ")
            file_scann(path)
        elif choice == "3":
            exit(0)
        else:
            print("Invalid choice")
        
if __name__ == "__main__":
    main()