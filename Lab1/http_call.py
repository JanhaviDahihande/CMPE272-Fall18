import requests
import time

for x in range(0, 3):
    request = requests.get("https://webhook.site/c49f0bdc-3c0b-4718-81fa-053b5fddc5aa")
    print ('Re %d : %s' % (x,request.headers['Date']) )
    time.sleep(5)