# HASS-simulated-sensor
A simulated sensor that generates a time-varying value ```V(t)``` given by the [function](https://en.wikipedia.org/wiki/Sine_wave) ```V(t) = M + A sin(2 pi (t - t_0) / w) + N(s)``` where:

- **M** = the mean value, default 0
- **A** = the amplitude of the sine wave, default 1
- **t** = the time that a value is generated at
- **t_0** = the time the sensor is started
- **w** = the time period for a single cycle of the sine wave, default value 60 seconds
- **N(s)** = the random Gaussian noise term with spread **s**, defaults to zero noise



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
