## SPUR GEAR CALCULATOR


# About This Project :

This program will generate some necessary parameters for the creation of a cylindrical spur gear using
3d CAD modeling.

- What is a Spur Gear ?

    * The most common and simple designed toothed wheel with parallel teeth wich mesh with another toothed part to transmit torque and speed.

-  A Spur Gear :

<img src="images/spur_gear.png" width=30% height=30%>


- Gear Terminology :

<img src="images/gear_terminology.png" width=30% height=30%>

<img src="images/gear_terminology_2.png" width=30% height=30%>

<img src="images/gear_terminology_3.png" width=30% height=30%>


* Module

The unit of size defined by ISO that indicates how big or small a gear is. Gears will only mesh with each other if they have teeth of the same module.

* Pitch Circle 

A Theoretical circle on wich all calculations are based. The diameter of pitch circle is called the effective diameter or pitch diameter.

* Circular Pitch

The distance from one point of a gear tooth to another tooth point measured along the pitch circle.

* Diametral Pitch

Relates to the ratio of gear teeth and pitch diameter. Pitch diameter is the measured diameter of a pitch circle. Essentially, the diametrical pitch of a gear is the number of gear teeth for each inch of pitch diameter.

* Addendum

Radial Height of the tooth from pitch Circle to top of the tooth.

* Addendum Circle

The circle wich limits the top of the gear tooth.

* Clearance

The radial distance from the top of the tooth to the bottom of the tooth.

* Deddendum

The radial depth of tooth to the pitch circle to the root of the tooth.

* Deddendum Circle

The circle wich limits the bottom of the gear tooth.

* Pressure Angle

The angle between the tooth face and the gear wheel tangent.

* Circular Pitch Angle

The angle at a pitch point between the line of pressure which is normal to the tooth surface, and the plane tangent to the pitch surface.

* Face Width

The axial length of a gear tooth is called the face width

* Backlash

The amount by which a tooth space exceeds the thickness of a gear tooth engaged in mesh.



# Basic Instruction : 

    1. Run main.py with python then type number of theeth and outside diameter (same as addendum circle diameter) .


    Example :

    Number of teeth: 
    25
    Outside Diameter (same as Addendum Circle): 
    54

    Will generate :

    - Module : 
    2.0 
 
    - Pitch Circle Diameter: 
    50.0 
 
    - Circular Pitch: 
    6.283185307179587 
 
    - Diametral Pitch : 
    0.5 
 
    - Addendum: 
    2.0
    - Addendum Circle Diameter: 
    54.0 
 
    - Clearance : 
    0.31415926535897937 
 
    - Deddendum : 
    2.3141592653589793 
 
    - Deddendum Circle Diameter: 
    45.37168146928204 
 
    - Pressure Angle (most common): 
    20 
 
    - Circular Pitch Angle : 
    3.6000000000000005 
 
    - Face Width : 
    10.0 
 
    - Backlash : 
 
    Average Backlash :  0.08
    Minimum Backlash :  0.06
    Maximum Backlash :  0.1

    