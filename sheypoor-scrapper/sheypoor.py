from scrapper import Scrapper
from bs4 import BeautifulSoup

class Sheypoor(Scrapper):
   """
   Sheypoor web scrapper class
   """
   posts = []

   # Fetch all base url posts
   def get_posts(self):
      posts = self.__get_posts()
      soup = BeautifulSoup(posts['body'], 'html.parser')
      articles = soup.find_all("article", class_='serp-item')

      # Parse each article
      for article in articles:
         self.posts.append(self.__parse(article))

   # Parse each post object
   def __parse(self, post):
      # Title
      title = post.find('h2').text

      # Time
      time      = "N/A"
      temp_time = post.select('time[datetime]')
      if(temp_time != []):
         time = temp_time[0].attrs['datetime']

      # Price
      price = post.find('strong', class_='item-price')
      if(price != None):
         price = price.text
      else:
         price = "N/A"

      # Number
      number = self.__get_number(post)

      return {
         'number': number,
         'title': title,
         'price': price,
         'time': time
      }

   # Send a HTTP request to base url
   def __get_posts(self):
      response = self.requests.get(self.base_url, allow_redirects=False)
      return { 'status': response.status_code, 'body': response.text }

   def __get_number(self, parsed_post):
      return "N/A" # Not going to write this one
