import MachineClientAPI

class GCodeSegment():
    def __init__(self, code, number, x, y, z, raw):
        self.code = code
        self.number = number 
        self.raw = raw
        self.x = x
        self.y = y
        self.z = z

        self.has_cords = (self.x is not None or self.y is not None or self.z is not None)

        if self.has_cords:
            if self.x == None:
                self.x = 0
            if self.y == None:
                self.y = 0
            if self.z == None:
                self.z = 0
            
        if self.has_cords:
            # Gcode line with XYZ coordinates for movement
            print (f'\t{self.code} {self.number} ({self.x}, {self.y}, {self.z})')
            self.call_machine_client_api__with_coordinates()
        else:
            # Gcode line with G M F T S codes and values
            print (f'\t{self.code} {self.number}')
            self.call_machine_client_api__without_coordinates()
            

    def call_machine_client_api__with_coordinates(self):
        MachineClientAPI.MachineClient.g_code(self, self.code, self.number)
        
        if (self.x == 0 and self.y == 0):
            # movement in z direction
            MachineClientAPI.MachineClient.move_z(self, float(self.z))
        elif (self.y == 0 and self.z == 0):
            # movement in x direction
            MachineClientAPI.MachineClient.move_x(self, float(self.x))
        elif (self.x == 0 and self.z == 0):
            # movement in y direction
            MachineClientAPI.MachineClient.move_y(self, float(self.y))
        else: 
            # movement in xyz direction
            MachineClientAPI.MachineClient.move(self, float(self.x), float(self.y), float(self.z))

    def call_machine_client_api__without_coordinates(self):
        MachineClientAPI.MachineClient.g_code(self, self.code, self.number)
            
    
    def command(self):
        return self.code + self.number
    
    def get_cords(self):
        return (self.x, self.y, self.z)
    
    def has_cords(self):
        return self.has_cords
    
    def get_cord(self, cord):
        cord = cord.upper()

        if cord == 'X':
            return self.x
        elif cord == 'Y':
            return self.y
        elif cord == 'Z':
            return self.z