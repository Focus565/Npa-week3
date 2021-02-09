"""Router"""
class Router:
    
    """create router"""
    def __init__(self, brand, model, hostname):
        self.brand = brand
        self.model = model
        self.hostname = hostname
        self.interfaces = {}

    def add_inf(self,interface_name):
        if interface_name not in self.interfaces:
            self.interfaces[interface_name]= "unassigned ip"