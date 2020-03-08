
def scrape():
    # Dependencies
    import pandas as pd
    from bs4 import BeautifulSoup as bs
    from splinter.browser import Browser
    import time
    #import requests
    #from selenium import webdriver


    executable_path = {'executable_path': 'chromedriver.exe'}
    Browser = Browser ("chrome")


    # NASA Mars News!
    # visit website
    news_url = "https://mars.nasa.gov/news/"
    Browser.visit(news_url)
    # create html object and parse with bs
    news_html = Browser.html
    news_soup = bs(news_html,'html.parser')
    # scrape the latest title and paragraph
    title = news_soup.find('div', class_='content_title')
    paragraph = news_soup.find('div', class_='article_teaser_body').get_text()
    title = title.text
    #paragraph = paragraph


    # JPL Mars Space Images!
    # visit website
    base_image_url = "https://www.jpl.nasa.gov"
    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    Browser.visit(image_url)
    # create html object and parse with beautifulsoup
    image_html = Browser.html
    image_soup = bs(image_html, 'html.parser')
    # scrape the feature image
    imgage_url = image_soup.find(id='full_image').get('data-fancybox-href')
    full_image = base_image_url + imgage_url


    # Mars Weather!
    # visit website
    base_weather_url = 'https://twitter.com/marswxreport?lang=en'
    weather_url='https://twitter.com/MarsWxReport/status/1233751572125028354'
    Browser.visit(weather_url)
    # create html object and parse with beautifulsoup
    time.sleep(1)
    weather_html = Browser.html
    weather_soup = bs(weather_html, 'lxml')
    # scrape the weather information
    weather = weather_soup.find('title')
    weather = weather.text


    # Mars Facts
    # visit the webset 
    facts1_url = 'https://space-facts.com/mars/'
    # extract mars facts and make it a dataframe
    facts1 = pd.read_html(facts1_url)
    facts1_df = facts1[0]
    facts1_df_html = facts1_df.to_html()
    # visit the webset 
    facts2_url = 'https://space-facts.com/mars/'
    # extract mars facts and make it a dataframe
    facts2 = pd.read_html(facts2_url)
    facts2_df = facts2[1]
    facts2_df_html = facts2_df.to_html()


    # Mars Hemispheres
    # visit the webse
    base_hemi_url = 'https://astrogeology.usgs.gov'
    hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    Browser.visit(hemi_url)
    # create html object and parse with beautifulsoup
    hemi_html = Browser.html
    hemi_soup = bs(hemi_html, 'html.parser')
    # scrape the hemisphere titles and images
    hemisphere_image_urls = []
    hemi_container = hemi_soup.find('div', id='product-section')
    hemi_images = hemi_container.find_all('div', class_='item')
    for images in hemi_images:
        title = images.find('h3').text
        link = images.find('a')['href']
        Browser.visit(base_hemi_url + link)
        soup = bs(Browser.html, 'html.parser')
        downloads = soup.find('div', class_='downloads')
        url = downloads.find('a')['href']
        hemisphere_image_urls.append({'title': title, 'img_url' : url})
    # hemi1
    hemi1 = hemisphere_image_urls[0]
    hemi1_title = hemi1["title"]
    hemi1_title
    hemi1 = hemisphere_image_urls[0]
    hemi1_img = hemi1["img_url"]
    hemi1_img  
    # hemi2
    hemi2 = hemisphere_image_urls[1]
    hemi2_title = hemi2["title"]
    hemi2_title
    hemi2 = hemisphere_image_urls[1]
    hemi2_img = hemi2["img_url"]
    hemi2_img
    # hemi3
    hemi3 = hemisphere_image_urls[2]
    hemi3_title = hemi3["title"]
    hemi3_title
    hemi3 = hemisphere_image_urls[2]
    hemi3_img = hemi3["img_url"]
    hemi3_img
    # hemi4
    hemi4 = hemisphere_image_urls[3]
    hemi4_title = hemi4["title"]
    hemi4_title
    hemi4 = hemisphere_image_urls[3]
    hemi4_img = hemi4["img_url"]
    hemi4_img

    # Dictionary
    mars_dict = {"news_title":title,
            "news_paragraph": paragraph,
            "featured_image_url":full_image,
            "weather":weather,
            "facts1":facts1_df_html,
            "facts2":facts2_df_html,
            "hemisphere_images_urls":hemisphere_image_urls,
            "hemi1_title":hemi1_title,
            "hemi1_img":hemi1_img,
            "hemi2_title":hemi2_title,
            "hemi2_img":hemi2_img,
            "hemi3_title":hemi3_title,
            "hemi3_img":hemi3_img,
            "hemi4_title":hemi4_title,
            "hemi4_img":hemi4_img,
          }
          
    return mars_dict
