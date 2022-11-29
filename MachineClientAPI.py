class MachineClient:
    def home(self):
        """ Moves machine to home position. """
        print("Moving to home.")
    def move(self, x, y, z):
        """ Uses linear movement to move spindle to given XYZ coordinates.
        Args:
            x (float): X axis absolute value [mm]
            y (float): Y axis absolute value [mm]
            z (float): Z axis absolute value [mm]
        """
        print("Moving to X={:.3f} Y={:.3f} Z={:.3f} [mm].".format(x, y, z))
    
    def move_x(self, value):
        """ Move spindle to given X coordinate. Keeps current Y and Z unchanged.
        Args:
         value (float): Axis absolute value [mm]
        """
        print("Moving X to {:.3f} [mm].".format(value))
    
    def move_y(self, value):
        """ Move spindle to given Y coordinate. Keeps current X and Z unchanged.
        Args:
            value(float): Axis absolute value [mm]
        """
        print("Moving Y to {:.3f} [mm].".format(value))
        
    def move_z(self, value):
        """ Move spindle to given Z coordinate. Keeps current X and Y unchanged.
        Args:
            value (float): Axis absolute value [mm]
        """
        print("Moving Z to {:.3f} [mm].".format(value))
        
    def set_feed_rate(self, value):
        """ Set spindle feed rate.
        Args:
            value (float): Feed rate [mm/s]
        """
        print("Using feed rate {} [mm/s].".format(value))
    
    def set_spindle_speed(self, value):
        """ Set spindle rotational speed.
        Args:
            value (int): Spindle speed [rpm]
        """
        print("Using spindle speed {} [mm/s].".format(value))
    
    def change_tool(self, tool_name):
        """ Change tool with given name.
        Args:
            tool_name (str): Tool name.
        """
        print("Changing tool '{:s}'.".format(tool_name))

    def coolant_on(self):
        """ Turns spindle coolant on. """
        print("Coolant turned on.")

    def coolant_off(self):
        """ Turns spindle coolant off. """
        print("Coolant turned off.")
        
    def g_code(self, code, value):
        """ CNC machine preparatory codes """
        if (code is not None and code == 'G'):
            if (value is not None and value == '00'):
                print("RAPID TO SAFE PLANE")
            elif (value is not None and value == '54'):
                print("USE FIXTURE OFFSET")
            elif (value is not None and value == '90'):
                print("RESET TO ABSOLUTE POSITION MODE")
            elif (value is not None and value == '01'):
                print("CUTTING STARTS")
            elif (value is not None and value == '17'):
                print("WHAT PLANE AN ARC IS MACHINED ON XY")
            elif (value is not None and value == '40'):
                print("CUTTER DIAMETER COMPENSATION")
            elif (value is not None and value == '49'):
                print("CANCELS TOOL LENGTH COMPENSATION")
            elif (value is not None and value == '80'):
                print("CANNED CYCLE CANCEL")
            elif (value is not None and value == '94'):
                print("FEED PER MINUTE")
            elif (value is not None and value == '91'):
                print("SWTICH TO INCREMENTAL POSTIONING NOT ABSOLUTE")
            elif (value is not None and value == '28'):
                print("GO BACK TO RECORDED ORGIN POINT IN MACHINE COORDINATE WORKSPACE")
            elif (value is not None and value == '21'):
                print("SWTICH CNC TO METRIC MODE")
            elif (value is not None and value == '90'):
                print("ABSOLUTE POSTIONING")
        elif (code is not None and code == 'M'):
            if (value is not None and value == '09'):
                print("TURN OFF COOLANT")
                MachineClient.coolant_off(self)
            elif (value is not None and value == '08'):
                print("TURN ON COOLANT")
                MachineClient.coolant_on(self)
            elif (value is not None and value == '05'):
                print("SPINDLE STOP")
            elif (value is not None and value == '06'):
                print("CHANGE TOOL")
            elif (value is not None and value == '03'):
                print("TURN SPINDLE CLOCKWISE")
            elif (value is not None and value == '30'):
                print("PROGRAM END")
        elif (code is not None and code == 'F'):
            if (value is not None):
                print("FEED RATE = " + value)
                MachineClient.set_feed_rate(self, value)
        elif (code is not None and code == 'T'):
            if (value is not None):
                print("LOAD TOOL NUMBER #" + value)
                MachineClient.change_tool(self, value)
        elif (code is not None and code == 'S'):
            if (value is not None):
                print("SET SPINDLE SPEED = " + value + "RPM")
                MachineClient.set_spindle_speed(self, value)