# ScrapeTask
Here I provide my solution of the problem I was presented with as a part of a tech recruitment process

# Task Description
Scrape relevant retail item data from a given URL and output it to a JSON file.

# Documentation
The solution uses [selenium](https://www.selenium.dev/) and requires a chromedriver.exe relevent to the current version installed on the client machine. You can find the chromedriver.exe version [here](https://chromedriver.chromium.org/downloads).

## classes.py
This file contains the class used to encapsulate and contain the scraped information.
The class  RetailItemData contains the following non-public fields:
```python
def __init__(self, name="", price=0.0, color = "", size=list() ) -> None:
        self._name = name #string -> name
        self._price = price #float -> price
        self._color = color #string -> color
        self._size = size #List(string) -> size
```
Default values are assigned when an instance of an object is created without arguments or with incomplete list of arguments.
Public field names corespond as shown in the snippet above
### Getters and setters
Every field has a dedicated getter and setter as follows:

```python
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
### Methods
The class contains 2 methods used as utilities for editing or encoding the class

The method add_size is used to add a string element to the field size of type list. It accepts a value and parses it into string type if it is not.
```python
def add_size(self,size_to_add):
        if not isinstance(size_to_add,str):
            size_to_add=str(size_to_add)
        self.size.append(size_to_add)
```

The method serialize_to_Json is used to serialize the current object to JSON format according to the task. It uses the object attribute __dict__  to retrive all fields and encodes the dictionary in JSON format and returns a string. 

```python
 def serialize_to_Json(self):
        json_str = json.dumps(self, default=lambda o: o.__dict__, sort_keys=False, indent=4)
        return re.sub(r'"_','"',json_str)
```

## utils.py
This file contains utility functions used by other modules of the project.

### log_message
This function is used by other modules to log activity. The function accepts 2 arguments, message and level_of_log.
The message argumetn recives the message to be loged in the file.
The level_of_log argument denotes the severity of the message to be logged. The function accepts 3 log levels:
-Error
-Warning
-Info
Filename of the log file follows the structure of dd-mm-yyyy. Each line in the log follows the following formating:
yyyy-MM-dd hh:mm:ss,fff
File is created if it does not exist.
```python
def log_message(message, level_of_log):
    filename = date.today().strftime("%d-%m-%Y")
    filename +=".log"
    filepath = os.path.join(os.getcwd(),"log/"+filename)
    if(not os.path.exists(filepath)):
        open(filepath,"x")
    logging.basicConfig(filename=filepath, level=logging.DEBUG, 
                        format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logger=logging.getLogger(__name__)
    if(level_of_log=="error"):
        logger.error(message)
        return
    if(level_of_log=="warning"):
        logger.warning(message)
        return
    if(level_of_log=="info"):
        logger.info(message)
        return
```

## main.py
Responsible for putting togather all elements of the solution and running the process.
Dictionary selectors_dict contains all the selector needed to locate and scrape all the elements.
All required directories are checked and created if they don't exist.
-.config directory contains config.cfg file responsible for configuring the path to the chrome driver
-output directory contains the output.json file generated after completion of the program
-log directory contains log files with all events that occured during program execution.

A chrome driver object is initiated and stored in driver variable.
Connection to the URL endpoint is verified via GET request.
Chrome driver loads the page and scrapes relevant information about price, name, color and available sizes.
Chrome is closed and a JSON file with the result is created.
The program exits.
