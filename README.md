# HASS-simulated-sensor
A simulated sensor for home-assistant. Image shows aliasing due to sampling interval.

```yaml
sensor:
  - platform: simulated

history_graph:
  simulated_sine_graph:
    name: 'simulated sensor'
    hours_to_show: 1
    entities:
      - sensor.simulated_sine
```
