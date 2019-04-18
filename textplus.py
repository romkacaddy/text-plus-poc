import json
import requests
import random
import uuid
import threading
"""
Textplus class
"""

class Textplus():
    
    udid = ""
    username = ""
    account_location = ""
    userId = ""
    ticket = ""
    grant_ticket = ""
    jid = ""
    
    def __init__(self):
        self.udid = str('{:16}'.format(random.randrange(1, 10**18)))
        self.username, account_location = self.make_user(self.udid)
        self.userId = account_location.split('/')[len(account_location.split('/'))-1]
        self.account_location = account_location
        self.ticket = self.get_ticket(self.username, self.udid)
        self.grant_ticket = self.grant_token(self.ticket, self.udid)
        self.jid = self.get_persona_info(self.udid, self.grant_ticket)["personas"][0]["jid"]
        self.persona_search(self.jid, self.udid, self.grant_ticket)
        self.post_device(self.udid, self.account_location, self.grant_ticket)
        self.get_number(self.udid, self.grant_ticket)
    
    def send_message(self, number, message): 


        headers = {
            
            "udid" : self.udid,
            "authorization" : "CASST " + self.grant_ticket,
            "content-type" : "application/json",
            "user-agent" : "okhttp/3.10.0"
            
        }
        
        
        data = {
        	"message": message,
        	"invites": [{
        		"phone": "+" + number
        	}]
        }
        #print(json.dumps(data));
        
        res = requests.post("https://ums.prd.gii.me/rewards/custom_invites/"+self.userId, proxies = {"http" : "socks4://localhost:9050", "https" : "socks4://localhost:9050"}, data=json.dumps(data), headers=headers)
        
        #print(res.content)
    
    def post_device(self, udid, account_location, grant_ticket):
        
        
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
    
    def persona_search(self, jid, udid, grant_ticket):
        
        headers = {
            
            "udid" : udid,
            "authorization" : "CASST " + grant_ticket,
            "content-type" : "application/json",
            "user-agent" : "okhttp/3.10.0"
            
        }
        
        
        res = requests.get("https://ums.prd.gii.me/personas/search/findByJidIn?jid="+jid+"&network=nextplus&size=1&projection=inline",proxies = {"http" : "socks4://localhost:9050", "https" : "socks4://localhost:9050"}, headers=headers)
    
    def get_persona_info(self, udid, grant_ticket):
        
        
        
        headers = {
            
            "udid" : udid,
            "authorization" : "CASST " + grant_ticket,
            "content-type" : "application/json",
            "user-agent" : "okhttp/3.10.0"
            
        }
        
        
        res = requests.get("https://ums.prd.gii.me/me?projection=inline", proxies = {"http" : "socks4://localhost:9050", "https" : "socks4://localhost:9050"}, headers=headers)
        
        return json.loads(res.content)
    
    
    def get_number(self, udid, grant_ticket):
        url_location = self.get_persona_info(udid, grant_ticket)["personas"][0]["id"]
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
    
    
    def grant_token(self, ticket, udid):
        
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
    
    
    
    def get_ticket(self, username, udid):
        
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
    
    def make_user(self, udid):
        
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
        
        self.res = requests.post("https://ums.prd.gii.me/registration/mobile", proxies = {"http" : "socks4://localhost:9050", "https" : "socks4://localhost:9050"}, data=json.dumps(data), headers=headers)
        return self.res.headers["username"], self.res.headers["location"]