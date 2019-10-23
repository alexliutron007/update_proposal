#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 14:47:04 2019

@author: alex.liu

"""



import requests

#base_urls
create_proposal_url = "https://api.shasta.trongrid.io/wallet/proposalcreate"
approve_proposal_url = "hhttps://api.shasta.trongrid.io/wallet/proposalapprove"
get_proposal_list_url = "https://api.shasta.trongrid.io/wallet/listproposals"
sign_url = "https://api.shasta.trongrid.io/wallet/gettransactionsign"
broast_url = "https://api.shasta.trongrid.io/wallet/broadcasttransaction"


# First proposal need to create
list_proposal = [{
                    "key": 9,
                    "value": 1
                },  
                {
                    "key": 10,
                    "value": 1
                }, 
                {
                    "key": 11,
                    "value": 20
                },  
                {
                    "key": 11,
                    "value": 10
                },    
                {
                    "key": 19,
                    "value": 100000000000
                },    
                {
                    "key": 15,
                    "value": 1
                },     
                { 
                    "key": 18,
                    "value": 1
                },   
                {
                    "key": 16,
                    "value": 1
                },
                {
                    "key": 20,
                    "value": 1
                }, 
                {
                    "key": 26,
                    "value": 1
                }]
# This proposal need approve when above proposal effect
list_proposal_01 = [  
                {
                    "key": 17,
                    "value": 250000000000
                },{ 
                    "key": 18,
                    "value": 1
                }]


# Witness & privateKey
owner_address = "xxxxxxxxxxx"
owner_address_privateKey = "xxxxxx"


# Generate transaction
def tran_sign_broadcast(para_json,url):
    #create trans
    trans_respon = requests.post(url,json=para_json)
                    
    print("**************trans_respon*************")
    print(trans_respon.json())                    
    trans_respon = dict(trans_respon.json())
                    
    sign_para = {"transaction":trans_respon,
                 "privateKey":owner_address_privateKey
                }
                         
    #sign
    sign_respon = requests.post(sign_url,json = sign_para)
    print("**************sign_respon*************")
    print(sign_respon.json())
    #broast
    broast_respon = requests.post(broast_url,json=sign_respon.json())
    print("**************broast_respon*************")
    print(broast_respon.json())
            
      
# Get proposal id
def get_proposal_id_list(get_proposal_list_url):
    get_proposal_id = requests.get(get_proposal_list_url)
    proposal_id_list = [ get_proposal_id.json()["proposals"][i]["proposal_id"] for i in range(0,len(get_proposal_id.json()["proposals"]))]
    return proposal_id_list
    
# Create proposal
def create_proposal(list_proposal):    
    for i in range(0,len(list_proposal)):
        create_proposal_para = {
            "owner_address" : owner_address,
            "parameters":[
                    list_proposal[i]
                ]}
        tran_sign_broadcast(create_proposal_para,create_proposal_url)
        
        
#  Approve proposal  
def approve_proposal(proposal_id_list):
    
    for proposal_id in proposal_id_list:
        
        approve_proposal_para = {
                 "owner_address" : owner_address, 
                 "proposal_id":proposal_id, 
                 "is_add_approval":True
                 }
        print(approve_proposal_para) 
        tran_sign_broadcast(approve_proposal_para,approve_proposal_url)
        
    print("===============Done!!!====================")




def main():
    create_proposal(list_proposal)
    proposal_id_list = get_proposal_id_list(get_proposal_list_url)
    approve_proposal(proposal_id_list)


if (__name__ == "__main__"):
    main()
























