# HASS-simulated-sensor

This is a home-assistant [custom component](https://home-assistant.io/developers/platform_example_sensor/) - place the custom_components folder in your configuration directory (or add its contents to an existing custom_components folder).

This component provides a simulated sensor that generates a time-varying signal ```V(t)``` given by the [function](https://en.wikipedia.org/wiki/Sine_wave):

 ```
 V(t) = M + A sin((2 pi (t - t_0) / w) + P) + N(s)
 ```

where:

- **M** = the mean value, default **0**
- **A** = the amplitude of the sine wave, default **1**
- **t** = the time when a value is generated
- **t_0** = the time when the sensor is started
- **w** = the time period for a single cycle of the sine wave, default value **60** seconds
- **P** = the phase offset to add, default value **0** degrees
- **N(s)** = the random [Gaussian noise](https://en.wikipedia.org/wiki/Gaussian_noise) with spread **s**, defaults value **0**


A simulated sensor with default values can be added to home-assistant and displayed using a  [history_graph](https://home-assistant.io/components/history_graph/) using the following config:

```yaml
sensor:
  - platform: simulated

history_graph:
  simulated_sensor_graph:
    name: 'simulated'
    hours_to_show: 1
    entities:
      - sensor.simulated
```

<p align="center">
<img src="https://github.com/robmarkcole/HASS-simulated-sensor/blob/master/images/HA_view.png" width="500">
</p>

To give an example of simulating real world data, we can create a simulated relative humidity sensor (in %) using the config below:

```yaml
- platform: simulated
  name: 'simulated relative humidity'
  unit: '%'
  amplitude: 0 # Turns off sine wave
  mean: 50
  spread: 10
  seed: 50
```
Here the sine wave contribution has been set to zero by configuring an amplitude of **0**, and a Gaussian noise signal with spread **10** is generated about a mean value of **50**. A graph of the data generated is below. Bear in mind that [due to statistics](https://en.wikipedia.org/wiki/Normal_distribution), approximately 30% of values are outside of the configured spread of **10**.

<p align="center">
<img src="https://github.com/robmarkcole/HASS-simulated-sensor/blob/master/images/simulated_humidity.png" width="500">
</p>

Configuration variables:
- **name** string (*Optional*): The name of the sensor
- **unit** string (*Optional*): The unit to apply
- **amplitude** number (*Optional*): The [amplitude](https://en.wikipedia.org/wiki/Amplitude) of the periodic components
- **mean** number (*Optional*): The [mean](https://en.wikipedia.org/wiki/Mean) level
- **period** number (*Optional*): The number of seconds for the [period](https://en.wikipedia.org/wiki/Periodic_function)
- **phase** number (*Optional*): The [phase](https://en.wikipedia.org/wiki/Phase_(waves)) offset (in degrees) to apply to the periodic component
- **spread** number (*Optional*): The spread ([FWHM](https://en.wikipedia.org/wiki/Full_width_at_half_maximum)) of the Gaussian noise
- **seed** number (*Optional*): The [seed](https://docs.python.org/3.6/library/random.html#random.seed) value for the random component
