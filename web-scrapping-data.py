
from bs4 import BeautifulSoup

response = requests.get('http://dataquestio.github.io/web-scraping-pages/simple.html')
content = response.content

# Initialize the parser, and pass in the content grabbed earlier.
parser = BeautifulSoup(content, 'html.parser')

# Get the body tag from the document by picking a branch off of the root.
body = parser.body
head = parser.head

# Get the p tag from the body.
p = body.p
title_text = head.title.text

# Print the text inside the p tag.
print(p.text)

parser = BeautifulSoup(content, 'html.parser')

head = parser.find_all('head')
title = head[0].find_all('title')
title_text = title[0].text

# Get the page content and set up a new parser.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple_ids.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Pass in the ID attribute to only get the element with that specific ID.
first_paragraph = parser.find_all("p", id="first")[0]
second_paragraph = parser.find_all('p', id='second')[0]
second_paragraph_text = second_paragraph.text

# Get the website that contains classes.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple_classes.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Get the first inner paragraph.
second_inner_paragraph_text = parser.find_all("p", class_="inner-text")[1].text
first_outer_paragraph_text = parser.find_all('p', class_='outer-text')[0].text


## CSS Selectors ##
# Get the website that contains classes and IDs.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Select all of the elements that have the first-item class.
first_outer_text = parser.select(".outer-text")[0].text
second_text = parser.select('#second')[0].text
# Print the text of the first paragraph (the first element with the first-item class).

## Nested CSS Selectors ##
# Get the Superbowl box score data.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/2014_super_bowl.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

total_plays = parser.select("#total-plays")[0]
patriots_total_plays = total_plays.select("td")[2]
patriots_total_plays_count = patriots_total_plays.text

total_yards = parser.select("#total-yards")[0]
seahawks_total_yards = total_yards.select("td")[1]
seahawks_total_yards_count = seahawks_total_yards.text
