# text-plus-poc
Programmatically creates accounts and sends texts via textplus.
Interested in how this hack was created? Read about it [here](https://ligma.vip/posts/textplus/)


# USE TOR!
I have the python requests setup to use TOR so your external IP doesnt get blocked.


for linux users 
```
sudo apt install tor
```

# Make tor change your external IP every 10 seconds
Change your torrc file to change the external IP every 10 seconds

https://2019.www.torproject.org/docs/tor-manual-dev.html.en#MaxCircuitDirtiness


# Requirements

Install requirements
```
pip install -r requirements.txt
```

# prefs.json
username_seed is the seed for usernames, AKA usernames will look like these.....

password is the same for all accounts

proxy contains all proxy information for requests

method can be either "phone" or "email". Phone numbers must have the following match: \+[0-9][0-9]{10}

