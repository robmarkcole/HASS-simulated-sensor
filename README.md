# HASS-simulated-sensor
A simulated sensor that generates a time-varying value ```V(t)``` given by the [function](https://en.wikipedia.org/wiki/Sine_wave):

 ```
 V(t) = M + A sin(2 pi (t - t_0) / w) + N(s)
 ```

where:

- **M** = the mean value, default **0**
- **A** = the amplitude of the sine wave, default **1**
- **t** = the time when a value is generated
- **t_0** = the time when the sensor is started
- **w** = the time period for a single cycle of the sine wave, default value **60** seconds
- **N(s)** = the random Gaussian noise with spread **s**, defaults value **0**


A simulated sensor with default values can be added to home-assistant and displayed using a with history_graph the following config:

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

To give an example of simulating real world data, we can create a simulated relative humidity sensor using the config below:

```yaml
- platform: simulated
  name: 'simulated relative humidity'
  unit: '%'
  amplitude: 0 # Turns off sine wave
  mean: 50
  spread: 10
  seed: 999
```
A graph of the data generated is below. Bear in mind that due to statistics, approximately 30% of values are outside of the configured spread of 10.
