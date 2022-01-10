import requests
from requests.api import delete
from requests.models import parse_url
import classes
from utils import *
from selenium import webdriver
import os
from decimal import Decimal
import re

# Dict with all selectors for ease of work ###################################################################
selectors_dict = {
    "name":'#app > main > div > div.product-actions > div.product-features-prices > div.product-features > h1',
    "price":'//*[@id="app"]/main/div/div[3]/div[1]/div[2]/meta[@itemprop="price"]',
    "color":'//*[@id="app"]/main/div/div[3]/div[2]/div[@class="colors-info"]/span',
    "sizes":'#sizeSelector > div > span'
}
############################################################################################################

#Set basic directories and url values and create missing directories######################

current_working_dir = os.getcwd()
url_to_scrape = "https://shop.mango.com/gb/women/skirts-midi/midi-satin-skirt_17042020.html?c=99"
log_dir = os.path.join(current_working_dir,"log")
if(not os.path.exists(log_dir)):
    os.mkdir(log_dir)
output_dir = os.path.join(current_working_dir,"output")
if(not os.path.exists(output_dir)):
    os.mkdir(output_dir)
config_file=os.path.join(current_working_dir,".config/config.cfg")
if(not os.path.exists(config_file)):
    log_message("No config file present at :"+config_file,"error")
    exit()

DRIVER_PATH = os.path.join(current_working_dir,"chromedriver.exe")
if(os.path.exists(config_file)):
    with open(config_file,"r") as cfg:
        cfg_path = cfg.read().strip()
        if(cfg_path!=""):
            DRIVER_PATH = cfg_path
#########################################################################################


# Init of driver and class of item######################################################
item_data = classes.RetailItemData()

scrape_success=False
if(url_to_scrape == ""):
    log_message("Incorrect input to scrape function by selector","error")
if(not os.path.exists(DRIVER_PATH)):
    log_message("No driver found in working directory","error")
    exit()
if(not requests.get(url_to_scrape).ok):
    log_message("No connection to "+url_to_scrape,"error")
    exit()
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

#########################################################################################


# Scrape data from webpage##############################################################
try:
    driver.get(url_to_scrape)
    item_data.name = driver.find_element_by_css_selector(selectors_dict["name"]).text
    price = driver.find_element_by_xpath(selectors_dict["price"]).get_attribute("content")
    if(re.match(r'[^0-9\.]',price)):
        price = re.sub(r'[^0-9\.]',"",price)
    try:
        item_data.price = float(price)
    except Exception as e:
        log_message(str(e),"error")
    item_data.color = driver.find_element_by_xpath(selectors_dict["color"]).text
    item_sizes = driver.find_elements_by_css_selector(selectors_dict["sizes"])
    for item_size in item_sizes:
        item_data.add_size(str(item_size.get_attribute("data-size")))

    log_message("Element  successfuly scraped","info")
except Exception as e:
    log_message(str(e),"error")
finally:
    driver.quit()
######################################################################################

# Serialize and write data to output#################################################
try:
    json_output = item_data.serialize_to_Json()
except Exception as e:
    log_message("The following error encountered while convertong object to JSON:"+str(e),"error")
    exit()
try:
    output_path = os.path.join(output_dir,"output.json")

    if(os.path.exists(output_path)):
        os.remove(output_path)
    with open(output_path,"x") as json_file:
        json_file.write(json_output)
except Exception as e:
    log_message("The following error encountered while writing JSON file:"+str(e),"error")
    exit()
#############################################################################################