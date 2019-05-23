from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient
import RPi.GPIO as GPIO
import time


#Shadow Client ID
SHADOW_CLIENT = "myShadowClient"
#Unique Host Name
HOST_NAME = "a1azsp5amzvmuf-ats.iot.us-east-2.amazonaws.com"
#AWS Root CA
ROOT_CA = "/boot/deviceSDK/AmazonRootCA1.pem"
#Private Key
PRIVATE_KEY = "/boot/deviceSDK/e7b2268d70-private.pem.key"
#Cert File
CERT_FILE = "/boot/deviceSDK/e7b2268d70-certificate.pem.crt"
#Shadow Handler Name
SHADOW_HANDLER = "RaspberryPi"


GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

#GPIO Pin Reference Numbers
TRIG = 4
ECHO = 18

#Create, configure, and connect a Shadow Client
myShadowClient = AWSIoTMQTTShadowClient(SHADOW_CLIENT)
myShadowClient.configureEndpoint(HOST_NAME, 8883)
myShadowClient.configureCredentials(ROOT_CA, PRIVATE_KEY, CERT_FILE)
myShadowClient.configureConnectDisconnectTimeout(10)
myShadowClient.configureMQTTOperationTimeout(5)
myShadowClient.connect()

#Create a programmatic representation of the shadow.
myDeviceShadow = myShadowClient.createShadowHandlerWithName(SHADOW_HANDLER, True)


#called whenever the Shadow is updated
def myShadowUpdateCallback(payload, responseStatus, token):
    print()
    print('UPDATE: $aws/things/' + SHADOW_HANDLER + '/shadow/update/#')
    print("payload = " + payload)
    print("responseStatus = " + responseStatus)
    print("token = " + token)

#Checks if object is a car
def is_car(distance):
    #Am I a car? Distance value is placeholder
    count = 0
    if distance <= 36:
        while True:
            count +=1
            if count >= 3:
                return True
                break
    else:
        return False

#get the distance    
def get_distance():
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

    GPIO.output(TRIG, True)
    time.sleep(0.0001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == False:
        start = time.time()

    while GPIO.input(ECHO) == True:
        end = time.time()

    sig_time = end-start
    distance = sig_time / 0.000148
    print('')
    print('')
    print('Distance: {} inches'.format(distance))
    return distance

while True:
    distance = get_distance()
    time.sleep(0.5)
    car = is_car(distance)
    if car == True:
        #Post method to AWS
        myDeviceShadow.shadowUpdate('{"state":{"reported":{"CAR":"YES"}}}',
                                    myShadowUpdateCallback, 5)
        print('SHADOW UPDATED - IS A CAR')
        time.sleep(5)
    else:
        myDeviceShadow.shadowUpdate('{"state":{"reported":{"CAR":"NO"}}}',
                                    myShadowUpdateCallback, 5)
        print('SHADOW UPDATED - NOT A CAR')
        time.sleep(5)
