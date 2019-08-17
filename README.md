# Parkable

# Description
Code for Parking Sensor Web Application designed during Digital Sciences Capstone Course at Kent State University. 

**Disclaimer:** This project is intended to be hosted in an AWS S3 Bucket for Static Web Hosting. Functions used rely on rooted device code, AWS IoT Rules, AWS IoT Shadow States, and S3 bucket permissions for creating files. The corresponding AWS Infrastructure is no longer active.

**How to:** Simply clone the entire git directory and launch index.html locally. Page will display as a static mock of the real functionality as if two parking spots are unavailable, and two are available. The Web Page was designed to appear clean and easy to read from a mobile device.

## Structure and Function
### Application Data Flow
* The Application works by running script.py on the device (A Raspberry Pi Ultrasonic Sensor), updating the devices JSON Shadow in AWS to a 'YES' or 'NO' value, triggers an IoT Rule to update a .txt file in S3 containing the value, and running the script in index.html on page load to retrieve the value and update the image / text value accordingly.
### Index.html
* Contains html for the static web page and the main javascript start() function to be ran on load. The function retrieves the necessary text file, located in S3, that holds the value updated by the device python script.
### Script.py
* This is the rooted Device script to be ran on the Raspberry Pi on device boot. This script gets a distance, determines whether the object is a car (within X distance) and updates it's shadow in AWS accordingly.
