var awsIot = require('aws-iot-device-sdk');
var name;

var thingShadows = awsIot.thingShadow({
   keyPath: './certs/e7b2268d70-private.pem.key',
   certPath: './certs/e7b2268d70-certificate.pem.crt',
   caPath: './certs/AmazonRootCA1.pem',
   clientId: 'arn:aws:iot:us-east-2:205839533183:thing/RaspberryPi',
   debug: true,
   host: 'a1azsp5amzvmuf-ats.iot.us-east-2.amazonaws.com'
});


//Set the name of the device we want, then execute these blocks
//For example, invidual names yadda yadda
name = 'RaspberryPi';
thingShadows.on('connect', function() {
    thingShadows.register(name, {}, function() {
       thingShadows.get(name);
    });
});

thingShadows.on('status',  function(name, stat, clientToken, stateObject) {
  console.log('received '+stat+' on '+name+': '+JSON.stringify(stateObject));
  var carState = stateObject.state.reported.CAR; //SUCCESSFULLY GETS CAR VALUE
  console.log(carState);
});
