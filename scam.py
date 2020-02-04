import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

#change the url to the request usel of the scam page
url = 'https://www.bcip.ac.in/cgi-sys/js/simple-expand.min.js'

names = json.loads(open('names.json').read())

for name in names:
    name_extra = ''.join(random.choice(string.digits))

    username = name.lower() + name_extra + "@gmail.com"
    password = "".join(random.choice(chars) for i in range(10))

    requests.post(url, allow_redirects=False, data={

       #change thes 2 to the form data 
         "l3onwen": username,
         "lbass": password

    })

    print ("sending username %s and password %s" % (username, password))
    
    # you can find the request url and the form data in the network sction in inspact page 
