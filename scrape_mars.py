from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd

# path to chrome browser doesnt working here. not sure whats up. 
def init_browser():
    executable_path = {"executable_path": "C:\Users\bvera\Desktop\chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

# scraping for the title and paragraph
def scrape():
    browser = init_browser()
    
    url = "https://mars.nasa.gov/news/8657/nasas-perseverance-rover-mission-getting-in-shape-for-launch/"
    browser.visit(url)

    time.sleep(1)

    html = browser.html
    soup = BeautifulSoup(html,"html.parser")

    title = soup.find("h1", class_='article_title').text
    
    paragraph = soup.find("div", class_='wysiwyg_content').text
    
# scraping for the featured mars image
    featured_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(featured_url)

    time.sleep(1)

    html = browser.html
    soup = BeautifulSoup(html,"html.parser")

    latest_image = soup.find('article')['style'].replace('background-image: url(','')

    homepage = 'https://www.jpl.nasa.gov/'

    featured_image_url = homepage + latest_image

#mars scrape, couldnt get the twitter formula here
    mars_weather_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(mars_weather_url)

    time.sleep(1)

    html = browser.html
    soup = BeautifulSoup(html,"html.parser")

    tweets = soup.find_all('div', class_='css-1dbjc4n r-150rngu r-16y2uox r-1wbh5a2')

#scraping data table
    table_url= "https://space-facts.com/mars/"

    btables =pd.read_html(table_url)
    
    df = tables[1]
    df.columns = ['Mars - Earth Comparison','Mars','Earth']
   
    mars_facts_table = df.to_html(classes='data table', index=False, header=False, border=0)

#scraping hemisphere data
# i gave up here :-(

    browser.quit()
