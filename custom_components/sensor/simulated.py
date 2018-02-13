"""
Adds a simulated sensor.

For more details about this platform, please refer to the documentation at
https://home-assistant.io/components/sensor.simulated/
"""
import logging
import numpy as np
import datetime as dt

from homeassistant.helpers.entity import Entity

_LOGGER = logging.getLogger(__name__)
SCAN_INTERVAL = dt.timedelta(seconds=0.1)
ICON = 'mdi:chart-line'


def setup_platform(hass, config, add_devices, discovery_info=None):
    """Set up the simulated sensor."""
    name = 'simulated_sine'
    unit_of_measurement = '%'
    seed = 100
    amplitude = 1
    period = dt.timedelta(seconds=30)
    sigma = 0.1
    add_devices([SimulatedSensor(name, amplitude, period, sigma, unit_of_measurement, seed)], True)


class SimulatedSensor(Entity):
    """Class for simulated sensor."""

    def __init__(self, name, amplitude, period, sigma, unit_of_measurement, seed):
        self._name = name
        self._unit_of_measurement = unit_of_measurement
        self._seed = seed
        self._start_time = dt.datetime.now()
        self._amplitude = amplitude
        self._period = period.total_seconds()*1e6   # timedelta
        self._sigma = sigma
        self._state = None

    def time_delta(self):
        dt1 = self._start_time
        dt2 = dt.datetime.now()
        delta_milliseconds = (dt2 - dt1).total_seconds()*1e6
        return delta_milliseconds

    def sine_calc(self):
        a = self._amplitude
        delta_t = self.time_delta()
        w = self._period
        s = self._sigma
        return (a * np.sin(2*np.pi*(delta_t)/w)) + np.random.normal(0, s)

    def update(self):
        self._state = self.sine_calc()

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def icon(self):
        """Icon to use in the frontend, if any."""
        return ICON

    @property
    def unit_of_measurement(self):
        """Return the unit this state is expressed in."""
        return self._unit_of_measurement

    @property
    def device_state_attributes(self):
        """Return other details about the sensor state."""
        attr = {
            'seed': self._seed,
            'start_time': self._start_time,
            }
        return attr
