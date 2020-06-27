# **Mqtt With Js**

to use mqtt lib in JavaScript use this cdn:

```js
<script src='https://cdnjs.cloudflare.com/ajax/libs/paho-mqtt/1.1.0/paho-mqtt.js'></script>
```

**[client](https://github.com/ashvinijangid/mqtt-protocol/blob/master/Js/client.html)**

```js
        var client = new Paho.Client("mqtt.eclipse.org", 80, "clientId");

        client.onConnectionLost = onConnectionLost;
        client.onMessageArrived = onMessageArrived;

        client.connect({
            onSuccess: onConnect
        });


        function onConnect() {
            client.subscribe("home_led_light");
            write("Connected");
        }

        function onConnectionLost(responseObject) {
            if (responseObject.errorCode !== 0) {
                write("onConnectionLost:" + responseObject.errorMessage);
            }
        }

        function onMessageArrived(message) {
            write(` ${message.destinationName} :: ${message.payloadString}`);
        }
```

[**Publisher**](https://github.com/ashvinijangid/mqtt-protocol/blob/master/Js/publisher.html)

```js
        var client = new Paho.Client("mqtt.eclipse.org", 80, "clientId");

        client.onConnectionLost = onConnectionLost;

        client.connect({
            onSuccess: onConnect
        });


        function onConnect() {
            write("Connected");
            write("Pusing Messsages");
            client.publish("home_led_light", "on", 1);
            client.publish("home_led_light", "off", 1);
            client.publish("home_led_light", "on", 1);
            write("Pusing Complete");
            client.end();
        }

        function onConnectionLost(responseObject) {
            if (responseObject.errorCode !== 0) {
                write("Connection Closed");
            }
        }
```