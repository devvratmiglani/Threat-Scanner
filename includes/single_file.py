import requests
import hashlib
import datetime
from prettytable import PrettyTable
from settings import API_KEY, API_URL_IP

VT_URL = "https://www.virustotal.com/api/v3/"
headers = {
         "Accept": "application/json",
         "x-apikey": API_KEY 
         }

class Colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    GREY  = '\33[90m'
    ENDC = '\033[0m'

def file_scann(file):
    file = file.strip("'\"")
    chunk = 65536 
    file_hash = hashlib.md5() 
    with open(file, 'rb') as f: 
        read_as_bytes = f.read(chunk) 
        while len(read_as_bytes) > 0: 
            file_hash.update(read_as_bytes) 
            read_as_bytes = f.read(chunk) 
    md5hash= file_hash.hexdigest()
    
    url_info = VT_URL + "files/" + md5hash 
    res = requests.get(url_info ,headers = headers)
    if res.status_code == 200:
        result = res.json()
        last_update = datetime.datetime.fromtimestamp(result.get("data").get("attributes").get("last_modification_date"))
        if result.get("data").get("attributes"):
                count = result.get("data").get("attributes").get("last_analysis_stats")
                results = result.get("data").get("attributes").get("last_analysis_results")
                print ()
                s = PrettyTable()
                s.field_names = [                    
                    Colors.RED + "Malicious" + Colors.ENDC, 
                    Colors.YELLOW + "Suspicious" + Colors.ENDC, 
                    Colors.GREEN + "Clean" + Colors.ENDC, 
                    "Last Updated"
                ]
                s.add_row([
                    str(count.get("malicious")),
                    str(count.get("suspicious")),
                    str(count.get("undetected")),
                    str(last_update)
                ])

                print(s)
                print()

                u = PrettyTable()
                u.field_names = ["Engine Name", "Result"]
                for k in results:
                    if results[k].get("category") == "malicious":
                        u.add_row([results[k].get( "engine_name"), Colors.RED + results[k].get("result") + Colors.ENDC])

                print(u)
                print()
                
    elif res.status_code == 400:
            print (Colors.RED + " connection error or wrong hash " + Colors.ENDC)
            print (Colors.RED + "status code: " + str(res.status_code) + Colors.ENDC)
    else:
     
           print (Colors.BLUE + " Unknown Hash " + Colors.ENDC)