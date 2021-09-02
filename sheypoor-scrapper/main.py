from sheypoor import Sheypoor
from rich.console import Console
from rich.table import Table

def main():
   # Configuration
   base_url = 'https://www.sheypoor.com/%D8%A7%DB%8C%D8%B1%D8%A7%D9%86'
   result_number   = 7 # Table List Result Number

   # Scrapper instance
   sheypoor_scrapper = Sheypoor(base_url=base_url)
   sheypoor_scrapper.get_posts()

   # Create Table
   table = Table(title=':moneybag: Sheypoor Ads :moneybag:', show_header=True, header_style="bold green")

   # Add Columns to Table
   table.add_column(':date: Time', justify="left", style='red', no_wrap=False)
   table.add_column(':iphone: Phone ', justify="center", style='red', no_wrap=True)
   table.add_column('Price :dollar:', justify="center", style='red', no_wrap=True)
   table.add_column('Title :pencil:', justify="right", style='cyan', no_wrap=True)

   # Append to Table
   for post in sheypoor_scrapper.posts[:result_number]:
      table.add_row(
         post['time'][:10],
         post['number'],
         post['price'],
         post['title']
      )

   # Display
   console = Console()
   console.print(table)

if __name__ == '__main__':
   main()
