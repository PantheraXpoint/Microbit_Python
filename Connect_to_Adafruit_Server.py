#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyttsx3

engine = pyttsx3 . init ()
engine . say ("I am AI python ")
engine . runAndWait ()


# In[2]:


import sys
from Adafruit_IO import MQTTClient

AIO_FEED_ID = "IOT_LAB"
AIO_USERNAME = "taunhatquang"
AIO_KEY = "aio_guRX32LXb1CRtPb5gHElwyDyvgo1"


# In[ ]:


def connected(client):
    print("Ket noi thanh cong ...")
    client.subscribe(AIO_FEED_ID)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload)

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

while True:
    pass


# In[ ]:




