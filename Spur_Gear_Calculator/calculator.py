import math

class SpurGear():
    ''' Calculate a Cylindrical External Spur Gear using the number of teeth and
    outside diameter for 3d modeling purpose '''

    def __init__(self, teeth, outside_diameter):
        self.teeth = teeth
        self.outside_diameter = outside_diameter


    def module(self):
        self.module = self.outside_diameter / (self.teeth + 2)
        print(" - Module : \n", self.module, "\n ")


    def pitch_circle_diameter(self):
        self.pitch_circle_diameter = self.module * self.teeth
        print(" - Pitch Circle Diameter: \n ", self.pitch_circle_diameter, "\n ")

    def circular_pitch(self):
        self.circular_pitch = self.pitch_circle_diameter * (math.pi / self.teeth)
        print(" - Circular Pitch: \n ", self.circular_pitch, "\n ")

    def diametral_pitch(self):
        self.diametral_pitch = 1 / self.module
        print(" - Diametral Pitch : \n ", self.diametral_pitch, "\n ")

    def addendum(self):
        self.addendum = self.module
        print(" - Addendum: \n ", self.addendum)

    def addendum_circle_diameter(self):
        self.addendum_circle_diameter = self.pitch_circle_diameter + (2*self.addendum)
        print(" - Addendum Circle Diameter: \n ", self.addendum_circle_diameter, "\n ")

    def clearance(self):
        self.clearance = self.circular_pitch / 20
        print(" - Clearance : \n ", self.clearance, "\n ")


    def deddendum(self):
        self.deddendum = self.clearance + self.addendum
        print(" - Deddendum : \n ", self.deddendum, "\n ")

    def deddendum_circle_diameter(self):
        self.deddendum_circle_diameter = self.pitch_circle_diameter - (2 * self.deddendum)
        print(" - Deddendum Circle Diameter: \n ", self.deddendum_circle_diameter, "\n ")
    
    def pressure_angle(self):
        self.pressure_angle = 20
        print("- Pressure Angle (most common): \n ", self.pressure_angle, "\n ")

    def circular_pitch_angle(self):
        self.circular_pitch_angle = self.circular_pitch * 360 / (self.pitch_circle_diameter * math.pi * 4)
        print(" - Circular Pitch Angle : \n ", self.circular_pitch_angle, "\n ")

    def face_width(self):
        self.face_width = self.module * 5
        print(" - Face Width : \n  ", self.face_width, "\n ")
    
    def backlash(self):
        self.average_backlash = 0.04 / self.diametral_pitch
        self.minimum_backlash = 0.03 / self.diametral_pitch
        self.maximum_backlash = 0.05 / self.diametral_pitch
        print(" - Backlash : \n ")
        print("Average Backlash : ", self.average_backlash)
        print("Minimum Backlash : ", self.minimum_backlash)
        print("Maximum Backlash : ", self.maximum_backlash)
