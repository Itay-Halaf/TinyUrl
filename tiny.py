import os
import requests
import os

def shorten_url(e):
    site_url = ""
    web_page = requests.get(e)
    return web_page

print("Url shortener")
url = str(input("> "))