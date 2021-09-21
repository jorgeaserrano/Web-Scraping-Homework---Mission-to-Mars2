
# Dependencies and Setup
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import json
import time
from IPython.display import Image, display

# MAC - Set browser
def init_browser():
	
	executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
	
mars_info = {}
	
# NASA Mars News
def scrape_info():
	
	browser = init_browser()
	
	# Visit NASA Mars News
	url = "https://redplanetscience.com/"
	browser.visit(url)
		
	# HTML Object
	html = browser.html
    soup = BeautifulSoup(html, "lxml")
		
	# Scrape the latest News Title and Paragraph Text
	news_title = first_row.find("div", {"class", "content_title"}).text
    news_paragraph = first_row.find("div", {"class": "article_teaser_body"}).text
	
	mars_info["news_title"] = news_title
	mars_info["news_paragraph"] = news_paragraph 


# JPL Mars Space Images - Featured Image
	
	# Visit JPL Mars Space Images
    url = "https://redplanetscience.com/"
    browser.visit(url)
	
    # HTML Object
    html = browser.html
    soup = BeautifulSoup(html, "lxml")

	# Find image url to the full size
	image = soup.find("img", {"class": "headerimage"}) featured_image_url = url + image["src"]
	
    # Connect website url with scrapped route
	featured_image_url =url + image["src"]
    featured_image_url = "https://spaceimages-mars.com/image/featured/mars3.jpg

	# Display Image
    display(Image(featured_image_url))
	
	
# Mars Facts

	# Visit Mars Facts
	url = "https://galaxyfacts-mars.com/"
    browser.visit(url)

	# HTML Object
    html = browser.html
    dfs = pd.read_html(html)

    # Create empty list
	len(hemis)
	
	# Find the mars facts DataFrame in the list
	DataFrame0 = dfs[0]

	# Find the mars facts DataFrame in the list
	DataFram1 = dfs[1]

	# Set index to Facts
	facts = dfs[1]
    facts = facts.set_index(0).T
    facts.columns = [x.strip(":") for x in facts.columns]

    html code
	facts_json = json.loads(facts.to_json(orient="records"))
	
	facts_json["facts_json"] = records


# Mars Hemispheres
	
	# Visit Mars Hemispheres
	url = "https://marshemispheres.com/"
    browser.visit(url)
	
	# HTML Object
    html = browser.html
    soup = BeautifulSoup(html, "lxml")
	
	# Find containers whcih has mars hemispheres information
	hemis = soup.find_all("div", {"class":"item"})

	# Create empty list
	len(hemis)

	# Sign main url for loop
	hemispheres_url = "https://astrogeology.usgs.gov"

	# Loop through the list of all hemispheres information
	for i in hemispheres:
		title = i.find("h3").text
		hemispheres_img = i.find("a", class_="itemLink product-item")["href"]
		
		# Visit the link that contains the full image website 
		browser.visit(hemi_url + hemis_img)
		
		# HTML Object
		html = browser.html
        soup = BeautifulSoup(html, "lxml")
		
		# Create full image url
	    link = url + soup.find("img", {"class", "wide-image"})["src"]
        title = soup.find("h2", {"class", "title"}).text
		
		data = {"img_url" : link, "title" : title})
         
        hemi_info.append(data)

# Display titles and images ulr
#hemispheres_info

	# Close the browser after scraping
	browser.quit()
