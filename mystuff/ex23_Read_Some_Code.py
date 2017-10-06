
#Go to bitbucket.org, github.com, or gitorious.org with your favorite web browser and search for "python."
#Pick a random project and click on it.
#Click on the Source tab and browse through the list of files and directories until you find a .py file.
#Start at the top and read through the code, taking notes on what you think it does.
#If any symbols or strange words seem to interest you, write them down to research later.
#https://first-web-scraper.readthedocs.io/en/latest/#act-3-web-scraping
import csv
import requests #module doesnt exist
from BeautifulSoup import BeautifulSoup #moduledoesnt exist
#Beautiful Soup is a Python library for pulling data out of HTML and XML files.
#At the beginning of your Python script, import the library
#Now you have to pass something to BeautifulSoup to create a soup object.

url = 'http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('tbody', attrs={'class': 'stripe'})

list_of_rows = []
for row in table.findAll('tr')[1:]:
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

outfile = open("./inmates.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Last", "First", "Middle", "Gender", "Race", "Age", "City", "State"])
writer.writerows(list_of_rows)
