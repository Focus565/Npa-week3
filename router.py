"""Router"""
class Router:
    
    """create router"""
    def __init__(self, brand, model, hostname):
        self.brand = brand
        self.model = model
        self.hostname = hostname
        self.interfaces = {}

    """add interface"""
    def add_inf(self,interface_name):
        if interface_name not in self.interfaces:
            self.interfaces[interface_name] = "not connect"
            return True
        return False

    "remove interface"
    def remove_inf(self,interface_name):
        if interface_name in self.interfaces:
            self.interfaces.pop(interface_name)
            return True
        return False

    "show interface"
    def show_infs(self):
        output = "Show interface of " + self.hostname + "\n" + self.hostname + ' has ' + str(len(self.interfaces)) + ' interfaces\n'
        for inf in self.interfaces:
            output += inf+'\n'
        return output

    "connect router"
    def connect(self, interface_name, target, target_interface_name):
        if interface_name in self.interfaces:
            if target_interface_name in target.interfaces:
                if self.interfaces[interface_name] == "not connect":
                    if target.interfaces[target_interface_name] == "not connect":
                        self.interfaces[interface_name] = target.hostname+' on interface '+target_interface_name
                        target.interfaces[target_interface_name] = self.hostname+' on interface '+interface_name
                        return True
        return False

    def show_cdp(self):
        output = ""
        for interface in self.interfaces:
            text = self.interfaces[interface]
            if text != "not connect":
                output += self.hostname+" interface "+interface+" connect to "+text+'\n'
        return output