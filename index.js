var awsIot = require('aws-iot-device-sdk');

var thingShadows = awsIot.thingShadow({
   keyPath: './certs/e7b2268d70-private.pem.key',
   certPath: './certs/e7b2268d70-certificate.pem.crt',
   caPath: './certs/AmazonRootCA1.pem',
   clientId: 'arn:aws:iot:us-east-2:205839533183:thing/RaspberryPi',
   debug: true,
   host: 'a1azsp5amzvmuf-ats.iot.us-east-2.amazonaws.com'
});

var device = awsIot.device({
   keyPath: './certs/e7b2268d70-private.pem.key',
  certPath: './certs/e7b2268d70-certificate.pem.crt',
    caPath: './certs/AmazonRootCA1.pem',
    clientId: 'arn:aws:iot:us-east-2:205839533183:thing/RaspberryPi',
      host: 'a1azsp5amzvmuf-ats.iot.us-east-2.amazonaws.com'
});

//
// Device is an instance returned by mqtt.Client(), see mqtt.js for full
// documentation.
//
device
  .on('connect', function() {
    console.log('connect');
    device.subscribe('$aws/things/RaspberryPi/shadow/get');
    device.publish('topic_2', JSON.stringify({ test_data: 1}));
  });




//
// This will print a console message when the connection to AWS IoT
// completes.
//
thingShadows.on('connect', function() {
   console.log('Connected to AWS IoT');
});
thingShadows.register('arn:aws:iot:us-east-2:205839533183:thing/RaspberryPi');
var shadow = thingShadows.get('arn:aws:iot:us-east-2:205839533183:thing/RaspberryPi');
console.log(shadow);
