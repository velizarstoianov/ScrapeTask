import json
import re

class RetailItemData:
    def __init__(self, name="", price=0.0, color = "", size=list() ) -> None:
        self._name = name
        self._price = price
        self._color = color
        self._size = size

# Getter and setter for name property#######################   
    def _get_name(self):
        return self._name
    def _set_name(self,val):
        if not isinstance(val, str):
            raise TypeError("name must be set to a string")
        self._name = val
    name=property(_get_name,_set_name)
############################################################

# Getter and setter for name property######################
    def _get_price(self):
        return self._price
    def _set_price(self,val):
        if not isinstance(val, float):
            raise TypeError("price must be set to float")
        self._price = val
    price=property(_get_price,_set_price)
##########################################################

# Getter and setter for color property#####################
    def _get_color(self):
        return self._color
    def _set_color(self,val):
        if not isinstance(val, str):
            raise TypeError("color must be set to string")
        self._color = val
    color=property(_get_color,_set_color)
##########################################################

# Getter and setter for size property####################
    def _get_size(self):
        return self._size
    def _set_size(self,val):
        if not isinstance(val, list()):
            raise TypeError("sizes must be list")
        self._size = val
    size=property(_get_size,_set_size)
#########################################################

# Helper functions for add of size to list and for json serialization
    def add_size(self,size_to_add):
        if not isinstance(size_to_add,str):
            size_to_add=str(size_to_add)
        self.size.append(size_to_add)

    def serialize_to_Json(self):
        json_str = json.dumps(self, default=lambda o: o.__dict__, sort_keys=False, indent=4)
        return re.sub(r'"_','"',json_str)