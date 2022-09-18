import time
import json
import re

def search_drugs():
    found =False
    print("****************************************************************")
    print("***************************Search Drugs*********************************")
    print("****************************************************************")
    drug_name=input("Enter the drug name to search : ")
    print(f'Searching for {drug_name} in the inventory...' )    
    #Open the inventory file
    with open("sample_all_medicins_info.json", 'r') as jf:
        #Parse the json
        medicine_data = json.load(jf)        
        for i in medicine_data:            
            match_drug = re.match('.*'+drug_name.lower()+'.*',i['name'].lower())
            if (match_drug):                
                print(i['name'])
                
                found = True
        if found is False:
            print("Medicine Not Found")

search_drugs()