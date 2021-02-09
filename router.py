"""Router"""
class Router:
    
    """create router"""
    def __init__(self, brand, model, hostname):
        self.brand = brand
        self.model = model
        self.hostname = hostname
        self.interfaces = []

    def add_inf(self,interface_name):
        if interface_name not in self.interfaces:
            self.interfaces.append(interface_name)

    def remove_inf(self,interface_name):
        if interface_name in self.interfaces:
            self.interfaces.remove(interface_name)