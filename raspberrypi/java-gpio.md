# Java GPIO control

## LED example

Adapted from [Robert Savage's example](https://pi4j.com/1.2/example/control.html)

```java
import com.pi4j.io.gpio.GpioController;
import com.pi4j.io.gpio.GpioFactory;
import com.pi4j.io.gpio.GpioPinDigitalOutput;
import com.pi4j.io.gpio.PinState;
import com.pi4j.io.gpio.RaspiPin;

public class ControlGpioExample {

    public static void main(String[] args) throws InterruptedException {
        System.out.println("GPIO LED example ... started.");
        // Intialise GPIO & get pin
        final GpioController gpio = GpioFactory.getInstance();
        GpioPinDigitalOutput pin = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_11);
        pin.high()                          // Turn LED on
        Thread.sleep(5000);                 // Pause 5 seconds
        pin.low();                          // Turn LED off
        Thread.sleep(5000);                 // Pause 5 seconds
        pin.toggle();                       // Toggle LED (ie: turn LED on)
        Thread.sleep(5000);                 // Pause 5 seconds
        pin.toggle();                       // Toggle LED (ie: turn LED off)
        Thread.sleep(5000);                 // Pause 5 seconds
        pin.pulse(1000, true);              // Turn on 1 second ... 'true' => use blocking
        boolean ledStatus = pin.isHigh();   // Should be set to false as LED is off
        gpio.shutdown();                    // Release all GPIO hooks
        System.out.println("Exiting");
    }
}
```

## Button example

There are two methods for responding to GPIO input: `addTrigger()` and `addListener()`. A bit of experimentation is required to determine which will be the most efficient method to use. 

Trigger example adapted from [Robert Savage's example](https://pi4j.com/1.2/example/trigger.html)

```java
import java.util.concurrent.Callable;
import com.pi4j.io.gpio.GpioController;
import com.pi4j.io.gpio.GpioFactory;
import com.pi4j.io.gpio.GpioPinDigitalInput;
import com.pi4j.io.gpio.GpioPinDigitalOutput;
import com.pi4j.io.gpio.PinPullResistance;
import com.pi4j.io.gpio.PinState;
import com.pi4j.io.gpio.RaspiPin;
import com.pi4j.io.gpio.trigger.GpioCallbackTrigger;
import com.pi4j.io.gpio.trigger.GpioPulseStateTrigger;
import com.pi4j.io.gpio.trigger.GpioSetStateTrigger;
import com.pi4j.io.gpio.trigger.GpioSyncStateTrigger;

public class TriggerGpioExample {

    public static void main(String[] args) throws InterruptedException {

        // create gpio controller & provision button
        final GpioController gpio = GpioFactory.getInstance();
        final GpioPinDigitalInput myButton = gpio.provisionDigitalInputPin(RaspiPin.GPIO_02, PinPullResistance.PULL_DOWN);

        // create a gpio callback trigger on button pin; when state changes, perform a callback
        // invocation on the user defined 'Callable' class instance
        myButton.addTrigger(new GpioCallbackTrigger(new Callable<Void>() {
            public Void call() throws Exception {
                System.out.println(" --> GPIO TRIGGER CALLBACK RECEIVED ");
                return null;
            }
        }));

        System.out.println("Listening... test the button");

        while (true) {          // keep program running until user aborts (CTRL-C)
            Thread.sleep(500);
        }
        // gpio.shutdown();   <--- implement this method call if you wish to terminate the Pi4J GPIO controller
    }
}
```

Listener example adapted from [Robert Savage's example](https://pi4j.com/1.2/example/listener.html)

```java
import com.pi4j.io.gpio.*;
import com.pi4j.io.gpio.event.GpioPinDigitalStateChangeEvent;
import com.pi4j.io.gpio.event.GpioPinListenerDigital;

public class ListenGpioExample {

    public static void main(String args[]) throws InterruptedException {

        // create gpio controller & provision button
        final GpioController gpio = GpioFactory.getInstance();
        final GpioPinDigitalInput myButton = gpio.provisionDigitalInputPin(RaspiPin.GPIO_02, PinPullResistance.PULL_DOWN);

        // create and register gpio pin listener
        myButton.addListener(new GpioPinListenerDigital() {
            @Override
            public void handleGpioPinDigitalStateChangeEvent(GpioPinDigitalStateChangeEvent event) {
                // Event triggered; display message
                System.out.println(" --> GPIO PIN CHANGE: " + event.getPin() + " = " + event.getState());
            }
        });

        System.out.println("Listening... test the button");

        while(true) {           // keep program running until user aborts (CTRL-C)
            Thread.sleep(500);
        }
        // gpio.shutdown();   <--- implement this method call if you wish to terminate the Pi4J GPIO controller
    }
}
```
