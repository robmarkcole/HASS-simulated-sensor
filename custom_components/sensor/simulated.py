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
SCAN_INTERVAL = dt.timedelta(seconds=1)
ICON = 'mdi:chart-line'


def setup_platform(hass, config, add_devices, discovery_info=None):
    """Set up the simulated sensor."""
    name = 'simulated_sine'
    unit_of_measurement = '%'
    period_s = 60
    seed = 100
    add_devices([SimulatedSensor(name, unit_of_measurement, period_s, seed)], True)


class SimulatedSensor(Entity):
    """Class for simulated sensor."""

    def __init__(self, name, unit_of_measurement, period_s, seed):
        """Initialize the sensor."""
        self._name = name
        self._unit_of_measurement = unit_of_measurement
        self._seed = seed
        self._state = None
        self._start_time = dt.datetime.now()
        self._mean = None # The mean level
        self._amplitude = 1.0 # The wave amplitude
        self._period_s = dt.timedelta(seconds=period_s)  # The time period in seconds
        self._noise = None # % (percent) of the amplitude

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

    def update(self):
        """Update the sensor."""
        elapsed_time_s = (dt.datetime.now() - self._start_time).seconds

        elapsed_periods = int(self.safe_division(elapsed_time_s, self._period_s.seconds))
        phase = self.safe_division(
                self._period_s.seconds, elapsed_time_s - (elapsed_periods*self._period_s.seconds))
        self._state = self._amplitude*np.sin(phase*2*np.pi) #np.random.random()

    def safe_division(self, x, y):
        if y == 0:
            return 0
        return x / y

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
