from .models import political_offices
from api.strings import *
from api.ver1.utils import generate_id, error, success, exists
from .strings import *
from api.ver1.validators import validate_dict


class Office:
    def __init__(self, id=None, type=None, name=None):
        self.id = id
        self.type = type
        self.name = name

    #create a political office.
    def add_office(self):
        """"Add a political office passed on instantiation, generates auto id"""
        office = { 
                    id_key: generate_id(political_offices), 
                    name_key:self.name, 
                    type_key: self.type
                }
        status = validate_dict(office)
        if status == ok_str:
            political_offices.append(office)
            return success(code=status_201, data=[office]) # return list of offices to display added office
        return status
        
    #gets a specific office.
    def get_office(self):
        status = exists(self.id, political_offices)
        if type(status) == dict:
            return success(status_201, [status])
        return error(office_id_str + not_found, status_404)

     #gets all offices.
    def get_offices(self):
        return success(status_201, political_offices)