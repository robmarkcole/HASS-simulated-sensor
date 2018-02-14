"""
Adds a simulated sensor.

For more details about this platform, please refer to the documentation at
https://home-assistant.io/components/sensor.simulated/
"""
import logging
import numpy as np
import datetime as datetime

from homeassistant.helpers.entity import Entity

_LOGGER = logging.getLogger(__name__)
SCAN_INTERVAL = datetime.timedelta(seconds=0.1)
ICON = 'mdi:chart-line'


def strfdelta(tdelta):
    """Helper to print timedelta."""
    d = {"days": tdelta.days}
    d["hours"], rem = divmod(tdelta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    output_str = """{days} days, {hours} hours,
    {minutes} minutes, {seconds} seconds""".format(**d)
    return output_str


def setup_platform(hass, config, add_devices, discovery_info=None):
    """Set up the simulated sensor."""
    name = 'simulated_sine'
    unit = '%'
    amp = 10
    mean = 50
    period = datetime.timedelta(seconds=30)
    phase = 90
    sigma = 0.95
    seed = 100
    sensor = SimulatedSensor(
        name, unit, amp, mean, period, phase, sigma, seed
        )
    add_devices([sensor], True)


class SimulatedSensor(Entity):
    """Class for simulated sensor."""

    def __init__(self, name, unit, amp, mean, period, phase, sigma, seed):
        """Init the class."""
        self._name = name
        self._unit = unit
        self._amp = amp
        self._mean = mean
        self._period = period
        self._phase = phase  # phase in degrees
        self._sigma = sigma
        self._seed = seed
        self._start_time = datetime.datetime.now()
        self._state = None

    def time_delta(self):
        """"Return the time difference between the current measurement
        and the start of the session."""
        dt0 = self._start_time
        dt1 = datetime.datetime.now()
        return dt1 - dt0

    def sine_calc(self):
        m0 = self._mean
        a0 = self._amp
        dt = self.time_delta().total_seconds()*1e6  # convert to  milliseconds
        w0 = self._period.total_seconds()*1e6
        s0 = self._sigma
        p0 = self._phase*np.pi/180  # Convert to radians
        periodic = (a0 * np.sin(2*np.pi*(dt)/w0) + p0)
        noise = np.random.normal(0, s0)
        return m0 + periodic + noise

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
        return self._unit

    @property
    def device_state_attributes(self):
        """Return other details about the sensor state."""
        attr = {
            'amplitude': self._amp,
            'mean': self._mean,
            'period': strfdelta(self._period),
            'phase': self._phase,
            'sigma': self._sigma,
            'seed': self._seed,
            }
        return attr
