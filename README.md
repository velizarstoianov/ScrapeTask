# ScrapeTask
Here I provide my solution of the problem I was presented with as a part of a tech recruitment process

# Task Description
Scrape relevant retail item data from a given URL and output it to a JSON file.

# Documentation
The solution uses [selenium](https://www.selenium.dev/) and requires a chromedriver.exe relevent to the current version installed on the client machine. You can find the chromedriver.exe version [here](https://chromedriver.chromium.org/downloads).

## classes.py
This file contains the class used to encapsulate and contain the scraped information.
The class  RetailItemData contains the following non-public fields:
```
def __init__(self, name="", price=0.0, color = "", size=list() ) -> None:
        self._name = name #string -> name
        self._price = price #float -> price
        self._color = color #string -> color
        self._size = size #List(string) -> size
```
Default values are assigned when an instance of an object is created without arguments or with incomplete list of arguments.
Public field names corespond as shown in the snippet above

Every field has a dedicated getter and setter as follows:

```
#Getter and setter for name property#######################   
    def _get_name(self):
        return self._name
    def _set_name(self,val):
        if not isinstance(val, str):
            raise TypeError("name must be set to a string")
        self._name = val
    name=property(_get_name,_set_name)
############################################################

#Getter and setter for name property######################
    def _get_price(self):
        return self._price
    def _set_price(self,val):
        if not isinstance(val, float):
            raise TypeError("price must be set to float")
        self._price = val
    price=property(_get_price,_set_price)
##########################################################

#Getter and setter for color property#####################
    def _get_color(self):
        return self._color
    def _set_color(self,val):
        if not isinstance(val, str):
            raise TypeError("color must be set to string")
        self._color = val
    color=property(_get_color,_set_color)
##########################################################

#Getter and setter for size property####################
    def _get_size(self):
        return self._size
    def _set_size(self,val):
        if not isinstance(val, list()):
            raise TypeError("sizes must be list")
        self._size = val
    size=property(_get_size,_set_size)
#########################################################
```
All setters raise a TypeError exception when an invalid value is passed to the field.
