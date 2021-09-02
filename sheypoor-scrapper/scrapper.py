from errors import BaseURLNotFound
import requests

class Scrapper:
   """
   Base scrapper class
   """

   def __init__(self, base_url=None):
      if(base_url == None):
         raise BaseURLNotFound()

      # Configure requests module
      self.requests = requests.Session()
      self.requests.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
      self.requests.headers['Accept-Encoding'] =  'utf-8'

      self.base_url = base_url
